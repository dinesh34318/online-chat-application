# Corporate Smart Messenger 💬

A comprehensive multi-page Streamlit application featuring a corporate "Smart Messenger" with user dashboard, messaging system, and calendar scheduling. It features a custom light theme with golden-brown accents, WhatsApp-like messaging interface, and seamless page routing.

## 📁 File Structure

This application follows Streamlit's official **Multi-Page App** architecture:

```text
CHATTING APPLICATION/
│
├── streamlit_login.py          # Main Entry File (Login Page)
├── home.py                     # Landing/Home Page
├── styles.py                   # Shared CSS styles
├── pages/
│   ├── signup.py              # User Registration Page
│   ├── user_dashboard.py      # User Dashboard with feature cards
│   ├── messages.py            # WhatsApp-like Messaging Interface
│   ├── calendar.py            # Calendar with Event Scheduling
│   └── admin_dashboard.py     # Admin Dashboard
└── backend/
    ├── auth.py                # Authentication logic
    └── database.py            # Database connection
```

## 🚀 How to Run

1. Open your terminal, PowerShell, or command prompt.
2. Ensure you are in the `CHATTING APPLICATION` directory.
3. Install required dependencies:
   ```bash
   pip install streamlit bcrypt pymongo python-dotenv
   ```
4. Start the application by running the **main entry file**:
   ```bash
   streamlit run streamlit_login.py
   ```
5. Streamlit will automatically open a tab in your default web browser (usually at `http://localhost:8501`).

## 🧩 Features

### Authentication & Navigation
- **Multi-page Navigation**: Uses Streamlit's `st.switch_page()` function to smoothly transition between pages natively.
- **Hidden Sidebar**: The default Streamlit multipage sidebar navigation has been hidden using custom CSS to make it feel like a real standalone app.
- **Role-based Access**: Separate dashboards for users and admins with authentication guards.

### User Dashboard
- **Compact 2x2 Grid Layout**: Messages, Calendar, Chatbot, and Settings cards
- **Hover Effects**: Cards and buttons have smooth hover animations with the brand color theme
- **Navigation Buttons**: Each card has functional buttons (View, Open, Chat, Config) that navigate to respective pages
- **Inline Features**: Chatbot and Settings open directly on the dashboard

### Messages Page
- **WhatsApp-like Interface**: Side-by-side chat list and conversation view
- **Chat List**: Shows contacts with last message, timestamp, and unread count
- **Real-time Messaging**: Type and send messages that appear in the conversation
- **Sample Conversations**: Pre-loaded chat data for demonstration

### Calendar Page
- **Monthly Calendar View**: Full calendar grid with day selection
- **Event Management**: Add events with title and time
- **Daily Events**: View events scheduled for selected dates
- **Notes Section**: Personal notes for each day

### Design & Styling
- **Custom Light Theme**: Forced light-mode styling using injected CSS, guaranteeing the forms and text look clean regardless of system settings.
- **Corporate Branding**: Configured with professional gold/amber thematic colors (`#A87B33`).
- **Responsive Design**: Wide layout with proper spacing and rounded corners
- **Hover Animations**: Smooth transitions on cards and buttons

## 🛠️ Modifying the UI

All styling is done via the `<style>` tags injected by `st.markdown(..., unsafe_allow_html=True)` at the top of each file.
- **Background Color**: Modify `.stApp { background-color: #f0f2f5; }`
- **Button Colors**: Modify `.stButton > button { background-color: #A87B33; }`
- **Card Styling**: Modify `.dash-card` classes in user_dashboard.py
- **Box Borders**: Adjust `border: 2px solid #d0d0d0;` for card outlines


# Final Deployed Website link
https://corporate-smart-messanger.onrender.com
