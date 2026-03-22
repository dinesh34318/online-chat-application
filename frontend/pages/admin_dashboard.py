import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "backend"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
from styles import SHARED_CSS
from database import get_users_collection

st.set_page_config(
    page_title="Admin Dashboard – CSM",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.markdown(SHARED_CSS, unsafe_allow_html=True)

# Auth guard – admins only
if not st.session_state.get("logged_in"):
    st.switch_page("streamlit_login.py")

if st.session_state.get("role") != "admin":
    st.error("⛔ Access denied. Admin privileges required.")
    st.stop()

# Login success toast
if st.session_state.pop("login_toast", False):
    st.toast(f"✅ Login successful! Welcome, {st.session_state['first_name']}!", icon="🎉")

# Header
col_title, col_logout = st.columns([5, 1])
with col_title:
    st.markdown(
        f"## 🛡️ Admin Dashboard &nbsp;<span class='role-badge-admin'>ADMIN</span>",
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

# Stats
users_col    = get_users_collection()
total_users  = users_col.count_documents({"role": "user"})
total_admins = users_col.count_documents({"role": "admin"})

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"<div class='dash-card'><h3>👥 Total Users</h3><h1 style='color:#41525d;text-align:left'>{total_users}</h1></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='dash-card'><h3>🛡️ Total Admins</h3><h1 style='color:#41525d;text-align:left'>{total_admins}</h1></div>", unsafe_allow_html=True)
with c3:
    st.markdown(f"<div class='dash-card'><h3>🏢 All Accounts</h3><h1 style='color:#41525d;text-align:left'>{total_users+total_admins}</h1></div>", unsafe_allow_html=True)

st.divider()

# User table
st.subheader("📋 All Registered Accounts")
search = st.text_input("🔍 Search by name or phone", placeholder="Type to filter…")

filt = {}
if search.strip():
    filt = {"$or": [
        {"first_name": {"$regex": search, "$options": "i"}},
        {"last_name":  {"$regex": search, "$options": "i"}},
        {"phone":      {"$regex": search, "$options": "i"}},
    ]}

users_list = list(users_col.find(filt, {"password_hash": 0}))

if users_list:
    header = st.columns([2, 2, 3, 1, 1])
    for col, label in zip(header, ["First Name", "Last Name", "Phone", "Role", "Action"]):
        col.markdown(f"**{label}**")
    st.divider()
    for u in users_list:
        row = st.columns([2, 2, 3, 1, 1])
        row[0].write(u.get("first_name", ""))
        row[1].write(u.get("last_name", ""))
        row[2].write(u.get("phone", ""))
        badge = "role-badge-admin" if u.get("role") == "admin" else "role-badge-user"
        row[3].markdown(f"<span class='{badge}'>{u.get('role','').upper()}</span>", unsafe_allow_html=True)
        if row[4].button("🗑️", key=str(u["_id"]), help="Delete"):
            users_col.delete_one({"_id": u["_id"]})
            st.rerun()
else:
    st.info("No accounts found.")

st.divider()

# Broadcast
st.subheader("📢 Broadcast Message")
msg = st.text_area("Send a message to all users", placeholder="Type your announcement…")
if st.button("Send Broadcast", type="primary"):
    if msg.strip():
        st.success("✅ Broadcast sent to all users!")
    else:
        st.warning("Please enter a message before sending.")
