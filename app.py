import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Noshay Navigations", page_icon="🧭", layout="centered")

# --- ADAPTIVE CSS FOR LIGHT/DARK MODE ---
st.markdown("""
    <style>
    /* Theme-agnostic variables */
    :root {
        --brand-green: #2e4a3d;
        --accent-gold: #c5a059;
    }

    /* Headings */
    h1, h2, h3 {
        color: var(--brand-green);
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* Price Card - Adapts to background */
    .price-card {
        padding: 30px;
        border-radius: 15px;
        border: 2px solid var(--brand-green);
        text-align: center;
        margin: 20px 0;
        background-color: rgba(46, 74, 61, 0.05);
    }

    /* Custom Button Style */
    div.stButton > button:first-child {
        background-color: var(--brand-green);
        color: white;
        border-radius: 10px;
        border: none;
        width: 100%;
        font-weight: bold;
    }

    /* Support for dark mode text visibility */
    @media (prefers-color-scheme: dark) {
        h1, h2, h3 {
            color: #9fbcac; /* Lighter sage green for dark mode readability */
        }
        .price-card {
            border-color: #9fbcac;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("🧭 Noshay Navigations")
st.markdown("### **Mapped for Adventure. Built for Life.**")

st.write("""
**Trail & Ultra Specialist | Performance Logistics | Exploration for All Levels**
""")

# --- HERO IMAGE ---
# Use the high-quality image we generated earlier
st.image("https://files.oaiusercontent.com/file-m7O6uI9hH8fK6yUuP6u3f6", 
         use_container_width=True)

st.divider()

# --- MISSION STATEMENT ---
st.header("The Strategy of the Stride")
st.write("""
Training shouldn't be a second full-time job. Whether you are prepping for your first 5K 
or a rugged 100-miler, **Noshay Navigations** specializes in the logistics of performance. 

I provide the map—helping you navigate work, family, and training—so you can focus on the exploration.
""")

# --- PRICING & SERVICES ---
st.header("The Navigation Package")

# Centered Price Card
st.markdown("""
<div class="price-card">
    <h1 style="margin:0;">$100/mo</h1>
    <p>Comprehensive Coaching & Logistics</p>
</div>
""", unsafe_allow_html=True)

# Columns for features
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### **The Plan**")
    st.write("📍 **Personalized Look-Ahead**")
    st.write("📅 **Adaptive Week-to-Week Planning**")
    st.write("⌚ **Interactive COROS Training Hub**")

with col2:
    st.markdown("#### **The Support**")
    st.write("📞 **Monthly Strategy Call**")
    st.write("💬 **Ad Hoc Text Communication**")
    st.write("🌲 **Specialized Trail/Ultra Expertise**")

st.divider()

# --- CALL TO ACTION / INTAKE ---
st.header("Ready to Plot Your Course?")
st.write("Tell me about your goals and your current schedule. Let's find the best route forward.")

with st.form("intake_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    current_goal = st.text_input("Target Race or Goal (Distance/Date)")
    schedule_constraint = st.text_area("What is your biggest logistical challenge? (e.g. Work travel, busy weekends, kids)")
    
    submitted = st.form_submit_button("Request My Route Map")
    if submitted:
        st.success(f"Route received, {name}! Check your email soon for your Initial Route Mapping questionnaire.")

# --- FOOTER ---
st.markdown("""
<div style="text-align: center; color: gray; font-size: 0.8em; margin-top: 50px;">
    Noshay Navigations © 2026 | All Levels. All Distances. One Map.
</div>
""", unsafe_allow_html=True)
