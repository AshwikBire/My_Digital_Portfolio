import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Ashwik Bire | Portfolio",
    page_icon="📊",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
    /* Background and font */
    body, .main {
        background-color: #f5f7fa;
        font-family: 'Segoe UI', sans-serif;
        color: #222;
    }

    /* Sidebar styling */
    .css-1d391kg, .css-1d391kg img {
        border-radius: 10px;
    }
    .css-1d391kg img {
        margin-bottom: 15px;
    }

    /* Section headers */
    h2, h3, h4 {
        color: #0e4d92;
        border-bottom: 1px solid #e6e6e6;
        padding-bottom: 5px;
    }

    /* Tabs styling */
    .stTabs [role="tab"] {
        font-weight: bold;
        padding: 12px;
        border: 1px solid #ccc;
        border-radius: 8px 8px 0 0;
        margin-right: 4px;
        background-color: #e3e8f0;
    }

    .stTabs [role="tab"][aria-selected="true"] {
        background-color: #0e4d92;
        color: white;
    }

    /* Footer */
    footer {
        display: none;
    }

    </style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.image("passport.jpg", width=180)  # Use local or GitHub image link
    st.markdown("## 📬 Contact Me")
    st.write("📧 ashwikbire@gmail.com")
    st.write("📱 8459291488")
    st.write("🌐 [LinkedIn](https://www.linkedin.com/in/ashwik-bire-b2a000186/)")

# ---------- MAIN TITLE ----------
st.title("✨ Ashwik Bire")
st.write("**Business Intelligence Enthusiast | Data Science | Power BI | Azure | Python | SQL | Spotfire**")

# ---------- ABOUT ME ----------
with st.expander("👤 About Me", expanded=True):
    st.markdown("""
    I am a **Data Analyst** with 2.9+ years of experience in Business Intelligence using Microsoft Power BI, SQL, and TIBCO Spotfire.  
    My work at **Atos Syntel** and **Birlasoft (TCS/FedEx APAC)** has earned me several recognitions, including a **Spot Award from CEO of Atos**.  
    I’m also passionate about nature photography, dance, and creative writing – they keep my creative spark alive.  
    """)

# ---------- TABS ----------
tab_labels = [
    "🎓 Education", "💼 Experience", "🛠️ Technologies", "🔧 Tools", "📁 Projects",
    "📜 Certifications", "🏆 Achievements", "🎯 Interests", "🌐 Social Sites", "📞 Contact"
]

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(tab_labels)

# ---------- EDUCATION ----------
with tab1:
    st.subheader("🎓 Education")
    st.markdown("""
- **Bachelor of Engineering, Electronics & Telecommunication** | 82.36%  
  *P.R. Pote College of Engineering and Management, Amravati – 2019-2022*

- **Diploma in Engineering** | 75%  
  *Dr. Panjabrao Deshmukh Polytechnic, Amravati – 2016-2019*

- **S.S.C (10th)** | 79%  
  *Janta High School Purnanager, Amravati – 2015-2016*
""")

# ---------- EXPERIENCE ----------
with tab2:
    st.subheader("💼 Experience")
    st.markdown("""
### VDA Infosolutions Pvt Ltd | Dec 2023 – Present  
**Role:** Data Analyst | **Clients:** TCS, Birlasoft  
- Developed dashboards for TIO asset management.  
- Automated report generation using Power BI and Excel.  
- Audited ticketing data and monitored SLA compliance.  

---

### Atos Syntel | Aug 2022 – Aug 2023  
**Role:** Associate Consultant | **Client:** FedEx APAC  
- Created airWISE dashboard with TIBCO Spotfire & TDV.  
- Involved in agile processes and daily stand-up meetings.  
- Translated business needs into insightful dashboards.
""")

# ---------- TECHNOLOGIES ----------
with tab3:
    st.subheader("🛠️ Technologies")
    st.markdown("""
- Python, SQL  
- Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn  
- Azure Data Factory, Azure Databricks  
- HTML, CSS, Bootstrap, JavaScript  
- Agile Methodologies (SAFe)
""")

