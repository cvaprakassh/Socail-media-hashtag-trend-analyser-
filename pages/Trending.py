import streamlit as st
import requests
from collections import Counter

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
content=trending_hashtags['body']

#display trending hashtags
# Count the occurrences of each hashtag
hashtag_counts = Counter()
for item in content:
    hashtags = item.get('tags', [])
    hashtag_counts.update(hashtags)

# Sort hashtags by count in descending order
sorted_hashtags = sorted(hashtag_counts.items(), key=lambda x: x[1], reverse=True)

# Display sorted hashtags with their counts
st.subheader("Trending Hashtags with Counts")
for hashtag, count in sorted_hashtags:
    st.write(f"#{hashtag} 🔥 {count}")

#if content:
 #   st.subheader("Trending Hashtags")
  #  for hashtag in content:
   #     st.write(f"#{hashtag['tags']}")
#else:
 #   st.write("No trending hashtags available at the moment.")

#st.write(trending_hashtags)
