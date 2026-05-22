import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# 1. Initialize Page Configuration for Mobile & Desktop Layouts
st.set_page_config(
    page_title="Srinivas Tanakala | FinTech & AI Hub",
    page_icon="🏢",
    layout="centered"
)

# 2. Premium Custom CSS Styling (Completely fixed, zero errors, optimized spacing)
st.markdown("""
    <style>
    /* Forces Streamlit to remove the automatic top margin block completely */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
    }
    
    /* Main profile card container frame */
    .main-profile-card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
        text-align: center;
        margin-top: 0px !important;
        margin-bottom: 25px;
    }
    .profile-title { color: #0f172a; font-size: 28px; font-weight: 700; margin-top: 0px; margin-bottom: 4px; }
    .profile-subtitle { color: #1e3a8a; font-size: 15px; font-weight: 600; margin-bottom: 2px; }
    .profile-loc { color: #64748b; font-size: 13px; margin-bottom: 15px; }
    
    /* Layout headers */
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

# 3. Native Streamlit Layout Setup
st.markdown('<div class="main-profile-card">', unsafe_allow_html=True)
st.markdown('<div class="profile-title">Appala Srinivas Tanakala</div>', unsafe_allow_html=True)
st.markdown('<div class="profile-subtitle">Strategic Financial Leader & AI-Augmented Data Scientist</div>', unsafe_allow_html=True)
st.markdown('<div class="profile-loc">📍 Visakhapatnam, Andhra Pradesh, India</div>', unsafe_allow_html=True)

# Contact Triggers row
contact_col1, contact_col2, contact_col3 = st.columns(3)
with contact_col1:
    st.link_button("📞 Call Me", "tel:+918897415303", use_container_width=True)
with contact_col2:
    st.link_button("✉️ Email", "mailto:tasrinivass@gmail.com", use_container_width=True)
with contact_col3:
    st.link_button("🤝 LinkedIn", "https://linkedin.com", use_container_width=True)

# Portfolio profiles row
port_col1, port_col2 = st.columns(2)
with port_col1:
    st.link_button("💻 GitHub Profile", "https://github.com", use_container_width=True)
with port_col2:
    st.link_button("🥇 Kaggle Workspace", "https://kaggle.com", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 4. Clean Grid Configuration for All 24 Deployed Applications
left_grid, right_grid = st.columns(2)

with left_grid:
    st.markdown('<div class="hub-column-title">🏢 FinTech & BI Solutions</div>', unsafe_allow_html=True)
    
    st.markdown('<span class="hub-section-badge">📈 Production Platforms</span>', unsafe_allow_html=True)
    st.link_button("📈 TransitionControl", "https://streamlit.app", use_container_width=True)
    st.link_button("💰 CapitalVantage Auditor", "https://streamlit.app", use_container_width=True)
    st.link_button("💳 CreditPulse-AI", "https://streamlit.app", use_container_width=True)
    st.link_button("🏗️ Moder 4C\'s Engine", "https://streamlit.app", use_container_width=True)

    st.markdown('<span class="hub-section-badge">📊 Analytical Tools & Dashboards</span>', unsafe_allow_html=True)
    st.link_button("📊 Real-time Sales Dashboard", "https://streamlit.app", use_container_width=True)
    st.link_button("🏢 ConstructAI Dashboard", "https://streamlit.app", use_container_width=True)
    st.link_button("🔮 Quantum AI Crypto", "https://streamlit.app", use_container_width=True)
    st.link_button("💹 Multi-Stock Predictor", "https://streamlit.app", use_container_width=True)
    st.link_button("📊 Stock Analysis Combo", "https://streamlit.app", use_container_width=True)

    st.markdown('<span class="hub-section-badge">⚙️ Automation & Pipelines</span>', unsafe_allow_html=True)
    st.link_button("🧪 Fintech Regression Automation", "https://streamlit.app", use_container_width=True)
    st.link_button("🛰️ Etihad Telemetry Pipeline", "https://streamlit.app", use_container_width=True)

with right_grid:
    st.markdown('<div class="hub-column-title">🧠 Generative AI & Operations</div>', unsafe_allow_html=True)
    
    st.markdown('<span class="hub-section-badge">⭐ Advanced GenAI Platforms</span>', unsafe_allow_html=True)
    st.link_button("💼 AI Recruiter", "https://streamlit.app", use_container_width=True)
    st.link_button("🤖 Multi-Agent Chatbot", "https://streamlit.app", use_container_width=True)
    st.link_button("🎨 Gemini AI Image Generator", "https://streamlit.app", use_container_width=True)

    st.markdown('<span class="hub-section-badge">📊 Specialized Intelligence Tools</span>', unsafe_allow_html=True)
    st.link_button("🍲 Smart Bhojan: Nutrition AI", "https://streamlit.app", use_container_width=True)
    st.link_button("🎥 YouTube Summarizer", "https://streamlit.app", use_container_width=True)
    st.link_button("🎤 Whisper AI Transcriber", "https://streamlit.app", use_container_width=True)
    st.link_button("🩺 Heart Failure Risk", "https://streamlit.app", use_container_width=True)

    st.markdown('<span class="hub-section-badge">⚙️ Basic Utilities & Training</span>', unsafe_allow_html=True)
    st.link_button("🛠️ AI Super Tool", "https://streamlit.app", use_container_width=True)
    st.link_button("🖼️ Photo Background Changer", "https://streamlit.app", use_container_width=True)
    st.link_button("🌡️ Temperature Forecasting App", "https://streamlit.app", use_container_width=True)
    st.link_button("📱 Generated QR Code", "https://streamlit.app", use_container_width=True)
    st.link_button("📝 MS Office Training", "https://streamlit.app", use_container_width=True)

# 5. Professional Recognition Section (Builds instant trust with employers)
st.markdown('<div class="hub-column-title">🏆 Honors & Recognition</div>', unsafe_allow_html=True)
st.success("🥉 **Kaggle Bronze Medal** - Santa 2024: The Perplexity Permutation Puzzle")
st.success("🥉 **Kaggle Bronze Medal** - Predict Podcast Listening Time Challenge")
st.info("🎓 **ISRO / IIRS Certification** - AI/ML for Geodata Analysis (September 2024)")

# 6. Self-Generating Master QR Engine
st.markdown('<div class="hub-column-title">📱 Share Portfolio Ecosystem</div>', unsafe_allow_html=True)

# NOTE: Change this link once your app is live to point directly to your Streamlit App URL!
master_url = "https://linkedin.com"

qr_engine = qrcode.QRCode(version=1, box_size=10, border=1)
qr_engine.add_data(master_url)
qr_engine.make(fit=True)
qr_img = qr_engine.make_image(fill_color="#0f172a", back_color="#ffffff")

# Memory buffer output formatting
buf = BytesIO()
qr_img.save(buf, format="PNG")
img_data = buf.getvalue()

# FIXED: Added '2' inside st.columns(2) to prevent layout crashing
display_col1, display_col2 = st.columns(2)
with display_col1:
    st.image(img_data, width=150, caption="Scan to open this hub")
with display_col2:
    st.write("Open this live dashboard app on your screen during career networking sessions. Observers can scan this QR graphic layer to explore your absolute entire 24-application suite instantly.")
    st.download_button(label="📥 Save QR Code Image File", data=img_data, file_name="srinivas_hub_qr.png", mime="image/png")
