import streamlit as st
import elotl.corpus
import pandas as pd

menu, content = st.columns([0.2, 0.8])
corpus = ""


with content:
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

    col1, col2 = st.columns(2)
    with col1:
        df["doc"] = df["doc"].replace("", "Sin documento")
        docs = df.groupby(by="doc")["doc"].count()
        st.table(docs.sort_values(ascending=False))

    with col2:
        df["variant"] = df["variant"].replace("", "Sin variante")
        variants = df.groupby(by="variant")["doc"].count()
        st.table(variants.sort_values(ascending=False))

with menu:
    st.page_link("app.py", label="Chante", icon="🏠")
    st.page_link("pages/normalizador.py", label="Normalizador", icon="📑")
    st.page_link("pages/analizadores.py", label="Analizador Morfológico", icon="✍🏼")
    st.page_link("pages/parallel_corpus.py", label="Corpus Paralelos", icon="📚")

    st.subheader(f"Estadísticas de {corpus.title()}")
    st.metric("Líneas 📊", len(df))
    st.metric("Documentos :book:", len(df["doc"].unique()))
    st.metric("Variantes 🗺️", len(df["variant"].unique()))
