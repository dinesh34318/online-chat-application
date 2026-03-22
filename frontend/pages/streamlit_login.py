import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

import streamlit as st
from styles import SHARED_CSS
from auth import login_user

st.set_page_config(
    page_title="Corporate Smart Messenger – Login",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed",
)
st.markdown(SHARED_CSS, unsafe_allow_html=True)

# Redirect if already logged in
if st.session_state.get("logged_in"):
    if st.session_state.get("role") == "admin":
        st.switch_page("pages/admin_dashboard.py")
    else:
        st.switch_page("pages/user_dashboard.py")

# Show signup success message
if st.session_state.pop("signup_success", False):
    st.success("✅ Signed up successfully! Please log in.")

st.title("Corporate Smart Messenger")
st.markdown("<p style='text-align:center;'>Log in to your workspace</p>", unsafe_allow_html=True)

with st.form("login_form"):
    phone    = st.text_input("Phone Number", placeholder="e.g. 9347321844")
    password = st.text_input("Password", type="password")
    st.checkbox("Keep me signed in")
    submitted = st.form_submit_button("Log In")

    if submitted:
        success, message, user_info = login_user(phone, password)
        if success:
            st.session_state["logged_in"]   = True
            st.session_state["role"]        = user_info["role"]
            st.session_state["first_name"]  = user_info["first_name"]
            st.session_state["last_name"]   = user_info["last_name"]
            st.session_state["login_toast"] = True
            if user_info["role"] == "admin":
                st.switch_page("pages/admin_dashboard.py")
            else:
                st.switch_page("pages/user_dashboard.py")
        else:
            for line in message.split("\n"):
                st.error(f"❌ {line}")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Don't have an account? Sign up", type="secondary", use_container_width=True):
        st.switch_page("pages/signup.py")
