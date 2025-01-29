import streamlit as st
import requests
import re
import json
import time


st.set_page_config(page_title="#Tag analyser", page_icon="🔥", layout="centered", initial_sidebar_state="expanded")
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
#tab1, tab2, tab3 = st.tabs(["#Tag Trending", "Create Post", "Post"])
col1,col2,col3 = st.columns(3)
with col1:
    #st.write("This is the #Tag Trending page")
    st.page_link("pages/Trending.py", label=" # Trending", icon="🔥")
with col2:
    #st.write("Create a post")
    st.page_link("SMedia.py", label="Home", icon="🏠")
    

with col3:
    #st.write("This is the Post page")
    st.page_link("SMedia.py", label="Post feeds", icon="📝")

#st.page_link("pages/Trending.py", label="# Tag Trending", icon="🔥")
#st.page_link("pages/Post.py", label="Post", icon="📝")
#st.page_link("http://www.google.com", label="Google", icon="🌎")

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
#st.title("Social Media Hashtag Trend Analyser")
#st.page_link("SMedia.py", label="Home", icon="🏠")

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
    
    

# Create a text area for user to enter post content


if 'text_value' not in st.session_state:
    st.session_state.text_value = ""
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

post_cont= st.text_area("Enter your post here",key=st.session_state.text_value,placeholder="#Tag1 #Tag2 #Tag3 , Post")
post_tags = re.findall(r"#(\w+)", post_cont)  # Extract hashtags from post content
#post_desc = re.sub(r"#(\w+)", "", post_cont).strip()  # Extract post description
post_id = get_next_id() # Get the next post ID
#st.write(type(post_id))
post_text=json.dumps({"postid":post_id,"post_content": post_cont, "tags": post_tags}) # Create a JSON object 
#st.write(post_text)

def clear_text(): 
        st.session_state.text_value = " "
        #st.session_state.rerun_trigger = True # to trigger rerun
        st.session_state.text_value = post_cont
#def refresh_page():
 #   st.experimental_rerun()
  #  st.button("Refresh", on_click=refresh_page)

col7, col6 = st.columns([2, 1])
with col7:
    if st.button("Post"):
        post_info(post_text)
        st.session_state.text_value = " "

col4, col5 = st.columns([9, 1])
with col5:
    if st.button("Clear"):
        st.session_state.button_clicked = True  # Change session state to trigger rerun
        clear_text()



if st.session_state.button_clicked:
    #st.write("The refreshed")
    st.session_state.text_value = post_cont
    clear_text()
    st.session_state.button_clicked = False 

    

# Function to fetch posts from an API
def fetch_posts():
    url = "https://go07cpukrh.execute-api.ap-south-1.amazonaws.com/Post-Stage"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching posts: {e}")
        return []
    
# Function to display posts
def display_posts(posts):
    if posts:
        st.subheader("Latests Posts")
        posts = sorted(posts, key=lambda x: x['postid'], reverse=True)


        #post_id = st.selectbox("Select Post ID", [post['postid'] for post in posts])
        #selected_post = next((post for post in posts if post['postid'] == post_id), None)
        #if selected_post:
         #   st.write(f"Post ID: {selected_post['postid']}")
          #  st.write(f"Content: {selected_post['post_content']}")
        for post in posts:
            st.write(f"{post['post_content']}")
            #st.write(f"Description: {post['description']}")
            st.write("-----")
    else:
        st.write("No posts available at the moment.")

# Fetch and display posts
posts = fetch_posts()
content = posts['body']
#st.write(content)

#st.write(posts)
display_posts(content)