# ---------- TOOLS ----------
with tab4:
    st.subheader("🔧 Tools")
    st.markdown("""
- Microsoft Power BI  
- TIBCO Spotfire 11.4x  
- Tableau Public  
- TIBCO Data Virtualization (TDV)
""")

# ---------- PROJECTS ----------
with tab5:
    st.subheader("📁 Projects")
    st.markdown("""
**🔹 Power BI Projects:**  
- [Hospital Activity UK Dashboard](https://github.com/AshwikBire/Hospital-Activity-UK-Dashboard.git)  
- [Amazon Sales Dashboard](https://github.com/AshwikBire/Amazon-Sales-Dashboard.git)  

**🔹 Web Development:**  
- [A_Naturography Website](https://ashwikbire.github.io/a_naturography.github.io)  
- [Online Food Ordering System](https://github.com/AshwikBire/ONLINE-FOOD-ORDERING-SYSTEM.git)  

**🔹 Python Project:**  
- [Road Line Detection using OpenCV](https://github.com/AshwikBire/Road-Line-Detector-using-Python.git)  

**🔹 IoT Academic Project:**  
- Conference Room Light Controller with Visitor Counter
""")

# ---------- CERTIFICATIONS ----------
with tab6:
    st.subheader("📜 Certifications")
    st.markdown("""
- [Microsoft Azure Fundamentals](https://learn.microsoft.com/en-us/users/ashwikbire-7557/credentials/7de31893d146bf69)  
- [Power BI Data Analyst Associate](https://learn.microsoft.com/en-us/users/ashwikbire-7557/credentials/b4324bff2a4c2081)  
- [Business Intelligence Foundation Professional](https://www.credly.com/badges/cbaf47fb-ac03-497d-8c73-12aa1c545e2c/public_url)  
- [Scrum Foundation](https://www.credly.com/badges/79aea45b-709c-4419-814b-930c88d25f92/linked_in_p)  
- [SQL Intermediate - HackerRank](https://www.hackerrank.com/certificates/79ec222704f3)  
- [Python Programming (Udemy)](https://www.udemy.com/certificate/UC-21d316ab-2820-482a-9abb-be3c7c9e0c3d/)  
- TIBCO Spotfire, Power BI (Udemy)
""")

# ---------- ACHIEVEMENTS ----------
with tab7:
    st.subheader("🏆 Achievements")
    st.markdown("""
- 🏅 Spot Recognition by CEO, Atos Syntel  
- 🥇 State Winner – Amrita Business Innovation Challenge  
- 🥇 1st Prize – Solo Dance, Paper Presentation  
- 🥉 Tech Quiz – PRPCEM  
- ✍️ Kavya Vachan Champion
""")

# ---------- INTERESTS ----------
with tab8:
    st.subheader("🎯 Interests & Hobbies")
    st.markdown("""
- Nature Photography 📸  
- Dance 💃  
- Creative Writing ✍️  
- Exploring Data Science & Innovation 🚀
""")

# ---------- SOCIAL SITES ----------
with tab9:
    st.subheader("🌐 Social Sites")
    st.markdown("""
- [LinkedIn](https://www.linkedin.com/in/ashwik-bire-b2a000186/)  
- [GitHub](https://github.com/AshwikBire)  
- [HackerRank](https://www.hackerrank.com/ashwikbire?hr_r=1)  
- [Photography Portfolio](https://ashwikbire.github.io/a_naturography.github.io)  
- [Instagram: A_Naturography](https://www.instagram.com/a_naturography/)  
- [Instagram: Shimmering Lines](https://www.instagram.com/_shimmering_lines_/)
""")

# ---------- CONTACT ----------
with tab10:
    st.subheader("📞 Contact Me")
    st.write("📧 ashwikbire@gmail.com")
    st.write("📱 8459291488")

# ---------- FOOTER ----------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<center>© 2025 Ashwik Bire | All rights reserved.</center>", unsafe_allow_html=True)