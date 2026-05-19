import streamlit as st
import datetime
import pandas as pd

# --- PAGE CONFIGURATION (Mobile App View Optimization) ---
st.set_page_config(
    page_title="SPCS Cruise Hub",
    page_icon="🚢",
    layout="centered",
    initial_sidebar_state="expanded" 
)

# --- PREMIUM OCEAN THEME & HIGH-CONTRAST TYPOGRAPHY ---
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">

    <style>
    /* Apply clean modern fonts globally */
    html, body, [class*="css"], p, li, span, label {
        font-family: 'Poppins', sans-serif !important;
        color: #000000 !important;
        font-size: 15px;
    }
    
    /* App background remains clean white for ultimate sunlight readability */
    .stApp { background-color: #FFFFFF; }
    
    /* Clean white background for the sidebar menu */
    [data-testid="stSidebar"] { 
        background-color: #FFFFFF; 
        border-right: 3px solid #0055D4; 
    }
    
    /* 🌊 STUNNING OCEAN GRADIENT HEADER PANEL 🌊 */
    .ocean-header-panel {
        background: linear-gradient(135deg, #002277 0%, #0055D4 50%, #0088FF 100%);
        padding: 25px 15px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 85, 212, 0.2);
        margin-bottom: 20px;
    }
    .main-title { font-size: 26px; font-weight: 700; color: #FFFFFF !important; margin-bottom: 4px; }
    .subtitle { font-size: 14px; color: #E0F0FF !important; margin-bottom: 0px; font-weight: 500; letter-spacing: 0.5px; }
    
    /* 📱 MOBILE USER NAVIGATION GUIDE BANNER 📱 */
    .mobile-instruction-banner {
        background-color: #EBF5FF;
        border: 2px dashed #0055D4;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 20px;
        animation: pulse 2s infinite;
    }
    .mobile-instruction-banner strong { color: #0033AA !important; font-size: 14px; }
    
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
    }
    .sub-title { font-size: 16px; font-weight: 600; color: #0033AA; margin-top: 18px; margin-bottom: 8px; border-bottom: 2px solid #0055D4; padding-bottom: 4px; }
    
    /* Styled notification boxes */
    .emergency-box { background-color: #FFF1F2; border: 2px solid #DC2626; padding: 15px; border-radius: 8px; color: #000000; margin-bottom: 15px; }
    .policy-box { background-color: #F0F7FF; border: 2px solid #0055D4; padding: 15px; border-radius: 8px; color: #000000; margin-bottom: 15px; }
    .dinner-box { background-color: #ECFDF5; border: 2px solid #059669; padding: 15px; border-radius: 8px; color: #000000; margin-bottom: 15px; }
    
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
    
    /* Social navigation box */
    .social-card { background-color: #FFFFFF; padding: 12px; border-radius: 8px; text-align: center; margin-bottom: 20px; border: 2px solid #E5E7EB; }
    .social-link { font-weight: 600; color: #0055D4 !important; text-decoration: underline; margin: 0 8px; }
    </style>
""", unsafe_allow_html=True)

# --- TRACK SELECTION STATE ---
if "current_topic" not in st.session_state:
    st.session_state.current_topic = "⏳ Countdown Timer"

# ==========================================
# --- SIDEBAR NAVIGATION (DRAWER PANE) ---
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='color:#0033AA; font-size:20px; font-weight:700; margin-bottom:2px; margin-top:10px;'>🧭 Trip Menu</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:13px; color:#555555 !important;'>Select any option below to instantly view details on your screen.</p>", unsafe_allow_html=True)
