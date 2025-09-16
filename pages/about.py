import streamlit as st

from utils import app_layout, page_configs

page_configs()
_, content = app_layout()

with content:
    st.header("Comunidad Elotl :corn:")
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
        - [Axolotl](https://axolotl-corpus.mx/search)
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
        st.markdown("#### Materiales didácticos")
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
        - [Mail](mailto:contacto@elotl.mx): `contacto@elotl.mx`
    """)
    st.caption("Hecho con :heart: por [Comunidad Elotl](https://elotl.mx)")
