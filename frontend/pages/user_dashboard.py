import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "backend"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
from styles import SHARED_CSS

st.set_page_config(
    page_title="User Dashboard – CSM",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.markdown(SHARED_CSS, unsafe_allow_html=True)
st.markdown("""
<style>
.dash-card {
    transition: all 0.3s ease;
    cursor: pointer;
    border: 2px solid #d0d0d0;
    border-radius: 10px;
    background-color: #ffffff;
    padding: 1rem;
    margin: 0.5rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.dash-card:hover {
    transform: translateY(-5px) scale(1.02);
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    background-color: #fafafa;
}
.stButton > button {
    background-color: #A87B33 !important;
    color: white !important;
    border: none;
    border-radius: 8px;
    padding: 0.5rem;
    font-weight: bold;
    transition: all 0.3s ease;
    margin-top: 0.5rem;
}
.stButton > button:hover {
    background-color: #8C662A !important;
    transform: scale(1.05);
    box-shadow: 0 4px 15px rgba(168, 123, 51, 0.3);
}
</style>
""", unsafe_allow_html=True)

# Auth guard
if not st.session_state.get("logged_in"):
    st.switch_page("pages/streamlit_login.py")

if st.session_state.get("role") == "admin":
    st.switch_page("pages/admin_dashboard.py")

# Login success toast
if st.session_state.pop("login_toast", False):
    st.toast(f"✅ Login successful! Welcome, {st.session_state['first_name']}!", icon="🎉")

# Ultra Compact Header
col_title, col_logout = st.columns([8, 1])
with col_title:
    st.markdown(
        f"**💬 Dashboard**",
        unsafe_allow_html=True,
    )
    st.markdown(f"Welcome, **{st.session_state['first_name']}**", unsafe_allow_html=True)
with col_logout:
    if st.button("🚪 Logout", use_container_width=True):
        for k in ("logged_in", "role", "first_name", "last_name"):
            st.session_state.pop(k, None)
        st.switch_page("pages/streamlit_login.py")

st.divider()

# Dashboard Features Grid - 2x2 Layout (Minimal)
row1_col1, row1_col2 = st.columns(2, gap="small")
row2_col1, row2_col2 = st.columns(2, gap="small")

# Messages Feature - Top Left
with row1_col1:
    if st.button("💬\n\n**Messages**\n\n0 unread messages\n\n**View**", key="messages_view_btn", use_container_width=True):
        st.switch_page("pages/messages.py")

# Calendar Feature - Top Right
with row1_col2:
    if st.button("📅\n\n**Calendar**\n\nSchedule & events\n\n**Open**", key="calendar_open_btn", use_container_width=True):
        st.switch_page("pages/calendar.py")

# Chatbot Feature - Bottom Left
with row2_col1:
    if st.button("🤖\n\n**Chatbot**\n\nAI assistant\n\n**Chat**", key="chatbot_chat_btn", use_container_width=True):
        st.session_state["selected_feature"] = "chatbot"
        st.rerun()

# Settings Feature - Bottom Right
with row2_col2:
    if st.button("⚙️\n\n**Settings**\n\nPreferences\n\n**Config**", key="settings_config_btn", use_container_width=True):
        st.session_state["selected_feature"] = "settings"
        st.rerun()

# Feature Details Section (only for chatbot and settings)
if "selected_feature" in st.session_state:
    st.divider()
    
    if st.session_state["selected_feature"] == "chatbot":
        st.markdown("#### 🤖 AI Chatbot Assistant")
        if "chatbot_messages" not in st.session_state:
            st.session_state["chatbot_messages"] = []

        for m in st.session_state["chatbot_messages"]:
            with st.chat_message(m["role"]):
                st.write(m["content"])

        prompt = st.chat_input("Ask me anything...")
        if prompt:
            st.session_state["chatbot_messages"].append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)
            
            bot_response = f"I understand you said: '{prompt}'. I'm here to help you with your chat application needs!"
            st.session_state["chatbot_messages"].append({"role": "assistant", "content": bot_response})
            with st.chat_message("assistant"):
                st.write(bot_response)
        
        col_clear, _ = st.columns([1, 3])
        with col_clear:
            if st.button("Clear Selection", use_container_width=True):
                st.session_state.pop("selected_feature", None)
                st.rerun()
        
    elif st.session_state["selected_feature"] == "settings":
        st.markdown("#### ⚙️ Settings")
        st.markdown("<div class='dash-card' style='padding: 1rem;'>", unsafe_allow_html=True)
        
        st.markdown("**Profile Settings**")
        st.markdown(f"**Name:** {st.session_state['first_name']} {st.session_state['last_name']}")
        st.markdown(f"**Role:** {st.session_state['role'].capitalize()}")
        
        st.markdown("**Notification Preferences**")
        col1, col2 = st.columns(2)
        with col1:
            email_notifications = st.checkbox("Email notifications", value=True)
        with col2:
            push_notifications = st.checkbox("Push notifications", value=True)
        
        st.markdown("**Appearance**")
        theme = st.selectbox("Theme", ["Light", "Dark"], index=0)
        
        col_save, col_clear = st.columns([1, 1])
        with col_save:
            if st.button("Save Settings", type="primary", use_container_width=True):
                st.success("Settings saved successfully!")
        with col_clear:
            if st.button("Clear Selection", use_container_width=True):
                st.session_state.pop("selected_feature", None)
                st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)

