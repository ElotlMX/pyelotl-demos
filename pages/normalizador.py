from unicodedata import normalize
from numpy import result_type
import streamlit as st

from elotl.nahuatl.orthography import Normalizer as NahuatlNormalizer
from elotl.otomi.orthography import Normalizer as OtomiNormalizer

NAHUATL_NORMS = ["sep", "inali", "ack", "ilv"]
OTOMI_NORMS = ["inali", "rfe", "ots", "otq"]

LANGS = {"Otomi": OTOMI_NORMS, "Nahuatl": NAHUATL_NORMS}

st.title("Normalizadores")
col1, col2 = st.columns([3, 1])
with col1:
    lang = st.selectbox("Elige una lengua:", LANGS.keys())
with col2:
    norma = st.selectbox("Elige una norma", LANGS[lang])

if lang == "Otomi":
    default_text = "ebu̱ ba eje man'aki ba te̱nga ra t'o̱jo̱ ra tjuju ra tsitlaltépets. tlatsopan, nubia ba o̱t'ra b'u̱i ja ra ndo̱m'ijmu."
    normalizador = OtomiNormalizer(norma)
else:
    default_text = "au in ye yujki in on tlenamakak niman ye ik teixpan on motlalia se tlakatl itech mokaua."
    normalizador = NahuatlNormalizer(norma)

result = st.text_area("Texto a normalizar", value=default_text)

st.subheader("Oración normalizada")
st.write(normalizador.normalize(result))
st.subheader("Representación fonética")
st.write(normalizador.to_phones(result))
