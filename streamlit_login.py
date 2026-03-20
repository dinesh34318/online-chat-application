import streamlit as st

st.set_page_config(page_title="Corporate Smart Messenger", page_icon="💬", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    .stApp { background-color: #f0f2f5; }
    .stApp header { background-color: #A87B33; }
    [data-testid="collapsedControl"] { display: none; }
    [data-testid="stSidebar"] { display: none; }
    .stTextInput input { border-radius: 8px; border: 1px solid #d1d5db; background-color: white !important; color: #41525d !important; }
    .stTextInput p { color: #8696a0 !important; }
    .stCheckbox p { color: #8696a0 !important; }
    .stForm [data-testid="stFormSubmitButton"] > button { width: 100%; border-radius: 24px; background-color: #A87B33; color: white; font-weight: bold; border: none; padding: 0.5rem 1rem; margin-top: 1rem; }
    .stForm [data-testid="stFormSubmitButton"] > button:hover { background-color: #8C662A; color: white; border: none; }
    button[kind="tertiary"] { color: #A87B33 !important; font-weight: bold; }
    h1 { text-align: center; color: #41525d !important; }
    p { color: #8696a0 !important; }
    [data-testid="stForm"] { background-color: white; padding: 2rem; border-radius: 10px; border: none; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
</style>
""", unsafe_allow_html=True)

st.title("Corporate Smart Messenger")
st.markdown("<p style='text-align: center;'>Log in to your workspace</p>", unsafe_allow_html=True)

with st.form("login_form"):
    st.text_input("Email / Phone Number")
    st.text_input("Password", type="password")
    st.checkbox("Keep me signed in")
    submitted = st.form_submit_button("Log In")
    if submitted:
        st.success("Logging in...")
        
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Don't have an account? Sign up", type="tertiary", use_container_width=True):
        st.switch_page("pages/signup.py")
