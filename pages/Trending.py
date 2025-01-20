import streamlit as st

st.set_page_config(
    page_title="Trending Page",
    page_icon="🔥",
    layout="centered",
)
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <h1 style='text-align: center; color: red;'>
        🔥 Trending # 🔥
    </h1>
    """,
    unsafe_allow_html=True,
)
st.page_link("SMedia.py", label="Home", icon="🏠")