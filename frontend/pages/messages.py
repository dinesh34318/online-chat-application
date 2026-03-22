import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "backend"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
from styles import SHARED_CSS

st.set_page_config(
    page_title="Messages - CSM",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.markdown(SHARED_CSS, unsafe_allow_html=True)

# Auth guard
if not st.session_state.get("logged_in"):
    st.switch_page("pages/streamlit_login.py")

if st.session_state.get("role") == "admin":
    st.switch_page("pages/admin_dashboard.py")

# WhatsApp-like CSS
st.markdown("""
<style>
.whatsapp-container {
    display: flex;
    height: 80vh;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    overflow: hidden;
}
.chat-list {
    width: 30%;
    border-right: 1px solid #e0e0e0;
    background-color: #f8f9fa;
    overflow-y: auto;
}
.chat-window {
    width: 70%;
    display: flex;
    flex-direction: column;
    background-color: #ffffff;
}
.chat-header {
    padding: 1rem;
    background-color: #A87B33;
    color: white;
    font-weight: bold;
}
.chat-messages {
    flex: 1;
    padding: 1rem;
    overflow-y: auto;
    background-color: #e5ddd5;
}
.chat-input {
    padding: 1rem;
    border-top: 1px solid #e0e0e0;
    background-color: #ffffff;
}
.chat-item {
    padding: 0.8rem;
    border-bottom: 1px solid #e0e0e0;
    cursor: pointer;
    transition: background-color 0.3s ease;
}
.chat-item:hover {
    background-color: #e8e8e8;
}
.chat-item.active {
    background-color: #d1d1d1;
}
.message {
    margin-bottom: 0.5rem;
    display: flex;
}
.message.sent {
    justify-content: flex-end;
}
.message.received {
    justify-content: flex-start;
}
.message-bubble {
    max-width: 70%;
    padding: 0.5rem 1rem;
    border-radius: 15px;
    word-wrap: break-word;
}
.message.sent .message-bubble {
    background-color: #dcf8c6;
    color: #000000;
}
.message.received .message-bubble {
    background-color: #ffffff;
    color: #000000;
}
.message-time {
    font-size: 0.7rem;
    color: #999;
    margin-top: 0.2rem;
}
</style>
""", unsafe_allow_html=True)

# Header
col_title, col_back = st.columns([6, 1])
with col_title:
    st.markdown("### 💬 Messages")
with col_back:
    if st.button("← Back", use_container_width=True):
        st.switch_page("pages/user_dashboard.py")

st.divider()

# Sample chat data
chats = [
    {"id": 1, "name": "John Doe", "last_message": "Hey, how are you?", "time": "10:30 AM", "unread": 2},
    {"id": 2, "name": "Jane Smith", "last_message": "See you tomorrow!", "time": "9:45 AM", "unread": 0},
    {"id": 3, "name": "Team Chat", "last_message": "Meeting at 3 PM", "time": "Yesterday", "unread": 5},
    {"id": 4, "name": "Support", "last_message": "Your issue has been resolved", "time": "Yesterday", "unread": 0},
]

# Initialize selected chat and messages
if "selected_chat" not in st.session_state:
    st.session_state.selected_chat = None

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = {}

# WhatsApp Interface Layout
col_chat_list, col_chat_window = st.columns([3, 7])

with col_chat_list:
    st.markdown("""
    <div class="chat-list">
        <div style="padding: 1rem; font-weight: bold; border-bottom: 1px solid #e0e0e0;">Chats</div>
    """, unsafe_allow_html=True)
    
    # Chat list
    for chat in chats:
        chat_class = "chat-item active" if st.session_state.selected_chat == chat["id"] else "chat-item"
        st.markdown(f"""
            <div class="{chat_class}" onclick="selectChat({chat['id']})">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <div style="font-weight: bold;">{chat['name']}</div>
                        <div style="font-size: 0.8rem; color: #666;">{chat['last_message']}</div>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 0.7rem; color: #999;">{chat['time']}</div>
                        {f"<div style='background-color: #A87B33; color: white; border-radius: 50%; width: 20px; height: 20px; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; margin-top: 0.2rem;'>{chat['unread']}</div>" if chat['unread'] > 0 else ""}
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"Open {chat['name']}", key=f"chat_{chat['id']}", use_container_width=True):
            st.session_state.selected_chat = chat["id"]
            # Initialize messages for this chat if not exists
            if chat["id"] not in st.session_state.chat_messages:
                st.session_state.chat_messages[chat["id"]] = [
                    {"role": "received", "content": "Hi there!", "time": "10:00 AM"},
                    {"role": "sent", "content": "Hello! How can I help you?", "time": "10:05 AM"},
                    {"role": "received", "content": chat['last_message'], "time": chat['time']},
                ]
            st.rerun()
    
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)

with col_chat_window:
    st.markdown("""
    <div class="chat-window">
    """, unsafe_allow_html=True)
    
    # Chat window content
    if st.session_state.selected_chat:
        selected_chat_data = next((chat for chat in chats if chat["id"] == st.session_state.selected_chat), None)
        if selected_chat_data:
            # Chat header
            st.markdown(f"""
            <div class="chat-header">
                {selected_chat_data['name']}
            </div>
            """, unsafe_allow_html=True)
            
            # Chat messages
            st.markdown(f"""
            <div class="chat-messages">
            """, unsafe_allow_html=True)
            
            # Get messages for current chat
            current_chat_messages = st.session_state.chat_messages.get(st.session_state.selected_chat, [])
            
            for msg in current_chat_messages:
                if msg["role"] == "received":
                    st.markdown(f"""
                    <div class="message received">
                        <div class="message-bubble">
                            {msg["content"]}
                            <div class="message-time">{msg["time"]}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="message sent">
                        <div class="message-bubble">
                            {msg["content"]}
                            <div class="message-time">{msg["time"]}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("""
            </div>
            """, unsafe_allow_html=True)
            
            # Chat input
            st.markdown("""
            <div class="chat-input">
            """, unsafe_allow_html=True)
            
            # Use a form for proper message sending and input clearing
            with st.form(key="message_form", clear_on_submit=True):
                message = st.text_input("Type a message...", key="message_input")
                submitted = st.form_submit_button("Send", use_container_width=True)
                
                if submitted and message:
                    # Add message to current chat
                    if st.session_state.selected_chat not in st.session_state.chat_messages:
                        st.session_state.chat_messages[st.session_state.selected_chat] = []
                    
                    st.session_state.chat_messages[st.session_state.selected_chat].append({
                        "role": "sent", 
                        "content": message, 
                        "time": "Just now"
                    })
                    
                    st.rerun()
            
            # Voice button outside form
            st.button("🎤", use_container_width=True)
                
            st.markdown("""
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="display: flex; align-items: center; justify-content: center; height: 400px; color: #999;">
            <div style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">💬</div>
                <div>Select a chat to start messaging</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)
