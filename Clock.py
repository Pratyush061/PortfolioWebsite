from io import BytesIO

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import datetime
from PIL import Image
import time

def draw_clock():
    now = datetime.datetime.now()
    fig, ax = plt.subplots()

    # Draw clock face
    clock_face = plt.Circle((0.5, 0.5), 0.4, color='white', ec='black')
    ax.add_artist(clock_face)

    # Draw hour marks
    for i in range(12):
        angle = np.deg2rad(60-i * 30)  # Subtract 90 degrees to start at the top
        x = 0.5 + 0.35 * np.cos(angle)
        y = 0.5 + 0.35 * np.sin(angle)
        ax.text(x, y, str(i + 1), horizontalalignment='center', verticalalignment='center')

    # Calculate hand positions
    second_angle = np.deg2rad((90-6*now.second)) #This is correct
    minute_angle = np.deg2rad(90-(6 * now.minute+now.second/10)) #This is also correct
    hour_angle = np.deg2rad(90-(30 * (now.hour % 12 + now.minute / 60)))
  # Account for minute contribution

    # st.write(now.second)
    # st.write(now.minute)
    # st.write(now.hour)

    # Draw hands
    ax.plot([0.5, 0.5 + 0.35 * np.cos(second_angle)], [0.5, 0.5 + 0.35 * np.sin(second_angle)], color='red')
    ax.plot([0.5, 0.5 + 0.3 * np.cos(minute_angle)], [0.5, 0.5 + 0.3 * np.sin(minute_angle)], color='black')
    ax.plot([0.5, 0.5 + 0.2 * np.cos(hour_angle)], [0.5, 0.5 + 0.2 * np.sin(hour_angle)], color='black', linewidth=3)

    # Set limits and aspect
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    # Convert plot to image
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img = Image.open(buf)
    plt.close(fig)

    return img

# Streamlit app
st.title('Analog Clock')
st.subheader("The current time is:")

placeholder = st.empty()

if 'running' not in st.session_state:
    st.session_state.running = False


col1,col2=st.columns(2)
if col1.button("Start the Clock"):
    st.session_state.running = True

if col2.button("End the Clock"):
    st.session_state.running = False

placeholder = st.empty()

img = draw_clock()
placeholder.image(img)

while st.session_state.running:
    new_img = draw_clock()  # Update the clock image
    placeholder.image(new_img) # Update the image in the placeholder


