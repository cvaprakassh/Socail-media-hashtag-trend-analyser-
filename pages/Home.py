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

# Function to check payload
def check_payload(payload):
    if "postid" not in payload:
        st.error("Post ID is missing.")
        return False
    if "post_content" not in payload:
        st.error("Post content is missing.")
        return False
    if "tags" not in payload:
        st.error("Tags are missing.")
        return False
    try:
        json.loads(json.dumps(payload))
    except ValueError as e:
        st.error("Payload is not a valid JSON.")
        return False
    return True



# Function to submit a post to the API
def post_info(post_text):
    url = "https://go07cpukrh.execute-api.ap-south-1.amazonaws.com/Post-Stage"  # API endpoint
    payload = json.loads(post_text)  # Convert JSON string to dictionary
    #check_payload(payload)
    
    try:    
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.error(f"Error submitting post: {e}")
        return
    #st.success("Post successfully submitted!")
    #st.write(response.text)
    #st.write(response.status_code)
    #st.write(response.json())
        
    if response.status_code == 200:
        st.success("Post successfully submitted!")
    else:
        st.error("Failed to submit post. Please try again.")
        st.write(response.text)

post_cont= st.text_area("Enter your post here","",placeholder="#Tag1 #Tag2 #Tag3 , Post")
post_tags = re.findall(r"#(\w+)", post_cont)  # Extract hashtags from post content
post_desc = re.sub(r"#(\w+)", "", post_cont).strip()  # Extract post description
post_id = get_next_id() # Get the next post ID
#st.write(type(post_id))
post_text=json.dumps({"postid":post_id,"post_content": post_desc, "tags": post_tags}) # Create a JSON object 
#st.write(post_text)
if st.button("Post"):
    post_info(post_text)


