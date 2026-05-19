import streamlit as st
import datetime
import pandas as pd

# --- PAGE CONFIGURATION (Mobile App View Optimization) ---
st.set_page_config(
    page_title="SPCS Cruise Hub",
    page_icon="🚢",
    layout="centered",
    initial_sidebar_state="collapsed" # Completely hides the native sidebar arrow
)

# --- PREMIUM CRUISE THEME, TYPOGRAPHY & FADED SHIP BACKGROUND ---
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">

    <style>
    /* 🌊 FADED CRUISE SHIP IN OCEAN BACKGROUND 🌊 */
    .stApp {
        background-image: linear-gradient(rgba(255, 255, 255, 0.90), rgba(255, 255, 255, 0.90)), 
                          url('https://images.unsplash.com/photo-1548574505-5e239809ee19?q=80&w=1600&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Completely hide the native Streamlit sidebar toggle arrow icon globally */
    [data-testid="sidebar-toggle"] {
        display: none !important;
    }

    /* Apply clean modern fonts globally to readable elements */
    html, body, p, li, span, label, div.stMarkdown {
        font-family: 'Poppins', sans-serif !important;
        color: #000000 !important;
        font-size: 15px;
    }
    
    /* 🌊 OCEAN GRADIENT TITLE HEADER PANEL 🌊 */
    .ocean-header-panel {
        background: linear-gradient(135deg, #002277 0%, #0055D4 50%, #0088FF 100%);
        padding: 25px 15px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 85, 212, 0.3);
        margin-bottom: 20px;
    }
    .main-title { font-size: 26px; font-weight: 700; color: #FFFFFF !important; margin-bottom: 4px; }
    .subtitle { font-size: 14px; color: #E0F0FF !important; margin-bottom: 0px; font-weight: 500; letter-spacing: 0.5px; }
    
    /* Dynamic section headers */
    .section-header { 
        background: linear-gradient(90deg, #0033AA, #0055D4); 
        color: #FFFFFF !important; 
        padding: 12px; 
        border-radius: 8px; 
        font-size: 17px; 
        font-weight: 600; 
        margin-bottom: 15px; 
        text-align: center; 
        box-shadow: 0 2px 8px rgba(0, 51, 170, 0.2);
    }
    .section-header span { color: #FFFFFF !important; }
    .sub-title { font-size: 16px; font-weight: 600; color: #0033AA; margin-top: 18px; margin-bottom: 8px; border-bottom: 2px solid #0055D4; padding-bottom: 4px; }
    
    /* White Card containers to overlay cleanly on top of the faded ocean backdrop */
    .content-card {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.06);
        border: 1px solid #E5E7EB;
        margin-bottom: 20px;
    }
    
    /* Customized Alert & Block Containers */
    .emergency-box { background-color: rgba(255, 241, 242, 0.95); border: 2px solid #DC2626; padding: 15px; border-radius: 8px; margin-bottom: 15px; }
    .policy-box { background-color: rgba(240, 247, 255, 0.95); border: 2px solid #0055D4; padding: 15px; border-radius: 8px; margin-bottom: 15px; }
    .dinner-box { background-color: rgba(236, 253, 245, 0.95); border: 2px solid #059669; padding: 15px; border-radius: 8px; margin-bottom: 15px; }
    
    /* Theme Outfit Badges */
    .outfit-badge { 
        background-color: #EBF5FF; 
        border: 1.5px solid #0055D4; 
        color: #0033AA !important; 
        padding: 6px 14px; 
        border-radius: 20px; 
        font-weight: 600; 
        font-size: 13px; 
        display: inline-block; 
        margin-bottom: 12px; 
    }
    .outfit-badge span { color: #0033AA !important; }
    
    /* Social navigation box */
    .social-card { background-color: rgba(255, 255, 255, 0.95); padding: 12px; border-radius: 8px; text-align: center; margin-bottom: 20px; border:
