import streamlit as st
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
st.title("Posts")
st.page_link("SMedia.py", label="Home", icon="🏠")