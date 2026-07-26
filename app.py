import base64
import re
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

BASE_DIR = Path(__file__).parent

st.set_page_config(page_title="For My Favorite Person", page_icon="🐻", layout="wide")

# Streamlit adds its own page padding/menu — strip that away so the site fills the frame.
st.markdown(
    """
    <style>
        .block-container { padding: 0 !important; max-width: 100% !important; }
        header, footer { visibility: hidden; height: 0; }
        iframe { display: block; }
    </style>
    """,
    unsafe_allow_html=True,
)


def load_text(name: str) -> str:
    raw = (BASE_DIR / name).read_bytes()
    # Handle files saved as UTF-8, UTF-8-with-BOM, or UTF-16 (common when a
    # file gets opened/saved in Notepad or another Windows editor).
    if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
        return raw.decode("utf-16")
    return raw.decode("utf-8-sig")


def to_data_uri(path: Path) -> str:
    mime = "image/jpeg" if path.suffix.lower() in (".jpg", ".jpeg") else "image/png"
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"


def build_page() -> str:
    html = load_text("index.html")
    css = load_text("style.css")
    js = load_text("script.js")

    # Inline the stylesheet and script so the component is fully self-contained.
    html = html.replace(
        '<link rel="stylesheet" href="style.css">', f"<style>{css}</style>"
    )
    html = html.replace('<script src="script.js"></script>', f"<script>{js}</script>")

    # Inline every local image as base64 so it survives inside the iframe.
    for match in re.findall(r'(?:src|href)="images/([^"]+)"', html):
        img_path = BASE_DIR / "images" / match
        if img_path.exists():
            html = html.replace(f"images/{match}", to_data_uri(img_path))

    return html


page_html = build_page()

# height controls how tall the visible frame is; the page scrolls inside it.
components.html(page_html, height=1000, scrolling=True)
