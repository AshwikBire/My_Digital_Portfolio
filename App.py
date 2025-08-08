import streamlit as st

# ---------  PAGE CONFIG ---------- #
st.set_page_config(
    page_title="Ashwik Bire | Portfolio",
    page_icon="📊",
    layout="wide"
)

# ---------  CUSTOM ADVANCED CSS  ---------- #
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        background-color: #000000 !important;
        color: #FFFFFF !important;
        font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif !important;
    }
    h1, h2, h3, h4, h5, h6, .st-emotion-cache-1v0mbdj, .st-emotion-cache-z5fcl4 {
        color: #1E90FF;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-shadow: 1px 1px 6px #2228;
    }
    .stSidebar, .css-6qob1r, [data-testid="stSidebar"] {
        background: #111111 !important;
    }
    .st-dl, a, a:visited {
        color: #1E90FF !important;  /* bright highlight links */
        text-decoration: none;
    }
    a:hover { text-decoration: underline; }
    .css-1aumxhk {background-color:transparent;}
    .stButton>button {
        color: #fff;
        background-color: #1E90FF;
        font-weight: 600;
        border-radius: 8px;
        border: none;
        padding: 0.6em 1.2em;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #1E90FF 60%, #22c8e5 100%);
        color: #fff;
    }
    .stImage>img, .stMarkdown img {
        border-radius: 12px; 
        border: 1.5px solid #222;
        box-shadow: 0 4px 16px #1E90FF22;
    }
    .stExpanderHeader {color: #1E90FF;}
    .st-expanderContent {background: #181818! important;}
    hr {border: 1px solid #282828;}
    ::selection {
        background: #1E90FF44;
    }
    </style>
""", unsafe_allow_html=True)

# ------------- SIDEBAR ------------- #
with st.sidebar:
    st.image("passport.jpg", width=170)
    st.markdown("## 📬 Contact")
    st.write("📧 <span style='color:#1E90FF'>ashwikbire@gmail.com</span>", unsafe_allow_html=True)
    st.write("📱 <span style='color:#1E90FF'>8459291488</span>", unsafe_allow_html=True)
    st.markdown("🌏 [LinkedIn](https://www.linkedin.com/)", unsafe_allow_html=True)

# ------------- MAIN CONTENT ----------- #
st.title("Ashwik Bire")
st.write("""
*Business Intelligence Enthusiast | Data Science | Data Analytics | Power BI | TDV | TIBCO Spotfire | Tableau | Python Machine Learning | SQL | Azure Data Engineering | Azure Databricks | PMO*
""")

with st.expander("💡 About Me", expanded=True):
    st.write("""
I am a Data Analyst with over 2.9 years of experience, skilled in Microsoft Power BI and TIBCO Spotfire, with work at Atos Syntel and for Birlasoft & FedEx APAC Client. 
I've been recognized by the CEO of Atos Syntel with a Spot Recognition Award and achieved top rank in the Amrita Business Innovation Challenge. 
I'm also passionate about nature photography, dance, and creative writing. My goal is to deliver valuable insights and excellent results for every project I work on.
    """)

tab_titles = [
    "Education", "Experience", "Technologies", "Tools", "Projects",
    "Certifications", "Achievements", "Interests", "Social Sites", "Contact"
]

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(tab_titles)

with tab1:
    st.subheader("📖 Education")
    st.markdown("""
- **Bachelor of Engineering, Electronics & Telecommunication** | Score: 82.36%  
  _P.R. Pote College of Engineering and Management, Amravati (SGBAU)_  
  2019 - 2022

- **Engineering Diploma** | Score: 75%  
  _DR. Panjabrao Deshmukh Polytechnic, Amravati_  
  2016 - 2019

- **S.S.C** | Score: 79%  
  _Janta High School Purnanager, Amravati_  
  2015 - 2016
    """)

with tab2:
    st.subheader("🧑‍💼 Experience")
    st.markdown("""
**Atos Syntel** | Aug 2022 – Aug 2023

_Project: Analytics COE (Centre of Excellence) APAC (Asia Pacific)_  
_Client: FedEx APAC_  
_Role: Associate Consultant_  
_Environment: TIBCO Spotfire 11x, DW, Power BI_

**Key Responsibilities:**
- Developed airWISE dashboard from inception using TIBCO Data Virtualization and custom visualizations.
- Supported and enhanced dashboards, managed migration across DEV, QA, and PROD.
- Collaborated in Agile, attended daily stand-ups and meetings.
- Translated raw data to actionable visualizations for stakeholders.

---

**VDA Infosolutions Pvt Ltd** | Dec 2023 – Present

_Designation: Data Analyst_  
_Clients: Tata Consultancy Services, Birlasoft Pvt Ltd_  
_Environment: Power BI Desktop, MS Excel_

**Key Responsibilities:**
- Maintained dashboards for monitoring incidents, issues, and service requests.
- Designed and implemented dashboards for asset management for TIO.
- Data validation/auditing for ticketing (Endurance Technologies).
- SLA monitoring and compliance analysis.
- Automated reports and visualization for efficiency.
    """)

with tab3:
    st.subheader("💻 Technologies")
    st.markdown("""
- **Python Programming**
- **SQL**
- Python Libraries: Numpy, Pandas, Matplotlib, Scikit-Learn, Seaborn, Scipy
- Azure Data Factory, Databricks
- SAFe Agile
- Frontend: HTML, CSS, JS, Bootstrap
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
**Power BI Projects:**  
- Hospital Activity UK Dashboard  
- Amazon Sales Dashboard

**Web Development Projects:**  
- A_Naturography Website  
- Online Food Ordering System

**IOT/Academic Project:**  
- Conference Room Light Controller with Bidirectional Visitor Counter

**Python Project:**  
- Road Line Detection using OpenCV
    """)

with tab6:
    st.subheader("🎓 Certifications")
    st.markdown("""
- Microsoft Azure Fundamental
- Microsoft Certified Power BI Data Analyst Associate
- Business Intelligence Foundation Professional
- Scrum Foundational Professional Certificate
- TIBCO Spotfire Development from Beginner to advanced
- Master Microsoft Power BI in 21 Days
- SQL Intermediate
- Front End Web Development Ultimate Course 2021
- Python Programming - Basics to Advanced
    """)

with tab7:
    st.subheader("🏆 Achievements")
    st.markdown("""
- Spot Recognition by CEO Atos Syntel (Sep 2022)
- State Winner – Amrita Business Innovation Challenge (Jun 2022)
- Appreciation Award – PRPCEM Amravati (May 2022)
- Coding Round – Techgig Code Gladiators (Aug 2021)
- 1st Prize – Paper Presentation, PRP College (Jan 2020)
- 1st Prize – Solo Dance Competition (Jan 2019)
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
- [LinkedIn](https://www.linkedin.com/)
- [HackerRank](https://www.hackerrank.com/)
- [GitHub](https://github.com/)
- [Photography Portfolio](#)
- Instagram: [A_Naturography](https://www.instagram.com/)
- Instagram: [Shimmering Lines](https://www.instagram.com/)
    """, unsafe_allow_html=True)

with tab10:
    st.subheader("📱 Contact")
    st.write("Email: <span style='color:#1E90FF'>ashwikbire@gmail.com</span>", unsafe_allow_html=True)
    st.write("Contact Number: <span style='color:#1E90FF'>8459291488</span>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.write("<div style='text-align:center; color:#888;'>© Ashwik Bire</div>", unsafe_allow_html=True)
