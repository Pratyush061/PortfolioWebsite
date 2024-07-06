# Imporing the necessary Libraries

from io import BytesIO
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
   "About":"I am passionate about computers and i vouch for them i have made several project in the field on Computer Vision and Natural Language processing ",
   "Tableau":"https://public.tableau.com/app/profile/vickytc/viz/SunnybrookTeam/Overview",
   "Medium":"https://medium.com/@vicky-note/about",
   "City":"Indore, India",
   "Photo":"""<a href=\"https://www.linkedin.com/in/vicky-tck/\"><img src=\"https://sn-assets.s3.us.cloud-object-storage.appdomain.cloud/projects/profile.png" width=\"200\"   alt=\"Profile\" title=\"Profile\"></a>""",
   "Email": "pjdev02@gmail.com"
}

embed_rss= {
    'rss':"""<div style="overflow-y: scroll; height:500px; background-color:green;"> <div id="retainable-rss-embed" 
        data-rss="https://medium.com/feed/@vicky-note"
        data-maxcols="3" 
        data-layout="grid"
        data-poststyle="inline" 
        data-readmore="Read the rest" 
        data-buttonclass="btn btn-primary" 
        data-offset="0"></div></div> <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>"""
}

# # Set the page configuration
# st.set_page_config(page_title='Template', layout="wide", page_icon='👧🏻')

# Load Lottie animation from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Apply local CSS styles from a file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#local_css("style/style.css")

# Load Lottie animations
lottie_gif = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
java_lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
docker_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
figma_lottie = load_lottieurl("https://lottie.host/5b6292ef-a82f-4367-a66a-2f130beb5ee8/03Xm3bsVnM.json")
js_lottie = load_lottieurl("https://lottie.host/fc1ad1cd-012a-4da2-8a11-0f00da670fb9/GqPujskDlr.json")

# # Display the photo in the sidebar
# st.sidebar.markdown(info['Photo'], unsafe_allow_html=True)

# Info section

def gradient(color1, color2, color3, content1, content2):
    st.markdown(
        f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
        f'<span style="color:{color3};">{content1}</span><br>'
        f'<span style="color:white;font-size:17px;">{content2}</span></h1>',
        unsafe_allow_html=True
    )

with st.container():
    col1, col2 = st.columns([8, 3])
    full_name = info['Full_Name']
    with col1:
        gradient('#FFD4DD', '#000395', 'e0fbfc', f"Hi, I'm {full_name}👋", info["Intro"])
        st.write("")
        st.write(info['About'])
    with col2:
        st_lottie(lottie_gif, height=280, key="data")
# ----------------- skillset ----------------- #


with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=70, width=70, key="python", speed=2.5)
    with col2:
        st_lottie(java_lottie, height=70, width=70, key="java", speed=4)
    with col3:
        st_lottie(my_sql_lottie, height=70, width=70, key="mysql", speed=2.5)
    with col4:
        st_lottie(git_lottie, height=70, width=70, key="git", speed=2.5)
    with col1:
        st_lottie(github_lottie, height=50, width=50, key="github", speed=2.5)
    with col2:
        st_lottie(docker_lottie, height=70, width=70, key="docker", speed=2.5)
    with col3:
        st_lottie(figma_lottie, height=50, width=50, key="figma", speed=2.5)
    with col4:
        st_lottie(js_lottie, height=50, width=50, key="js", speed=1)



