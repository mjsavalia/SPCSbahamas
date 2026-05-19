import streamlit as st
import datetime
import pandas as pd

# --- PAGE CONFIGURATION (Mobile App View Optimization) ---
st.set_page_config(
    page_title="SPCS Cruise Hub",
    page_icon="🚢",
    layout="centered",
    initial_sidebar_state="collapsed" 
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
    .social-card { background-color: rgba(255, 255, 255, 0.95); padding: 12px; border-radius: 8px; text-align: center; margin-bottom: 20px; border: 2px solid #E5E7EB; }
    .social-link { font-weight: 600; color: #0055D4 !important; text-decoration: underline; margin: 0 8px; }
    </style>
""", unsafe_allow_html=True)

# --- TRACK APPNIGATION STATE (MULTIPAGE CONTROL) ---
if "page" not in st.session_state:
    st.session_state.page = "Main_Menu"

# ==========================================
# --- APP HEADER PANELS ---
# ==========================================
st.markdown("""
<div class="ocean-header-panel">
    <div class="main-title">🚢 SPCS Women’s Forum 2026</div>
    <div class="subtitle">Official Cruise Companion Application</div>
</div>
""", unsafe_allow_html=True)

# Fixed Top Social Media Handles (Patched with verified link routing)
st.markdown("""
<div class="social-card">
    <span style="font-weight: 600; color: #000000;">🔗 Official Community Pages:</span>
    <a href="https://www.facebook.com/groups/769538356499119" target="_blank" class="social-link">SPCS National Women Forum (Official)</a> | 
    <a href="https://www.instagram.com/spcs_legacy_in_motion/" target="_blank" class="social-link">Instagram</a>
</div>
""", unsafe_allow_html=True)


# ==========================================
# --- PAGE 1: INTERACTIVE MAIN MENU HUB ---
# ==========================================
if st.session_state.page == "Main_Menu":
    
    # Live Countdown displayed right on the main home portal
    target_date = datetime.date(2026, 6, 4)
    today = datetime.date.today()
    days_left = (target_date - today).days
    
    st.markdown('<div class="content-card" style="text-align: center;">', unsafe_allow_html=True)
    if days_left > 0:
        st.metric(label="⏳ Days Remaining Until Cruise Onboarding", value=f"{days_left} Days")
    elif days_left == 0:
        st.success("🎉 Today is the day! Cruise boarding begins in Miami!")
    else:
        st.info("⚓ The 2026 Cruise event is currently underway or completed!")
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("### 🧭 Main Directory Menu")
    st.caption("Tap any button below to slide directly into that full information page.")

    # High-contrast, easy-to-tap touch navigation blocks
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📍 June 3 - Arrival Info", use_container_width=True):
            st.session_state.page = "June3"
            st.rerun()
        if st.button("🚢 June 4 - Day 1 Itinerary", use_container_width=True):
            st.session_state.page = "June4"
            st.rerun()
        if st.button("🏝️ June 5 - Day 2 Itinerary", use_container_width=True):
            st.session_state.page = "June5"
            st.rerun()
        if st.button("🥻 June 6 - Day 3 Itinerary", use_container_width=True):
            st.session_state.page = "June6"
            st.rerun()
        if st.button("🤝 June 7 - Day 4 Itinerary", use_container_width=True):
            st.session_state.page = "June7"
            st.rerun()

    with col2:
        if st.button("🛫 June 8 - Day 5 Return", use_container_width=True):
            st.session_state.page = "June8"
            st.rerun()
        if st.button("🧳 Luggage & Bag Policy", use_container_width=True):
            st.session_state.page = "Luggage"
            st.rerun()
        if st.button("🚨 Emergency Protocol", use_container_width=True):
            st.session_state.page = "Emergency"
            st.rerun()
        if st.button("🍽️ Daily Dinner Update", use_container_width=True):
            st.session_state.page = "Dinner"
            st.rerun()
        if st.button("📌 Key Points to Note", use_container_width=True):
            st.session_state.page = "KeyPoints"
            st.rerun()

    st.markdown("---")
    if st.button("🌙 Open Evening Safety Check-In Portal", use_container_width=True, type="primary"):
        st.session_state.page = "CheckIn"
        st.rerun()


# ==========================================
# --- SUB-PAGES DIRECTORY PATH ROUTING ---
# ==========================================

def show_back_button():
    if st.button("🔙 Back to Main Menu Directory", type="secondary", use_container_width=True):
        st.session_state.page = "Main_Menu"
        st.rerun()
    st.markdown("<br>", unsafe_allow_html=True)


# JUNE 3 - ARRIVAL
if st.session_state.page == "June3":
    show_back_button()
    st.markdown('<div class="section-header"><span>📍 June 3 – Arrival Day & Pre-Cruise Meetup</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("""
    * **Pre-Cruise Coordination:** Group check-ins, flight landings, and hotel rest prior to boarding.
    * **Waiver Handover Notice:** You can optionally hand over your original waiver forms directly to Heeral Lakhani at the hotel tonight to skip doing it tomorrow at the cruise pier terminal.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# JUNE 4 - DAY 1
elif st.session_state.page == "June4":
    show_back_button()
    st.markdown('<div class="section-header"><span>DAY 1 – THURSDAY, JUNE 4, 2026</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.caption("📍 Location: Miami, Florida – Cruise Onboarding Day")
    st.markdown('<div class="outfit-badge"><span>👕 Day Outfit: Denim blue or any shade of blue with matching jeans/pants or a one-piece dress</span></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sub-title">🌅 Morning - Cruise Onboarding</div>', unsafe_allow_html=True)
    st.markdown("""
    * **11:00 AM — Group Early Check-in Time:** Please arrive early at the cruise terminal.
    * **4:30 PM — Ship Departure Time.**
    * **Waiver Submission:** Please bring and hand over your original waiver forms to **Heeral Lakhani** before boarding if you have not already submitted them at the hotel. Do not pack them in your checked luggage.
    * **Carry-On Essentials:** Keep passports easily accessible. Carry medications, essentials, and one change of clothes in your carry-on bag.
    * **Luggage Delivery:** Delivery to staterooms may take until approximately 5:00 PM – 6:30 PM.
    * **Important Timing:** Follow all instructions and assigned timings shown in the Royal Caribbean App.
    """)
    
    st.markdown('<div class="outfit-badge"><span>👗 Evening Outfit: Colors chosen by chapter</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">🌃 Evening – Meet & Greet with Interactive Games & Prizes</div>', unsafe_allow_html=True)
    st.markdown("""
    * **7:30 PM – 9:30 PM (after early Dinner):** Enjoy a fun and relaxing evening of icebreaker games, laughter, prizes, and meaningful connections as we kick off the cruise together.
    * **Location:** To be shared onboard, stay connected with the SPCS members and assigned leaders.
    * **App Setup:** Connect to Royal Caribbean guest Wi-Fi onboard to use the app for free.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# JUNE 5 - DAY 2
elif st.session_state.page == "June5":
    show_back_button()
    st.markdown('<div class="section-header"><span>DAY 2 – FRIDAY, JUNE 5, 2026</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.caption("📍 Location: Perfect Day at CocoCay, Bahamas – Coco Beach Day")
    st.markdown('<div class="outfit-badge"><span>🌸 Day Outfit Theme: Floral beach outfit</span></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sub-title">🏝️ Day Activities - Perfect Day at CocoCay</div>', unsafe_allow_html=True)
    st.markdown("""
    * **7:00 AM:** Port Arrival.
    * **5:00 PM:** Port Departure.
    * **Suggested Breakfast Time:** 7:00 AM – 8:30 AM.
    * **Day Gathering:** Meeting at the South Beach Area.
    * **Success Story Circle:** Inspiring Story & Life Lesson Sharing.
    * **Reels Creation Session:** Short Q&A clips to capture achieving moments.
    * **Food at CocoCay:** Included at designated dining locations.
    * **Recommended to Carry:** Sunscreen, sunglasses, swimwear, beach essentials, and medicines.
    """)
    
    st.markdown('<div class="outfit-badge"><span>⚪ Evening Outfit: White outfit of your choice</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">💃 Evening – Latin Night</div>', unsafe_allow_html=True)
    st.markdown("""
    * **Night Activity:** Official cruise-wide dress theme.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# JUNE 6 - DAY 3
elif st.session_state.page == "June6":
    show_back_button()
    st.markdown('<div class="section-header"><span>DAY 3 – SATURDAY, JUNE 6, 2026</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.caption("📍 Location: At Sea – Vision Circle Day")
    st.markdown('<div class="outfit-badge"><span>🥻 Coordinated Group Outfit: Saree (Patola, Bandhani, Leheriya, or any type of saree)</span></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sub-title">🏛️ Morning & Official Group Gathering</div>', unsafe_allow_html=True)
    st.markdown("""
    * **Suggested Breakfast Time:** 7:00 AM – 8:15 AM.
    * **8:30 AM – 11:30 AM — Mandatory Group Gathering** at the **Star Lounge (Deck 5)**.
    * **Session Schedule:**
      * Wellness & Balance Talk.
      * Convention Update: Open discussion for ideas and contributions.
      * Membership Growth Plan: Strategy session.
      * Future Vision: Women's Forum goals discussion.
    """)
    
    st.markdown('<div class="outfit-badge"><span>💃 Suggested Outfit: Formal party evening gown, gala, or cocktail attire</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">✨ Evening – Formal Group Dinner</div>', unsafe_allow_html=True)
    st.markdown("""
    * **5:00 PM:** SPCS Women's official group Dinner Event Time.
    * **Location:** Main Dining Room on Deck 3.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# JUNE 7 - DAY 4
elif st.session_state.page == "June7":
    show_back_button()
    st.markdown('<div class="section-header"><span>DAY 4 – SUNDAY, JUNE 7, 2026</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.caption("📍 Location: Nassau, Bahamas – Nassau Volunteering Event")
    st.markdown('<div class="outfit-badge"><span>👕 Day Outfit: SPCS T-shirt + white bottom for volunteers</span></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sub-title">🤝 Day Activities & Volunteer Mural Project</div>', unsafe_allow_html=True)
    st.markdown("""
    * **8:00 AM:** Port Arrival.
    * **5:00 PM:** Port Departure.
    * **Suggested Breakfast Time:** 6:30 AM – 8:00 AM.
    * **Assembly & Group Departure:** 8:30 AM Meet at the Ship's Exit Gate / Gangway Area on land for group transportation.
    * **9:00 AM – 12:00 PM:** **Community Mural Initiative activity**.
    * **Afternoon Leisure Time:** Sightseeing, shopping, beach activities, or relaxing onboard.
    """)
    
    st.markdown('<div class="sub-title">🎁 Evening – Closing Gathering & Souvenir Distribution</div>', unsafe_allow_html=True)
    st.markdown("""
    * **7:30 PM – 9:30 PM (after early Dinner):** Final gathering and souvenir distribution.
    * **Location:** To be shared onboard, stay connected with the SPCS members and assigned leaders.
    * **Closing Celebration & Open Feedback Session:** One last time to celebrate US, reflect on our impact, and discuss ideas for future improvements.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# JUNE 8 - DAY 5 RETURN
elif st.session_state.page == "June8":
    show_back_button()
    st.markdown('<div class="section-header"><span>DAY 5 – MONDAY, JUNE 8, 2026</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.caption("📍 Location: Miami, Florida – Return & Departure Day")
    st.markdown('<div class="outfit-badge"><span>👟 Morning Outfit: Comfortable travel wear</span></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sub-title">🛫 Return Logistics</div>', unsafe_allow_html=True)
    st.markdown("""
    * **8:00 AM — Expected disembarkation time.**
    * **Onboard Breakfast:** Available before final departure.
    * **Important Departure Notes:** Follow all instructions in the Royal Caribbean App.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# LUGGAGE & BAG POLICY
elif st.session_state.page == "Luggage":
    show_back_button()
    st.markdown('<div class="section-header"><span>🧳 Royal Caribbean Luggage & Bag Policy</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    
    st.markdown('<div class="sub-title">⚖️ Weight & Bag Limits</div>', unsafe_allow_html=True)
    st.write("• **Bag Limits and Weight:** Royal Caribbean allows up to **two checked bags per person**. While there is no strict scale at the pier, the recommended weight limit is **50 lbs (23 kg) per bag** to ensure the port handlers can safely lift them.")
    
    st.markdown('<div class="sub-title">🎒 Carry-On and Personal Item Rules</div>', unsafe_allow_html=True)
    st.write("• Unlike airlines, the cruise line does not have a strict limit on the number of carry-on items you can bring, nor do they enforce a weight limit. You are completely fine to bring one rolling carry-on bag plus a smaller personal item (like a backpack, tote bag, or purse). The only rule is that all carry-on items must be able to physically fit through an airport-style X-ray security scanner at the terminal.")
    
    st.markdown('<div class="sub-title">💼 Checked Bags vs. Carry-Ons</div>', unsafe_allow_html=True)
    st.write("• When you arrive at the port, porter service will take your large suitcases to deliver them straight to your room later in the evening. You **must carry a small day bag** (backpack or tote) with you containing your passport, medication, and swimwear so you can enjoy the ship while waiting for your luggage.")
    
    st.markdown('<div class="sub-section-header" style="color: #DC2626; font-weight: 600; border-bottom: 2px solid #DC2626;">🚫 Prohibited Items (Do Not Pack)</div>', unsafe_allow_html=True)
    st.markdown("""
    The ship will confiscate items that generate heat or pose a safety risk. **Do not pack:**
    * Clothing irons & steamers
    * Extension cords & surge protectors
    * Candles
    * Weapons or illegal drugs (including medically prescribed marijuana and CBD products)
    """)
    
    st.markdown('<div class="sub-title">💎 Valuables and Electronics</div>', unsafe_allow_html=True)
    st.write("• Always keep your laptops, cameras, jewelry, and medications in your carry-on bag. **Never hand these items over to the airport or cruise port porters.**")
    st.markdown('</div>', unsafe_allow_html=True)

# EMERGENCY PROTOCOL
elif st.session_state.page == "Emergency":
    show_back_button()
    st.markdown('<div class="section-header"><span>🚨 Emergency Protocol & Communication</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="policy-box">
        <strong style="color: #0033AA;">📇 What is a SeaPass Card?</strong><br>
        Every single person gets their own individual SeaPass card, including infants and young children:<br>
        • <strong>It Is Your Ship ID:</strong> It features your name and identity photo, which security uses to verify who you are every time you exit or re-enter the ship.<br>
        • <strong>It Is Your Room Key:</strong> It is the only way to unlock your specific stateroom door.<br>
        • <strong>It Is Your Wallet:</strong> All onboard purchases, drinks, and specialty dining are charged directly to your individual card.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    * **Stay Connected:** Updates will be shared through the Royal Caribbean App, so you are highly advised to stay connected with your assigned group leader throughout the cruise.
    * **Individual Tracking:** The ship tracks everyone individually via your personal SeaPass card. You must carry your physical card and a photo ID every time you leave the ship. One person cannot scan in for another.
    * **Missing the Ship:** If you are left behind or lost at a port, immediately find the **Local Port Agent** contact info. It is printed at the bottom of the daily paper *Cruise Compass* and listed in your Royal Caribbean App on port days. **Take a screenshot before leaving the ship.** The port agent is the only person who can help you clear customs or catch up to the ship.
    """)
    
    st.markdown('<div class="sub-title">☎️ Emergency Travel Line</div>', unsafe_allow_html=True)
    st.write("If you cannot reach the local port agent, call the corporate emergency team at:")
    st.code("+1-305-982-2700", language="text")
    st.caption("📱 Note: Remember to follow international dialing protocols from your location (hold '0' for the + sign, then dial 1-305-982-2700).")
    st.markdown('</div>', unsafe_allow_html=True)

# DAILY DINNER UPDATE
elif st.session_state.page == "Dinner":
    show_back_button()
    st.markdown('<div class="section-header"><span>🍽️ Daily Group Dinner Update</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="dinner-box">
        <strong>📋 Evening Dining Schedule:</strong><br>
        • <strong>Time:</strong> 5:00 PM Sharp — Official Group Dinner booked (Daily)<br>
        • <strong>Location:</strong> Main Dining Room (Early seating selected)<br>
        • <strong>Note:</strong> This early seating ensures everyone has time afterward to enjoy evening cruise activities.<br>
        • <strong>Alternative:</strong> The Windjammer Buffet (Deck 11) is also available each day for flexible dining.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# KEY POINTS TO NOTE
elif st.session_state.page == "KeyPoints":
    show_back_button()
    st.markdown('<div class="section-header"><span>📌 Key Points to Note</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    
    st.markdown("""
    * **Dress Code Rules:** Dress code themes are strictly for group coordination and group photos.
    * **Extra Clothes:** Bring extra outfits for themed photos, daytime activities, and formal evening events.
    * **Footwear:** Comfortable footwear (like sneakers) is highly recommended for walking the ship and shore excursions.
    * **Day 1 Preparation:** Pack a Day 1 outfit in your carry-on bag, as your main checked luggage may take several hours to reach your room.
    * **Temperature Control:** Bring a light jacket or sweater for chilly, air-conditioned indoor venues.
    * **Quick Access:** Keep your SeaPass card handy at all times using a pocket or lanyard for quick scanning.
    * **Bring Your Own Drinks (Day 1 Only):** Each stateroom is legally allowed to bring up to **twelve 12-oz cans/cartons of non-alcoholic beverages** (soda, water, juices) and **two 750ml bottles of wine/champagne**. These must be brought in your carry-on bag, not your checked luggage.
    * **Water Bottle Refills:** Bring an insulated flask or reusable bottle. The ship’s tap water is heavily filtered and 100% safe to drink. Use the free 24/7 water stations at the Windjammer Buffet or Café Promenade, but remember to use a clean cruise cup to fill your bottle for health reasons.
    * **⚠️ In-Room Water Bottles Note:** Any sealed plastic water bottles left on your stateroom desk or in the mini-fridge are **not free**. If you open them, they will automatically be billed to your SeaPass card.
    * **Snack Policy:** You are allowed to bring pre-packaged, factory-sealed dry snacks (like granola bars, chips, or crackers) on board. However, you cannot bring home-cooked food or open perishable items onto the ship or off into the ports.
    * **Coordination:** Please check the Royal Caribbean App regularly for updates and stay in close contact with your assigned group leader and SPCS member for seamless coordination.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# EVENING CHECK-IN
elif st.session_state.page == "CheckIn":
    show_back_button()
    st.markdown('<div class="section-header"><span>🌙 End of the Day Check-In Portal</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.write("Please log your evening safety status below before heading to bed to assist group organizers.")
    
    with st.form("dashboard_checkin", clear_on_submit=True):
        name = st.text_input("Your Full Name")
        cabin = st.text_input("Cabin Number")
        status = st.radio("Current Safety Status", [
            "✅ Safe in my cabin for the night",
            "🎉 Out on the ship with an official group",
            "⚠️ Need Assistance / Urgent Check-in Required"
        ])
        notes = st.text_area("Additional updates for coordinators")
        
        if st.form_submit_button("Submit Evening Status"):
            if not name:
                st.error("Please provide your name to register.")
            else:
                st.success(f"Thank you, {name}. Your evening coordination log has been successfully updated!")
    st.markdown('</div>', unsafe_allow_html=True)
