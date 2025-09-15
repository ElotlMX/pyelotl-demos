import csv
import streamlit as st

from elotl.nahuatl.orthography import Normalizer as NahuatlNormalizer
from elotl.otomi.orthography import Normalizer as OtomiNormalizer

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
