SHARED_CSS = """
<style>
    .stApp { background-color: #f0f2f5; }
    .stApp header { background-color: #A87B33; }
    [data-testid="collapsedControl"] { display: none; }
    [data-testid="stSidebar"] { display: none; }
    .stTextInput input { border-radius: 8px; border: 1px solid #d1d5db; background-color: white !important; color: #41525d !important; }
    .stTextInput p { color: #8696a0 !important; }
    .stCheckbox p { color: #8696a0 !important; }
    .stSelectbox label { color: #8696a0 !important; }
    .stForm [data-testid="stFormSubmitButton"] > button { width: 100%; border-radius: 24px; background-color: #A87B33; color: white; font-weight: bold; border: none; padding: 0.5rem 1rem; margin-top: 1rem; }
    .stForm [data-testid="stFormSubmitButton"] > button:hover { background-color: #8C662A; color: white; border: none; }
    button[kind="secondary"] { color: #A87B33 !important; font-weight: bold; }
    h1 { text-align: center; color: #41525d !important; }
    p  { color: #8696a0 !important; }
    [data-testid="stForm"] { background-color: white; padding: 2rem; border-radius: 10px; border: none; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .dash-card { background: white; border-radius: 12px; padding: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 1rem; color: #41525d; }
    .dash-card h3 { color: #A87B33; margin-top: 0; }
    .role-badge-admin { display: inline-block; background: #A87B33; color: white; border-radius: 12px; padding: 2px 12px; font-size: 0.8rem; font-weight: bold; }
    .role-badge-user  { display: inline-block; background: #41525d; color: white; border-radius: 12px; padding: 2px 12px; font-size: 0.8rem; font-weight: bold; }
</style>
"""
