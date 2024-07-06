
# api_key = st.secrets['GOOGLE_API_KEY']
import streamlit as st

api_key="AIzaSyC83C8rwcxdmSsR5b4bUj_EjywHCsmn9gE"
# genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

# Load the image
image_path = 'About_Me.jpeg'

text = ("Hello! I'm Pratyush Jain, a passionate"
        " B.Tech student specializing in Information Technology at"
        " Shri G.S. Institute Of Technology And Science, Indore, Madhya Pradesh."
        " My journey in the world of technology and innovation has equipped me with strong skills in programming, data structures, algorithms, and several key areas of computer science.")

# Custom CSS for styling columns and containers
container_style = """
        <style>
        /* Style columns */
        [data-testid="column"] {
            box-shadow: rgb(0 0 0 / 50%) 0px 2px 10px -1px, rgb(0 0 0 / 14%) 0px 1px 1px 0px, rgb(0 0 0 / 12%) 0px 1px 3px 0px;
            border-radius: 100px;
            padding: 10% 5% 5% 4.5%;
        }

        }
        </style>
        """

# Inject custom CSS
st.markdown(container_style, unsafe_allow_html=True)

# Streamlit layout

# <-----Streamlit Application for the Typewriter Effect ---->

col1, col2 = st.columns(2)

with col1:
    st.subheader('Hi 👏🏿')
    st.title("Pratyush J.👦🏻")
    st.write(text)

with col2:
    st.subheader(" ")
    st.image(image_path)

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


    if st.button("ASK", use_container_width=100):
        response = model.generate_content(prompt)
        st.write(response.text)


# st.title("Skills")
#
# color = st.select_slider(
#     "Select a color of the rainbow",
#     options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"])
# st.write("My favorite color is", color)

with st.container(border=True):
    # Title
    st.title("Skills 🤹🏻")

# # Skill sliders
# programming = st.slider("Programming", 0, 100, 70)
# machine_learning = st.slider("Machine Learning", 0, 100, 40)
# computer_vision = st.slider("Computer Vision", 0, 100, 60)
# web_development = st.slider("Web Development", 0, 100, 40)


    # Data for pie chart
    skills_data = {
        'Skills': ['Programming', 'Machine Learning', 'Computer Vision', 'Web Development'],
        'Proficiency': [70, 50, 60, 40]
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
    explode_values = [0, 0.2, 0, 0]   # Set burst effect for the second slice (index 1)
    fig.update_traces(pull=explode_values)  # Apply explosion

# Additional customizations (adjust as needed)
    fig.update_traces(textposition='inside', textfont_size=14, textinfo='percent+label')
    fig.update_layout(
        paper_bgcolor='rgba(255,100,100,0.4)',  # Set a semi-transparent background
        font={'color': 'white'}  # Set white text color for better contrast
    )

# Display the pie chart with burst effect
    st.plotly_chart(fig)
