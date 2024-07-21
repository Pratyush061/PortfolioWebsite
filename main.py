# Importing the necessary libraries
from io import BytesIO
import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
import google.generativeai as genai
import os
from streamlit_navigation_bar import st_navbar
from io import BytesIO
import streamlit as st
import time
import pandas as pd
import numpy as np
import plotly.express as px

# Set up the navigation bar
pages = ["Home", "About Me","Projects","Contact Me"]

# In about me section you can add your own custom chatbot.
page = st_navbar(pages)

# Define a function to handle navigation
def load_page(page_name):
    if page_name == "Home":
        with open("Home.py", encoding="utf8") as f:
            exec(f.read(), globals())
    elif page_name=="About Me":
        st.markdown("# Hi 👏🏿")
        with open("About_Me.py", encoding="utf8") as f:
            exec(f.read(), globals())
    elif page_name == "Projects":
        st.title("Projects 🪄")
        with open("Projects.py", encoding="utf8") as f:
            exec(f.read(), globals())
    elif page_name == "Contact Me":
        st.title("Contact Me 📞")
        with open("Contact_Me.py", encoding="utf8") as f:
            exec(f.read(), globals())

# Load the selected page
load_page(page)
