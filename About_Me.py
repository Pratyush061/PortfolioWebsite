
# api_key = st.secrets['GOOGLE_API_KEY']
# Imporing the necessary Libraries
import base64
import threading
from io import BytesIO
import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
import google.generativeai as genai
import os
api_key="AIzaSyC83C8rwcxdmSsR5b4bUj_EjywHCsmn9gE"
# genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

# Load the image
image_path = 'images/About_Me.jpeg'


text = (
        "Passionate Data Scientist | "
        "Python & ML Enthusiast |"
        " NLP & Deep Learning "
        "| Computer Vision"
        "| Algorithm "
        "| AI-driven Solutions "
        "| Seeking to Innovate and Transform with Data."
       )


# Custom CSS for styling columns and containers
container_style = """
<style>
/* Style columns */


[data-testid="column"] {
    box-shadow: 0px 4px 12px  rgba(0, 0, 0, 5), 0px 1px 3px rgba(0, 0, 0, 8);
    border-radius: 20px;
    padding: 20px;
    background-color: #a5f9f9;
    transition: transform 0.5s;
    # animation-name: example;
    # animation-duration: 4s;
}

[data-testid="column"]:hover {
    transform: scale(1.04);
}

/* Style container for the image */
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    padding: 18px;
}

.container img {
    border-radius: 50%;
    max-width: 90%;
    height: auto;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    margin-top: 20px;
    margin-bottom: 20px;
}

</style>
"""


# Profile image file
with open("images/About_Me.jpeg", "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


 # CSS styles file
with open("imganimation.css") as f:
   st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)




# Inject custom CSS
st.markdown(container_style, unsafe_allow_html=True)

# Streamlit layout

# <-----Streamlit Application for the Typewriter Effect ---->

custom_col1, custom_col2 = st.columns(2)

 # CSS styles file
with open("Typewriter.css") as f:
    st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)



with custom_col1:
    # Display the typewriter text
    st.markdown(f"""
            <div class="heading">
                <h1>{"Hello! I am"}</h1>
            </div>
            """, unsafe_allow_html=True)
    st.markdown(f"""
        <div class="typewriter">
            <h1>{"Pratyush J.👦🏻"}</h1>
        </div>
        """, unsafe_allow_html=True)
    st.write(text)

with custom_col2:
    st.write(f"""
    <div class="container">
        <div class="box">
            <div class="spin-container">
                <div class="shape">
                    <div class="bd">
                        <img src="{img}" alt="Profile Image" >
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# <<<<-----Streamlit Typewriter Effect------>>>>>>>>



with st.container(border=True):

    st.title("Know More About Me 🎯")


# st.write("Ask anything About Me ")

# st.markdown("") # for changing the background

# Load Lottie animation from a URL

#<---- Loading Animations Using Lottie ------>
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

# Apply local CSS styles from a file
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"""{f.read()}</style>""", unsafe_allow_html=True)

#local_css("style/style.css")

# Load Lottie animations
    lottie_gif = load_lottieurl("https://lottie.host/54a91536-4fd5-4d10-8041-827cbce8060f/RPTxx1bRNf.json")


    st_lottie(lottie_gif, height=250, key="data")

# <----- Animations loading completed------>

    option = st.selectbox(
        "What you want to Ask?",
        ("About Me", "General questions"))


    persona ="""

    You are Pratyush AI bot. You help people answer questions about your self (i.e Murtaza)
    Answer as if you are responding . dont answer in second or third person.
    If you don't know they answer you simply say "That's a secret"


    Pratyush Jain is a dedicated and enthusiastic B.Tech student specializing in Information Technology at Shri G.S. Institute Of Technology And Science, Indore, Madhya Pradesh. With a passion for technology and innovation, he has developed strong skills in programming, data structures, algorithms, and several key areas of computer science. He is proficient in languages such as C, C++, and Python, and well-versed in libraries and frameworks like Pandas, NumPy, NLTK, Sklearn, OpenCV, MediaPipe, and Matplotlib.

    Pratyush has undertaken several impactful projects. He developed a Movie Recommender System using Python and NLP techniques, achieving effective content-based recommendations. His work on Plant Disease Classification involved a robust CNN model, reaching a 97.7% accuracy on test data. In the Drug Target Prediction project, he created a deep learning model that processed molecular and protein sequence data to predict drug interactions. Additionally, he built an OpenCV AI Virtual Keyboard, incorporating real-time hand tracking and gesture recognition.

    Recognized for his problem-solving abilities, Pratyush is a 4-star coder on HackerRank and has received bronze medals on Kaggle for his contributions to notebooks and discussions. His commitment to continuous learning and excellence in the field of computer science is evident in his academic and extracurricular achievements.
    
    
    Pratyush is based in Ujjain, Madhya Pradesh, and can be contacted via email at pratyushjj02@gmail.com. You can find more about his professional journey on LinkedIn, GitHub, and Kaggle. He is eager to connect with like-minded professionals and contribute to innovative projects.

    Contact Information:

    Phone: +91-7987517018
    Email: pratyushjj02@gmail.com
    LinkedIn: LinkedIn Profile
    GitHub: GitHub Profile
    Kaggle: Kaggle Profile

    """
    user_question = st.text_input(" ")
    if option == "About Me":
        prompt = persona + "Here is what the user asked: " + user_question
    elif option == "General questions":
        prompt = user_question
    else:
        prompt = "Wrong option selected"


    # Logic to handle the button click and generate response
    if st.button("ASK", use_container_width=100):
        response = model.generate_content(prompt)
        st.write(response.text)



with st.container(border=True):
    # Title
    st.title("Skills 🤹🏻")


    # Data for pie chart
    skills_data = {
        'Skills': ['Programming', 'Machine Learning', 'Computer Vision', 'Web Development'],
        'Proficiency': [70, 60, 50, 40]
    }

    df = pd.DataFrame(skills_data)

    # Define custom colors for pie slices
    colors = ['royalblue', 'coral', 'white', 'gold']  # Adjust colors as desired

    # Create pie chart with customizations and burst effect
    fig = px.pie(
        df,
        values='Proficiency',
        names='Skills',
        title='Skills Proficiency',
        color_discrete_sequence=px.colors.sequential.speed,  # Set custom colors
        hole=.3,        # Adjust hole size for donut effect (0 for full pie)
    )


# You can get color scales from:https://plotly.com/python/builtin-colorscales/

# Apply burst effect to a specific slice (adjust index for desired slice)
    explode_values = [0, 0 ,0.15, 0]   # Set burst effect for the second slice (index 1)
    fig.update_traces(pull=explode_values)  # Apply explosion

# Additional customizations (adjust as needed)
    fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent+label')
    fig.update_layout(
        paper_bgcolor='rgba(153,51,51,0.3)',  # Set a semi-transparent background
        font={'color': 'white'}  # Set white text color for better contrast
    )

# Display the pie chart with burst effect
    st.plotly_chart(fig)

