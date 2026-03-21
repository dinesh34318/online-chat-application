import streamlit as st
import base64

def set_page_config():
    """Set page configuration"""
    st.set_page_config(
        page_title="AI OrgChat - AI-Powered Organization Chat Platform",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

def load_custom_css():
    """Load custom CSS for modern styling"""
    css = """
    <style>
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #7e8ba3 100%);
        min-height: 100vh;
    }
    
    /* Hide default Streamlit elements */
    .stDeployButton, #MainMenu, footer {
        visibility: hidden;
        height: 0;
    }
    
    /* Navigation Bar */
    .navbar {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        padding: 1rem 2rem;
        border-radius: 15px;
        margin: 1rem 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: sticky;
        top: 0;
        z-index: 1000;
    }
    
    .nav-brand {
        font-size: 1.8rem;
        font-weight: bold;
        background: linear-gradient(45deg, #00d4ff, #090979);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .nav-menu {
        display: flex;
        gap: 2rem;
        align-items: center;
    }
    
    .nav-item {
        color: #333;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s;
    }
    
    .nav-item:hover {
        color: #00d4ff;
    }
    
    .nav-buttons {
        display: flex;
        gap: 1rem;
    }
    
    /* Hero Section */
    .hero-section {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 4rem 3rem;
        margin: 2rem;
        text-align: center;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: bold;
        background: linear-gradient(45deg, #00d4ff, #090979);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1.5rem;
        line-height: 1.2;
    }
    
    .hero-description {
        font-size: 1.2rem;
        color: #555;
        margin-bottom: 2.5rem;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.6;
    }
    
    .hero-buttons {
        display: flex;
        gap: 1.5rem;
        justify-content: center;
        flex-wrap: wrap;
    }
    
    /* Buttons */
    .btn-primary {
        background: linear-gradient(45deg, #10b981, #059669);
        color: white;
        padding: 1rem 2.5rem;
        border: none;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
        text-decoration: none;
        display: inline-block;
    }
    
    .btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4);
    }
    
    .btn-secondary {
        background: white;
        color: #090979;
        padding: 1rem 2.5rem;
        border: 2px solid #090979;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
        text-decoration: none;
        display: inline-block;
    }
    
    .btn-secondary:hover {
        background: #090979;
        color: white;
        transform: translateY(-2px);
    }
    
    /* Features Section */
    .features-section {
        margin: 3rem 2rem;
    }
    
    .section-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        color: white;
        margin-bottom: 3rem;
    }
    
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin: 0 auto;
        max-width: 1200px;
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s, box-shadow 0.3s;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #333;
        margin-bottom: 1rem;
    }
    
    .feature-description {
        color: #666;
        line-height: 1.6;
    }
    
 
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        
        .navbar {
            flex-direction: column;
            gap: 1rem;
        }
        
        .nav-menu {
            flex-direction: column;
            gap: 1rem;
        }
        
        .hero-buttons {
            flex-direction: column;
            align-items: center;
        }
        
        .features-grid {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def create_navbar():
    """Create navigation bar"""
    st.markdown("""
    <div class="navbar">
        <div class="nav-brand">🤖 AI OrgChat</div>
        <div class="nav-menu">
            <a href="#home" class="nav-item">Home</a>
            <a href="#features" class="nav-item">Features</a>
            <a href="#technology" class="nav-item">Technology</a>
        </div>
        <div class="nav-buttons">
            <a href="#login" class="btn-secondary">Login</a>
            <a href="#signup" class="btn-primary">Sign Up</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_hero_section():
    """Create hero section"""
    st.markdown("""
    <div class="hero-section" id="home">
        <h1 class="hero-title">AI-Powered Organization Chat Platform</h1>
        <p class="hero-description">
            A smart communication platform for organizations where every user has a personal AI assistant powered by RAG. 
            The system learns from conversations and can automatically assist with tasks like meeting scheduling and knowledge retrieval.
        </p>
        <div class="hero-buttons">
            <a href="#signup" class="btn-primary">Sign Up</a>
            <a href="#login" class="btn-secondary">Login</a>
        </div>
    </div>
    """, unsafe_allow_html=True)




def main():
    """Main function to run the homepage"""
    set_page_config()
    load_custom_css()
    
    # Create all sections
    create_navbar()
    create_hero_section()
    
    # Add JavaScript for smooth scrolling
    st.markdown("""
    <script>
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    </script>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
