import streamlit as st

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
menu, content = st.columns([0.2, 0.8])

with menu:
    st.page_link("app.py", label="Chante", icon="🏠")
    st.page_link("pages/normalizador.py", label="Normalizador", icon="📑")
    st.page_link("pages/analizadores.py", label="Analizador Morfológico", icon="✍🏼")
    st.page_link("pages/parallel_corpus.py", label="Corpus Paralelos", icon="📚")
    st.page_link("pages/about.py", label="Acerca de nosotræs", icon="🌽")


with content:
    st.title("Herramientas Interactivas para Lenguas Originarias: `py-elotl`")
    st.subheader("Bienvenida al demo de elotl 🤗")
    st.markdown(
        "Este sitio es una demostración de las capacidades y características principales del paquete [`py-elotl`](https://pypi.org/project/elotl/). Nuestro objetivo es desarrollar tecnologías del lenguaje accesibles para las lenguas originarias de México."
    )

    st.markdown("""
    ### Características

    #### Analizador morfológico

    Descompone palabras complejas en sus partes más pequeñas (raíz, prefijos, sufijos) para revelar su estructura gramatical interna. Ideal para entender la formación de palabras.

    #### Normalizador ortográfico

    Estandariza textos con variaciones de escritura a cierta ortografía.

    #### Corpus paralelos

    Explora, búsca palabras y frases en colecciones de textos bilingües, mostrando ejemplos de uso en contextos con su traducción.

    """)
    st.caption("Hecho con :heart: por [Comunidad Elotl](https://elotl.mx)")
