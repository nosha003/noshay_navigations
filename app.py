import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Noshay Navigations", page_icon="🧭", layout="centered")

# --- CUSTOM CSS FOR BRANDING ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f1;
    }
    h1, h2, h3 {
        color: #2e4a3d;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stButton>button {
        background-color: #2e4a3d;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 25px;
    }
    .price-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e0e0e0;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("🧭 Noshay Navigations")
st.subheader("Mapped for Adventure. Built for Life.")

st.markdown("""
**Trail & Ultra Specialist | Performance Logistics | Exploration for All Levels**
---
""")

# --- HERO IMAGE ---
# Note: Replace the URL below with your actual hosted image link
st.image("https://images.unsplash.com/photo-1551632432-c735e8a03278?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", 
         caption="Your Life is the Terrain. We Map the Training.")

# --- MISSION STATEMENT ---
st.header("The Strategy of the Stride")
st.write("""
Running doesn't happen in a vacuum—it happens between meetings, family dinners, and daily commitments. 
Whether you are training for your first 5K or your dream 100-miler, **Noshay Navigations** specializes 
in the logistics of performance. 

I don't just give you a template; I help you **navigate the week.** I provide the map so you can 
focus on the exploration.
""")

# --- SERVICES / TIERS ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🏁 Foundation")
    st.write("Starting your trail journey or building a base? We map the safety and the fun.")

with col2:
    st.markdown("### ⛰️ Elevation")
    st.write("Targeting a PR or a new distance? We navigate the technical shifts needed to level up.")

with col3:
    st.markdown("### 🗺️ Exploration")
    st.write("Specialized logistics for the Ultra-endurance athlete. Managing the high-mileage life.")

st.divider()

# --- PRICING SECTION ---
st.header("Coaching Navigation Package")
st.markdown("""
<div class="price-card">
    <h2 style="margin-bottom: 0;">$100 / month</h2>
    <p style="color: #666;">Comprehensive Coaching for Every Distance</p>
</div>
""", unsafe_allow_html=True)

st.write("") # Spacer
c1, c2 = st.columns(2)

with c1:
    st.markdown("#### **What’s Included:**")
    st.write("✅ **Personalized Look-Ahead:** A long-term vision of your season goals.")
    st.write("✅ **Week-to-Week Planning:** Dynamic schedules that adapt to your real life.")
    st.write("✅ **COROS Training Hub:** Full utilization of Coros data for interactive feedback.")

with c2:
    st.markdown("#### **Communication:**")
    st.write("📞 **Monthly Phone Call:** Deep dive into strategy and progress.")
    st.write("💬 **Ad Hoc Text Support:** Quick questions? On-the-fly adjustments? I'm a text away.")
    st.write("🏃 **Expert Guidance:** Specialized trail, ultra, and exploration advice.")

# --- CALL TO ACTION ---
st.divider()
st.header("Ready to Plot Your Course?")
contact_form = st.container()
with contact_form:
    name = st.text_input("Name")
    email = st.text_input("Email")
    goal = st.selectbox("What are we navigating toward?", ["First Trail Race", "Personal Best", "Ultra Distance", "General Fitness/Exploration"])
    message = st.text_area("Tell me about your schedule and your goals.")
    
    if st.button("Request Consultation"):
        st.success(f"Thanks {name}! I'll reach out to help you map your journey.")

# --- FOOTER ---
st.markdown("""
---
*Noshay Navigations © 2026* | **Mapped for Adventure. Built for Life.**
""")
