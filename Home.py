# Imporing the necessary Libraries

from io import BytesIO
import base64
import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
import google.generativeai as genai
import os
# <------Imported the libraries------>

# Generative AI model API key

# api_key = st.secrets['GOOGLE_API_KEY']
api_key="AIzaSyC83C8rwcxdmSsR5b4bUj_EjywHCsmn9gE"
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

#<-------  API Key  --------->

# Define the info dictionary (replace the example values with your actual data)
info = {
   "Pronoun": "his",
   "Name": "Pratyush",
   "Full_Name": "Pratyush Jain",
   "Intro": "A passionate Data Scientist and Computer Vision Engineer",
   "About":"Student⚜️Freelancer⚜️Youtuber⚜️Avid book reader",

   "City":"Indore, India",
   "Email": "pjdev02@gmail.com"
}





# Load Lottie animation from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Apply local CSS styles from a file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("container.css")

# # Load Lottie animations
lottie_gif = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
java_lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
AI_lottie = load_lottieurl("https://lottie.host/14b33d36-44aa-4562-a63d-2759cde9e9f3/bfpFyUPZKC.json")
blank_lottie = load_lottieurl("https://lottie.host/631d38ac-8e17-4d59-a811-caf8a72f4310/LJxyJQOw1t.json")
webd = load_lottieurl("https://lottie.host/2e31f940-2dd6-4db0-aa6a-d31e7961ad48/B3047KhCSd.json")


# Profile image file
with open("images/Home.jpg", "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# Embedding the HTML with CSS class for each container

st.markdown(f"""
<div class="container">
    <div class="content">
        <div class="text">
            <h1>PRATYUSH JAIN.👨🏻‍💻 & 🍵</h1>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.write(" ")

st.markdown(f"""
<div class="container">
    <div class="content">
        <div class="box">
            <div class="spin-container">
                <div class="shape">
                    <div class="bd">
                        <img src="{img}" alt="Profile Image">
                    </div>
                </div>
            </div>
        </div>
        <div class="text">
            <p>{info['About']}</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


st.write(" ")
# ----------------- skillset ----------------- #



# Content wrapped in the styled container
with st.container(border=True):
    st.subheader('🏢 Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=70, width=70, key="python", speed=2.5)
    with col1:
        st_lottie(blank_lottie, height=70, width=70, key="blnk", speed=2.5)
    with col2:
        st_lottie(blank_lottie, height=70, width=70, key="blank", speed=2.5)
    with col2:
        st_lottie(AI_lottie, height=100, width=100, key="AI", speed=2.5)
    with col3:
        st_lottie(github_lottie, height=70, width=70, key="github", speed=2.5)
    with col4:
        st_lottie(blank_lottie, height=70, width=70, key="blk", speed=2.5)
    with col4:
        st_lottie(webd, height=100, width=100, key="webd", speed=1)
