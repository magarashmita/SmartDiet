import streamlit as st
from PIL import Image

import base64

import streamlit as st

st.markdown("""
    <style>
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 10vh;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='centered'><h1 style='color: #2c3e50;'>About Us!</h1></div>", unsafe_allow_html=True)



def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:pages/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('about.jpg')

def about_us():
    

    html = """
       <div style="background-color:#F0F0F0;padding:10px;border-radius:10px; margin-top:20px">
            <p>Welcome to our diet recommendation page! Our mission is to provide you with personalized diet recommendations based on your unique needs and preferences. We believe that a healthy diet is essential for a healthy lifestyle, and we want to help you achieve your health goals.</p>
        </div>

        <div style="background-color:#F0F0F0;padding:10px;border-radius:10px; margin-top:20px">
            <h2 style="color:#FFA500">Our Team</h2>
            <p>We are a group of three Bachelor of Science in Computer Science and Information Technology students, Ashmita Thapa Magar, Neha Lama Tamang, and Rinu Maharjan, who have developed a web application as part of our project work for the 7th semester of our degree program.</p>
        </div>

        <div style="background-color:#F0F0F0;padding:10px;border-radius:10px;margin-top:20px">
            <h2 style="color:#FFA500">Application</h2>
            <p> Our application is focused on providing diet recommendations to users based on their dietary preferences, health goals, and other factors. Our application uses a variety of algorithms and data sources to provide users with personalized recommendations. We have also included features that allow users to track their progress, set reminders, and share their progress with friends and family. We are passionate about using technology to improve people's lives, and we believe that our application has the potential to do just that. We hope that you find our website informative and useful, and we welcome any feedback or suggestions you may have.</p>
        </div>
       
    """

    st.markdown(html, unsafe_allow_html=True)

about_us()