# ----------------- timeline ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('📌 Career Snapshot')

    # load data
    with open('example.json', "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=400)



# -----------------  projects  -----------------  #
with st.container():
    st.markdown("""""")
    st.subheader("⚒️ My Projects")
    col1, col2 = st.columns([0.95, 0.05])
    with col1:
        with st.expander('See the Projects'):
            components.html(
                """
                <!DOCTYPE html>
                <html>  
                    <title>Basic HTML</title>  
                    <body style="width:130%">  
                        <div class='projectsPlaceholder' id='viz1684205791200' style='position: static'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Su&#47;SunnybrookTeam&#47;Overview&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='SunnybrookTeam&#47;Overview' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Su&#47;SunnybrookTeam&#47;Overview&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684205791200');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1350px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='1550px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1350px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='1550px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.minHeight='5750px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
                    </body>  
                </HTML>
                """
                , height=400, scrolling=True
            )
    st.markdown(""" <a href={}> <em>🔗 access to the link </a>""".format(info['Tableau']), unsafe_allow_html=True)

# ----------------- medium ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('✍️ Medium')
    col1, col2 = st.columns([0.95, 0.05])
    with col1:
        with st.expander('Display my latest posts'):
            components.html(embed_rss['rss'], height=400)

        st.markdown(""" <a href={}> <em>🔗 access to the link </a>""".format(info['Medium']), unsafe_allow_html=True)

## You can add Something Here

    # -----------------  contact  ----------------- #
    with col1:
        st.subheader("📨 Contact Me")
        contact_form = f"""
        <form action="https://formsubmit.co/{info["Email"]}" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)


#
# # Load and rotate the image
# image_path = 'images/20240626_111515.jpg'
# image = Image.open(image_path)
# rotated_image = image.rotate(270)  # Rotate the image by 90 degrees
#
# # Streamlit layout
# col1, col2 = st.columns(2)
#
# with col1:
#
#     st.title("Pratyush Jain")
#
# with col2:
#     st.image(rotated_image)
#
# st.subheader(' ')
# st.title("ABOUT ME ")
#
# # st.markdown("") # for changing the background
#
# user_question = st.text_input("")
#
# persona="""
#
# You are Pratyush AI bot. You help people answer questions about your self (i.e Murtaza)
#  Answer as if you are responding . dont answer in second or third person.
#  If you don't know they answer you simply say "That's a secret"
#
#
# Pratyush Jain is a dedicated and enthusiastic B.Tech student specializing in Information Technology at Shri G.S. Institute Of Technology And Science, Indore, Madhya Pradesh. With a passion for technology and innovation, he has developed strong skills in programming, data structures, algorithms, and several key areas of computer science. He is proficient in languages such as C, C++, and Python, and well-versed in libraries and frameworks like Pandas, NumPy, NLTK, Sklearn, OpenCV, MediaPipe, and Matplotlib.
#
# Pratyush has undertaken several impactful projects. He developed a Movie Recommender System using Python and NLP techniques, achieving effective content-based recommendations. His work on Plant Disease Classification involved a robust CNN model, reaching a 97.7% accuracy on test data. In the Drug Target Prediction project, he created a deep learning model that processed molecular and protein sequence data to predict drug interactions. Additionally, he built an OpenCV AI Virtual Keyboard, incorporating real-time hand tracking and gesture recognition.
#
# Recognized for his problem-solving abilities, Pratyush is a 4-star coder on HackerRank and has received bronze medals on Kaggle for his contributions to notebooks and discussions. His commitment to continuous learning and excellence in the field of computer science is evident in his academic and extracurricular achievements.
#
# Pratyush is based in Ujjain, Madhya Pradesh, and can be contacted via email at pratyushjj02@gmail.com. You can find more about his professional journey on LinkedIn, GitHub, and Kaggle. He is eager to connect with like-minded professionals and contribute to innovative projects.
#
# Contact Information:
#
# Phone: +91-7987517018
# Email: pratyushjj02@gmail.com
# LinkedIn: LinkedIn Profile
# GitHub: GitHub Profile
# Kaggle: Kaggle Profile
#
# """
#
#
#
#
# if st.button("ASK" , use_container_width=500):
#     prompt=persona+"Here is the question that the user asked: "+user_question
#     response = model.generate_content(prompt)
#     st.write(response.text)
#
#  #components.html("""thecode""")
#
# #I can upload the resume and the custom chatbots give the answer to the user
#
# col1,col2=st.columns(2)
# st.title(" ")
#
# with col1:
#     st.subheader("My channel")
#     for i in range(5):
#         st.write("My channel name is The best")
#
# with col2:
#     st.video("https://youtu.be/BFlRmIvqwSA?si=a6qL3krtRgqVIKOZ")
#
#
# #                       <---Day 1 Ended --->
#
# st.subheader(" ")
# st.title("My Setup")
#
# st.image("images/setup.jpg")
#
# st.write(" ")
# st.title("My Skills")
#
# st.slider("Programming Skills",0,100,70)
# st.slider("Robotics Skills",0,100,20)
# st.slider("Teaching Skills",0,100,50)
#
# st.title("Gallery")
#
# col1,col2,col3=st.columns(3)
#
# #Try nested loops
# with col1:
#     st.image("images/g1.jpg")
#     st.image("images/g2.jpg")
#     st.image("images/g3.jpg")
#
# with col2:
#     st.image("images/g4.jpg")
#     st.image("images/g5.jpg")
#     st.image("images/g6.jpg")
#
# with col3:
#     st.image("images/g7.jpg")
#     st.image("images/g8.jpg")
#     st.image("images/g9.jpg")
#
# st.write(" ")
#
# st.write("Contact Us")
#
# st.title("For any inquiries,please contact me at")
#
# st.write("pjdev02@gmail.com")
#
#
#
#
# #
# # x = st.slider('Programming Skills')  # 👈 this is a widget
# # st.write(x, 'squared is', x * x)
# #
# # st.text_input("Your name", key="name")
# #
# #
# # if st.checkbox('Show emojis'):
# #     st.write("🤖🤖🤖😊😊😊")
# #
# #
# # FAQs= ["What is your name " ,"Where do you belong to","What is your lucky number?"]
# #
# # Answers=["My name is Pratyush","I am from Ujjain","69"]
# #
# # options = st.selectbox(
# #     'Some FAQs?',FAQs
# # )
# # # options="What is your name"
# #
# # # if options in FAQs:
# # #     st.write(Answers)
# #
# # for key,i in enumerate(FAQs):
# #     if i==options:
# #         st.write(Answers[key])
# #
# #
# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )
#
# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )
#
# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')
#
# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")
#
#
#





















# import time
#
# 'Starting a long computation...'
#
# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)
#
# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)
#
# '...and now we\'re done!'


