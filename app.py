import streamlit as st
import requests
import os

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

    .pillar-card {
        background-color: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 30px 20px;
        height: 100%;
        transition: transform 0.2s ease, border-color 0.2s ease;
        text-align: center;
    }
    .pillar-card:hover {
        transform: translateY(-5px);
        border-color: var(--accent-green);
    }
    .pillar-icon {
        font-size: 40px;
        margin-bottom: 15px;
        display: block;
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
        # st.image("https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=500&q=80", use_container_width=True)
        st.image("images/landscape.jpg", use_container_width=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # p1, p2, p3 = st.columns(3)
    # with p1:
    #     st.markdown('<div class="pillar-title">🌱 Foundation</div>', unsafe_allow_html=True)
    #     st.markdown('<div class="pillar-text">Navigating the transition from road to trail or building your first base. We map the terrain and the fun.</div>', unsafe_allow_html=True)
    # with p2:
    #     st.markdown('<div class="pillar-title">🏔️ Elevation</div>', unsafe_allow_html=True)
    #     st.markdown('<div class="pillar-text">Targeting a PR or a new distance? Performance logistics tailored to level up relative to your individual goals.</div>', unsafe_allow_html=True)
    # with p3:
    #     st.markdown('<div class="pillar-title">🗺️ Exploration</div>', unsafe_allow_html=True)
    #     st.markdown('<div class="pillar-text">Specialized for the adventures of life. We navigate the tactical shifts needed for long-term health and speed.</div>', unsafe_allow_html=True)

    # --- COACHING PILLARS SECTION ---
    st.markdown('<div style="color: var(--text-header); font-size: 26px; font-weight: 700; margin-top: 20px; margin-bottom: 25px;">Coaching Pillars</div>', unsafe_allow_html=True)
    
    p1, p2, p3 = st.columns(3)
    
    with p1:
        st.markdown(f"""
            <div class="pillar-card">
                <span class="pillar-icon">🌱</span>
                <div class="pillar-title">Foundation</div>
                <div class="pillar-text">
                    Navigating the transition from road to trail or building your first base, we focus on the 
                    <b>bio-logistics</b> of a resilient engine. We build a foundation solid enough to support 
                    your mileage goals while accounting for the energy needed for your day to day life.
                </div>
            </div>
        """, unsafe_allow_html=True)
                    # We map the terrain and the fun, ensuring a resilient engine for the long haul.

    with p2:
        st.markdown(f"""
            <div class="pillar-card">
                <span class="pillar-icon">🏔️</span>
                <div class="pillar-title">Elevation</div>
                <div class="pillar-text">
                    Targeting a PR or a new distance? Looking for accountability? <b>Elevation</b> is the strategic 
                    leap from where you are to the athlete you want to become. We apply analytical rigor to movement 
                    and energy variables to level up performance—<b>however you define it.</b>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with p3:
        st.markdown(f"""
            <div class="pillar-card">
                <span class="pillar-icon">🗺️</span>
                <div class="pillar-title">Exploration</div>
                <div class="pillar-text">
                    Ultra-distance training should be a source of joy, not a second job. We prioritize adventure-led 
                    long runs and tactical shifts that keep the 'why' alive, ensuring you reach the finish line 
                    with a full capacity battery and a genuine love for the process and the dirt.
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('<div style="color: var(--text-header); font-size: 26px; font-weight: 700; margin-top: 40px; margin-bottom: 15px;">The Strategy of the Stride</div>', unsafe_allow_html=True)
    # st.markdown('<div style="font-size: 15px; line-height: 1.7; color: var(--text-body);">Running doesn’t happen in a vacuum—it happens between meetings, family, and daily commitments. Whether training for your first 5k or a 100-miler, I provide the logistics of performance mapped to your real life. I provide the map so you can focus on the exploration.</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 15px; line-height: 1.7; color: var(--text-body);">Performance is a logistical puzzle. Running doesn’t exist in a vacuum; it happens between meetings, family, and daily commitments. Whether training for your first 5k or a 100-miler, I bridge the gap between your ambitious goals and your day to day life. Using science-backed methodology, I coordinate the performance logistics of your training to align with your reality, so you can focus entirely on the exploration.</div>', unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown('<div style="color: var(--text-header); font-size: 26px; font-weight: 700; margin-bottom: 25px;">Coaching Navigation Package</div>', unsafe_allow_html=True)

    pkg_col1, pkg_col2 = st.columns([1, 1.2])

    with pkg_col1:
        st.markdown("#### What's Included:")
        st.write("✅ **Personalized Look-Ahead:** A long-term vision of your season goals.")
        st.write("✅ **Week-to-Week Planning:** Dynamic schedules that adapt to your real life.")
        st.write("✅ **COROS Training Hub:** Full utilization of technical metrics.")

    with pkg_col2:
        st.markdown("#### Communication:")
        st.write("📞 **Monthly Phone Call:** Deep dive into strategy and progress.")
        st.write("💬 **Ad Hoc Text Support:** Quick questions? On-the-fly adjustments? I'm a text away.")
        st.write("🏃 **Expert Guidance:** Specialized trail, ultra, and exploration advice.")
        
    st.markdown(f"""
            <div class="price-card-container">
                <div style="color: var(--accent-green); font-size: 36px; font-weight: 700;">$100 <span style="font-size:18px; font-weight:400; color: var(--text-body); opacity: 0.7;">/ month</span></div>
                <div style="color: var(--text-body); font-size:14px; margin-top:8px;">Comprehensive Coaching for Every Distance</div>
                <div style="color: var(--text-body); font-size:10px; margin-top:8px;">*Financial capacity shouldn't be a barrier to quality coaching. I am open to sliding scale discussions based on your needs and the type of support we design together.</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # --- INTAKE FORM SECTION ---
    st.markdown('<div style="color: var(--text-header); font-size: 26px; font-weight: 700; margin-bottom: 20px;">Ready to Plot Your Course?</div>', unsafe_allow_html=True)
    st.write("Ready to Plot Your Course? Submit the intake form below. Once received, I will reach out to schedule a 30-minute connection to review your logistics and verify the fit before we begin mapping your training.", unsafe_allow_html=True)

    # --- CONFIGURATION ---
    # Use Streamlit Secrets for these in production
    EMAIL = st.secrets["EMAIL"]
    PASSWORD = st.secrets["PASSWORD"]
    def send_professional_email(name, email, goal, message):
        try:
            # Create the email container
            msg = MIMEMultipart()
            msg['From'] = EMAIL
            msg['To'] = EMAIL
            msg['Subject'] = f"Noshay Navigations Inquiry: {name}"

            # Email Body
            body = f"""
            New Inquiry from Noshay Navigations:
            
            Name: {name}
            Email: {email}
            Goal: {goal}
            
            Logistics & Schedule:
            {message}
            """
            msg.attach(MIMEText(body, 'plain'))

            # Connect to Gmail's server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls() # Secure the connection
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)
            server.quit()
            return True
        except Exception as e:
            st.error(f"Error: {e}")
            return False

    # --- THE FORM ---
    with st.form("intake_form", clear_on_submit=True):
        col_name, col_email = st.columns(2)
        with col_name:
            name = st.text_input("Name", placeholder="Your Name")
        with col_email:
            email = st.text_input("Email", placeholder="Your Email Address")
        
        goal = st.text_input("Training Goal / Target Race / Milestone", placeholder="e.g., Running Consistency or Mountain Lakes 100M or First 10K")
        msg = st.text_area("Logistics & Schedule", placeholder="Tell me about your current weekly mileage and commitments...")
        
        submit_button = st.form_submit_button("Request Consultation")

        if submit_button:
            if name and email:
                with st.spinner("Sending intake form..."):
                    if send_professional_email(name, email, goal, msg):
                        st.success("✅ Logistics received. I'll reach out to start your mapping shortly!")
                        st.balloons()
            else:
                st.warning("Error sending request. Please fill in all fields or check your connection and try again.")

    # with st.form("intake_form", clear_on_submit=True):
    #     col_name, col_email = st.columns(2)
    #     with col_name:
    #         name = st.text_input("Name", placeholder="Your Name")
    #     with col_email:
    #         email = st.text_input("Email", placeholder="Your Email Address")
        
    #     goal = st.text_input("Training Goal / Target Race / Milestone", placeholder="e.g., Running Consistency or Oregon Cascades 100M or First 10K")
    #     msg = st.text_area("Logistics & Schedule", placeholder="Tell me about your current weekly mileage and commitments...")
        
    #     submit_button = st.form_submit_button("Request Consultation")

    #     if submit_button:
    #         if name and email:
    #             # FormSubmit AJAX Endpoint
    #             CONTACT_EMAIL = "jmnosh@gmail.com"
    #             url = f"https://formsubmit.co/ajax/{CONTACT_EMAIL}"
                
    #             payload = {
    #                 "Name": name,
    #                 "Email": email,
    #                 "Goal": goal,
    #                 "Message": msg,
    #                 "_subject": f"New Noshay Navigations Lead: {name}",
    #                 "_captcha": "false"  # Optional: Disable captcha for cleaner AJAX experience
    #             }
                
    #             try:
    #                 # Using a timeout to ensure the app doesn't hang
    #                 response = requests.post(url, json=payload, timeout=10)
                    
    #                 if response.status_code == 200:
            #             st.success("✅ Logistics received. I'll reach out to start your mapping shortly!")
            #             st.balloons()
            #         else:
            #             st.error("Error sending request. Please check your connection and try again.")
            #     except Exception as e:
            #         # st.error("Connection error. Please verify your internet and try again.")
            #         st.error(f"Error {response.status_code}: {response.text}")
            # else:
            #     st.warning("Please provide both your name and email to initiate the briefing.")

elif page == "Research & Resources":

    st.markdown('<div class="main-title">Resource Library</div>', unsafe_allow_html=True)
    st.markdown('<div class="tagline">Coordinates for the starting line and the long haul.</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size: 18px; color: var(--text-body); margin-bottom: 25px; line-height: 1.6;">
        This is just a <b>small taste</b> of the many public resources available out there — from training tools to local 
        groups — to help kick off your training from research to community
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### 🏃 Foundational Training")
    st.write("Essential reading for building a resilient engine.")
    st.markdown("""
    * **[80/20 Running Principles](https://www.8020endurance.com/):** The science of slowing down to get faster.
    * **[TrainingPeaks Blog](https://www.trainingpeaks.com/blog/):** Gold-standard basics for aerobic base building.
    * **[Couch to 5K (C25K)](https://www.c25k.com/):** The classic roadmap for the absolute beginner.
    * **[Runners World Strength for Runners](https://www.runnersworld.com/strength-training/):** Foundational injury prevention.
    """)

    st.markdown("### 🌲 PNW Trails & Communities")
    st.write("Local knowledge for navigating the Portland dirt.")
    st.markdown("""
    * **[Wy'east Wolfpack](https://www.wyeastwolfpack.com/):** A staple community for local group runs and mountain training.
    * **[Portland Trail Series](http://www.portlandtrailseries.com/):** The best way to get 'race-intensity' training on local Forest Park singletrack.
    * **[Forest Park Conservancy](https://forestparkconservancy.org/):** Real-time updates on Wildwood Trail conditions and bridge closures.
    * **[Territory Run Co.](https://territoryrun.co/):** A Portland-based community hub for trail culture and local meetups.
    """)

    st.markdown("### 🗺️ Trail & Navigation Tools")
    st.write("The software you need to plot your course.")
    st.markdown("""
    * **[Strava Global Heatmap](https://www.strava.com/heatmap):** Essential for finding common running trails from city roads to backcountry trails.
    * **[AllTrails (Condition Reports)](https://www.alltrails.com/):** Use this specifically for recent 'Trip Reports' to check for snow levels or downed trees.
    * **[Gaia GPS](https://www.gaiagps.com/):** Tool for mapping technical PNW routes where cell service is non-existent.
    * **[Coros Training Hub](https://training.coros.com/)** – A powerful public platform for analyzing your workout data, tracking load, and managing your "infrastructure" over time.
    """)

    st.divider()

    st.markdown("### 🧪 Advanced Endurance Science")
    st.write("Cutting-edge research for the long-distance specialist.")

    # -------------------------
    st.markdown("#### 🔥 Fueling, Metabolism & GI Function")
    st.markdown("""
    * **[The Fueling Window: Intra-workout Timing](https://pubmed.ncbi.nlm.nih.gov/):** Research on gut training and consistent 60–90 g/hr intake to prevent late-race failure.
    * **[GU Energy Lab – Ultra Research](https://guenergy.com/blogs/nutrition-lab):** Carbohydrate oxidation and fueling efficiency at hour 10+.
    * **[Metabolic Efficiency & Fat Oxidation](https://www.metabolismjournal.com/):** Balancing fat adaptation without sacrificing high-end glycolytic power.
    """)

    # -------------------------
    st.markdown("#### 🏃 Training Structure, Load & Adaptation")
    st.markdown("""
    * **[Training Load & Endurance Adaptation](https://pubmed.ncbi.nlm.nih.gov/40623829/):** How cumulative stress drives (or limits) performance.
    * **[Elite Endurance Training Characteristics](https://www.trailrunnermag.com/training/trail-tips-training/the-science-behind-how-elite-runners-train/):** What elite runners actually do, not just what theory suggests.
    * **[Monitoring Training Load & Fatigue](https://onlinelibrary.wiley.com/doi/full/10.1111/sms.70208):** Practical frameworks for managing long-term consistency.
    * **[Muscular Endurance for Ultrarunners](https://trainright.com/muscular-endurance-ultrarunners-high-rep-strength-training/):** High-rep strength training and durability.
    """)

    # -------------------------
    st.markdown("#### 🧠 Physiology, Fatigue & Performance Limits")
    st.markdown("""
    * **[Physiological Stress After Ultramarathons](https://www.mdpi.com/2075-1729/13/10/1946):** What actually happens to the body post-race.
    * **[Critical Speed & Ultra Performance](https://www.frontiersin.org/journals/physiology):** How intensity work preserves muscle fiber recruitment deep into long races.
    * **[Physiological, Perceptual & Performance Limits](https://journals.lww.com/acsm-msse/fulltext/2022/05000/physiological,_perceptual,_and_performance.16.aspx):** Central vs peripheral fatigue in endurance events.
    """)

    # -------------------------
    st.markdown("#### 🧬 Sex, Age & Individual Differences")
    st.markdown("""
    * **[Female Physiology in Endurance Running](https://www.irunfar.com/women-rule-female-physiology-in-endurance-running):** Key considerations often overlooked in training design.
    * **[Sex Differences in Endurance Performance](https://www.mdpi.com/2411-5142/10/4/482):** Physiological distinctions with real-world implications.
    * **[Age & Endurance Performance Trends](https://pmc.ncbi.nlm.nih.gov/articles/PMC5992463/):** Longevity, peak performance, and aging in endurance sport.
    """)

    # -------------------------
    st.markdown("#### ⏱️ Tapering, Peaking & Recovery")
    st.markdown("""
    * **[Evidence-Based Tapering Models](https://pmc.ncbi.nlm.nih.gov/articles/PMC10171681/):** Systematic review of taper strategies.
    * **[How to Taper for Long Races](https://www.trailrunnermag.com/training/trail-tips-training/how-to-taper-for-long-races/):** Practical application for trail and ultra athletes.
    * **[Preventing the Taper Tantrum](https://trainright.com/tapering-ultrarunning-prevent-taper-tantrum/):** Managing fitness, fatigue, and athlete psychology.
    """)

# * **[Endurance Training Intensity Distribution](https://link.springer.com/article/10.1186/s40798-022-00438-7):** Polarized vs threshold-heavy approaches.
# * **[Science of Ultra – Fueling Logistics](https://www.scienceofultra.com/podcasts/131):** Why stomach shutdown happens and how to plan a rescue strategy.
# * **[Science of Ultra – GI Distress Study](https://www.scienceofultra.com/podcasts/131):** The most common cause of ultra DNFs and how to mitigate it.
# * **[Cognitive Fatigue & Pacing](https://www.tandfonline.com/journals/rjsp20):** Decision-making and mental load during 100-mile races.
# * **[Psychological Predictors of Ultra Success](https://www.amhsr.org/articles/the-psychological-indicators-of-success-in-ultrarunninga-review-of-the-current-psychological-predictors-in-ultrarunning-12405.html):** Mental traits correlated with ultrarunning performance.

# st.markdown("""
# * **[The Fueling Window: Intra-workout timing](https://pubmed.ncbi.nlm.nih.gov/):** Recent studies on 'gut training' suggest consistent 60-90g/hr intake regardless of intensity to prevent late-race failure.
# * **[Intensity vs. Distance (2023 Study)](https://www.frontiersin.org/journals/physiology):** New data on 'Critical Speed' in ultras—how training at higher intensities preserves muscle fiber recruitment during 100-mile efforts.
# * **[Metabolic Efficiency & Fat Oxidation](https://www.metabolismjournal.com/):** Exploring the balance of fat-adaptation without sacrificing high-end glycolytic power.
# * **[Science of Ultra: Fueling Logistics](https://www.scienceofultra.com/podcasts/131):** A deep dive into why your stomach shuts down and how to coordinate a rescue plan.
# * **[GU Energy Lab - Ultra Research](https://guenergy.com/blogs/nutrition-lab):** Specifics on carbohydrate oxidation at hour 10+.
# * **[Science of Ultra - GI Distress Study](https://www.scienceofultra.com/podcasts/131):** Navigating the most common reason for Ultra DNF.
# * **[Journal of Sports Sciences - Pacing](https://www.tandfonline.com/journals/rjsp20):** Recent studies on cognitive fatigue in 100-mile events.
# """)

## Tapering
# https://trainright.com/tapering-ultrarunning-prevent-taper-tantrum/
# https://www.trailrunnermag.com/training/trail-tips-training/how-to-taper-for-long-races/
# https://www.strongerbyscience.com/tapering/
# https://pmc.ncbi.nlm.nih.gov/articles/PMC10171681/#sec012
# https://www.aspireadventurerunning.com/tapering-period-the-hardest-part-spring-training-community/ 
# http://article.sapub.org/10.5923.j.sports.20180801.02.html

## Training
# https://pubmed.ncbi.nlm.nih.gov/40623829/
# https://trainright.com/muscular-endurance-ultrarunners-high-rep-strength-training/
# https://www.mdpi.com/2075-4663/13/11/385
# https://www.trailrunnermag.com/training/trail-tips-training/the-science-behind-how-elite-runners-train/
        # https://link.springer.com/article/10.1186/s40798-022-00438-7
# https://pubmed.ncbi.nlm.nih.gov/32064575/
# https://journals.lww.com/acsm-msse/fulltext/2022/05000/physiological,_perceptual,_and_performance.16.aspx
# https://onlinelibrary.wiley.com/doi/full/10.1111/sms.70208
# https://www.mdpi.com/1424-8220/25/2/533
# https://pubmed.ncbi.nlm.nih.gov/41334713/

## Physiology and Nutrition
# https://pubmed.ncbi.nlm.nih.gov/40239961/
# https://www.mdpi.com/2411-5142/10/4/482
# https://www.irunfar.com/women-rule-female-physiology-in-endurance-running
# https://www.amhsr.org/articles/the-psychological-indicators-of-success-in-ultrarunninga-review-of-the-current-psychological-predictors-in-ultrarunning-12405.html#:~:text=Ultrarunning%20is%20a%20rapidly%20growing%20field%2C%20warranting,on%20traits%20correlated%20with%20success%20in%20ultramarathons.
# https://www.mdpi.com/2075-1729/13/10/1946#:~:text=In%20contrast%2C%20performance%20tests%20used,12%20weeks%20after%20an%20ultramarathon.
# https://pmc.ncbi.nlm.nih.gov/articles/PMC6315825/#:~:text=The%20long%20duration%20of%20an,~3700%20kcal%20%5B17%5D.
# https://pmc.ncbi.nlm.nih.gov/articles/PMC5992463/#:~:text=The%20average%20age%20at%20the,Doppelmayr%20and%20Molkenthin%2C%202004).


elif page == "My Story & Accomplishments":
    st.markdown('<div class="main-title">Who am I?</div>', unsafe_allow_html=True)
    
    col_bio, col_image = st.columns([1.6, 1])
    
    with col_bio:
        st.markdown(f"""
        <div style="font-size: 16px; line-height: 1.7; color: var(--text-body); text-align: justify;">
            <p>
                My name is <b>Jaclyn Noshay</b>. I am a Portland-based ultra-endurance athlete and a 
                <b>Genetics PhD</b> working in Agricultural R&D. My professional life is spent solving 
                age-old biological puzzles—using data and strategy to rethink how we grow and sustain life. 
                I am fascinated by novel approaches to complex systems, whether that’s inside a DNA 
                sequence or out on a single-track trail.
            </p>
            <p>
                My own athletic coordinates have shifted over a decade of experience—evolving from 
                a youth soccer player and collegiate triathlete into the novice track and road 
                circuits before finding my home in the ultra-trail community. This journey taught 
                me that while every athlete's path is distinct, the objective is always the same: 
                finding the specific strategy that turns a daunting distance into an achievable reality.
            </p>
            <p>
                Two years ago, my husband and I moved to Portland to shorten the gap between our 
                front door and the mountains. We wanted to stop "fitting in" the outdoors and start 
                integrating it. But even with the trails closer, the juggle didn't get easier—it 
                just got more intentional.
            </p>
            <p>
                <b>The real talk is this:</b> I am not a professional athlete, and if you’re reading this, 
                you likely aren't either. I don’t have a six-hour recovery window or a support crew 
                tracking my every move. I am the scientist, usually behind a computer managing 
                the logistics of R&D while navigating the same crowded 24-hour clock that you are. 
                I have a career to maintain, a family to be present for, and a calendar that doesn't 
                care about my mileage goals.
            </p>
            <p>
                In the ultra-running world, the "grind" is often glorified at the expense of everything 
                else. But I’ve learned that a training plan is destined to fail if it requires you to blow 
                up your professional integrity or ignore the people you love. A plan that doesn’t 
                account for the Tuesday where you’re mentally drained from a data-heavy day, a friend’s 
                wedding weekend, or a Saturday spent on the sidelines of soccer games is <b>unsustainable</b>.
            </p>
            <p>
                I am obsessed with the piece of the sport we don't talk about enough: 
                <b>The Bio-Logistics of the Whole Person.</b> Performance isn't just about what 
                your legs can do; it’s about how your training interacts with your stress levels, 
                your sleep, and your "capacity battery."
            </p>
            <p>
                Using the same analytical rigor I apply to genetics, I help athletes map their 
                training to the actual terrain of their lives. We don't just look at heart rate zones; 
                we look at your calendar. We don't just count miles; we count the cost of the juggle.
            </p>
            <p style="font-size: 18px; color: var(--text-header); font-weight: 700; margin-top: 25px;">
                Your Life is the Terrain. We Map the Training.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_image:
        st.image("images/nobusiness.jpg", caption="No Business - First 100 mile race!", use_container_width=False)
        

    # st.divider()
    
    # --- COACHING EXPERIENCE ---
    # st.markdown('### Coaching Experience')
    # Emily, Lance, Steffi ...


    st.divider()
    
    # --- PERSONAL BESTS SECTION ---
    st.markdown("### 🏆 The Field Log")

    col_stats1, col_stats2 = st.columns(2)
    with col_stats1:
        st.markdown(f"""
            <div class="stat-card">
                <div style="font-size:14px; color: var(--text-body); opacity: 0.8;">UltraSignup Rank</div>
                <div class="stat-val">91.85%</div>
                <div style="font-size:12px; margin-top:10px;">Consistently ranked in the top tier of female ultra-athletes.</div>
            </div>
        """, unsafe_allow_html=True)
    with col_stats2:
        st.markdown(f"""
            <div class="stat-card">
                <div style="font-size:14px; color: var(--text-body); opacity: 0.8;">Overall Finish Rate</div>
                <div class="stat-val">100%</div>
                <div style="font-size:12px; margin-top:10px;">Technical efficiency across 100M, 100K, and 50K distances.</div>
            </div>
        """, unsafe_allow_html=True)

    st.divider()

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

    st.write("") # Spacer
    st.link_button("View Full UltraSignup Profile", "https://ultrasignup.com/results_participant.aspx?fname=Jaclyn&lname=Noshay")
    st.write("") # Spacer

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

# --- FOOTER ---
st.markdown(f"""
    <div style="text-align: center; border-top: 1px solid var(--border-color); margin-top: 60px; padding: 30px; font-size: 13px; color: var(--text-header); opacity: 0.8;">
        Noshay Navigations © 2026 &nbsp; | &nbsp; Portland, Oregon &nbsp; | &nbsp; Mapped for Adventure. Built for Life.
    </div>
""", unsafe_allow_html=True)