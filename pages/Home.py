import streamlit as st
import requests
import re
import json

#create id auto increment
def get_next_id():
    try:
        with open("id_counter.json", "r") as file:
            data = json.load(file)
            current_id = data["current_id"]
    except FileNotFoundError:
        current_id = 0

    next_id = current_id + 1

    with open("id_counter.json", "w") as file:
        json.dump({"current_id": next_id}, file)

    return next_id

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
def post_info(post_text):
    url = "https://go07cpukrh.execute-api.ap-south-1.amazonaws.com/Post-Stage"  # API endpoint
    payload = {"content": post_text}
    headers = {"Content-Type": "application/json"}
        
    response = requests.post(url, json=payload, headers=headers)
        
    if response.status_code == 201:
        st.success("Post successfully submitted!")
    else:
        st.error("Failed to submit post. Please try again.")

post_cont= st.text_area("Enter your post here","",placeholder="#Tag1 #Tag2 #Tag3 , Post")
post_tags = re.findall(r"#(\w+)", post_cont)  # Extract hashtags from post content
post_desc = re.sub(r"#(\w+)", "", post_cont).strip()  # Extract post description
post_id = get_next_id()  # Get the next post ID
post_text=json.dumps({"id": post_id, "description": post_desc, "tags": post_tags}) # Create a JSON object 

if st.button("Post"):
    post_info(post_text)

