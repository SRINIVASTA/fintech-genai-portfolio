import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# 1. Initialize Clean Page Configuration
st.set_page_config(
    page_title="Appala Srinivas Tanakala | FinTech & AI Hub",
    page_icon="🏢",
    layout="centered"
)

# 2. Premium Custom CSS (Forces clean hierarchy and dominant header typography)
st.markdown("""
    <style>
    /* Completely removes the native header, search icon, and top empty space */
    header, [data-testid="stHeader"], .st-emotion-cache-18ni7th {
        display: none !important;
        background: transparent !important;
    }
    
    /* Forces the primary app layout container to start right at the pixel top line */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        margin-top: 0px !important;
    }
    
    /* Main profile card container frame */
    .main-profile-card {
        background-color: #ffffff;
        padding: 30px 24px;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
        text-align: center;
        margin-top: 0px !important;
        margin-bottom: 25px;
    }
    
    /* DOMINANT TYPOGRAPHY: Forces your name and title to be bold and prominent */
    .profile-title { 
        color: #0f172a !important; 
        font-size: 34px !important; 
        font-weight: 800 !important; 
        margin-top: 0px !important; 
        margin-bottom: 8px !important;
        line-height: 1.2 !important;
        letter-spacing: -0.5px !important;
    }
    .profile-subtitle { 
        color: #1e3a8a !important; 
        font-size: 18px !important; 
        font-weight: 700 !important; 
        margin-bottom: 6px !important;
        line-height: 1.4 !important;
    }
    .profile-loc { 
        color: #475569 !important; 
        font-size: 14px !important; 
        font-weight: 600 !important;
        margin-bottom: 20px !important; 
    }
    
    /* Balanced Category grid layout headers */
    .hub-column-title {
        color: #1e3a8a;
        font-size: 16px;
        font-weight: 800;
        border-bottom: 3px solid #1e3a8a;
        padding-bottom: 6px;
        margin-top: 25px;
        margin-bottom: 15px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .hub-section-badge {
        font-size: 11px;
        color: #475569;
        font-weight: 700;
        margin-top: 12px;
        margin-bottom: 6px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        background-color: #f1f5f9;
        padding: 4px 8px;
        border-radius: 4px;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Clean Profile Header Workspace (Dominates the page with strict typography rules)
st.markdown('<div class="main-profile-card">', unsafe_allow_html=True)
st.markdown('<div class="profile-title">Appala Srinivas Tanakala</div>', unsafe_allow_html=True)
st.markdown('<div class="profile-subtitle">Strategic Financial Leader & AI-Augmented Data Scientist</div>', unsafe_allow_html=True)
st.markdown('<div class="profile-loc">📍 Visakhapatnam, Andhra Pradesh, India</div>', unsafe_allow_html=True)

# Contact Communication buttons
contact_col1, contact_col2, contact_col3 = st.columns(3)
with contact_col1:
    st.link_button("📞 Call Me", "tel:+918897415303", use_container_width=True)
with contact_col2:
    st.link_button("✉️ Email", "mailto:tasrinivass@gmail.com", use_container_width=True)
with contact_col3:
    st.link_button("🤝 LinkedIn", "https://www.linkedin.com/in/srinivas-t-a-557637119/", use_container_width=True)

# Portfolios buttons row
port_col1, port_col2 = st.columns(2)
with port_col1:
    st.link_button("💻 GitHub Profile", "https://github.com/srinivasta", use_container_width=True)
with port_col2:
    st.link_button("🥇 Kaggle Workspace", "https://kaggle.com/srinivasta", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 4. Two-Column Workspace Layout for Your 24 Applications
left_grid, right_grid = st.columns(2)

with left_grid:
    st.markdown('<div class="hub-column-title">🏢 FinTech & BI Solutions</div>', unsafe_allow_html=True)
    
    st.markdown('<span class="hub-section-badge">📈 Production Platforms</span>', unsafe_allow_html=True)
    st.link_button("📈 TransitionControl", "https://transition-command-center-hwyfkbtfvwcitg94dufcwg.streamlit.app/")
    st.link_button("💰 CapitalVantage Auditor", "https://5nemtiurhbntuup3etwc8f.streamlit.app/")
    st.link_button("💳 CreditPulse-AI", "https://creditpulse-ai-ow7sdnqsrbt6yf4ddtrxmc.streamlit.app/")
    st.link_button("🏗️ Moder 4C's Engine", "https://moder-4c-s-dynamic-policy-engine-am7fzqxlcyxmxyqxsfpugp.streamlit.app")

    st.markdown('<span class="hub-section-badge">📊 Analytical Tools & Dashboards</span>', unsafe_allow_html=True)
    st.link_button("📊 Real-time Sales Dashboard", "https://real-time-sales-dashboard-key6zivh5fnkane3t8x6v2.streamlit.app")
    st.link_button("🏢 ConstructAI Dashboard", "https://gfxbyvznuvhyqbxwwyj4os.streamlit.app")
    st.link_button("💹 Multi-Stock Predictor", "https://stock-predictor-app-cqwmt2o3nwmpti92u8n7j2.streamlit.app")
    st.link_button("📊 Stock Analysis Combo", "https://stock-analysis-combo-c7zmpbn2skp5h8rnrpchdy.streamlit.app/") 

    st.markdown('<span class="hub-section-badge">⚙️ Automation & Pipelines</span>', unsafe_allow_html=True)
    st.link_button("🧪 Fintech Regression Automation", "https://fintech-regression-automation-xmg7yrkex5apmvc29knpxl.streamlit.app/") 
    st.link_button("🛰️ Etihad Telemetry Pipeline", "https://etihad-telemetry-pipeline-hoxpbysyd8exh9xwrwjezj.streamlit.app/") 

with right_grid:
    st.markdown('<div class="hub-column-title">🧠 Generative AI & Operations</div>', unsafe_allow_html=True)
    
    st.markdown('<span class="hub-section-badge">⭐ Advanced GenAI Platforms</span>', unsafe_allow_html=True)
    st.link_button("💼 AI Recruiter", "https://airecruiter-bjhauwjq4ncyh6p8q7diot.streamlit.app/") 
    st.link_button("🤖 Multi-Agent Chatbot", "https://multi-agent-chatbot-yv35yj5g7obpbibcxnwrme.streamlit.app")
    st.link_button("🎨 Gemini AI Image Generator", "https://gemini-image-generator-bdyowfxxqb4q5htbrrgjzv.streamlit.app")

    st.markdown('<span class="hub-section-badge">📊 Specialized Intelligence Tools</span>', unsafe_allow_html=True)
    st.link_button("🍲 Smart Bhojan: Nutrition AI", "https://smartbhojan-9hebtsjz3wun3adggzry6s.streamlit.app")
    st.link_button("🎥 YouTube Summarizer", "https://geminitubesummarizer-5ra24rq4meqoogtkfbzpzt.streamlit.app")
    st.link_button("🎤 Whisper AI Transcriber", "https://myvideosummarizer-g5xpetuztm8zfowruaeutm.streamlit.app")
    st.link_button("🩺 Heart Failure Risk", "https://heartfailure-gaufwbwfmh2j2u8ytzfmm5.streamlit.app")

    st.markdown('<span class="hub-section-badge">⚙️ Basic Utilities & Training</span>', unsafe_allow_html=True)
    st.link_button("🛠️ AI Super Tool", "https://ai-super-tool-uxhxpvn4lqyc7szmsdqtl8.streamlit.app")
    st.link_button("🖼️ Photo Background Changer", "https://photo-bg-changer-kdrxyvhjx3ibr4ccoddm3f.streamlit.app")
    st.link_button("🌡️ Temperature Forecasting App", "https://temperature-forecasting-app-9ffwo5g3we4onfokxpca4g.streamlit.app/") 
    st.link_button("📱 Generated QR Code", "https://generatedqrcode-o4c9u7iprbc9bzkqrxqu4j.streamlit.app/") 
    st.link_button("📝 MS Office Training", "https://ms-office-training-zokxafpvnvpaoyxjyz5vtk.streamlit.app/") 

# 5. Professional Honors Component
st.markdown('<div class="hub-column-title">🏆 Honors & Recognition</div>', unsafe_allow_html=True)
st.success("🥉 **Kaggle Bronze Medal** - Santa 2024: The Perplexity Permutation Puzzle")
st.success("🥉 **Kaggle Bronze Medal** - Predict Podcast Listening Time Challenge")
st.info("🎓 **ISRO / IIRS Certification** - AI/ML for Geodata Analysis (September 2024)")

# 6. Self-Generating Master QR Engine Component
st.markdown('<div class="hub-column-title">📱 Master Ecosystem Link</div>', unsafe_allow_html=True)

# Update this placeholder URL string with your new live app link once Streamlit initializes!
master_url = "https://fintech-genai-portfolio-hocbgkk7tkd2wwcgvehgre.streamlit.app/"

qr_engine = qrcode.QRCode(version=1, box_size=10, border=1)
qr_engine.add_data(master_url)
qr_engine.make(fit=True)
qr_img = qr_engine.make_image(fill_color="#0f172a", back_color="#ffffff")

# Build image formatting streams
buf = BytesIO()
qr_img.save(buf, format="PNG")
img_data = buf.getvalue()

display_col1, display_col2 = st.columns(2)
with display_col1:
    st.image(img_data, width=150, caption="Scan to open this hub")
with display_col2:
    st.download_button(label="📥 Save Master QR Image", data=img_data, file_name="srinivas_hub_qr.png", mime="image/png")
