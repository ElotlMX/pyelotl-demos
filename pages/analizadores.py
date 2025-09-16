import re
from pathlib import Path

import streamlit as st
from elotl.huave.morphology import Analyzer as HuaveAnalyzer
from elotl.nahuatl.config import SUPPORTED_LANG_CODES as NAHUATL_LANGS
from elotl.nahuatl.morphology import Analyzer as NahuatlAnalyzer
from elotl.otomi.morphology import Analyzer as OtomiAnalyzer
from spacy_streamlit import visualize_ner

from utils import get_tagged_sent, write_feedback

st.set_page_config(
    page_title="Elotl MX",
    page_icon="🌽",
    menu_items={
        "About": """
        ### Comunidad de Elotl :corn:
        https://elotl.mx
        """
    },
    layout="wide",
)

COLORS = {
    "ADJ": "#c9e2ef",
    "ADP": "#67F7D4",
    "ADV": "#F1B1D6",
    "AUX": "#f5f5f5",
    "CCONJ": "#f69f91",
    "DET": "#fbddf0",
    "INTJ": "#f4c025",
    "NOUN": "#bfe1d9",
    "NUM": "#fff9e6",
    "PART": "#ffebec",
    "PRON": "#7ba7cc",
    "PROPN": "#05ad80",
    "PUNTC": "#077fa6",
    "SCONJ": "#dedede",
    "VERB": "#aa9cfc",
    "X": "#dedede",
}

ANALIZER_FEEDBACK_FILE = "analizer_feedback.csv"
ANALIZER_HEADER = [
    "lang",
    "lang_code",
    "original_text",
    "tagged_sent",
    "corrected_analysis",
]


def format_feats(token):
    return "|".join(
        [f"{k}={v}" for k, v in sorted(token.analyses[0][0][0]["feats"].items())]
    )


def get_tagged_words(text: str, tokens) -> list[dict]:
    entities = []
    for token in tokens:
        idx1 = text.index(token.wordform)
        idx2 = idx1 + len(token.wordform)
        pos = token.pos if token.pos is not None else ""
        entities.append({"start": idx1, "end": idx2, "label": pos})
    return [{"text": text, "ents": entities}]


menu, content = st.columns([0.2, 0.8])

with menu:
    st.page_link("app.py", label="Chante", icon="🏠")
    st.page_link("pages/normalizador.py", label="Normalizador", icon="📑")
    st.page_link("pages/analizadores.py", label="Analizador Morfológico", icon="✍🏼")
    st.page_link("pages/parallel_corpus.py", label="Corpus Paralelos", icon="📚")
    st.page_link("pages/about.py", label="Acerca de nosotræs", icon="🌽")

with content:
    st.title("Analizadores morfológicos (Beta)")
    LANGS = ["Nahuatl", "Otomi", "Huave"]

    lang = st.selectbox("Elige una lengua", LANGS)

    if lang == "Otomi":
        analizer = OtomiAnalyzer()
        default_text = ""
    elif lang == "Nahuatl":
        example_texts = {
            "azz": [
                "keni mochiuaj in motakualtsin",
                "Se youal keman takistok uan amo metstona, itech milaj, uelis se kinitas miyakej sitalimej itech iluikak",
            ],
            "nhi": [
                "otechinmacaya xocomeh",
                "neh niquihtoz ce historia cuando onicatca niconetl",
                "onicchihuazquia mas amo onechilhuihqueh",
            ],
            "nci": ["niquitta moxochiuh", "nican noconetzin"],
        }
        col1, col2 = st.columns([0.3, 0.7])
        with col1:
            lang_code = st.radio(
                "Selecciona una variante",
                NAHUATL_LANGS,
                captions=[
                    "Nahúatl de Zacatlán-Ahuacatlán-Tepetzintla",
                    "Nahúatl Clásico",
                    "Nahúatl de la Sierra Nororiental de Puebla",
                ],
                index=2,
            )
        with col2:
            examples_str = ""
            for example in example_texts[lang_code]:
                examples_str += f"\n- *{example}*"
            st.markdown(f"""
            #### Ejemplos:

            {examples_str}
            """)
        default_text = example_texts[lang_code][1]
        analizer = NahuatlAnalyzer(lang_code=lang_code)
    else:
        analizer = HuaveAnalyzer()
        default_text = "Teat tepood tambas mal wiiüd sawün win"

    text = st.text_input("Texto a analizar", value=default_text)

    if text:
        clean_text = re.sub(r"[^\w\s]", "", text).lower()
        tokens = analizer.analyse(clean_text)
        tagged = get_tagged_words(clean_text, tokens)
        visualize_ner(
            doc=tagged,
            labels=[token.pos for token in tokens if token.pos is not None] + ["X"],
            colors=COLORS,
            title="Etiquetas POS",
            show_table=False,
            manual=True,
        )

        sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
        st.caption("¿Este análisis es correcto?")
        selected = st.feedback("thumbs", key="analizer_feedback")
        if selected is not None:
            if sentiment_mapping[selected] == ":material/thumb_down:":
                st.error(
                    "Lamentamos que el resultado no sea adecuado",
                    icon=":material/mood_bad:",
                )
                manual_analisys = st.text_area(
                    "Análisis correcto",
                    placeholder="Ayudanos a mejorar agregando el análisis correcto",
                    key="corrected_analysis",
                    disabled=st.session_state.get("analizer_feedback_sent", False),
                )
                if "analizer_feedback_sent" not in st.session_state:
                    st.session_state.analizer_feedback_sent = False
                send_button = st.button(
                    "Enviar",
                    icon=":material/send:",
                    disabled=st.session_state.analizer_feedback_sent,
                )
                if (
                    send_button
                    and manual_analisys
                    and not st.session_state.analizer_feedback_sent
                ):
                    # Save feedback
                    file_path = Path(ANALIZER_FEEDBACK_FILE)
                    tagged_sent = get_tagged_sent(tokens)
                    # TODO: Add features from analisis
                    if lang == "Nahuatl":
                        data = [
                            lang,
                            lang_code,
                            f'"{text}"',
                            f'"{tagged_sent}"',
                            f'"{manual_analisys.strip()}"',
                        ]
                    else:
                        data = [
                            lang,
                            "",
                            f'"{text}"',
                            f'"{tagged_sent}"',
                            f'"{manual_analisys.strip()}"',
                        ]
                    write_feedback(file_path, data, ANALIZER_HEADER)
                    st.session_state.analizer_feedback_sent = True
                    st.success("Gracias por tu contribución :material/star_shine:")
                elif st.session_state.analizer_feedback_sent:
                    st.info(
                        "Ya enviaste tu contribución en esta sesión :material/info:"
                    )
            else:
                # TODO: What to do with positive feedback?
                st.success("Gracias por tu valoración :material/star_shine:")
        st.markdown("## Características por palabra")
        for i, token in enumerate(tokens, start=1):
            st.markdown(f"#### {token.wordform}")
            if token.lemma:
                st.caption(f"Lema: _{token.lemma}_")
            if token.analyses and token.analyses[0][0][0]["feats"]:
                st.code("\n".join(format_feats(token).split("|")))
