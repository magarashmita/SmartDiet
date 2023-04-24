import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.sidebar.success("Select a recommendation app.")

import streamlit.components.v1 as components
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('Smartdiet jumbotorn.jpg')


def jumbotron():
    st.markdown(
        """
        <div class="jumbotron">
            <h1 class="display-4">Welcome to Smart Diet!👋</h1>
            <p class="lead">Your ultimate destination for healthy living and wellness.</p>
            <hr class="my-4">
            <p>From easy and healthy diet plan, to expert tips on mindful eating, and everything in between, we've got you covered.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    jumbotron()

st.markdown('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">', unsafe_allow_html=True)


import base64

# Define the image path and read the image file
image_path = "salmonsd.png"
with open(image_path, "rb") as f:
    image_bytes = f.read()

# Define the HTML for the cards with the image and text
cards_html = f"""
    <div class="row">
        <div class="col-sm-6">
              <img src="data:image/png;base64,{base64.b64encode(image_bytes).decode()}" class="card-img-top" style="width: 30rem; height: 30rem" alt="My Image">
        </div>
        <div class="col-sm-6">
            <div class="card" style="width: 18rem;">
                <div class="card-body">
                    <h5 class="card-title">Why Choose SMART DIET?</h5>
                    <h6 class="card-subtitle mb-2 text-muted">Your Diet Partner</h6>
                    <p class="card-text">Our mission is to inspire and empower you to live your best life, starting with what you eat. With a focus on nutritious, delicious, and sustainable diets, we aim to make healthy eating accessible and achievable for everyone.</p>
                </div>
            </div>
        </div>
    </div>
"""

# Add CSS styling to the HTML code
css_code = """
    <style>
        .card {
            margin: 2rem;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            transition: 0.3s;
            border-radius: 5px;
        }
        
        .card:hover {
            box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
        }
        
        .card-img-top {
            height: 200px;
            object-fit: cover;
            border-radius: 5px 5px 0 0;
        }
        
        .card-body {
            padding: 1rem;
        }
    </style>
"""

# Display the HTML code with the CSS styling
st.markdown(css_code + cards_html, unsafe_allow_html=True)


