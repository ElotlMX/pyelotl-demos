import streamlit as st

NOT_FOUND_MSG = ["Not found :("]

st.set_page_config(
    page_title="Elotl MX",
    page_icon="🌍",
    menu_items={
        "About": """
        ### Comunidad de Elotl
        https://elotl.mx
        """
    },
    layout="wide",
)
menu, content = st.columns([0.2, 0.8])

with menu:
    st.subheader("Apps:")
    st.page_link("app.py", label="Home", icon="🏠")
    st.page_link("pages/normalizador.py", label="Normalizador", icon="🌍")
    st.page_link("pages/analizadores.py", label="Analizador Morfológico", icon="🍞")
    st.page_link("pages/parallel_corpus.py", label="Corpus Paralelos", icon="🍞")


with content:
    st.title("Comunidad Elotl :corn:")

    st.subheader("Ligas de interés")
    st.markdown("""
        - [Página de la comunidad](https://elotl.mx)
        - [Twitter](https://elotl.mx)
        - [Facebook](https://elotl.mx)
        - [GitHub](https://github.com/ElotlMX/)
    """)
