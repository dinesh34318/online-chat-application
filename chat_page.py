import streamlit as st
from datetime import datetime
from user_store import create_user, get_user_by_id
from msg_store import save_message, load_messages

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Chattr",
    page_icon="💬",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap');

    /* Global */
    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }
    .stApp {
        background: #0e0e14;
        color: #e8e8f0;
    }

    /* Hide default Streamlit chrome */
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 780px; margin: auto; }

    /* ── App shell ── */
    .chat-header {
        position: sticky;
        top: 0;
        z-index: 100;
        background: #0e0e14ee;
        backdrop-filter: blur(12px);
        border-bottom: 1px solid #ffffff12;
        padding: 18px 28px 14px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .chat-header-logo {
        font-family: 'Space Mono', monospace;
        font-size: 22px;
        font-weight: 700;
        color: #a78bfa;
        letter-spacing: -1px;
    }
    .chat-header-room {
        font-size: 13px;
        color: #6b6b80;
        margin-left: auto;
        font-family: 'Space Mono', monospace;
    }
    .online-dot {
        width: 8px; height: 8px;
        background: #4ade80;
        border-radius: 50%;
        display: inline-block;
        margin-right: 6px;
        box-shadow: 0 0 6px #4ade80aa;
    }

    /* ── Message feed ── */
    .messages-wrapper {
        padding: 24px 28px 120px;
        display: flex;
        flex-direction: column;
        gap: 6px;
    }
    .date-divider {
        text-align: center;
        color: #44445a;
        font-size: 11px;
        font-family: 'Space Mono', monospace;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin: 18px 0 10px;
    }

    /* Bubble base */
    .msg-row {
        display: flex;
        align-items: flex-end;
        gap: 10px;
        margin-bottom: 2px;
    }
    .msg-row.me { flex-direction: row-reverse; }

    .avatar {
        width: 32px; height: 32px;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 13px; font-weight: 700;
        flex-shrink: 0;
        font-family: 'Space Mono', monospace;
    }
    .bubble {
        max-width: 68%;
        padding: 10px 15px;
        border-radius: 18px;
        font-size: 14.5px;
        line-height: 1.55;
        word-break: break-word;
    }
    .bubble.them {
        background: #1c1c2a;
        border: 1px solid #ffffff0d;
        border-bottom-left-radius: 4px;
        color: #d8d8ee;
    }
    .bubble.me {
        background: linear-gradient(135deg, #7c3aed, #a855f7);
        border-bottom-right-radius: 4px;
        color: #fff;
    }
    .meta {
        font-size: 11px;
        color: #44445a;
        margin-top: 3px;
        font-family: 'Space Mono', monospace;
    }
    .meta.me { text-align: right; }
    .meta .name { color: #7c6faa; font-weight: 600; margin-right: 5px; }

    /* ── Input bar ── */
    .input-bar {
        position: fixed;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 100%;
        max-width: 780px;
        background: #0e0e14f5;
        backdrop-filter: blur(16px);
        border-top: 1px solid #ffffff10;
        padding: 14px 20px 18px;
        display: flex;
        gap: 10px;
        align-items: center;
        z-index: 200;
    }
    div[data-testid="stTextInput"] input {
        background: #18182a !important;
        border: 1px solid #2e2e44 !important;
        border-radius: 14px !important;
        color: #e8e8f0 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 14.5px !important;
        padding: 12px 18px !important;
        caret-color: #a78bfa;
    }
    div[data-testid="stTextInput"] input:focus {
        border-color: #7c3aed !important;
        box-shadow: 0 0 0 3px #7c3aed22 !important;
        outline: none !important;
    }
    div[data-testid="stTextInput"] input::placeholder { color: #44445a !important; }

    div[data-testid="stButton"] button {
        background: linear-gradient(135deg, #7c3aed, #a855f7) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 20px !important;
        font-family: 'Space Mono', monospace !important;
        font-size: 13px !important;
        font-weight: 700 !important;
        cursor: pointer !important;
        transition: opacity 0.15s;
        white-space: nowrap;
    }
    div[data-testid="stButton"] button:hover { opacity: 0.85 !important; }

    /* ── Login panel ── */
    .login-wrap {
        min-height: 100vh;
        display: flex; align-items: center; justify-content: center;
        padding: 40px 20px;
    }
    .login-card {
        background: #13131f;
        border: 1px solid #ffffff0d;
        border-radius: 24px;
        padding: 48px 44px;
        width: 100%; max-width: 420px;
        text-align: center;
    }
    .login-logo {
        font-family: 'Space Mono', monospace;
        font-size: 36px; font-weight: 700;
        color: #a78bfa;
        letter-spacing: -2px;
        margin-bottom: 8px;
    }
    .login-sub {
        color: #44445a; font-size: 13.5px;
        margin-bottom: 36px;
    }

    /* User ID badge */
    .uid-badge {
        display: inline-block;
        background: #1c1c2a;
        border: 1px solid #2e2e44;
        border-radius: 8px;
        padding: 6px 12px;
        font-family: 'Space Mono', monospace;
        font-size: 10px;
        color: #7c6faa;
        letter-spacing: 0.5px;
        margin-bottom: 18px;
        word-break: break-all;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Helpers ───────────────────────────────────────────────────────────────────

AVATAR_COLORS = [
    ("#7c3aed", "#18182a"), ("#06b6d4", "#0a1a1f"), ("#f59e0b", "#1f180a"),
    ("#10b981", "#0a1f17"), ("#f43f5e", "#1f0a0e"), ("#8b5cf6", "#15102a"),
]

def avatar_style(username: str):
    idx = sum(ord(c) for c in username) % len(AVATAR_COLORS)
    return AVATAR_COLORS[idx]

def fmt_time(iso: str) -> str:
    try:
        dt = datetime.fromisoformat(iso)
        return dt.strftime("%H:%M")
    except Exception:
        return ""

def fmt_date(iso: str) -> str:
    try:
        dt = datetime.fromisoformat(iso)
        today = datetime.now().date()
        if dt.date() == today:
            return "Today"
        return dt.strftime("%b %d, %Y")
    except Exception:
        return ""

def render_bubble(msg: dict, is_me: bool):
    fg, bg = avatar_style(msg["username"])
    initial = msg["username"][0].upper()
    bubble_cls = "me" if is_me else "them"
    row_cls = "me" if is_me else ""
    avatar_html = f'<div class="avatar" style="background:{bg};color:{fg}">{initial}</div>'
    bubble_html = f'<div class="bubble {bubble_cls}">{msg["content"]}</div>'
    meta = f'<div class="meta {bubble_cls}">'
    if not is_me:
        meta += f'<span class="name">{msg["username"]}</span>'
    meta += f'{fmt_time(msg["timestamp"])}</div>'

    if is_me:
        st.markdown(
            f'<div class="msg-row {row_cls}">{avatar_html}<div><div style="display:flex;justify-content:flex-end">{bubble_html}</div>{meta}</div></div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="msg-row">{avatar_html}<div>{bubble_html}{meta}</div></div>',
            unsafe_allow_html=True,
        )

# ── Session state init ────────────────────────────────────────────────────────
if "user" not in st.session_state:
    st.session_state.user = None
if "input_key" not in st.session_state:
    st.session_state.input_key = 0

# ── Login screen ──────────────────────────────────────────────────────────────
# ── Login screen ──────────────────────────────────────────────────────────────
if st.session_state.user is None:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 2, 1])
    with col:
        st.markdown('<div class="login-logo">chattr.</div>', unsafe_allow_html=True)
        st.markdown('<div class="login-sub">pick a name and jump right in</div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        username = st.text_input("Username", placeholder="your username…", label_visibility="collapsed")
        if st.button("Enter chat →", use_container_width=True):
            if username.strip():
                user = create_user(username.strip())
                st.session_state.user = user
                st.rerun()
            else:
                st.error("Please enter a username.")
    st.stop()

# ── Chat page ─────────────────────────────────────────────────────────────────
user = st.session_state.user

# Header
st.markdown(
    f"""
    <div class="chat-header">
        <div class="chat-header-logo">chattr.</div>
        <div class="chat-header-room">
            <span class="online-dot"></span>general
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# User ID badge
st.markdown(
    f'<div style="padding:10px 28px 0"><div class="uid-badge">UID · {user["user_id"]}</div></div>',
    unsafe_allow_html=True,
)

# Message feed
messages = load_messages(limit=200)

st.markdown('<div class="messages-wrapper">', unsafe_allow_html=True)

last_date = None
for msg in messages:
    d = fmt_date(msg["timestamp"])
    if d != last_date:
        st.markdown(f'<div class="date-divider">── {d} ──</div>', unsafe_allow_html=True)
        last_date = d
    render_bubble(msg, is_me=(msg["user_id"] == user["user_id"]))

st.markdown("</div>", unsafe_allow_html=True)

# Input bar
st.markdown('<div class="input-bar">', unsafe_allow_html=True)
col1, col2 = st.columns([5, 1])
with col1:
    new_msg = st.text_input(
        "Message",
        placeholder="type a message…",
        label_visibility="collapsed",
        key=f"msg_input_{st.session_state.input_key}",
    )
with col2:
    send = st.button("Send ↑")
st.markdown("</div>", unsafe_allow_html=True)

if send and new_msg.strip():
    save_message(
        user_id=user["user_id"],
        username=user["username"],
        content=new_msg.strip(),
    )
    st.session_state.input_key += 1
    st.rerun()