import streamlit as st

# Set page config
st.set_page_config(
    page_title="Ashwik Bire | Portfolio",
    page_icon="📊",
    layout="wide",
)

# Sidebar with contact
with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/68031207", width=160)  # You can use your photo or GitHub avatar link here
    st.markdown("## 📬 Contact")
    st.write("📧 ashwikbire@gmail.com")
    st.write("📱 8459291488")
    st.write("🌏 [LinkedIn](https://www.linkedin.com/in/ashwik-bire-b2a000186/)")

st.title("Ashwik Bire")
st.write("""
**Business Intelligence Enthusiast | Data Science | Data Analytics | Power BI | TDV | TIBCO Spotfire | Tableau | Python Machine Learning | SQL | Azure Data Engineering | Azure Databricks | PMO**
""")

with st.expander("About Me", expanded=True):
    st.write("""
I am a Data Analyst with over 2.5 years of experience, skilled in Microsoft Power BI and TIBCO Spotfire, with work at Atos Syntel and for Birlasoft & FedEx APAC Client. I’ve been recognized by the CEO of Atos Syntel with a Spot Recognition Award for my contributions and achieved top rank in the Amrita Business Innovation Challenge Powered By Unstop (Dare 2 Compete). I’m also passionate about nature photography, dance, and creative writing, which fuel my creativity and attention to detail. My goal is to deliver valuable insights and excellent results for every project I work on.
""")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([
    "Education", "Experience", "Technologies", "Tools", "Projects", "Certifications",
    "Achievements", "Interests", "Social Sites", "Contact"
])

with tab1:
    st.subheader("Education")
    st.markdown("""
- **Bachelor of Engineering, Electronics & Telecommunication** | Score: 82.36%  
  *P.R. Pote College of Engineering and Management, Amravati (SGBAU)*  
  *2019 - 2022*
- **Engineering Diploma** | Score: 75%  
  *DR. Panjabrao Deshmukh Polytechnic, Amravati*  
  *2016 - 2019*
- **S.S.C** | Score: 79%  
  *Janta High School Purnanager, Amravati*  
  *2015 - 2016*
""")

with tab2:
    st.subheader("Experience")
    st.markdown("""
### Atos Syntel | Aug 2022 – Aug 2023
- **Project:** Analytics COE (Centre of Excellence) APAC (Asia Pacific)
- **Client:** FedEx APAC
- **Role:** Associate Consultant
- **Environment:** TIBCO Spotfire 11x, DW, Power BI

**Key Responsibilities:**
- Developed airWISE dashboard from inception using TIBCO Data Virtualization and custom visualizations.
- Supported and enhanced dashboards, managed migration across DEV, QA, and PROD.
- Collaborated in Agile, attended daily stand-ups and meetings.
- Translated raw data to actionable visualizations for stakeholders.

---

### VDA Infosolutions Pvt Ltd | Dec 2023 – Present
- **Designation:** Data Analyst
- **Clients:** Tata Consultancy Services, Birlasoft Pvt Ltd
- **Environment:** Power BI Desktop, MS Excel

**Key Responsibilities:**
- Maintained dashboards for monitoring incidents, issues, and service requests.
- Designed and implemented dashboards for asset management for TIO.
- Data validation/auditing for ticketing (Endurance Technologies).
- SLA monitoring and compliance analysis.
- Automated reports and visualization for efficiency.
""")

with tab3:
    st.subheader("Technologies")
    st.markdown("""
- **Python Programming**
- **SQL**
- Python Libraries: Numpy, Pandas, Matplotlib, Scikit-Learn, Seaborn, Scipy
- Azure Data Factory, Databricks
- SAFe Agile
- Frontend: HTML, CSS, JS, Bootstrap
""")

with tab4:
    st.subheader("Tools")
    st.markdown("""
- Power BI Desktop
- TIBCO Spotfire 11.4x
- Tableau Public
- TIBCO Data Virtualization (TDV)
""")

with tab5:
    st.subheader("Projects")
    st.markdown("""
**Power BI Projects:**
- [Hospital Activity UK Dashboard](https://github.com/AshwikBire/Hospital-Activity-UK-Dashboard.git)
- [Amazon Sales Dashboard](https://github.com/AshwikBire/Amazon-Sales-Dashboard.git)

**Web Development Projects:**
- [A_Naturography Website](https://ashwikbire.github.io/a_naturography.github.io)
- [Online Food Ordering System](https://github.com/AshwikBire/ONLINE-FOOD-ORDERING-SYSTEM.git)

**IOT/Academic Project:**
- Conference Room Light Controller with Bidirectional Visitor Counter

**Python Project:**
- [Road Line Detection using OpenCV](https://github.com/AshwikBire/Road-Line-Detector-using-Python.git)
""")

with tab6:
    st.subheader("Certifications")
    st.markdown("""
- [Microsoft Azure Fundamental](https://learn.microsoft.com/en-us/users/ashwikbire-7557/credentials/7de31893d146bf69)
- [Microsoft Certified Power BI Data Analyst Associate](https://learn.microsoft.com/en-us/users/ashwikbire-7557/credentials/b4324bff2a4c2081)
- [Business Intelligence Foundation Professional](https://www.credly.com/badges/cbaf47fb-ac03-497d-8c73-12aa1c545e2c/public_url)
- [Scrum Foundational Professional Certificate](https://www.credly.com/badges/79aea45b-709c-4419-814b-930c88d25f92/linked_in_p)
- TIBCO Spotfire Development from Beginner to advance
- Master Microsoft Power BI in 21 Days
- [SQL Intermediate](https://www.hackerrank.com/certificates/79ec222704f3)
- [Front End Web Development Ultimate Course 2021](https://www.linkedin.com/sharing/share-offsite/?url=http%3A%2F%2Fude.my%2FUC-3bacc955-2f7b-4e2e-9340-a6cc4f4121a4)
- [Python Programming - Basics to Advanced](https://www.udemy.com/certificate/UC-21d316ab-2820-482a-9abb-be3c7c9e0c3d/)
""")

with tab7:
    st.subheader("Achievements")
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
    st.subheader("Interests & Hobbies")
    st.markdown("""
- Nature photography
- Dance
- Creative writing
- Continuous learning & skill development
""")

with tab9:
    st.subheader("Social Sites")
    st.markdown("""
- [LinkedIn](https://www.linkedin.com/in/ashwik-bire-b2a000186/)
- [HackerRank](https://www.hackerrank.com/ashwikbire?hr_r=1)
- [GitHub](https://github.com/AshwikBire)
- [Photography Portfolio](https://ashwikbire.github.io/a_naturography.github.io)
- [Instagram: A_Naturography](https://www.instagram.com/a_naturography/)
- [Instagram: Shimmering Lines](https://www.instagram.com/_shimmering_lines_/)
""")

with tab10:
    st.subheader("Contact")
    st.write("**Email:** ashwikbire@gmail.com")
    st.write("**Contact Number:** 8459291488")

st.markdown("<hr>", unsafe_allow_html=True)
st.write("© Ashwik Bire")

