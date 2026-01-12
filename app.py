import streamlit as st
import requests

# --- PAGE CONFIG ---
st.set_page_config(page_title="Noshay Navigations", page_icon="🧭", layout="wide")

# --- REFINED CSS FOR EXACT LAYOUT ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* Background Hue */
    .stApp {
        background-color: #f1f4ef; /* Subtle Green Hue */
    }

    /* Top Nav Bar - Removed right side icons */
    .nav-header {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        padding: 10px 0;
        border-bottom: 1px solid #d1d8d1;
        margin-bottom: 30px;
    }

    /* Hero Proportions */
    .main-title {
        color: #2e4a3d;
        font-size: 48px;
        font-weight: 700;
        margin-bottom: 0px;
        letter-spacing: -1px;
    }
    .tagline {
        color: #3e5c46;
        font-size: 26px; /* Larger Slogan */
        font-weight: 500;
        margin-top: -5px;
        margin-bottom: 15px;
    }
    .sub-labels {
        color: #2e4a3d;
        font-size: 15px;
        font-weight: 500;
        background: rgba(46, 74, 61, 0.1);
        padding: 5px 10px;
        border-radius: 5px;
        display: inline-block;
    }

    /* Image Sizing */
    .hero-img {
        border-radius: 12px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
    }

    /* Pillar Styling with Emojis */
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

    hr {
        border: 0;
        border-top: 1px solid #d1d8d1;
        margin: 40px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- TOP NAVIGATION ---
st.markdown("""
    <div class="nav-header">
        <div style="display:flex; align-items:center; gap:12px;">
            <span style="font-size:24px;">🧭</span>
            <span style="font-weight:700; font-size:20px; color:#2e4a3d; letter-spacing: -0.5px;">Noshay Navigations</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
# Adjusting column ratio to make text area larger and image area smaller
col_text, col_img = st.columns([2.2, 1])

with col_text:
    st.markdown('<div class="main-title">Noshay Navigations</div>', unsafe_allow_html=True)
    st.markdown('<div class="tagline">🌲 Mapped for Adventure. Built for Life.</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-labels">🏁 Trail & Ultra Specialist | Performance | Exploration for All Levels</div>', unsafe_allow_html=True)

with col_img:
    # Smaller, contained image
    st.image("https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=500&q=80", use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- THE PILLARS ---
p1, p2, p3 = st.columns(3)
with p1:
    st.markdown('<div class="pillar-title">🌱 Foundation</div>', unsafe_allow_html=True)
    st.markdown('<div class="pillar-text">Starting your trail journey or building. We map the terrain and the fun for every beginner level.</div>', unsafe_allow_html=True)
with p2:
    st.markdown('<div class="pillar-title">🏔️ Elevation</div>', unsafe_allow_html=True)
    st.markdown('<div class="pillar-text">Targeting your PR or new distance? Logistics tailored to level up your performance.</div>', unsafe_allow_html=True)
with p3:
    st.markdown('<div class="pillar-title">🗺️ Exploration</div>', unsafe_allow_html=True)
    st.markdown('<div class="pillar-text">Specialized for high-mileage life. We navigate the tactical shifts needed for long-term health.</div>', unsafe_allow_html=True)

# --- STRATEGY SECTION ---
st.markdown('<div style="color: #1a1a1a; font-size: 26px; font-weight: 700; margin-top: 40px; margin-bottom: 15px;">The Strategy of the Stride</div>', unsafe_allow_html=True)
st.markdown('<div style="font-size: 15px; line-height: 1.7; color: #333;">Running doesn’t happen in a vacuum—it happens between meetings, family, and daily commitments. Whether training for your first 5k or a 100-miler, I provide the logistics of performance mapped to your real life. I provide the map so you can focus on the exploration.</div>', unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

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
        <div style="color: #1a1a1a; font-size: 36px; font-weight: 700;">$100 <span style="font-size:18px; font-weight:400; color:#666;">/ month</span></div>
        <div style="color:#333; font-size:14px; margin-top:8px;">Comprehensive Coaching for Every Distance</div>
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
        if name and email: # Basic validation
            # The FormSubmit endpoint
            url = f"https://formsubmit.co/ajax/jmnosh@gmail.com" # <--- REPLACE WITH YOUR EMAIL
            
            # Prepare the data payload
            payload = {
                "Name": name,
                "Email": email,
                "Goal": goal,
                "Message": msg,
                "_subject": f"New Noshay Navigations Lead: {name}"
            }
            
            # Send the request in the background
            response = requests.post(url, json=payload)
            
            if response.status_code == 200:
                st.success("Logistics received. I'll reach out to start your mapping shortly!")
            else:
                st.error("There was an error sending your request. Please try again or email me directly.")
        else:
            st.warning("Please provide both your name and email address.")

# --- FOOTER ---
st.markdown(f"""
    <div style="text-align: center; border-top: 1px solid #d1d8d1; margin-top: 60px; padding: 30px; font-size: 13px; color: #2e4a3d; opacity: 0.8;">
        Noshay Navigations © 2026 &nbsp; | &nbsp; Mapped for Adventure. Built for Life.
    </div>
""", unsafe_allow_html=True)