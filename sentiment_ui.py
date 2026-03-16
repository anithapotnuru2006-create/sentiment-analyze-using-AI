import streamlit as st
from textblob import TextBlob
import base64

# Function to set background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        h1, h2, h3, h4, h5, h6, p, label {{
            color: white !important;
            font-weight: bold;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function
add_bg_from_local("photo.jpeg")
# Page title
st.title("Sentiment Analysis ")

st.write("Enter a paragraph to check whether it is Positive, Negative, or Neutral.")

# Text input
text = st.text_area("Enter your text here")

if st.button("Analyze Sentiment"):

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity 

    if polarity > 0:
        st.success("Positive Sentiment 😊")#Green color
        
    elif polarity < 0:
        st.error("Negative Sentiment 😞")#Red color
       
    else:
        st.info("Neutral Sentiment 😐")