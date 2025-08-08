import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ashwik Bire | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FONTS, ICONS, GLOBAL ADVANCED CSS ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Montserrat:wght@700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<style>
:root {
    --primary: #1E90FF;
    --bg: #000;
    --sidebar-bg: #0B0C10;
    --tab-radius: 1.1em;
    --tab-shadow: 0 2px 20px #1E90FF22;
}
html, body, [class*="css"] {
    background: var(--bg) !important;
    color: #fff !important;
    font-family: 'Roboto', sans-serif;
}
[data-testid="stSidebar"] {
    background: var(--sidebar-bg) !important;
    color: #fff;
}
.stImage>img {
    border-radius: 14px;
    border: 2px solid var(--primary);
    box-shadow: 0 8px 32px #1E90FF29;
    margin-bottom: 0.7em;
}
h1, h2, h3, h4, h5, h6 {
    font-family: 'Montserrat', sans-serif !important;
    color: var(--primary) !important;
    font-weight: 800 !important;
    letter-spacing: 0.03em;
}
a, .st-dl a {
    color: var(--primary) !important;
    text-decoration: none !important;
    font-weight: 600 !important;
    transition: color 0.2s;
}
a:hover, a:focus {
    color: #22c8e5 !important;
    text-decoration: underline !important;
}
.stButton>button {
    background: linear-gradient(90deg, var(--primary) 60%, #22c8e5 100%);
    border-radius: 11px;
    border: none;
    color: #fff;
    font-weight: 700;
    font-family: 'Montserrat',sans-serif;
    padding: 0.7em 1.4em;
    box-shadow: 0 6px 14px #1E90FF49;
    margin-top: 1.1em;
    margin-bottom: 1em;
    background-size: 200% 100%;
    background-position: right bottom;
    transition: all 0.25s cubic-bezier(.25,.8,.25,1);
}
.stButton>button:hover {
    background-position: left bottom;
    color: #fff;
    box-shadow: 0 1px 22px #1E90FF6c;
}
hr {border: 1px solid #20232a!important;}
/* --- TABS CUSTOM BLACK DESIGN --- */
.stTabs [role="tablist"] {
    background: var(--bg) !important;
    border-radius: var(--tab-radius) var(--tab-radius) 0 0 !important;
    box-shadow: var(--tab-shadow);
    margin-bottom: 1.2rem;
    padding: 0.2em 0.5em 0 0.5em;
    gap: 0.7rem;
    min-height: 3.1em;
}
.stTabs [role="tab"] {
    background: var(--bg) !important;
    color: #bbb !important;
    font-size: 1.11em;
    border-radius: var(--tab-radius) var(--tab-radius) 0 0 !important;
    padding: 0.56em 1.7em 0.56em 1.1em;
    font-family: 'Montserrat', 'Roboto', sans-serif !important;
    font-weight: 700;
    margin-right: 0.2em;
    border: none !important;
    box-shadow: none;
    opacity: 0.68;
    position: relative;
    transition: all 0.27s;
}
.stTabs [role="tab"]:hover:not([aria-selected="true"]) {
    background: #11131b !important;
    color: #fff !important;
    box-shadow: 0 0px 12px #1E90FF33;
    cursor: pointer;
    opacity: 1.0;
    transform: translateY(-3px) scale(1.045);
}
.stTabs [role="tab"][aria-selected="true"] {
    background: linear-gradient(90deg,var(--primary) 75%,#22c8e5 120%)!important;
    color: #fff !important;
    font-size: 1.13em;
    font-weight: 800;
    opacity: 1.0;
    box-shadow: 0 5px 20px #1E90FF55;
    z-index: 2;
    transform: translateY(-1px) scale(1.00);
}
.tab-icon {
    margin-right: 0.7em;
    font-size: 1.17em;
    vertical-align: middle;
    display: inline-block;
    opacity: 0.9;
}
.stTabs [role="tab"][aria-selected="true"] .tab-icon {
    filter: drop-shadow(0 0 6px #0007);
    opacity: 1.0;
}
.stTabs [data-testid="stTabBody"] > div {
    background: var(--bg) !important;
    border-radius: 0 0 var(--tab-radius) var(--tab-radius) !important;
    box-shadow: var(--tab-shadow);
    padding: 2em;
    min-height: 340px;
}
/* Expander */
.stExpanderHeader {
    color: var(--primary) !important;
    font-weight: bold;
    font-family: 'Montserrat',sans-serif;
    letter-spacing:0.02em;
}
/* Anywhere else */
::selection{background:#1e90ff7d;color:#fff;}
</style>
""", unsafe_allow_html=True)



# --- SIDEBAR PROFILE ---
with st.sidebar:
    st.image("passport.jpg", width=160)
    st.markdown("## 📬 Contact")
    st.write("📧 [ashwikbire@gmail.com](mailto:ashwikbire@gmail.com)")
    st.write("📱 8459291488")
    st.markdown("[🌏 LinkedIn](https://www.linkedin.com/in/your-profile)")



# --- MAIN HEADER ---
st.title("Ashwik Bire")

st.markdown(
    "*Business Intelligence Enthusiast | Data Science | Data Analytics | Power BI | TDV | TIBCO Spotfire | Tableau | Python Machine Learning | SQL | Azure Data Engineering | Azure Databricks | PMO*"
)

with st.expander("💡 About Me", expanded=True):
    st.markdown("""
I am a Data Analyst with 2.9+ years' experience, skilled in Power BI and TIBCO Spotfire, with work at Atos Syntel and Birlasoft & FedEx APAC Client.  
Spot Recognition Award from Atos Syntel CEO. Top rank – Amrita Business Innovation Challenge.  
Passionate about nature photography, dance, and creative writing, fueling creativity and detail.
    """)

# --- TABS: ICONS + NAMES ---
ICONS = [
    '<i class="fa-solid fa-graduation-cap tab-icon"></i>',    # Education
    '<i class="fa-solid fa-briefcase tab-icon"></i>',         # Experience
    '<i class="fa-solid fa-microchip tab-icon"></i>',         # Technologies
    '<i class="fa-solid fa-wrench tab-icon"></i>',            # Tools
    '<i class="fa-solid fa-diagram-project tab-icon"></i>',   # Projects
    '<i class="fa-solid fa-certificate tab-icon"></i>',       # Certifications
    '<i class="fa-solid fa-trophy tab-icon"></i>',            # Achievements
    '<i class="fa-solid fa-heart tab-icon"></i>',             # Interests
    '<i class="fa-brands fa-connectdevelop tab-icon"></i>',   # Social Sites
    '<i class="fa-solid fa-envelope tab-icon"></i>'           # Contact
]
NAMES = [
    "Education", "Experience", "Technologies", "Tools", "Projects",
    "Certifications", "Achievements", "Interests", "Social Sites", "Contact"
]
TABS = [ICONS[i] + NAMES[i] for i in range(len(NAMES))]

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(TABS)

# --- TAB 1: EDUCATION ---
with tab1:
    st.subheader("📖 Education")
    st.markdown("""
- **Bachelor of Engineering, Electronics & Telecommunication** | 82.36%  
  _P.R. Pote College of Engineering and Management, Amravati (SGBAU)_ | 2019-2022  
- **Engineering Diploma** | 75%  
  _DR. Panjabrao Deshmukh Polytechnic, Amravati_ | 2016-2019  
- **S.S.C** | 79%  
  _Janta High School Purnanager, Amravati_ | 2015-2016
    """)

# --- TAB 2: EXPERIENCE ---
with tab2:
    st.subheader("🧑‍💼 Experience")
    st.markdown("""
**Atos Syntel** | Aug 2022 – Aug 2023  
_Project: Analytics COE APAC | Client: FedEx APAC | Role: Associate Consultant_  
- Developed airWISE dashboard from inception using TDV and custom visualizations.  
- Managed migrations DEV → QA → PROD.  
- Agile collaboration, daily stand-ups, meetings.  
- Translated data into actionable visualizations.

---

**VDA Infosolutions Pvt Ltd** | Dec 2023 – Present  
_Designation: Data Analyst | Clients: TCS, Birlasoft_  
- Maintained & designed dashboards for incidents, assets, SLA compliance.  
- Data validation & auditing for ticketing.  
- Automated reporting and visualizations.
    """)

# --- TAB 3: TECHNOLOGIES ---
with tab3:
    st.subheader("💻 Technologies")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
- **Python, SQL**
- Numpy, Pandas, Matplotlib, Scikit-Learn, Seaborn, SciPy
        """)
    with col2:
        st.markdown("""
- Azure Data Factory, Azure Databricks
- SAFe Agile
- HTML, CSS, JS, Bootstrap
        """)

# --- TAB 4: TOOLS ---
with tab4:
    st.subheader("🛠️ Tools")
    st.markdown("""
- Power BI Desktop  
- TIBCO Spotfire 11.4x  
- Tableau Public  
- TIBCO Data Virtualization (TDV)
    """)

# --- TAB 5: PROJECTS ---
with tab5:
    st.subheader("📊 Projects")
    st.markdown("""
**Power BI:** Hospital Activity UK Dashboard, Amazon Sales Dashboard  
**Web:** A_Naturography Website, Online Food Ordering System  
**IoT/Academic:** Conference Room Light Controller with Bidirectional Counter  
**Python:** Road Line Detection using OpenCV
    """)

# --- TAB 6: CERTIFICATIONS ---
with tab6:
    st.subheader("🎓 Certifications")
    st.markdown("""
Microsoft Azure Fundamental, Power BI Data Analyst Associate,  
Business Intelligence Foundation Professional, Scrum FPC,  
TIBCO Spotfire Beginner → Advanced, Master Power BI in 21 Days,  
SQL Intermediate, FE Web Dev Ultimate Course 2021, Python Programming B2A
    """)

# --- TAB 7: ACHIEVEMENTS ---
with tab7:
    st.subheader("🏆 Achievements")
    st.markdown("""
- Spot Recognition by CEO Atos Syntel (Sep 2022)  
- State Winner – Amrita Business Innovation Challenge (Jun 2022)  
- Appreciation Award – PRPCEM (May 2022)  
- Coding Round – Techgig Code Gladiators (Aug 2021)  
- 1st Prize – Paper Presentation (Jan 2020)  
- 1st Prize – Solo Dance (Jan 2019)  
- 3rd Prize – Technical Quiz (Jan 2019)  
- 1st Prize – Kavya Vachan (Jan 2017)
    """)

# --- TAB 8: INTERESTS/HOBBIES ---
with tab8:
    st.subheader("🌱 Interests & Hobbies")
    st.markdown("""
- Nature photography  
- Dance  
- Creative writing  
- Continuous learning & skill development
    """)

# --- TAB 9: SOCIAL SITES ---
with tab9:
    st.subheader("🌐 Social Sites")
    st.markdown("""
- [LinkedIn](https://www.linkedin.com/in/your-profile)  
- [HackerRank](https://www.hackerrank.com/)  
- [GitHub](https://github.com/your-profile)  
- [Photography Portfolio](#)  
- Instagram: [A_Naturography](https://www.instagram.com/A_Naturography)  
- Instagram: [Shimmering Lines](https://www.instagram.com/ShimmeringLines)
    """)

# --- TAB 10: CONTACT ---
with tab10:
    st.subheader("📱 Contact")
    st.markdown("""
- Email: [ashwikbire@gmail.com](mailto:ashwikbire@gmail.com)  
- Contact Number: 8459291488
    """)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;color:#888;'>© Ashwik Bire</div>", unsafe_allow_html=True)
