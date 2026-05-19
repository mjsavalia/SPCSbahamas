import streamlit as st
import datetime
import pandas as pd

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="SPCS Vacation Hub",
    page_icon="🚢",
    layout="centered"
)

# --- CUSTOM CSS FOR MODERN STYLING ---
st.markdown("""
    <style>
    .main-title { font-size: 34px; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size: 18px; color: #4B5563; text-align: center; margin-bottom: 25px; }
    .announcement-card { background-color: #FEF3C7; border-left: 5px solid #F59E0B; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
    .emergency-card { background-color: #FEE2E2; border-left: 5px solid #EF4444; padding: 15px; border-radius: 5px; margin-bottom: 20px; color: #991B1B; }
    .social-box { background-color: #F3F4F6; padding: 15px; border-radius: 8px; text-align: center; margin-bottom: 20px; }
    .social-icon { font-size: 20px; margin: 0 10px; text-decoration: none; color: #1E3A8A; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER & TITLE ---
st.markdown('<div class="main-title">🚢 SPCS Community Vacation Hub</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your central station for itineraries, safety, and coordination</div>', unsafe_allow_html=True)

# --- SIDEBAR: SOCIALS & EMERGENCY CONTACTS ---
with st.sidebar:
    st.header("🔗 Connect & Follow")
    st.markdown("""
    <div class="social-box">
        <p style="margin-bottom: 10px; font-weight: bold; color: #374151;">Stay Connected</p>
        <a href="https://instagram.com" target="_blank" class="social-icon">📸 Instagram</a>  
        <a href="https://facebook.com" target="_blank" class="social-icon">👥 Facebook</a>
    </div>
    """, unsafe_allow_html=True)
    
    st.header("🚨 Urgent Contacts")
    st.markdown("**Group Coordinator Line:**")
    st.code("+1 (555) 019-2831", language="text")
    st.markdown("**Ship/Port Emergency:**")
    st.code("+1 (555) 014-9982", language="text")
    st.caption("Keep these numbers saved in your phone contacts prior to departure!")

# --- NAVIGATION TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["⏳ Countdown & Itinerary", "🚨 Emergency Safety", "🌙 Nightly Check-In", "👥 Attendee Hub"])

# --- TAB 1: COUNTDOWN & ITINERARY ---
with tab1:
    # Countdown
    target_date = datetime.date(2026, 6, 3)
    today = datetime.date.today()
    days_left = (target_date - today).days
    
    if days_left > 0:
        st.metric(label="Days Until Miami Meetup", value=f"{days_left} Days")
        st.progress(max(0, min(100, (100 - days_left * 4)))) 
    elif days_left == 0:
        st.success("🎉 Today is the day! Welcome to Miami! Time to kick off the trip.")
    else:
        st.info("⚓ The cruise is underway! Enjoy the Bahamas!")

    st.markdown("---")
    st.subheader("📅 Group Schedule")
    
    itinerary_data = {
        "Day / Date": ["Wed, June 3", "Thu, June 4", "Fri, June 5", "Sat, June 6", "Sun, June 7"],
        "Activity": [
            "🛬 Arrival Day & Meetup in Miami",
            "🚢 Boarding Freedom of the Seas",
            "🏝️ Bahamas Island Excursion & Group Dinner",
            "🌊 Sea Day & Evening Gala",
            "🏁 Return to Port & Flights Home"
        ],
        "Time / Location": ["All Day - Hotel Lobby", "12:00 PM - Port of Miami", "9:00 AM - Cococay / Nassau", "All Day - Main Deck", "8:00 AM - Port of Miami"]
    }
    st.table(pd.DataFrame(itinerary_data))

# --- TAB 2: EMERGENCY SAFETY PROCEDURES ---
with tab2:
    st.subheader("🚨 Emergency Protocol & Procedures")
    
    st.markdown("""
    <div class="emergency-card">
        <strong>⚠️ IF YOU GET SEPARATED OR LOSE SIGNAL:</strong><br>
        1. <strong>Do Not Panic:</strong> Head to the nearest ship guest services desk or designated excursion landmark.<br>
        2. <strong>Ship Time:</strong> Always keep your watch set to <strong>Ship Time</strong>. Do not rely on your cell phone clock as it may shift timezones automatically.<br>
        3. <strong>All-Aboard Times:</strong> The ship will not wait for late passengers. Be back at least 1 hour before scheduled port departure.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("🛡️ Medical & Health Emergencies"):
        st.markdown("""
        * **On the Ship:** Dial the medical emergency number on any ship phone instantly. Medical bays are located on Deck 1.
        * **On Land / Excursions:** Stick to your assigned group buddies. If separated, notify local port authority staff immediately and present your cruise ship card.
        """)
        
    with st.expander("📇 Essential Info to Screenshot"):
        st.markdown("""
        **Ship Name:** Freedom of the Seas  
        **Departure Port:** Port of Miami, FL  
        **Important Note:** Take a physical picture of your passport page and save it locally on your camera roll so you can access it offline.
        """)

# --- TAB 3: END OF THE DAY CHECK-IN PORTAL ---
with tab3:
    st.subheader("🌙 End of the Day Check-In")
    st.write("To ensure everyone makes it back safely each evening, please check in before winding down for the night.")
    
    # Simple, mobile-friendly check-in form
    with st.form("check_in_form", clear_on_submit=True):
        st.write("### 📍 Submit Your Status")
        traveler_name = st.text_input("Your Full Name")
        
        safety_status = st.radio(
            "What is your current status?",
            ["✅ Safe in my cabin / room", "⏳ Out on the ship (with a group)", "⚠️ Need Assistance / Call me"]
        )
        
        current_location = st.text_input("Current Location / Room #", placeholder="e.g., Cabin 6214, or Star Lounge")
        notes = st.text_area("Notes or updates for the group leaders (Optional)", placeholder="e.g., Staying out for the comedy show with Jessica.")
        
        submitted_checkin = st.form_submit_button("Submit Evening Check-In")
        
        if submitted_checkin:
            if not traveler_name:
                st.error("Please enter your name before submitting.")
            else:
                st.success(f"Thank you, {traveler_name}! Your status has been successfully logged.")
                # In a full-stack production app, this data would save to a live database or Google Sheet.
                # For this localized version, it outputs confirmation directly.
                if "⚠️" in safety_status:
                    st.error("❗ A coordinator has been flagged that you need assistance. Please call the emergency line if urgent.")

# --- TAB 4: ATTENDEE HUB ---
with tab4:
    st.subheader("👥 Group Roster & Travel Status")
    
    attendee_data = {
        "Name": ["Sarah M.", "Jessica T.", "Elena R.", "Michelle W."],
        "Traveling From": ["Texas", "Maryland", "North Carolina", "Ohio"],
        "Miami Arrival": ["Confirmed (June 3)", "Confirmed (June 3)", "Arriving June 4", "Confirmed (June 3)"]
    }
    st.dataframe(pd.DataFrame(attendee_data), use_container_width=True)
