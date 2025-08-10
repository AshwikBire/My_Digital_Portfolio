import streamlit as st

st.set_page_config(
    page_title="Ashwik Bire | Portfolio",
    page_icon="📊",
    layout="wide"
)

# -- CUSTOM CSS STYLING --
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Montserrat:wght@700&display=swap" rel="stylesheet">
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

# -- SIDEBAR PROFILE --
with st.sidebar:
    st.image("passport.jpg", width=160)
    st.markdown("## 📬 Contact")
    st.write("📧 [ashwikbire@gmail.com](mailto:ashwikbire@gmail.com)")
    st.write("📱 8459291488")
    st.markdown("[🌏 LinkedIn](https://www.linkedin.com/in/your-profile)")

# -- MAIN HEADER --
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

# -- TABS: EMOJI ICONS + NAMES --
tab_titles = [
    "🎓 Education",
    "💼 Experience",
    "💻 Technologies",
    "🛠️ Tools",
    "📊 Projects",
    "🎓 Certifications",
    "🏆 Achievements",
    "💚 Interests",
    "🌐 Social Sites",
    "📱 Contact"
]
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(tab_titles)

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
**Atos Syntel** — *Associate Consultant*  
Aug 2022 – Aug 2023 | Project: Analytics COE APAC | Client: FedEx APAC  
Technologies & Tools: TIBCO Spotfire 11x, TIBCO Data Virtualization (TDV), Power BI, SQL, Data Warehouse

- Designed, developed, and deployed the *airWISE* dashboard from scratch using TDV and advanced Spotfire visualizations to monitor APAC regional performance metrics.
- Managed seamless dashboard migrations across DEV → QA → PROD environments, ensuring zero downtime and consistent data accuracy.
- Collaborated in a SAFe Agile environment with daily stand-ups, sprint planning, and retrospectives to deliver analytics solutions on time.
- Translated complex business requirements into clear technical designs and actionable data insights, enabling faster decision-making for APAC business leads.
- Improved dashboard loading times by optimizing SQL queries and implementing data caching, reducing report load time by approximately 35%.
- Conducted rigorous data validation to ensure data integrity across FedEx APAC analytics reports.

---

**VDA Infosolutions Pvt Ltd** — *Data Analyst*  
Dec 2023 – Present | Clients: Tata Consultancy Services (TCS), Birlasoft Pvt Ltd  
Technologies & Tools: Power BI Desktop, SQL Server, MS Excel, DAX, SharePoint

- Developed and maintained interactive Power BI dashboards for incident management, issue tracking, and SLA compliance monitoring, enhancing visibility for IT governance teams.
- Designed optimized asset management dashboards for TIO to track IT asset lifecycles, usage, and compliance effectively.
- Performed comprehensive ticketing data audits ensuring accuracy and compliance.
- Automated recurring reports and visualizations using DAX measures and scheduled Power BI refreshes, reducing manual reporting efforts by 40%.
- Implemented real-time KPI tracking visuals for SLA compliance, enabling proactive breach detection.
- Collaborated cross-functionally with stakeholders to refine data requirements and improve reporting accuracy.

""")


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

    # --- STREAMLIT & WEB APPS ---
    st.markdown("### 🌐 Streamlit Apps / Dashboards")
    st.markdown("""
- [Learn2BI – Interactive BI Learning Platform](https://learn2bi-85twalgwbjgchgz57dxdta.streamlit.app/)
- [Stock Market Dashboard](https://ashwik-s-stock-market-dashboard-5qpd6ccjaw9hs6vs8dpfsn.streamlit.app/)
- [Jarvis AI Assistant](https://jarvis-ai-assistant-acihfrbdbxuxdx4jmaship.streamlit.app/)
- [My Learning App](https://my-learning-app-w7dos3mgvuuyrvkzgdzaph.streamlit.app/)
- [Engineering Calculator](https://engineeringcalculator-fafmivvbvwvsw4jckqxjkl.streamlit.app/)
- [My Digital Portfolio](https://mydigitalportfolio-clraahzxkszmlpjqjdpuxt.streamlit.app/)
- [Object Recognition App](https://object-recognition-vxwcn8cdwvh9htsvhuq4s4.streamlit.app/)
    """)

    st.markdown("### 📊 Power BI Dashboards")
    st.markdown("""
- **Hospital Activity UK Dashboard** – Power BI  
- **Amazon Sales Dashboard** – Power BI
    """)

    # --- WEB PROJECTS ---
    st.markdown("### 💻 Web Development Projects")
    st.markdown("""
- [A_Naturography Website](https://ashwikbire.github.io/Resume.github.io/)
    """)

    # --- IOT / ACADEMIC ---
    st.markdown("### 📡 IoT / Academic Project")
    st.markdown("""
- Conference Room Light Controller with Bidirectional Visitor Counter
    """)

    # --- PYTHON ---
    st.markdown("### 🐍 Python Project")
    st.markdown("""
- Road Line Detection using OpenCV
    """)


with tab6:
    st.subheader("🎓 Certifications")
    st.markdown("""
- [Microsoft Azure Fundamental](https://learn.microsoft.com/en-us/users/ashwikbire-7557/credentials/7de31893d146bf69)
- [Microsoft Certified Power BI Data Analyst Associate](https://learn.microsoft.com/en-us/users/ashwikbire-7557/credentials/b4324bff2a4c2081)
- [Business Intelligence Foundation Professional Certificate](https://www.credly.com/badges/cbaf47fb-ac03-497d-8c73-12aa1c545e2c/public_url)
- [Scrum Foundational Professional Certificate](https://www.credly.com/badges/79aea45b-709c-4419-814b-930c88d25f92/linked_in_p)
- [TIBCO Spotfire Development from Beginner to Advance](https://ude.my/UC-196a08f2-2e26-4c46-a11a-791877109bfc)
- [Master Microsoft Power BI in 21 Days](https://ude.my/UC-67d2eb25-91e580-821-22110650542)
- [SQL Intermediate](https://www.hackerrank.com/certificates/79ec222704f3)
- [Front End Web Development Ultimate Course 2021](http://ude.my/UC-3bacc955-2f7b-4e2e-9340-a6cc4f4121a4)
- [Python Programming - From Basics to Advanced level](https://www.udemy.com/certificate/UC-21d316ab-2820-482a-9abb-be3c7c9e0c3d/)
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
    st.subheader("💚 Interests & Hobbies")
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
