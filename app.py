import streamlit as st
import requests

# --- PAGE CONFIG ---
st.set_page_config(page_title="Noshay Navigations", page_icon="🧭", layout="wide")

# --- REFINED CSS FOR EXACT LAYOUT & NAVIGATION ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* Background Hue */
    .stApp {
        background-color: #f1f4ef; /* Subtle Green Hue */
    }

    /* Top Nav Bar - Dropdown Style */
    .nav-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px 0;
        border-bottom: 1px solid #d1d8d1;
        margin-bottom: 20px;
    }

    /* Hero Proportions */
    .main-title {
        color: #2e4a3d;
        font-size: 52px; /* Slightly larger */
        font-weight: 700;
        margin-bottom: 0px;
        letter-spacing: -1px;
    }
    .tagline {
        color: #3e5c46;
        font-size: 28px; /* Larger Slogan to fill space */
        font-weight: 500;
        margin-top: -5px;
        margin-bottom: 15px;
        line-height: 1.2;
    }
    .sub-labels {
        color: #2e4a3d;
        font-size: 15px;
        font-weight: 500;
        background: rgba(46, 74, 61, 0.1);
        padding: 5px 12px;
        border-radius: 5px;
        display: inline-block;
    }

    /* Pillar Styling */
    .pillar-title {
        color: #2e4a3d;
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .pillar-text {
        font-size: 14px;
        color: #4a4a4a;
        line-height: 1.6;
    }

    /* Price Card (Dashed) */
    .price-card-container {
        background-color: white;
        border: 2px dashed #9fbcac;
        border-radius: 12px;
        padding: 40px 20px;
        text-align: center;
    }

    /* Button Styling */
    .stButton > button {
        background-color: #2e4a3d !important;
        color: white !important;
        border-radius: 6px !important;
        padding: 10px 30px !important;
        font-weight: 600 !important;
    }

    /* Custom Dropdown placement */
    .stSelectbox {
        margin-top: -15px;
    }

    hr {
        border: 0;
        border-top: 1px solid #d1d8d1;
        margin: 30px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- TOP NAVIGATION & DROPDOWN ---
# This creates the header bar with the logo on left and dropdown on right
col_logo, col_nav = st.columns([2, 1])

with col_logo:
    st.markdown("""
        <div style="display:flex; align-items:center; gap:12px; padding-top:10px;">
            <span style="font-size:24px;">🧭</span>
            <span style="font-weight:700; font-size:20px; color:#2e4a3d; letter-spacing: -0.5px;">Noshay Navigations</span>
        </div>
    """, unsafe_allow_html=True)

with col_nav:
    # Dropdown menu for navigation
    page = st.selectbox(
        "Navigation",
        ["🗺️ Coaching", "📚 Research & Resources", "🏆 Accomplishments"],
        label_visibility="collapsed"
    )

st.markdown("<hr style='margin-top:0;'>", unsafe_allow_html=True)

# --- PAGE LOGIC ---

if page == "🗺️ Coaching":
    # --- HERO SECTION ---
    col_text, col_img = st.columns([2.5, 1]) # Tightened ratio for larger slogan

    with col_text:
        st.markdown('<div class="main-title">Noshay Navigations</div>', unsafe_allow_html=True)
        st.markdown('<div class="tagline">Mapped for Adventure. <br>Built for Life.</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-labels">🏁 Portland-Based Trail & Ultra Specialist | Performance Logistics</div>', unsafe_allow_html=True)

    with col_img:
        # Smaller, cleaner image footprint
        st.image("https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=500&q=80", use_container_width=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # --- THE PILLARS ---
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="pillar-title">🌱 Foundation</div>', unsafe_allow_html=True)
        st.markdown('<div class="pillar-text">Navigating the transition from road to trail or building your first base. We map the terrain and the fun.</div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="pillar-title">🏔️ Elevation</div>', unsafe_allow_html=True)
        st.markdown('<div class="pillar-text">Targeting a PR or a new distance? Performance logistics tailored to level up your vertical game.</div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="pillar-title">🗺️ Exploration</div>', unsafe_allow_html=True)
        st.markdown('<div class="pillar-text">Specialized for high-mileage life. We navigate the tactical shifts needed for long-term health and speed.</div>', unsafe_allow_html=True)

    # --- STRATEGY SECTION ---
    st.markdown('<div style="color: #1a1a1a; font-size: 26px; font-weight: 700; margin-top: 40px; margin-bottom: 15px;">The Strategy of the Stride</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 15px; line-height: 1.7; color: #333;">Running doesn’t happen in a vacuum—it happens between meetings, family, and daily commitments. Whether training for your first 5k or a 100-miler in the PNW, I provide the logistics of performance mapped to your real life. I provide the map so you can focus on the exploration.</div>', unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # --- COACHING PACKAGE SECTION ---
    st.markdown('<div style="color: #1a1a1a; font-size: 26px; font-weight: 700; margin-bottom: 25px;">Coaching Navigation Package</div>', unsafe_allow_html=True)

    pkg_col1, pkg_col2 = st.columns([1, 1.2])

    with pkg_col1:
        st.markdown("""
            <div class="price-card-container">
                <div style="color: #2e4a3d; font-size: 36px; font-weight: 700;">$100 <span style="font-size:18px; font-weight:400; color:#666;">/ month</span></div>
                <div style="color:#666; font-size:14px; margin-top:8px;">Comprehensive Coaching for Every Distance</div>
            </div>
        """, unsafe_allow_html=True)

    with pkg_col2:
        st.markdown("### What's Included:")
        st.write("✅ **Personalized Look-Ahead:** Season-long vision and goal alignment.")
        st.write("✅ **Week-to-Week Planning:** Dynamic schedules built for real life.")
        st.write("✅ **COROS Training Hub:** Data-driven technical metrics.")
        st.write("📞 **Monthly Deep Dive:** Phone strategy calls + Ad Hoc text support.")

    st.markdown("<hr>", unsafe_allow_html=True)

    # --- INTAKE FORM SECTION ---
    st.markdown('<div style="color: #1a1a1a; font-size: 26px; font-weight: 700; margin-bottom: 20px;">Ready to Plot Your Course?</div>', unsafe_allow_html=True)

    with st.form("intake_form", clear_on_submit=True):
        name = st.text_input("Name", placeholder="Your Name")
        email = st.text_input("Email", placeholder="Your Email Address")
        goal = st.text_input("Goal", placeholder="What race or milestone are we targeting?")
        msg = st.text_area("Message", placeholder="Tell me about your schedule and goals...")
        
        submit_button = st.form_submit_button("Request Consultation")

        if submit_button:
            if name and email:
                url = f"https://formsubmit.co/ajax/jmnosh@gmail.com"
                payload = {
                    "Name": name,
                    "Email": email,
                    "Goal": goal,
                    "Message": msg,
                    "_subject": f"New Noshay Navigations Lead: {name}"
                }
                try:
                    response = requests.post(url, json=payload)
                    if response.status_code == 200:
                        st.success("Logistics received. I'll reach out to start your mapping shortly!")
                    else:
                        st.error("Error sending request. Please try again.")
                except:
                    st.error("Connection error. Please try again.")
            else:
                st.warning("Please provide both your name and email address.")

elif page == "📚 Research & Resources":
    st.markdown('<div class="main-title">Resource Library</div>', unsafe_allow_html=True)
    st.markdown('<div class="tagline">Science-backed navigation for the long haul.</div>', unsafe_allow_html=True)
    
    st.divider()

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### 🧪 Endurance Science")
        st.markdown("""
        * **[Science of Ultra](https://www.scienceofultra.com/podcasts):** Master-level physiological breakdowns.
        * **[ISSN Guidelines](https://jissn.biomedcentral.com/):** Evidence-based fueling protocols.
        * **[The FASTER Study](https://www.metabolismjournal.com/article/S0026-0495(15)00334-0/fulltext):** Research on metabolic efficiency.
        """)
    with col_b:
        st.markdown("### 🗺️ Trail & Navigation Tools")
        st.markdown("""
        * **[CalTopo](https://caltopo.com/):** High-level topographic planning.
        * **[FarOut Guides](https://faroutguides.com/):** Long-distance thru-run navigation.
        * **[Forest Park Conservancy](https://forestparkconservancy.org/):** Local Portland trail maps and updates.
        """)

elif page == "🏆 Accomplishments":
    st.markdown('<div class="main-title">The Field Log</div>', unsafe_allow_html=True)
    st.markdown('<div class="tagline">Jaclyn Noshay: Experience on the Dirt.</div>', unsafe_allow_html=True)
    
    # ADDED: Professional link button to your results
    st.link_button("View Full Results on UltraSignup", 
                   "https://ultrasignup.com/results_participant.aspx?fname=Jaclyn&lname=Noshay",
                   type="primary")
    
    st.divider()

    col_stats1, col_stats2 = st.columns(2)
    with col_stats1:
        st.info("🏔️ **Ultra Distance Specialist**")
        st.write("Consistent finisher of challenging West Coast trail events, with multiple top-tier finishes in the 100M and 100K distances.")
    with col_stats2:
        st.success("🌲 **PNW Expert**")
        st.write("Deep familiarity with the steep grades and technical terrain of Oregon and Washington trail systems.")

    st.markdown('<div class="section-header">Recent Race Results</div>', unsafe_allow_html=True)
    
    # Refined based on updated UltraSignup Participant Data
    st.table([
        {"Year": "2024", "Event": "Oregon Cascades 100", "Dist": "100 Miler", "Result": "5th Overall"},
        {"Year": "2024", "Event": "Siskiyou Out Back (SOB)", "Dist": "100K", "Result": "13th Overall"},
        {"Year": "2024", "Event": "Smith Rock Classic", "Dist": "50K", "Result": "8th Overall"},
        {"Year": "2023", "Event": "Superior Fall Trail Race", "Dist": "100 Miler", "Result": "8th Overall"},
        {"Year": "2022", "Event": "No Business 100", "Dist": "100 Miler", "Result": "6th Overall"}
    ])
    
    st.markdown("""
    > **Coach's Perspective:** My race history is a map of lessons learned. From the high desert heat of Smith Rock to the rugged technicality of the Superior 100, 
    > I leverage my personal experience to help you navigate the logistics of your own specific race day.
    """)

# --- FOOTER ---
st.markdown(f"""
    <div style="text-align: center; border-top: 1px solid #d1d8d1; margin-top: 60px; padding: 30px; font-size: 13px; color: #2e4a3d; opacity: 0.8;">
        Noshay Navigations © 2026 &nbsp; | &nbsp; Portland, Oregon &nbsp; | &nbsp; Mapped for Adventure. Built for Life.
    </div>
""", unsafe_allow_html=True)