from pathlib import Path
import streamlit as st

from elotl.nahuatl.orthography import Normalizer as NahuatlNormalizer
from elotl.otomi.orthography import Normalizer as OtomiNormalizer

from utils import write_feedback

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

NORMALIZE_FEEDBACK_FILE = "normalize_feedback.csv"
NOMALIZE_FEEDBACK_HEADER = ["lang", "norma", "original_text", "auto_normalized", "manual_normalized"]

NAHUATL_NORMS = ["sep", "inali", "ack", "ilv"]
OTOMI_NORMS = ["inali", "rfe", "ots", "otq"]

LANGS = {"Otomi": OTOMI_NORMS, "Nahuatl": NAHUATL_NORMS}

menu, content = st.columns([0.2, 0.8])

with menu:
    st.page_link("app.py", label="Chante", icon="🏠")
    st.page_link("pages/normalizador.py", label="Normalizador", icon="📑")
    st.page_link("pages/analizadores.py", label="Analizador Morfológico", icon="✍🏼")
    st.page_link("pages/parallel_corpus.py", label="Corpus Paralelos", icon="📚")
    st.page_link("pages/about.py", label="Acerca de nosotræs", icon="🌽")

with content:
    st.title("Normalizadores")
    col1, col2 = st.columns([3, 1])
    with col1:
        lang = st.selectbox("Elige una lengua:", LANGS.keys())
    with col2:
        norma = st.selectbox("Elige una norma", LANGS[lang])

    if lang == "Otomi":
        default_text = "ebu̱ ba eje man'aki ba te̱nga ra t'o̱jo̱ ra tjuju ra citlaltépetl."
        normalizador = OtomiNormalizer(norma)
    else:
        default_text = "au in ye yujki in on tlenamakak niman ye ik teixpan on motlalia se tlakatl itech mokaua."
        normalizador = NahuatlNormalizer(norma)

    text = st.text_area("Texto a normalizar", value=default_text)

    st.subheader("Oración normalizada")
    normalized_text = normalizador.normalize(text)
    st.write(normalized_text)
    st.subheader("Representación fonética")
    phonetic_text = normalizador.to_phones(text)
    st.write(phonetic_text)


    sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
    st.caption("¿Esta normalización es correcta?")
    selected = st.feedback("thumbs", key="normalize_feedback")
    if selected is not None:
        if sentiment_mapping[selected] == ":material/thumb_down:":
            st.error(
                "Lamentamos que el resultado no sea adecuado",
                icon=":material/mood_bad:",
            )
            manual_analisys = st.text_area(
                "Normalización correcta",
                placeholder="Ayudanos a mejorar agregando el análisis correcto",
                key="corrected_analysis",
                disabled=st.session_state.get("norm_feedback_sent", False)
            )
            if "norm_feedback_sent" not in st.session_state:
                st.session_state.norm_feedback_sent = False
            send_button = st.button("Enviar", icon=":material/send:", disabled=st.session_state.norm_feedback_sent)
            if send_button and manual_analisys and not st.session_state.norm_feedback_sent:
                # Save feedback
                file_path = Path(NORMALIZE_FEEDBACK_FILE)
                data = [lang, norma, f'"{text}"', f'"{normalized_text}"', f'"{manual_analisys.strip()}"']
                write_feedback(file_path, data, NOMALIZE_FEEDBACK_HEADER)
                st.session_state.norm_feedback_sent = True
                st.success("Gracias por tu contribución :material/star_shine:")
            elif st.session_state.norm_feedback_sent:
                st.info("Ya enviaste tu contribución en esta sesión :material/info:")
        else:
            # TODO: What to do with positive feedback?
            st.success("Gracias por tu valoración :material/star_shine:")
