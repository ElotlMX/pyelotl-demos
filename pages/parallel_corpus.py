import streamlit as st
import elotl.corpus
import pandas as pd

st.title("Corpus paralelos")

corpus = st.selectbox(
    "Elige una corpus:", [lang[0] for lang in elotl.corpus.list_of_corpus()]
)

COLUMNS = ["Español", "", "variant", "doc"]


df = pd.DataFrame(elotl.corpus.load(corpus))


if corpus == "axolotl":
    COLUMNS[1] = "Nahuatl"
    df.columns = COLUMNS + ["iso"]
elif corpus == "kolo":
    COLUMNS[1] = "Mixteco"
    df.columns = COLUMNS
elif corpus == "tsunkua":
    COLUMNS[1] = "Otomí"
    df.columns = COLUMNS + ["pdf", "id"]
    del df["pdf"]
    del df["id"]


st.dataframe(df, hide_index=True)

st.subheader(f"Estadísticas de {corpus.title()}")

col1, col2 = st.columns([1, 3])
with col1:
    st.metric("Líneas ", len(df))
    st.metric("Documentos :book:", len(df["doc"].unique()))
    st.metric("Variantes", len(df["variant"].unique()))

with col2:
    st.dataframe(df.groupby(by="doc")["variant"].count())
    st.dataframe(df.groupby(by="variant")["doc"].count())
