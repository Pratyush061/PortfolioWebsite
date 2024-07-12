import streamlit as st



def load_page(page_name):
        with open("Clock.py" , encoding="utf8") as f:
            exec(f.read(), globals())




# CSS styles file
with open("projects.css") as f:
   st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Project section
st.markdown("""
<div class="container">
    <div class="project-title">Movie Recommender System | Python, Pandas, NLP, Bag of Words</div>
    <div class="project-details">
        <ul>
            <li>Developed a content-based movie recommendation system using Python and pandas.</li>
            <li>Identified important columns for recommendation, including genres, keywords, overview, cast, and crew.</li>
            <li>Used NLP techniques such as stemming to preprocess textual data.</li>
            <li>Implemented a bag-of-words approach using Count Vectorizer to represent movie tags.</li>
            <li>Deployed the model using Streamlit and Heroku.</li>
        </ul>
    </div>
</div>

<div class="container">
    <div class="project-title">Plant Disease Classification | Python, TensorFlow</div>
    <div class="project-details">
        <ul>
            <li>Utilized the Plant Village dataset containing images of healthy and diseased plant leaves for multiple plant species.</li>
            <li>Implemented data augmentation techniques such as random flipping and rotation to increase model robustness and generalization.</li>
            <li>Designed a CNN architecture consisting of convolutional and pooling layers followed by fully connected layers for classification.</li>
            <li>Utilized the Adam optimizer and Sparse Categorical Cross-entropy loss function for model training.</li>
            <li>Achieved a high accuracy of 97.7% on the test set after running for 32 epochs.</li>
        </ul>
    </div>
</div>

<div class="container">
    <div class="project-title">Drug Target Prediction | Python, TensorFlow, Matplotlib</div>
    <div class="project-details">
        <ul>
            <li>Data Preparation: Loaded the dataset from a CSV file containing columns for SMILES notation, protein sequences, and a target property (pKd).</li>
            <li>Data Preprocessing: Tokenized the SMILES and protein sequences using Keras' Tokenizer, and then padded to ensure uniform sequence length. Converted target property values into numpy arrays.</li>
            <li>Model Building: Constructed a deep learning model using Keras' Functional API. The model architecture included separate branches for processing the SMILES and protein sequences, followed by max pooling, concatenated, and additional dense layers for prediction.</li>
            <li>Model Training: Compiled the model with an Adam optimizer and Mean Squared Error (MSE) loss function. Trained on the training data with early stopping to prevent overfitting.</li>
        </ul>
    </div>
</div>

<div class="container">
    <div class="project-title">OpenCV AI Virtual Keyboard | OpenCV, MediaPipe, PyAutoGUI</div>
    <div class="project-details">
        <ul>
           <li>Taking inspiration from Murtaza Sir YouTube channel I developed and customized the AI virtual keyboard  </li>
            <li>Developed a Virtual Keyboard using Computer Vision with real-time webcam feed integration, hand tracking, gesture recognition, and keyboard control.</li>
            <li>Implemented functionality for keypress detection and text input based on hand gestures.</li>
            <li>Provided dynamic background options for user customization.</li>
        </ul>
    </div>
</div>
<div class="container">
    <div class="project-title">Image Classification System | Python, TensorFlow, OpenCV, Deep Learning</div>
    <div class="project-details">
        <ul>
            <li>Built a data pipeline for image processing.</li>
            <li>Preprocessed images for deep learning using OpenCV.</li>
            <li>Created a deep neural network classifier with TensorFlow.</li>
            <li>Evaluated model performance through training and validation metrics.</li>
            <li>Deployed the model and tested with new data.</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)


st.subheader(" ")
st.subheader("Miscellaneous Projects By me")



# Load the selected page
load_page(page)

st.subheader("And the list goes on....")







