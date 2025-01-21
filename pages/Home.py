import streamlit as st
import requests
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
# Function to submit a post to the API
def post_content(post_text):
    url = "https://go07cpukrh.execute-api.ap-south-1.amazonaws.com/Post-Stage"  # API endpoint
    payload = {"content": post_text}
    headers = {"Content-Type": "application/json"}
        
    response = requests.post(url, json=payload, headers=headers)
        
    if response.status_code == 201:
        st.success("Post successfully submitted!")
    else:
        st.error("Failed to submit post. Please try again.")

post_text= st.text_area("Enter your post here","",placeholder="#Tag1 #Tag2 #Tag3 , Post")
if st.button("Post"):
    post_content(post_text)

