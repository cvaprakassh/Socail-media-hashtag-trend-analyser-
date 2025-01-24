import streamlit as st
import requests

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
        st.subheader("Posts")
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