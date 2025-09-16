import streamlit as st

from utils import app_layout, page_configs

page_configs()

_, content = app_layout()

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
