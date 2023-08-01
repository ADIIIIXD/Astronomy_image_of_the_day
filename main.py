import streamlit as st
import requests as rq

key = "y7AqcfwZiVfshfvdKwC0VXXeRbb1MUHk31Exop6X"
url = f"https://api.nasa.gov/planetary/apod?api_key={key}"

# requesting data and stored in json format
response = rq.get(url)
content = response.json()

# extracting values from content
date = content["date"]
explanation = content["explanation"]
title = content["title"]

# processing image
image_url = rq.get(content["hdurl"])
image = image_url.content
with open("img.jpg", "wb") as file:
    file.write(image)

# streamlit webpage
st.set_page_config(layout="wide")

cl1, cl2, cl3 = st.columns([0.5, 3, 0.5])
with cl2:
    st.title(title)
    st.subheader(date)
    st.image("img.jpg")
    st.info(explanation)
