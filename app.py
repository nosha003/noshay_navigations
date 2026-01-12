import streamlit as st
import requests

# --- PAGE CONFIG ---
st.set_page_config(page_title="Noshay Navigations", page_icon="🧭", layout="wide")

# --- ADAPTIVE NATIVE CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* This targets the main background using Streamlit's internal variable */
    .stApp {
        font-family: 'Inter', sans-serif;
    }

    /* Top Nav Bar - Bottom border adapts to theme */
    .nav-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px 0;
        border-bottom: 1px solid rgba(128, 128, 128, 0.2);
        margin-bottom: 20px;
    }

    /* Titles use the primary 'text' color of the current theme */
    .main-title {
        color: var(--text-color);
        font-size: 52px;
        font-weight: 700;
        margin-bottom: 0px;
        letter-spacing: -1px;
    }

    /* Use your brand green as a secondary accent color */
    .tagline {
        color: #3e5c46; 
        font-size: 28px;
        font-weight: 500;
        margin-top: -5px;
        margin-bottom: 15px;
        line-height: 1.2;
    }

    /* Sub-labels with a semi-transparent background that works on light or dark */
    .sub-labels {
        font-size: 15px;
        font-weight: 500;
        background: rgba(62, 92, 70, 0.15);
        color: #3e5c46;
        padding: 5px 12px;
        border-radius: 5px;
        display: inline-block;
    }

    /* Cards that adapt their background based on the theme */
    .stat-card, .price-card-container {
        background-color: rgba(128, 128, 128, 0.05);
        padding: 25px;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.1);
        text-align: center;
    }

    .stat-val {
        color: #3e5c46;
        font-size: 28px;
        font-weight: 700;
    }

    /* Hamburger Dropdown fix */
    div[data-baseweb="select"] {
        width: 75px !important;
        float: right;
    }

    /* Button stays brand-consistent */
    .stButton > button {
        background-color: #2e4a3d !important;
        color: white !important;
        border: none !important;
    }

    hr {
        border: 0;
        border-top: 1px solid rgba(128, 128, 128, 0.2);
        margin: 30px 0;
    }
    </style>
    """, unsafe_allow_html=True)


# --- TOP NAVIGATION (HAMBURGER STYLE) ---
col_left, col_right = st.columns([5, 1])

with col_left:
    st.markdown("""
        <div style="display:flex; align-items:center; gap:12px;">
            <span style="font-size:24px;">🧭</span>
            <span style="font-weight:700; font-size:20px; color:#2e4a3d;">Noshay Navigations</span>
        </div>
    """, unsafe_allow_html=True)

with col_right:
    # The '☰' serves as the label for the dropdown
    page = st.selectbox("☰", ["Coaching", "Research & Resources", "My Story & Accomplishments"], label_visibility="visible")

st.markdown("<hr style='margin-top:0;'>", unsafe_allow_html=True)

# --- PAGE LOGIC ---

if page == "Coaching":
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

    # --- COACHING PACKAGE SECTION ---
    st.markdown('<div style="color: #1a1a1a; font-size: 26px; font-weight: 700; margin-bottom: 25px;">Coaching Navigation Package</div>', unsafe_allow_html=True)

    pkg_col1, pkg_col2 = st.columns([1, 1.2])

    with pkg_col1:
        st.markdown("### What's Included:")
        st.write("✅ **Personalized Look-Ahead:** A long-term vision of your season goals.")
        st.write("✅ **Week-to-Week Planning:** Dynamic schedules that adapt to your real life.")
        st.write("✅ **COROS Training Hub:** Full utilization of technical metrics.")

    with pkg_col2:
        st.markdown("#### **Communication:**")
        st.write("📞 **Monthly Phone Call:** Deep dive into strategy and progress.")
        st.write("💬 **Ad Hoc Text Support:** Quick questions? On-the-fly adjustments? I'm a text away.")
        st.write("🏃 **Expert Guidance:** Specialized trail, ultra, and exploration advice.")
        
    st.markdown("""
            <div class="price-card-container">
                <div style="color: #2e4a3d; font-size: 36px; font-weight: 700;">$100 <span style="font-size:18px; font-weight:400; color:#666;">/ month</span></div>
                <div style="color:#666; font-size:14px; margin-top:8px;">Comprehensive Coaching for Every Distance</div>
            </div>
        """, unsafe_allow_html=True)

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

elif page == "Research & Resources":
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

elif page == "About & Accomplishments":
    st.markdown('<div class="main-title">About Jaclyn Noshay</div>', unsafe_allow_html=True)
    
    col_bio, col_stats = st.columns([1.5, 1])
    
    with col_bio:
        st.write("""
        I am a Portland-based ultra-endurance athlete and coach who believes that performance is a logistical puzzle. 
        With over a decade of experience on the dirt—ranging from the technical alpine trails of the PNW to the 
        humid, rugged forests of the East Coast—I have learned that training for a 100-miler shouldn't 
        require sacrificing your career or family life.
        
        My coaching philosophy is simple: **I provide the map, you provide the engine.**
        """)
        st.link_button("View Full UltraSignup Profile", "https://ultrasignup.com/results_participant.aspx?fname=Jaclyn&lname=Noshay")

    with col_stats:
        # Displaying DP and Rankings from UltraSignup
        st.markdown(f"""
            <div class="stat-card">
                <div style="font-size:14px; color:gray;">UltraSignup Rank</div>
                <div class="stat-val">91.85%</div>
                <div style="font-size:12px; margin-top:10px;">Consistently ranked in the top tier of female ultra-athletes.</div>
            </div>
            <br>
            <div class="stat-card">
                <div style="font-size:14px; color:gray;">Overall Finish Rate</div>
                <div class="stat-val">100%</div>
                <div style="font-size:12px; margin-top:10px;">Technical efficiency across 100M, 100K, and 50K distances.</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🏆 The Field Log")
    st.table([
        {"Year": "2024", "Event": "Oregon Cascades 100M", "Rank": "5th Female", "Category": "100 Miler"},
        {"Year": "2024", "Event": "Siskiyou Out Back 100K", "Rank": "13th Overall", "Category": "100K"},
        {"Year": "2024", "Event": "Smith Rock Classic 50K", "Rank": "8th Female", "Category": "50K"},
        {"Year": "2023", "Event": "Superior Fall Trail Race 100M", "Rank": "8th Female", "Category": "100 Miler"},
        {"Year": "2022", "Event": "No Business 100M", "Rank": "6th Female", "Category": "100 Miler"}
    ])

# --- FOOTER ---
st.markdown(f"""
    <div style="text-align: center; border-top: 1px solid #d1d8d1; margin-top: 60px; padding: 30px; font-size: 13px; color: #2e4a3d; opacity: 0.8;">
        Noshay Navigations © 2026 &nbsp; | &nbsp; Portland, Oregon &nbsp; | &nbsp; Mapped for Adventure. Built for Life.
    </div>
""", unsafe_allow_html=True)