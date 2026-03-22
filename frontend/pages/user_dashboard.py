import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "backend"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
from styles import SHARED_CSS

st.set_page_config(
    page_title="User Dashboard – CSM",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed",
)
st.markdown(SHARED_CSS, unsafe_allow_html=True)

# Auth guard
if not st.session_state.get("logged_in"):
    st.switch_page("streamlit_login.py")

if st.session_state.get("role") == "admin":
    st.switch_page("admin_dashboard.py")

# Login success toast
if st.session_state.pop("login_toast", False):
    st.toast(f"✅ Login successful! Welcome, {st.session_state['first_name']}!", icon="🎉")

# Header
col_title, col_logout = st.columns([5, 1])
with col_title:
    st.markdown(
        f"## 💬 My Dashboard &nbsp;<span class='role-badge-user'>USER</span>",
        unsafe_allow_html=True,
    )
    st.markdown(f"Welcome, **{st.session_state['first_name']} {st.session_state['last_name']}**")
with col_logout:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚪 Logout", use_container_width=True):
        for k in ("logged_in", "role", "first_name", "last_name"):
            st.session_state.pop(k, None)
        st.switch_page("streamlit_login.py")

st.divider()

# Cards
c1, c2 = st.columns(2)
with c1:
    st.markdown("<div class='dash-card'><h3>💬 Messages</h3><p>You have <strong>0</strong> unread messages.</p></div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div class='dash-card'><h3>👤 My Profile</h3><p>Manage your account details and preferences.</p></div>", unsafe_allow_html=True)

st.divider()

# Chat
st.subheader("💬 Chat")
if "messages" not in st.session_state:
    st.session_state["messages"] = []

for m in st.session_state["messages"]:
    with st.chat_message(m["role"]):
        st.write(m["content"])

prompt = st.chat_input("Type a message…")
if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    reply = f"Echo: {prompt}"
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)

st.divider()

with st.expander("⚙️ Account Settings"):
    st.markdown(f"**Name:** {st.session_state['first_name']} {st.session_state['last_name']}")
    st.markdown(f"**Role:** {st.session_state['role'].capitalize()}")
    st.info("Profile editing coming soon.")
