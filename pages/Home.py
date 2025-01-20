import streamlit as st
st.set_page_config(
    page_title="Social Media Hashtag Trend Analyser",
    page_icon=":hash:",
    layout="centered",
    initial_sidebar_state="auto",
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
st.title("Social Media Hashtag Trend Analyser")
st.page_link("SMedia.py", label="Home", icon="🏠")
post= st.text_area("Enter your post here","",placeholder="#Tag1 #Tag2 #Tag3 , Post")