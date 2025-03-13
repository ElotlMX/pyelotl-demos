import streamlit as st

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
    st.subheader("Características:")
    st.page_link("app.py", label="Chante", icon="🏠")
    st.page_link("pages/normalizador.py", label="Normalizador", icon="📑")
    st.page_link("pages/analizadores.py", label="Analizador Morfológico", icon="✍🏼")
    st.page_link("pages/parallel_corpus.py", label="Corpus Paralelos", icon="📚")


with content:
    st.title("Comunidad Elotl :corn:")

    st.subheader("¿Quienes somos?")
    st.markdown("""
    Somos una comunidad de entusiastas interesados por el desarrollo e investigación de tecnologías del lenguaje aplicadas a las lenguas originarias de México. Nuestras herramientas y recursos digitales son libres y gratuitos.

    Actualmente nuestro equipo está formado por voluntarios y becarios con diversos perfiles:

    - Licenciatura en literatura hispánica/lingüística
    - Doctorado en lingüística computacional
    - Doctorado en lingüística
    - Licenciatura en Ciencias de la Computación
    - Licenciatura en Matemáticas
    - Ingeniería en Computación
    """)
    st.subheader("Proyectos")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        #### Corpus paralelos

        - [Tsunkua](https://tsunkua.elotl.mx/)
        - [Axolotl]()
        - [Kolo](https://kolo.elotl.mx/)
        """)
        st.image("img/axolotl.png")
    with col2:
        st.markdown("""
        #### Desarrollo y código 🤓

        - [py-elotl 🐍](https://github.com/ElotlMX/py-elotl)
        - [Esquite](https://github.com/ElotlMX/Esquite)
        - [API 👩🏼‍💻](https://api.elotl.mx/v1/search/)
        - [Repositorio público 🏛️](https://github.com/ElotlMX/)
        """)
        st.image("img/github_elotl.png")
    with col3:
        st.markdown("#### Materiales didacticos")
        st.markdown(
            "[Todas las infografías](https://elotl.mx/proyectos/materiales-didacticos/infografias-nahuatl/)"
        )
        st.image("img/animales_nahuatl.png")

    st.subheader("Ligas de interés")
    st.markdown("""
        - [Página de la comunidad](https://elotl.mx)
        - [Twitter](https://x.com/elotlmx/)
        - [Facebook](https://www.facebook.com/comunidadelotl)
        - [Blog](https://elotl.mx/blog/)
        - [Mail](contacto@elotl.mx)
    """)
