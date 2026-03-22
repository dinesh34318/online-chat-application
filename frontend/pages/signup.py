import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "backend"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
from styles import SHARED_CSS
from auth import signup_user

st.set_page_config(
    page_title="Join Corporate Smart Messenger",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed",
)
st.markdown(SHARED_CSS, unsafe_allow_html=True)

# Redirect if already logged in
if st.session_state.get("logged_in"):
    if st.session_state.get("role") == "admin":
        st.switch_page("admin_dashboard.py")
    else:
        st.switch_page("user_dashboard.py")

st.title("Join Corporate Smart Messenger")
st.markdown("<p style='text-align:center;'>Create an account to start messaging</p>", unsafe_allow_html=True)

with st.form("signup_form"):
    col_a, col_b = st.columns(2)
    with col_a:
        first_name = st.text_input("First Name *")
    with col_b:
        last_name = st.text_input("Last Name *")

    phone            = st.text_input("Phone Number *", placeholder="e.g. 9347321844")
    password         = st.text_input("Password *", type="password",
                                     help="Min 8 chars · 1 uppercase · 1 number · 1 special char")
    confirm_password = st.text_input("Confirm Password *", type="password")
    role             = st.selectbox("Sign up as", options=["user", "admin"],
                                    format_func=lambda r: "👤 User" if r == "user" else "🛡️ Admin")

    submitted = st.form_submit_button("Sign Up")

    if submitted:
        success, message = signup_user(first_name, last_name, phone, password, confirm_password, role)
        if success:
            st.session_state["signup_success"] = True
            st.success("✅ Account created successfully! Please go to the login page to sign in.")
            st.markdown("### 🚀 Next Steps")
            st.markdown("1. Click the **Go to Home Page** button below")
            st.markdown("2. Click the **Login** button")
            st.markdown("3. Use your new credentials to sign in")
        else:
            for line in message.split("\n"):
                st.error(f"❌ {line}")

# Show Go to Home Page button if signup was successful
if st.session_state.get("signup_success"):
    st.divider()
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🏠 Go to Home Page", use_container_width=True, type="primary"):
            st.switch_page("home.py")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Already have an account? Go to Login", type="secondary", use_container_width=True):
        st.info("👈 Please use the navigation buttons on the Home Page to go to Login")
