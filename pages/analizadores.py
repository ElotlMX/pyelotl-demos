import streamlit as st
from spacy_streamlit import visualize_ner
from elotl.nahuatl.morphology import Analyzer as NahuatlAnalyzer
from elotl.otomi.morphology import Analyzer as OtomiAnalyzer
from elotl.huave.morphology import Analyzer as HuaveAnalyzer
from elotl.nahuatl.config import SUPPORTED_LANG_CODES as NAHUATL_LANGS

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


def format_feats(token):
    return "|".join(
        [f"{k}={v}" for k, v in sorted(token.analyses[0][0][0]["feats"].items())]
    )


def get_tagged_words(text: str, tokens) -> list[dict]:
    entities = []
    for token in tokens:
        idx1 = text.index(token.wordform)
        idx2 = idx1 + len(token.wordform)
        pos = token.pos if token.pos is not None else "X"
        entities.append({"start": idx1, "end": idx2, "label": pos})
    return [{"text": text, "ents": entities}]


menu, content = st.columns([0.2, 0.8])

with menu:
    st.subheader("Características:")
    st.page_link("app.py", label="Chante", icon="🏠")
    st.page_link("pages/normalizador.py", label="Normalizador", icon="📑")
    st.page_link("pages/analizadores.py", label="Analizador Morfológico", icon="✍🏼")
    st.page_link("pages/parallel_corpus.py", label="Corpus Paralelos", icon="📚")

with content:
    st.title("Analizadores morfológicos (Beta)")
    LANGS = ["Nahuatl", "Otomi", "Huave"]

    lang = st.selectbox("Elige una lengua", LANGS)

    if lang == "Otomi":
        analizer = OtomiAnalyzer()
        default_text = ""
    elif lang == "Nahuatl":
        # default_text = "otechinmacaya xocomeh"
        default_text = "Se youal keman takistok uan amo metstona, itech milaj, uelis se kinitas miyakej sitalimej itech iluikak"
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
        analizer = NahuatlAnalyzer(lang_code=lang_code)
    else:
        analizer = HuaveAnalyzer()
        default_text = "Teat tepood tambas mal wiiüd sawün win"

    text = st.text_input("Texto a analizar", value=default_text)

    if text:
        tokens = analizer.analyse(text)
        tagged = get_tagged_words(text, tokens)
        visualize_ner(
            doc=tagged,
            labels=[token.pos for token in tokens if token.pos is not None],
            colors=COLORS,
            title="Etiquetas POS",
            show_table=False,
            manual=True,
        )
        st.markdown("## Características por palabra")
        for i, token in enumerate(tokens, start=1):
            st.markdown(f"#### {token.wordform}")
            if token.lemma:
                st.caption(f"Lema: _{token.lemma}_")
            if token.analyses and token.analyses[0][0][0]["feats"]:
                st.code("\n".join(format_feats(token).split("|")))
