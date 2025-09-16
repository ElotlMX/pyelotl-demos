import csv
from pathlib import Path

import streamlit as st
from elotl.utils.morphology import Token


def page_configs():
    """Set Streamlit page configurations"""
    st.set_page_config(
        page_title="Elotl MX",
        page_icon="🌽",
        menu_items={"About": "### Comunidad de Elotl :corn:\nhttps://elotl.mx"},
        layout="wide",
    )


def app_layout():
    """Create a two-column layout with a sidebar menu and main content area"""
    menu, content = st.columns([0.2, 0.8])
    with menu:
        st.page_link("app.py", label="Chante", icon="🏠")
        st.page_link("pages/normalizador.py", label="Normalizador", icon="📑")
        st.page_link(
            "pages/analizadores.py", label="Analizador Morfológico", icon="✍🏼"
        )
        st.page_link("pages/parallel_corpus.py", label="Corpus Paralelos", icon="📚")
        st.page_link("pages/about.py", label="Acerca de nosotræs", icon="🌽")
    return menu, content


def format_feats(token: Token) -> str:
    """Format the morphological features of a token into a string representation

    Parameters
    ----------
    token : Token
        A Token object containing morphological analyses

    Returns
    -------
    str
        A string representation of the token's morphological
          features in the format "key=value|key=value
    """
    return "|".join(
        [f"{k}={v}" for k, v in sorted(token.analyses[0][0][0]["feats"].items())]
    )


def get_tagged_words(text: str, tokens: list[Token]) -> list[dict]:
    """Get a list of dictionaries representing the tagged words in a sentence

    Parameters
    ----------
    text : str
        The original text of the sentence
    tokens : list[Token]
        List of Token objects representing the tokens in the sentence

    Returns
    -------
    list[dict]
        A list of dictionaries in the format required by spacy-streamlit's visualize_ner function
    """
    entities = []
    for token in tokens:
        idx1 = text.index(token.wordform)
        idx2 = idx1 + len(token.wordform)
        pos = token.pos if token.pos is not None else ""
        entities.append({"start": idx1, "end": idx2, "label": pos})
    return [{"text": text, "ents": entities}]


def write_feedback(file_path: Path, row: list[str], header: list[str]) -> None:
    """Append a feedback row to a CSV file, creating it with a header if it doesn't exist

    Parameters
    ----------
    file_path : Path
        Path to the CSV file
    row : list[str]
        List of strings representing the row to append
    header : list[str]
        List of strings representing the header row

    Returns
    -------
    None
    """
    # TODO: Use sqlite instead of CSV
    if not file_path.exists():
        file_path.touch()
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        has_header = next(reader, None) is not None
    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not has_header:
            writer.writerow(header)
        writer.writerow(row)


def get_tagged_sent(tokens: list[Token]) -> str:
    """Get a string representation of the tagged tokens in a sentence

    Parameters
    ----------
    tokens : list[Token]
        List of Token objects representing the tokens in the sentence

    Returns
    -------
    str
        A string representation of the tagged tokens in the format "wordform/POS"
    """
    return " ".join(
        [f"{token.wordform}/{token.pos}" for token in tokens if token.pos is not None]
    )
