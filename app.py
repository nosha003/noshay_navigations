import streamlit as st
import requests

# --- PAGE CONFIG ---
st.set_page_config(page_title="Noshay Navigations", page_icon="🧭", layout="wide")

# --- REFINED DUAL-MODE CSS (CLEAN DROPDOWN) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* 1. COLOR VARIABLES */
    :root {
        --bg-color: #f1f4ef;
        --text-header: #2e4a3d;
        --text-body: #333333;
        --card-bg: #ffffff;
        --border-color: #d1d8d1;
        --accent-green: #3e5c46;
    }

    @media (prefers-color-scheme: dark) {
        :root {
            --bg-color: #0f1410;
            --text-header: #c5d1c9;
            --text-body: #e0e0e0;
            --card-bg: #1a211b;
            --border-color: #2d382f;
            --accent-green: #89a391;
        }
    }

    .stApp {
        background-color: var(--bg-color);
        font-family: 'Inter', sans-serif;
    }

    /* 2. HEADER & DROPDOWN ALIGNMENT */
    .nav-header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 10px;
        border-bottom: 1px solid var(--border-color);
        margin-bottom: 25px;
    }

    /* Forces the selectbox to stay small and aligned right */
    div[data-testid="stHorizontalBlock"] > div:last-child {
        display: flex;
        justify-content: flex-end;
        align-items: center;
    }

    /* 3. TYPOGRAPHY */
    .main-title {
        color: var(--text-header);
        font-size: 52px;
        font-weight: 700;
        margin-bottom: 0px;
        letter-spacing: -1px;
    }

    .tagline {
        color: var(--accent-green);
        font-size: 28px;
        font-weight: 500;
        margin-top: -5px;
        margin-bottom: 15px;
    }

    .sub-labels {
        color: var(--text-header);
        font-size: 15px;
        background: rgba(137, 163, 145, 0.2);
        padding: 5px 12px;
        border-radius: 5px;
        display: inline-block;
    }

    .pillar-title {
        color: var(--text-header);
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .pillar-text {
        font-size: 14px;
        color: var(--text-body);
        line-height: 1.6;
    }

    /* 4. COMPONENTS */
    .stat-card, .price-card-container {
        background-color: var(--card-bg);
        padding: 25px;
        border-radius: 12px;
        border: 1px solid var(--border-color);
        text-align: center;
        color: var(--text-body);
    }

    .stat-val {
        color: var(--accent-green);
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .stButton > button {
        background-color: #2e4a3d !important;
        color: white !important;
        border-radius: 6px !important;
    }

    hr { border-top: 1px solid var(--border-color); margin: 30px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- TOP NAVIGATION (IN-LINE) ---
header_col1, header_col2 = st.columns([3, 1])

with header_col1:
    st.markdown("""
        <div style="display:flex; align-items:center; gap:12px; padding-top:8px;">
            <span style="font-size:24px;">🧭</span>
            <span style="font-weight:700; font-size:22px; color:var(--text-header);">Noshay Navigations</span>
        </div>
    """, unsafe_allow_html=True)

with header_col2:
    page = st.selectbox(
        "Select Page",
        ["Coaching", "Research & Resources", "My Story & Accomplishments"],
        label_visibility="collapsed"
    )

st.markdown("<hr style='margin-top:0;'>", unsafe_allow_html=True)

# --- PAGE LOGIC ---

if page == "Coaching":
    col_text, col_img = st.columns([2.5, 1])

    with col_text:
        st.markdown('<div class="main-title">Noshay Navigations</div>', unsafe_allow_html=True)
        st.markdown('<div class="tagline">Mapped for Adventure. Built for Life.</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-labels">🏁 Portland-Based Trail & Ultra Specialist | Performance Logistics</div>', unsafe_allow_html=True)

    with col_img:
        st.image("https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=500&q=80", use_container_width=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="pillar-title">🌱 Foundation</div>', unsafe_allow_html=True)
        st.markdown('<div class="pillar-text">Navigating the transition from road to trail or building your first base. We map the terrain and the fun.</div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="pillar-title">🏔️ Elevation</div>', unsafe_allow_html=True)
        st.markdown('<div class="pillar-text">Targeting a PR or a new distance? Performance logistics tailored to level up relative to your individual goals.</div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="pillar-title">🗺️ Exploration</div>', unsafe_allow_html=True)
        st.markdown('<div class="pillar-text">Specialized for the adventures of life. We navigate the tactical shifts needed for long-term health and speed.</div>', unsafe_allow_html=True)

    st.markdown('<div style="color: var(--text-header); font-size: 26px; font-weight: 700; margin-top: 40px; margin-bottom: 15px;">The Strategy of the Stride</div>', unsafe_allow_html=True)
    # st.markdown('<div style="font-size: 15px; line-height: 1.7; color: var(--text-body);">Running doesn’t happen in a vacuum—it happens between meetings, family, and daily commitments. Whether training for your first 5k or a 100-miler, I provide the logistics of performance mapped to your real life. I provide the map so you can focus on the exploration.</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 15px; line-height: 1.7; color: var(--text-body);">Performance is a logistical puzzle. Running doesn’t exist in a vacuum; it happens between meetings, family, and daily commitments. Whether training for your first 5k or a 100-miler, I bridge the gap between your ambitious goals and your day to day life. Using science-backed methodology, I coordinate the performance logistics of your training to align with your reality, so you can focus entirely on the exploration.</div>', unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown('<div style="color: var(--text-header); font-size: 26px; font-weight: 700; margin-bottom: 25px;">Coaching Navigation Package</div>', unsafe_allow_html=True)

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
        
    st.markdown(f"""
            <div class="price-card-container">
                <div style="color: var(--accent-green); font-size: 36px; font-weight: 700;">$100 <span style="font-size:18px; font-weight:400; color: var(--text-body); opacity: 0.7;">/ month</span></div>
                <div style="color: var(--text-body); font-size:14px; margin-top:8px;">Comprehensive Coaching for Every Distance</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown('<div style="color: var(--text-header); font-size: 26px; font-weight: 700; margin-bottom: 20px;">Ready to Plot Your Course?</div>', unsafe_allow_html=True)

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
    st.markdown('<div class="tagline">Coordinates for the starting line and the long haul.</div>', unsafe_allow_html=True)
    
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🏃 Foundational Training")
        st.write("Essential reading for building a resilient engine.")
        st.markdown("""
        * **[80/20 Running Principles](https://www.8020endurance.com/):** The science of slowing down to get faster.
        * **[TrainingPeaks Blog](https://www.trainingpeaks.com/blog/):** Gold-standard basics for aerobic base building.
        * **[Couch to 5K (C25K)](https://www.c25k.com/):** The classic roadmap for the absolute beginner.
        * **[Runners World Strength for Runners](https://www.runnersworld.com/strength-training/):** Foundational injury prevention.
        * **[Strength for Trail Runners](https://www.irunfar.com/):** Pre-hab routines specifically for the eccentric loading of PNW downhills.
        """)

        st.markdown("### 🧪 Advanced Endurance Science")
        st.write("Cutting-edge studies for the long-distance specialist.")
        st.write("Recent research focusing on the 'Logistics of the Engine'.")
        st.markdown("""
        * **[The Fueling Window: Intra-workout timing](https://pubmed.ncbi.nlm.nih.gov/):** Recent studies on 'gut training' suggest consistent 60-90g/hr intake regardless of intensity to prevent late-race failure.
        * **[Intensity vs. Distance (2023 Study)](https://www.frontiersin.org/journals/physiology):** New data on 'Critical Speed' in ultras—how training at higher intensities preserves muscle fiber recruitment during 100-mile efforts.
        * **[Metabolic Efficiency & Fat Oxidation](https://www.metabolismjournal.com/):** Exploring the balance of fat-adaptation without sacrificing high-end glycolytic power.
        * **[Science of Ultra: Fueling Logistics](https://www.scienceofultra.com/podcasts/131):** A deep dive into why your stomach shuts down and how to coordinate a rescue plan.
        * **[GU Energy Lab - Ultra Research](https://guenergy.com/blogs/nutrition-lab):** Specifics on carbohydrate oxidation at hour 10+.
        * **[Science of Ultra - GI Distress Study](https://www.scienceofultra.com/podcasts/131):** Navigating the most common reason for Ultra DNF.
        * **[Journal of Sports Sciences - Pacing](https://www.tandfonline.com/journals/rjsp20):** Recent studies on cognitive fatigue in 100-mile events.
        """)

    with col2:
        st.markdown("### 🗺️ Trail & Navigation Tools")
        st.write("The software you need to plot your course.")
        st.markdown("""
        * **[Strava Global Heatmap](https://www.strava.com/heatmap):** Essential for finding 'hidden' trail connectors in the Gorge or Tillamook.
        * **[AllTrails (Condition Reports)](https://www.alltrails.com/):** Use this specifically for recent 'Trip Reports' to check for snow levels or downed trees.
        * **[Gaia GPS](https://www.gaiagps.com/):** My preferred tool for mapping technical PNW routes where cell service is non-existent.
        * **[CalTopo](https://caltopo.com/):** Technical elevation profile planning for high-vert days.
        """)

        st.markdown("### 🌲 PNW Trails & Communities")
        st.write("Local knowledge for navigating the Portland dirt.")
        st.markdown("""
        * **[Wy'east Wolfpack](https://www.wyeastwolfpack.com/):** A staple community for local group runs and mountain training.
        * **[Portland Trail Series](http://www.portlandtrailseries.com/):** The best way to get 'race-intensity' training on local Forest Park singletrack.
        * **[Forest Park Conservancy](https://forestparkconservancy.org/):** Real-time updates on Wildwood Trail conditions and bridge closures.
        * **[Territory Run Co.](https://territoryrun.co/):** A Portland-based community hub for trail culture and local meetups.
        """)


elif page == "My Story & Accomplishments":
    st.markdown('<div class="main-title">Who am I?</div>', unsafe_allow_html=True)
    
    col_bio, col_stats = st.columns([1.5, 1])
    
    with col_bio:
        st.write("""
        My name is Jaclyn Noshy. I am a Portland-based ultra-endurance athlete and coach who believes that performance 
        is a logistical puzzle. With over a decade of experience on the dirt—ranging from the technical alpine trails of 
        the PNW to the humid, rugged forests of the East Coast—I have learned that training for a 100-miler shouldn't 
        require sacrificing your career or family life.
        
        My own coordinates have shifted over the years: I evolved from a youth soccer player and collegiate triathlete 
        into the novice track and road circuits before finding my home in the ultra-trail community. This journey taught 
        me that while every athlete's path is distinct, the objective is the same: finding the specific strategy that turns 
        a daunting distance into an achievable reality.

        My coaching philosophy is simple: **Your Life is the Terrain. We Map the Training.**
        """)
        # My coaching philosophy is simple: **I provide the map, you provide the engine.**
        st.link_button("View Full UltraSignup Profile", "https://ultrasignup.com/results_participant.aspx?fname=Jaclyn&lname=Noshay")

    with col_stats:
        st.markdown(f"""
            <div class="stat-card">
                <div style="font-size:14px; color: var(--text-body); opacity: 0.8;">UltraSignup Rank</div>
                <div class="stat-val">91.85%</div>
                <div style="font-size:12px; margin-top:10px;">Consistently ranked in the top tier of female ultra-athletes.</div>
            </div>
            <br>
            <div class="stat-card">
                <div style="font-size:14px; color: var(--text-body); opacity: 0.8;">Overall Finish Rate</div>
                <div class="stat-val">100%</div>
                <div style="font-size:12px; margin-top:10px;">Technical efficiency across 100M, 100K, and 50K distances.</div>
            </div>
        """, unsafe_allow_html=True)

    st.divider()

    # --- PERSONAL BESTS SECTION ---
    st.markdown('### ⚡ Personal Bests')
    pr_col1, pr_col2 = st.columns(2)
    
    with pr_col1:
        st.markdown("**Road & Speed**")
        st.markdown("""
        * **5K:** 18:53 (2020)
        * **Half Marathon:** 1:28:36 (Knoxville Half Marathon 2023)
        * **Marathon:** 3:07:11 (Boston Marathon 2024)
        """)

    with pr_col2:
        st.markdown("**Trail & Ultra**")
        st.markdown("""
        * **50K:** 4:20:34 (Chester Woods 2020)
        * **100K:** 10:33:51 (Zion Ultras 2023)
        * **100 Miler:** 17:51:03 (Oregon Cascades 2024)
        """)

    st.markdown("### 🏆 The Field Log")
    st.table([
        {"Year": "2025", "Event": "The Bear 100", "Rank": "5th Female, 27th Overall", "Category": "100 Miler"},
        {"Year": "2025", "Event": "Miwok 100k", "Rank": "4th Female, 30th Overall", "Category": "100K"},
        {"Year": "2024", "Event": "Oregon Cascades 100M", "Rank": "2nd Female, 5th Overall", "Category": "100 Miler"},
        {"Year": "2024", "Event": "Volcanic 50K", "Rank": "2nd Female, 12th Overall", "Category": "50K"},
        {"Year": "2024", "Event": "Siskiyou Out Back 100K", "Rank": "3rd Female, 13th Overall", "Category": "100K"},
        {"Year": "2024", "Event": "Smith Rock Classic 50K", "Rank": "2nd Female, 8th Overall", "Category": "50K"},
        {"Year": "2023", "Event": "Superior Fall Trail Race 100M", "Rank": "2nd Female, 8th Overall", "Category": "100 Miler"},
        {"Year": "2022", "Event": "No Business 100M", "Rank": "1st Female, 6th Overall", "Category": "100 Miler"}
    ])

# --- FOOTER ---
st.markdown(f"""
    <div style="text-align: center; border-top: 1px solid var(--border-color); margin-top: 60px; padding: 30px; font-size: 13px; color: var(--text-header); opacity: 0.8;">
        Noshay Navigations © 2026 &nbsp; | &nbsp; Portland, Oregon &nbsp; | &nbsp; Mapped for Adventure. Built for Life.
    </div>
""", unsafe_allow_html=True)