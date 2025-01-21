import streamlit as st
import requests
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
    st.page_link("pages/Home.py", label="Create Post", icon="✍️")

with col3:
    #st.write("This is the Post page")
    st.page_link("pages/Post.py", label="Post Feeds", icon="📝")

#st.page_link("pages/Trending.py", label="# Tag Trending", icon="🔥")
#st.page_link("pages/Post.py", label="Post", icon="📝")
#st.page_link("http://www.google.com", label="Google", icon="🌎")

# Function to fetch trending hashtags from an API
def fetch_trending_hashtags():
    url = "https://go07cpukrh.execute-api.ap-south-1.amazonaws.com/Post-Stage"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching trending hashtags: {e}")
        return []

# Display trending hashtags
trending_hashtags = fetch_trending_hashtags()
if trending_hashtags:
    st.subheader("Trending Hashtags")
    st.write(trending_hashtags) 
    for hashtag in trending_hashtags:
        st.write(f"#{hashtag}")
else:
    st.write("No trending hashtags available at the moment.")