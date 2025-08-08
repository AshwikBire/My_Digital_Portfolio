import streamlit as st

# Set page configuration with customized theme
st.set_page_config(
    page_title="Ashwik Bire | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for fonts, colors, and layout
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #f8f9fa, #eef2f7);
    }
    .sidebar .sidebar-content {
        background: #e0f7fa !important;
    }
    h1, h2, h3, h4 {
        font-family: 'Segoe UI', 'Helvetica Neue', Arial, 'sans-serif';
    }
    .stTabs [role="tablist"] {
        flex-wrap: wrap !important;
        gap: 6px !important;
    }
    .css-1v0mbdj, .stTabs [role="tab"] {
        background: #a7ffeb !important;
        border-radius: 6px;
        margin-bottom: 2px;
        color: #00796b !important;
        font-weight: bold !important;
    }
    .stTabs [aria-selected="true"] {
        background: #004d40 !important;
        color: #fff !important;
    }
    .stMarkdown hr {
        border: 1px solid #26a69a;
        margin: 18px 0 10px 0;
    }
    .info-card {
        background: #fffde7;
        border-radius: 10px;
        padding: 14px 18px;
        box-shadow: 0 1px 8px #eee;
    }
    .contact-icon {
        font-size: 23px;
        margin-right: 8px;
        color: #00796b;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar design
with st.sidebar:
    st.image("passport.jpg", width=160)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h4>📬 Contact</h4>", unsafe_allow_html=True)
    st.write(f'<span class="contact-icon">📧</span> <a href="mailto:ashwikbire@gmail.com">ashwikbire@gmail.com</a>', unsafe_allow_html=True)
    st.write(f'<span class="contact-icon">📱</span> 8459291488', unsafe_allow_html=True)
    st.write(f'<span class="contact-icon">🌏</span> <a href="https://linkedin.com/in/ashwikbire" target="_blank">LinkedIn (Profile)</a>', unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("**Location:** Amravati, Maharashtra")
    st.markdown("""
    <div style='text-align:center'>
        <img src='https://img.icons8.com/fluency/48/instagram-new.png' width='24'/>
        <img src='https://img.icons8.com/color/48/github.png' width='24'/>
        <img src='https://img.icons8.com/color/48/hackerrank.png' width='24'/>
    </div>
    """, unsafe_allow_html=True)

# Main header
st.markdown('<h1 style="color:#00695c;margin-bottom:0">Ashwik Bire</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="color:#26a69a;margin-top:0;">Business Intelligence | Data Analytics | Data Science</h3>', unsafe_allow_html=True)

st.markdown("""
<div class="info-card">
<p>
    <b>Microsoft Power BI</b> · <b>TIBCO Spotfire</b> · <b>Tableau</b> · <b>Python</b> · <b>SQL</b> · <b>Azure Data Engineering</b> · <b>TDV</b> · <b>Databricks</b> · <b>PMO</b>
</p>
</div>
""", unsafe_allow_html=True)

with st.expander("About Me", expanded=True):
    st.markdown("""
    <div style="font-size:1.15em;">
    Data Analyst with nearly 3 years' experience in Power BI, TIBCO Spotfire, at Atos Syntel for Birlasoft & FedEx APAC. 
    <br><br>
    CEO-awarded at Atos, state winner of Amrita Business Innovation Challenge. 
    <br><br>
    Passionate about nature photography, dance, and creative writing—fueling creativity and attention to detail. <br>
    <b>Goal:</b> Deliver valuable, actionable insights and excellent results for every project.
    </div>
    """, unsafe_allow_html=True)

# Tabs for content
tabs = st.tabs([
    "🎓 Education", "💼 Experience", "🖥️ Technologies", "🛠️ Tools",
    "📈 Projects", "📝 Certifications", "🏆 Achievements", "🎯 Interests",
    "🌐 Social Sites", "📪 Contact"
])

with tabs[0]:
    st.subheader("Education")
    st.markdown("""
    **Bachelor of Engineering, Electronics & Telecommunication**  
    P.R. Pote College of Engineering and Management, Amravati (SGBAU) | 2019 - 2022  
    <b>Score:</b> 82.36%  
    ---
    **Engineering Diploma**  
    DR. Panjabrao Deshmukh Polytechnic, Amravati | 2016 - 2019  
    <b>Score:</b> 75%  
    ---
    **S.S.C**  
    Janta High School Purnanager, Amravati | 2015 - 2016  
    <b>Score:</b> 79%
    """, unsafe_allow_html=True)

with tabs[1]:
    st.subheader("Experience")
    st.markdown("""
    <b>Atos Syntel</b> <br> <i>Aug 2022 – Aug 2023</i>
    <ul>
        <li>Developed airWISE dashboard from inception using TIBCO Data Virtualization and custom visualizations.</li>
        <li>Dashboard maintenance, migration management across environments.</li>
        <li>Agile collaboration, attended daily stand-ups.</li>
        <li>Translated raw data to actionable visualizations for stakeholders.</li>
    </ul>
    <hr>
    <b>VDA Infosolutions Pvt Ltd</b> <br> <i>Dec 2023 – Present</i>
    <ul>
        <li>Maintained dashboards for asset monitoring, incidents, SLA compliance.</li>
        <li>Designed/implemented asset management dashboards for TIO.</li>
        <li>Automated reporting for improved efficiency.</li>
        <li>Data validation, auditing, and ticketing analysis.</li>
    </ul>
    """, unsafe_allow_html=True)

with tabs[2]:
    st.subheader("Technologies")
    st.markdown("""
    <span style="color:#00695c">Python (Numpy, Pandas, Matplotlib, Scikit-Learn, Seaborn, Scipy)</span>  
    <span style="color:#00796b">SQL</span>  
    <span style="color:#00897b">Azure Data Factory, Databricks</span>  
    <span style="color:#009688">SAFe Agile</span>  
    <span style="color:#00bcd4">Frontend: HTML, CSS, JS, Bootstrap</span>
    """, unsafe_allow_html=True)

with tabs[3]:
    st.subheader("Tools")
    st.markdown("""
    - Power BI Desktop
    - TIBCO Spotfire 11.4x
    - Tableau Public
    - TIBCO Data Virtualization (TDV)
    """, unsafe_allow_html=True)

with tabs[4]:
    st.subheader("Projects")
    st.markdown("""
    <ul>
    <li><b>Power BI:</b> UK Hospital Activity Dashboard, Amazon Sales Dashboard</li>
    <li><b>Web:</b> A_Naturography Website, Online Food Ordering System</li>
    <li><b>IOT/Academic:</b> Conference Room Light Controller & Bi-Directional Counter</li>
    <li><b>Python:</b> Road Line Detection using OpenCV</li>
    </ul>
    """, unsafe_allow_html=True)

with tabs[5]:
    st.subheader("Certifications")
    st.markdown("""
    <ul>
    <li>Microsoft Azure Fundamental</li>
    <li>Microsoft Certified Power BI Data Analyst Associate</li>
    <li>Business Intelligence Foundation Professional</li>
    <li>Scrum Foundational Professional Certificate</li>
    <li>TIBCO Spotfire Development (Beginner to Advanced)</li>
    <li>Master Power BI in 21 Days</li>
    <li>SQL Intermediate</li>
    <li>Front End Web Development Ultimate Course 2021</li>
    <li>Python Programming - Basics to Advanced</li>
    </ul>
    """, unsafe_allow_html=True)

with tabs[6]:
    st.subheader("Achievements")
    st.markdown("""
    <ul>
    <li>🟢 Spot Recognition by CEO Atos Syntel (Sep 2022)</li>
    <li>🟢 State Winner – Amrita Business Innovation Challenge (Jun 2022)</li>
    <li>🟢 Appreciation Award – PRPCEM Amravati (May 2022)</li>
    <li>🟢 Coding Round – Techgig Code Gladiators (Aug 2021)</li>
    <li>🟢 1st Prize – Paper Presentation, PRP College (Jan 2020)</li>
    <li>🟢 1st Prize – Solo Dance Competition (Jan 2019)</li>
    <li>🟢 3rd Prize – Technical Quiz (Jan 2019)</li>
    <li>🟢 1st Prize – Kavya Vachan (Jan 2017)</li>
    </ul>
    """, unsafe_allow_html=True)

with tabs[7]:
    st.subheader("Interests & Hobbies")
    st.markdown("""
    <ul>
    <li>Nature photography</li>
    <li>Dance</li>
    <li>Creative writing</li>
    <li>Continuous learning & skill development</li>
    </ul>
    """, unsafe_allow_html=True)

with tabs[8]:
    st.subheader("Social Sites")
    st.markdown("""
    <ul>
    <li><a href="https://linkedin.com/in/ashwikbire" target="_blank">LinkedIn</a></li>
    <li><a href="https://www.hackerrank.com/ashwikbire" target="_blank">HackerRank</a></li>
    <li><a href="https://github.com/ashwikbire" target="_blank">GitHub</a></li>
    <li><a href="#" target="_blank">Photography Portfolio</a></li>
    <li>Instagram: <a href="https://instagram.com/A_Naturography" target="_blank">A_Naturography</a></li>
    <li>Instagram: <a href="https://instagram.com/ShimmeringLines" target="_blank">Shimmering Lines</a></li>
    </ul>
    """, unsafe_allow_html=True)

with tabs[9]:
    st.subheader("Contact")
    st.markdown("""
    <span class="contact-icon">📧</span> <a href="mailto:ashwikbire@gmail.com">ashwikbire@gmail.com</a><br>
    <span class="contact-icon">📱</span> 8459291488
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div style="text-align:center;color:#00695c;">© Ashwik Bire</div>', unsafe_allow_html=True)
