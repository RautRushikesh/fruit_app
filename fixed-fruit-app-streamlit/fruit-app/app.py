
import streamlit as st
import streamlit_authenticator as stauth
from PIL import Image
import os
import yaml
from yaml.loader import SafeLoader

st.set_page_config(page_title="Fruit Detection App", layout="wide")

# FIXED: Get full path for config.yaml
config_path = os.path.join(os.path.dirname(__file__), '.streamlit', 'config.yaml')
with open(config_path) as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    st.sidebar.success(f"Welcome *{name}*")
    st.sidebar.page_link("pages/2_Upload_and_Detection.py", label="Upload & Detect")
    st.sidebar.page_link("pages/3_Summary.py", label="Summary")
    st.sidebar.page_link("pages/4_Yield_Estimation.py", label="Yield Estimation")
    authenticator.logout("Logout", "sidebar")
    st.title("Fruit Detection and Yield Estimation App")
    st.info("Use the sidebar to navigate.")
elif authentication_status is False:
    st.error("Username/password is incorrect")
elif authentication_status is None:
    st.warning("Please enter your username and password")
