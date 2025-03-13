import streamlit as st
from elotl.nahuatl.morphology import Analyzer as NahuatlAnalyzer
from elotl.otomi.morphology import Analyzer as OtomiAnalyzer
from elotl.huave.morphology import Analyzer as HuaveAnalyzer


def format_feats(token):
    return "|".join(
        [f"{k}={v}" for k, v in sorted(token.analyses[0][0][0]["feats"].items())]
    )


menu, content = st.columns([0.2, 0.8])

with menu:
    st.subheader("Características:")
    st.page_link("app.py", label="Chante", icon="🏠")
    st.page_link("pages/normalizador.py", label="Normalizador", icon="📑")
    st.page_link("pages/analizadores.py", label="Analizador Morfológico", icon="✍🏼")
    st.page_link("pages/parallel_corpus.py", label="Corpus Paralelos", icon="📚")


with content:
    st.title("Analizadores morfológicos")
    LANGS = ["Otomi", "Nahuatl", "Huave"]

    lang = st.selectbox("Elige una lengua", LANGS)

    if lang == "Otomi":
        analizer = OtomiAnalyzer()
        default_text = ""
    elif lang == "Nahuatl":
        analizer = NahuatlAnalyzer()
        default_text = "otechinmacaya xocomeh"
    else:
        analizer = HuaveAnalyzer()
        default_text = ""

    text = st.text_input("Texto a analizar", value=default_text)

    if text:
        for i, token in enumerate(analizer.analyse(text), start=1):
            st.subheader(f"#{i} {token.wordform}")
            st.code(f"POS: {token.pos}\nLEMMA: {token.lemma}")
            st.markdown("##### Características")
            st.code("\n".join(format_feats(token).split("|")))
            st.divider()
