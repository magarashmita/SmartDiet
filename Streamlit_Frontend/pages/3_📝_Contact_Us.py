import streamlit as st
from PIL import Image

import base64

st.header(":mailbox: Get In Touch With Us!") 


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
add_bg_from_local('contact.jpg')

contact_form ="""

<form action="https://formsubmit.co/2079design.team@gmail.com" method="POST">
     <input type ="hidden" name ="_captcha" value="false">
     <input type="text" name="name" placeholder="Enter your name" required>
     <input type="email" name="email" placeholder ="Your email address" required>
     <textarea name="message" placeholder="Share your thoughts"></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form,unsafe_allow_html=True)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("pages/style.css")


