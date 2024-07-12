import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import base64

# st.image('images/bear_telephone.png')

import base64



import streamlit as st
import base64



# Your Streamlit map code
with st.container():
    col1, col2 = st.columns([3, 1])  # Adjust column widths as needed



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("contact.css")

# Profile image file
with open("images/contact.png", "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


st.markdown(f"""


<div class="container">
  <div class="content">
    <img src="{img}" class="image" alt="Image Description">
  </div>
</div>
""", unsafe_allow_html=True)

#
#
# # Inject custom CSS
# st.markdown(container_style, unsafe_allow_html=True)



# Custom latitude and longitude

city_coordinates = {
    'lat': [22.7196],  # Latitude of City
    'lon': [75.8577]  # Longitude of City
    }

# Create DataFrame
df = pd.DataFrame(city_coordinates)

# Display the map
st.map(df)

col1,col2=st.columns([1,1])

with col1:
    import streamlit as st

    # Define the HTML and CSS styling
    contact_info = """
        <style>
            .contact-info {
                max-width: 400px;
                margin: auto;
                padding: 20px;
                background-color: #f9f9f9;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .contact-info h3 {
                font-size: 24px;
                color: #333;
                margin-bottom: 10px;
            }
            .contact-info p {
                font-size: 18px;
                color: #666;
                margin-bottom: 5px;
            }
        </style>
        <div class="contact-info">
            <h3>Reach out to Me!!</h3>
            <p>+0123456789</p>
            <p>pratyushjj02@gmail.com</p>
            <p>INDORE, M.P.</p>
        </div>
    """

    # Render the contact information with styled CSS
    st.markdown(contact_info, unsafe_allow_html=True)

# -----------------  contact  -----------------

with col2:
    st.write(" ")
    st.subheader("📨 Contact Me")
    # Define the contact form HTML with added classes
    contact_form = """
        <style>
            .contact-form {
                max-width: 400px;
                margin: auto;
                padding: 20px;
                background-color: #f9f9f9;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .contact-form input[type="text"],
            .contact-form input[type="email"],
            .contact-form textarea {
                width: 100%;
                padding: 10px;
                margin: 5px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
                box-sizing: border-box;
            }
            .contact-form textarea {
                height: 150px;
            }
            .contact-form button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                float: right;
            }
            .contact-form button:hover {
                background-color: #45a049;
            }
        </style>
        <div class="contact-form">
            <form action="https://formsubmit.co/pjdev02@gmail.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <br>
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>
        </div>
    """

    # Render the contact form with styled CSS
    st.markdown(contact_form, unsafe_allow_html=True)