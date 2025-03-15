import streamlit as st
from spacy import displacy
from spacy_streamlit import visualize_ner
from elotl.nahuatl.morphology import Analyzer as NahuatlAnalyzer
from elotl.otomi.morphology import Analyzer as OtomiAnalyzer
from elotl.huave.morphology import Analyzer as HuaveAnalyzer

COLORS = {
    "ADJ": "#0621A6",
    "ADP": "#67F7D4",
    "ADV": "#F1B1D6",
    "AUX": "#f5f5f5",
    "CCONJ": "#ef486f",
    "DET": "#6642d1",
    "INTJ": "#f4c025",
    "NOUN": "#bfe1d9",
    "NUM": "#fff9e6",
    "PART": "#ffebec",
    "PRON": "#047c5c",
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
    return [{"text": text, "ents": entities, "title": "Etiquetas POS"}]


menu, content = st.columns([0.2, 0.8])

with menu:
    st.subheader("Características:")
    st.page_link("app.py", label="Chante", icon="🏠")
    st.page_link("pages/normalizador.py", label="Normalizador", icon="📑")
    st.page_link("pages/analizadores.py", label="Analizador Morfológico", icon="✍🏼")
    st.page_link("pages/parallel_corpus.py", label="Corpus Paralelos", icon="📚")


with content:
    st.title("Analizadores morfológicos")
    LANGS = ["Nahuatl", "Otomi", "Huave"]

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
        tokens = analizer.analyse(text)
        tagged = get_tagged_words(text, tokens)
        for i, token in enumerate(tokens, start=1):
            st.subheader(f"#{i} {token.wordform}")
            st.code(f"POS: {token.pos}\nLEMMA: {token.lemma}")
            st.markdown("##### Características")
            st.code("\n".join(format_feats(token).split("|")))
            st.divider()
        st.code(tagged)
        visualize_ner(
            doc=tagged,
            labels=[token.pos for token in tokens],
            colors=COLORS,
            show_table=False,
            manual=True,
        )
