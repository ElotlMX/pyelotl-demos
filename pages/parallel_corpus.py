import elotl.corpus
import pandas as pd
import streamlit as st

from utils import app_layout, page_configs

page_configs()
menu, content = app_layout()


with content:
    st.title("Corpus paralelos")
    corpus = ""
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

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Documentos")
        df["doc"] = df["doc"].replace("", "Sin documento")
        docs = df.groupby(by="doc")["doc"].count()
        docs.sort_values(ascending=False, inplace=True)
        docs_str = ""
        for doc in docs.keys():
            docs_str += f"- {docs[doc]} :: {doc}\n"
        st.code(docs_str)

    with col2:
        st.subheader("Variantes")
        df["variant"] = df["variant"].replace("", "Sin variante")
        variants = df.groupby(by="variant")["doc"].count()
        st.dataframe(
            variants.sort_values(ascending=False),
            column_config={"variant": "Variante", "doc": "#"},
        )

with menu:
    st.subheader(f"Estadísticas de {corpus.title()}")
    st.metric("Líneas 📊", len(df))
    st.metric("Documentos :book:", len(df["doc"].unique()))
    st.metric("Variantes 🗺️", len(df["variant"].unique()))
