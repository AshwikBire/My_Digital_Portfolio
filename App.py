import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ashwik Bire | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# FONT, ICONS & ADVANCED CSS
# ---------------------------------------------------------
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Montserrat:wght@600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" crossorigin="anonymous" />
<style>
:root {
    --primary: #1E90FF;
    --bg: #000;
    --secondary-bg: #111;
    --tab-radius: 0.8em;
    --tab-shadow: 0 2px 20px #1E90FF22;
}
html, body, [class*="css"] {
    background-color: var(--bg) !important;
    color: #fff !important;
    font-family: 'Roboto', sans-serif;
}
h1, h2, h3, h4, h5, h6 {
    font-family: 'Montserrat', sans-serif;
    color: var(--primary);
    font-weight: 700;
}
/* SIDEBAR */
[data-testid="stSidebar"] {
    background-color: var(--secondary-bg) !important;
}
.stImage>img {
    border-radius: 16px;
    border: 2px solid var(--primary);
    box-shadow: 0 4px 20px var(--tab-shadow);
}
/* LINKS */
a { color: var(--primary); text-decoration: none; font-weight: 600; }
a:hover { color: #22c8e5; text-decoration: underline; }
/* BUTTONS */
.stButton>button {
    background: linear-gradient(90deg, var(--primary) 60%, #22c8e5 100%);
    border-radius: 12px;
    border: none;
    color: #fff;
    font-weight: 700;
    padding: 0.7em 1.5em;
    box-shadow: 0 4px 12px var(--tab-shadow);
    background-size: 200% 100%;
    background-position: right bottom;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background-position: left bottom;
}
/* TABS - BAR */
.stTabs [role="tablist"] {
    background: var(--bg) !important;
    border-radius: var(--tab-radius) var(--tab-radius) 0 0 !important;
    box-shadow: var(--tab-shadow);
    margin-bottom: 1rem;
    padding: 0.3em 0.5em;
    gap: 0.6rem;
    min-height: 3.2em;
}
/* INDIVIDUAL TABS */
.stTabs [role="tab"] {
    background: var(--bg) !important;
    color: #bbb !important;
    font-size: 1.15em;
    border-radius: var(--tab-radius) var(--tab-radius) 0 0 !important;
    padding: 0.6em 1.8em 0.6em 1.2em;
    font-family: 'Montserrat', 'Roboto', sans-serif !important;
    font-weight: 600;
    transition: all 0.3s ease;
}
.stTabs [role="tab"]:hover:not([aria-selected="true"]) {
    background: #191D21 !important;
    color: #fff !important;
    box-shadow: 0 0px 12px #1E90FF33;
    transform: translateY(-2px) scale(1.04);
}
.stTabs [role="tab"][aria-selected="true"] {
    background: var(--primary) !important;
    color: #fff !important;
    font-size: 1.16em;
    box-shadow: 0 4px 20px #1E90FF44;
}
/* TAB ICONS */
.tab-icon {
    margin-right: 0.5em;
    font-size: 1.2em;
    vertical-align: middle;
}
.stTabs [data-testid="stTabBody"] > div {
    background: var(--bg) !important;
    border-radius: 0 0 var(--tab-radius) var(--tab-radius) !important;
    box-shadow: var(--tab-shadow);
    padding: 2em;
}
hr {border:1px solid #333;}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    st.image("passport.jpg", width=170)
    st.markdown("## 📬 Contact")
    st.write("📧 [ashwikbire@gmail.com](mailto:ashwikbire@gmail.com)")
    st.write("📱 8459291488")
    st.markdown("[🌏 LinkedIn](https://www.linkedin.com/in/your-profile)")

# ---------------------------------------------------------
# MAIN - HEADER
# ---------------------------------------------------------
st.title("Ashwik Bire")
st.markdown(
    "*Business Intelligence Enthusiast | Data Science | Data Analytics | Power BI | TDV | TIBCO Spotfire | Tableau | Python Machine Learning | SQL | Azure Data Engineering | Azure Databricks | PMO*")

with st.expander("💡 About Me", expanded=True):
    st.markdown("""
I am a Data Analyst with over 2.9 years of experience, skilled in Power BI and TIBCO Spotfire, with work at Atos Syntel and Birlasoft & FedEx APAC Client.  
Recognized by the CEO of Atos Syntel with a Spot Recognition Award; top rank in the Amrita Business Innovation Challenge.  
Passionate about nature photography, dance, creative writing, with a goal to deliver valuable insights and excellent results.
""")

# ---------------------------------------------------------
# TAB ICONS & TITLES
# ---------------------------------------------------------
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
TABS_TITLES = [ICONS[i] + NAMES[i] for i in range(len(NAMES))]

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(TABS_TITLES)

# ---------------------------------------------------------
# TAB CONTENTS
# ---------------------------------------------------------
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

with tab2:
    st.subheader("🧑‍💼 Experience")
    st.markdown("""
**Atos Syntel** | Aug 2022 – Aug 2023  
_Project: Analytics COE APAC | Client: FedEx APAC | Role: Associate Consultant_  
- Developed airWISE dashboard from inception using TDV and custom visualizations.  
- Managed migrations DEV → QA → PROD.  
- Agile collaboration, daily stand-ups, meetings.  
- Translated data into actionable visualizations.

**VDA Infosolutions Pvt Ltd** | Dec 2023 – Present  
_Designation: Data Analyst | Clients: TCS, Birlasoft_  
- Maintained & designed dashboards for incidents, assets, SLA compliance.  
- Data validation & auditing for ticketing.  
- Automated reporting and visualizations.
    """)

with tab3:
    st.subheader("💻 Technologies")
    st.markdown("""
- Python, SQL  
- NumPy, Pandas, Matplotlib, Scikit-Learn, Seaborn, SciPy  
- Azure Data Factory, Azure Databricks  
- SAFe Agile  
- HTML, CSS, JS, Bootstrap
    """)

with tab4:
    st.subheader("🛠️ Tools")
    st.markdown("""
- Power BI Desktop  
- TIBCO Spotfire 11.4x  
- Tableau Public  
- TIBCO Data Virtualization (TDV)
    """)

with tab5:
    st.subheader("📊 Projects")
    st.markdown("""
**Power BI:** Hospital Activity UK Dashboard, Amazon Sales Dashboard  
**Web:** A_Naturography Website, Online Food Ordering System  
**IoT/Academic:** Conference Room Light Controller with Bidirectional Counter  
**Python:** Road Line Detection using OpenCV
    """)

with tab6:
    st.subheader("🎓 Certifications")
    st.markdown("""
Microsoft Azure Fundamental, Power BI Data Analyst Associate,  
Business Intelligence Foundation Professional, Scrum FPC,  
TIBCO Spotfire Beginner → Advanced, Master Power BI in 21 Days,  
SQL Intermediate, FE Web Dev Ultimate Course 2021, Python Programming B2A
    """)

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

with tab8:
    st.subheader("🌱 Interests & Hobbies")
    st.markdown("""
- Nature photography  
- Dance  
- Creative writing  
- Continuous learning & skill development
    """)

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

with tab10:
    st.subheader("📱 Contact")
    st.markdown("""
- Email: [ashwikbire@gmail.com](mailto:ashwikbire@gmail.com)  
- Contact Number: 8459291488
    """)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;color:#888;'>© Ashwik Bire</div>", unsafe_allow_html=True)
