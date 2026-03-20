# Corporate Smart Messenger 💬

A basic multi-page Streamlit application featuring a corporate "Smart Messenger" Login and Sign-up interface. It features a custom light theme with golden-brown accents and seamless page routing.

## 📁 File Structure

This application follows Streamlit's official classic **Multi-Page App** architecture:

```text
CHATTING APPLICATION/
│
├── streamlit_login.py      # The Main Entry File (Login Page)
└── pages/
    └── signup.py           # The Secondary Page (Signup Page)
```

## 🚀 How to Run

1. Open your terminal, PowerShell, or command prompt.
2. Ensure you are in the `CHATTING APPLICATION` directory.
3. Start the application by running the **main entry file**:

   ```bash
   streamlit run streamlit_login.py
   ```

4. Streamlit will automatically open a tab in your default web browser (usually at `http://localhost:8501`).

## 🧩 Features
- **Multi-page Navigation**: Uses Streamlit's `st.switch_page()` function to smoothly transition between the login and sign-up windows natively.
- **Hidden Sidebar**: The default Streamlit multipage sidebar navigation has been hidden using custom CSS to make it feel like a real standalone app.
- **Custom Light Theme**: Forced light-mode styling using injected CSS, guaranteeing the forms and text look clean regardless of system settings.
- **Corporate Branding**: Configured with professional gold/amber thematic colors (`#A87B33`).

## 🛠️ Modifying the UI
All styling is done via the `<style>` tags injected by `st.markdown(..., unsafe_allow_html=True)` at the top of each file.
- **Background Color**: Modify `.stApp { background-color: #f0f2f5; }`
- **Button Colors**: Modify `.stForm [data-testid="stFormSubmitButton"] > button { background-color: #A87B33; }`
