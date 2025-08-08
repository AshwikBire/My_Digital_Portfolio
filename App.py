import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="Ashwik Bire | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Google Fonts and FontAwesome icons, add custom CSS including animations and dark mode switch
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Montserrat:wght@600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" crossorigin="anonymous" />
    <style>
        /* Base styling */
        html, body, [class*="css"] {
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: 'Roboto', sans-serif;
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        :root {
            --bg-color: #000000;
            --sidebar-bg: #111111;
            --text-color: #FFFFFF;
            --primary-color: #1E90FF;
            --secondary-color: #22c8e5;
            --header-font: 'Montserrat', sans-serif;
            --shadow-color: #1E90FF44;
        }
        /* Dark mode variables */
        .dark-mode {
            --bg-color: #000000;
            --sidebar-bg: #111111;
            --text-color: #FFFFFF;
        }
        /* Light mode variables */
        .light-mode {
            --bg-color: #f5f5f5;
            --sidebar-bg: #ffffff;
            --text-color: #222222;
        }

        /* Headers */
        h1, h2, h3, h4, h5, h6 {
            font-family: var(--header-font);
            color: var(--primary-color);
            font-weight: 700;
            letter-spacing: 0.05em;
            text-shadow: 1px 1px 6px #2228;
            margin-bottom: 0.25em;
        }

        /* Sidebar background and image styling */
        .css-6qob1r, [data-testid="stSidebar"] {
            background-color: var(--sidebar-bg) !important;
            padding-top: 1rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        .stImage>img {
            border-radius: 16px;
            border: 2px solid var(--primary-color);
            box-shadow: 0 4px 20px var(--shadow-color);
            transition: transform 0.3s ease;
        }
        .stImage>img:hover {
            transform: scale(1.05);
        }

        /* Links */
        a, .st-dl a {
            color: var(--primary-color);
            text-decoration: none;
            font-weight: 600;
            transition: color 0.3s ease;
        }
        a:hover, a:focus {
            color: var(--secondary-color);
            text-decoration: underline;
        }

        /* Buttons */
        .stButton>button {
            background: linear-gradient(90deg, var(--primary-color) 60%, var(--secondary-color) 100%);
            border-radius: 12px;
            border: none;
            color: #fff;
            font-weight: 700;
            padding: 0.7em 1.5em;
            box-shadow: 0 4px 12px var(--shadow-color);
            transition: background-position 0.3s ease;
            background-size: 200% 100%;
            background-position: right bottom;
        }
        .stButton>button:hover {
            background-position: left bottom;
            cursor: pointer;
        }

        /* Tabs active styling */
        .stTabs [role="tablist"] button[aria-selected="true"] {
            background-color: var(--primary-color) !important;
            color: #fff !important;
            font-weight: 700 !important;
            border-radius: 12px 12px 0 0 !important;
            box-shadow: 0 2px 10px var(--shadow-color);
        }

        /* Expander header */
        .stExpanderHeader {
            color: var(--primary-color);
            font-weight: 700;
            cursor: pointer;
            transition: color 0.3s ease;
        }
        .stExpanderHeader:hover {
            color: var(--secondary-color);
        }
        .st-expanderContent {
            background-color: var(--sidebar-bg);
            border-left: 3px solid var(--primary-color);
            padding: 1rem;
            border-radius: 0 0 10px 10px;
            margin-bottom: 2rem;
        }

        /* Horizontal rule */
        hr {
            border: 1px solid #282828;
            margin-top: 2rem;
            margin-bottom: 2rem;
        }

        /* Selection */
        ::selection {
            background: var(--primary-color);
            color: #000;
        }

        /* Dark mode toggle container */
        #darkmode-toggle {
            position: fixed;
            top: 12px;
            right: 12px;
            z-index: 9999;
        }
        /* Responsive columns spacing */
        .custom-columns > div {
            padding-right: 1rem;
        }
    </style>

    <script>
        // Dark mode toggle script to switch CSS variables and persist preference
        const toggleSwitch = () => {
            const body = document.body;
            body.classList.toggle('light-mode');
            body.classList.toggle('dark-mode');
            if(body.classList.contains('dark-mode')){
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        }

        document.addEventListener('DOMContentLoaded', function () {
            const savedTheme = localStorage.getItem('theme') || 'dark';
            if(savedTheme === 'light') {
                document.body.classList.add('light-mode');
            } else {
                document.body.classList.add('dark-mode');
            }
        });
    </script>

    <!-- Dark mode toggle button -->
    <div id="darkmode-toggle" style="color: var(--primary-color); font-size: 1.5rem; cursor: pointer;" title="Toggle light/dark mode" onclick="toggleSwitch()">
        <i class="fa-regular fa-moon"></i>
    </div>
""", unsafe_allow_html=True)

# Sidebar content
with st.sidebar:
    st.image("passport.jpg", width=170)
    st.markdown("## 📬 Contact")
    st.write("📧 ", "[ashwikbire@gmail.com](mailto:ashwikbire@gmail.com)")
    st.write("📱 8459291488")
    st.markdown("[🌏 LinkedIn](https://www.linkedin.com/in/your-profile)")

# Main content
st.title("Ashwik Bire")
st.markdown(
    "*Business Intelligence Enthusiast | Data Science | Data Analytics | Power BI | TDV | TIBCO Spotfire | Tableau | Python Machine Learning | SQL | Azure Data Engineering | Azure Databricks | PMO*")

with st.expander("💡 About Me", expanded=True):
    st.markdown("""
I am a Data Analyst with over 2.9 years of experience, skilled in Microsoft Power BI and TIBCO Spotfire, with work at Atos Syntel and for Birlasoft & FedEx APAC Client.  
I've been recognized by the CEO of Atos Syntel with a Spot Recognition Award and achieved top rank in the Amrita Business Innovation Challenge.  
I'm passionate about nature photography, dance, and creative writing — fueling creativity and attention to detail.  
My goal is to deliver valuable insights and excellent results for every project I work on.
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

**Responsibilities:**
- Developed airWISE dashboard from inception using TIBCO Data Virtualization and custom visualizations.
- Managed dashboard migration across DEV, QA, and PROD.
- Collaborated with Agile teams attending daily stand-ups and meetings.
- Delivered actionable visualizations for stakeholders.

---

**VDA Infosolutions Pvt Ltd** | Dec 2023 – Present

_Designation: Data Analyst_  
_Clients: Tata Consultancy Services, Birlasoft Pvt Ltd_  
_Environment: Power BI Desktop, MS Excel_

**Responsibilities:**
- Maintained dashboards monitoring incidents, issues, and service requests.
- Designed asset management dashboards for TIO.
- Performed data validation and auditing for ticketing.
- Monitored SLA compliance.
- Automated reporting and visualization processes.
    """)

with tab3:
    st.subheader("💻 Technologies")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
- Python Programming
- SQL
- Python Libraries: Numpy, Pandas, Matplotlib, Scikit-Learn, Seaborn, Scipy
        """)
    with col2:
        st.markdown("""
- Azure Data Factory
- Azure Databricks
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
st.markdown("""
<div style="text-align:center; color:#888;">© Ashwik Bire</div>
""", unsafe_allow_html=True)
