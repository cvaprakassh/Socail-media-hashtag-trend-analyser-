import streamlit as st
st.page_link("your_app.py", label="Home", icon="🏠")
st.title(" Blue[#Tag analyser] :sunglasses:")
st.page_link("pages/Trending.py", label="# Tag Trending", icon="🔥")
st.page_link("pages/post.py", label="Post", icon="📝")
#st.page_link("http://www.google.com", label="Google", icon="🌎")

post= st.text_area("Enter your post here","",placeholder="#Tag1 #Tag2 #Tag3 , Post")