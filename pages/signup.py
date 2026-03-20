import streamlit as st

st.set_page_config(page_title="Join Corporate Smart Messenger", page_icon="💬", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    .stApp { background-color: #f0f2f5; }
    .stApp header { background-color: #A87B33; }
    [data-testid="collapsedControl"] { display: none; }
    [data-testid="stSidebar"] { display: none; }
    .stTextInput input { border-radius: 8px; border: 1px solid #d1d5db; background-color: white !important; color: #41525d !important; }
    .stTextInput p { color: #8696a0 !important; }
    .stForm [data-testid="stFormSubmitButton"] > button { width: 100%; border-radius: 24px; background-color: #A87B33; color: white; font-weight: bold; border: none; padding: 0.5rem 1rem; margin-top: 1rem; }
    .stForm [data-testid="stFormSubmitButton"] > button:hover { background-color: #8C662A; color: white; border: none; }
    button[kind="tertiary"] { color: #A87B33 !important; font-weight: bold; }
    h1 { text-align: center; color: #41525d !important; }
    p { color: #8696a0 !important; }
    [data-testid="stForm"] { background-color: white; padding: 2rem; border-radius: 10px; border: none; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
</style>
""", unsafe_allow_html=True)

st.title("Join Corporate Smart Messenger")
st.markdown("<p style='text-align: center;'>Create an account to start messaging</p>", unsafe_allow_html=True)

with st.form("signup_form"):
    col_a, col_b = st.columns(2)
    with col_a:
        st.text_input("First Name")
    with col_b:
        st.text_input("Last Name")
    st.text_input("Email / Phone Number")
    st.text_input("Password", type="password")
    st.text_input("Confirm Password", type="password")
    submitted = st.form_submit_button("Sign Up")
    if submitted:
        st.success("Account created! Connecting to workspace...")
        
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Already have an account? Log in", type="tertiary", use_container_width=True):
        st.switch_page("streamlit_login.py")
