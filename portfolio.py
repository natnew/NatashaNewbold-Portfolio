import streamlit as st
import webbrowser as wb
import time
from PIL import Image
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from streamlit_javascript import st_javascript

icon = Image.open("images/Copilot_14.jpg")
st.set_page_config(page_title="Natasha's Portfolio", page_icon=icon, layout="centered")

def css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css("assets/style.css")

with st.sidebar:       
    navigation = option_menu(
        menu_title=None,
        options=["Home", "Skills", "Projects", "Competitions", "Contact"],
        icons=["house", "stars", "book", "award", "person-rolodex"],
        orientation="vertical",
        default_index=0,
        styles={
            "container": {
                "align-items": "center",
                "text-align": "center",
                "background": "transparent",
                "margin-top": "20px"
            },
            "icon": {
                "color": "#000", 
                "font-size": "20px"
            },
            "nav-link": {
                "display": "flex",
                "justify-content": "center",
                "align-items": "center",
                "text-align": "center",
                "font-size": "15px",
                "--hover-color": "#7FB1AF",
                "font-weight": "bold",
            },
            "nav-link-selected": {"background-color": "#04AA6D"},
        }
    )

    st.markdown(
        """
        <div style="background-color: transparent; margin-top: 50px; text-align: center;">
            <p style="font-size: 15px; font-weight: bold">
                &copy; 2025 Natasha. All Rights Reserved.        
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

if navigation == "Home":
    def typewrite(text: str):
        with open("assets/style.css") as f:
            css = f.read()

        with open("assets/main.js") as f:
            js = f.read()

        html = f"""
        <!DOCTYPE html>
        <head>
        <style>
            {css}
        </style>
        </head>
        <body>
            <p id="typewrite" data-content="" style="background-color: transparent;">{text}</p>
            <script>
                {js}
            </script>
        </body>
        </html>
        """
        return html

    text = "WELCOME TO MY PORTFOLIO WEBSITE.."
    typewrite_txt = typewrite(text)
    components.html(typewrite_txt, height=40)

    about = """I am Natasha, a passionate Machine Learning/AI Engineer with extensive experience in creating intelligent solutions. 
    I have honed my skills in machine learning, deep learning, natural language processing, and software development. 
    With a commitment to innovation and precision, I strive to build impactful technologies that shape the future.
    """
    typewrite_abt = typewrite(about)
    col1, col2 = st.columns(2)

    profile = Image.open("images/Copilot_14.jpg")  # Replace with your profile image path
    
    time.sleep(2)

    st.markdown("""
        <style>
            img {
                margin-top: 70px;
                border-radius: 10px;
                width: 300px;
            }
        </style>
        """, unsafe_allow_html=True)
    
    with col1:
        st.image(profile)
    with col2:
        components.html(typewrite_abt, height=400)

if navigation == "Skills":
    skills = {
        "Python": 95,
        "Data Analysis": 90,
        "Deep Learning": 85,
        "Machine Learning": 90,
        "Natural Language Processing": 80,
        "SQL": 75,
        "Cloud Platforms (AWS/GCP)": 80,
        "TensorFlow & PyTorch": 85,
    }

    progress_bar_styles = """
        <style>
        p {
            color: white !important;
            margin: 7px 0;
        }
        .progress-bar {
            background-color: #ddd;
            border-radius: 10px;
            margin: 7px 0;
        }
        .progress-bar div {
            background-color: #04AA6D;
            color: white;
            text-align: center;
            border-radius: 10px;
            transition: width 0.3s ease-in-out;
        }
        </style>
    """

    st.write("### :star: Skills")
    st.markdown(progress_bar_styles, unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    for skill, level in skills.items():
        col1.write(skill)
        progress_bar = f'<div style="width: {level}%;"><b>{level}%</b></div>'
        col2.markdown(f'<div class="progress-bar">{progress_bar}</div>', unsafe_allow_html=True)

if navigation == "Projects":
    st.write("### :book: Projects")
    st.markdown("""
    <style>
    a {
        text-align: center !important;
        color: white !important;
        text-decoration: none;
    }
    a:hover {
        color: #04AA6D !important;
    }
    </style>
    """, unsafe_allow_html=True)
    cards = [
        {"title": "Chatbot for Healthcare", "image": "images/Copilot_14.jpg", "link": "https://github.com/natasha/project1"},
        {"title": "Predictive Analytics for E-commerce", "image": "images/Copilot_14.jpg", "link": "https://github.com/natasha/project2"},
        {"title": "Computer Vision in Retail", "image": "images/Copilot_14.jpg", "link": "https://github.com/natasha/project3"},
    ]

    col1, col2, col3 = st.columns(3)
    for col, card in zip([col1, col2, col3], cards):
        col.image(card['image'], width=220)
        col.markdown(f"[{card['title']}]({card['link']})")

if navigation == "Competitions":
    st.write("### :medal: Competitions")
    cards = [
        {"title": "AI Hackathon Winner", "image": "images/Copilot_15.jpg", "link": "https://example.com/comp1"},
        {"title": "Kaggle Silver Medalist", "image": "images/Copilot_16.jpg", "link": "https://example.com/comp2"},
    ]
    col1, col2 = st.columns(2)
    for col, card in zip([col1, col2], cards):
        col.image(card['image'])
        col.markdown(f"[{card['title']}]({card['link']})")

if navigation == "Contact":
    st.write("### :mailbox_closed: Get In Touch With Me!")
    contact_form = """
    <form action="https://formsubmit.co/natashalondon2021@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" style="resize: none;" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    media = [
        {"title": "LinkedIn", "image": "images/Copilot_17.jpg", "link": "https://linkedin.com/in/natasha"},
        {"title": "GitHub", "image": "images/Copilot_17.jpg", "link": "https://github.com/natasha"},
        {"title": "Kaggle", "image": "images/Copilot_17.jpg", "link": "https://kaggle.com/natasha"},
    ]

    col1, col2, col3 = st.columns(3)
    for col, medium in zip([col1, col2, col3], media):
        col.image(medium['image'], width=40)
        col.markdown(f"[{medium['title']}]({medium['link']})")
