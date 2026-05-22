import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# 1. Page Configuration for Mobile Responsiveness
st.set_page_config(
    page_title="Srinivas Tanakala | Digital Card",
    page_icon="💼",
    layout="centered"
)

# 2. Custom CSS to style the Profile Card & UI Buttons
st.markdown("""
    <style>
    .main-card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin-bottom: 25px;
    }
    .profile-name { color: #0f172a; font-size: 28px; font-weight: 700; margin-bottom: 4px; }
    .profile-subtitle { color: #1e3a8a; font-size: 15px; font-weight: 600; margin-bottom: 2px; }
    .profile-location { color: #64748b; font-size: 13px; margin-bottom: 15px; }
    .column-title {
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
    .section-badge {
        font-size: 12px;
        color: #475569;
        font-weight: 700;
        margin-top: 12px;
        margin-bottom: 6px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        background-color: #f8fafc;
        padding: 4px 8px;
        border-radius: 4px;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Profile Header Block
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown('<div class="profile-name">Appala Srinivas Tanakala</div>', unsafe_allow_html=True)
st.markdown('<div class="profile-subtitle">Strategic Financial Leader & AI-Augmented Data Scientist</div>', unsafe_allow_html=True)
st.markdown('<div class="profile-location">📍 Visakhapatnam, Andhra Pradesh, India</div>', unsafe_allow_html=True)

# Quick Contact Buttons
c1, c2, c3 = st.columns(3)
with c1:
    st.link_button("📞 Call Me", "tel:+918897415303", use_container_width=True)
with c2:
    st.link_button("✉️ Email", "mailto:tasrinivass@gmail.com", use_container_width=True)
with c3:
    st.link_button("🤝 LinkedIn", "https://linkedin.com", use_container_width=True)

# Portfolio Profiles
p1, p2 = st.columns(2)
with p1:
    st.link_button("💻 GitHub Portfolio", "https://github.com", use_container_width=True)
with p2:
    st.link_button("🥇 Kaggle Profile", "https://kaggle.com", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 4. Two-Column Layout for All 24 Web Applications
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="column-title">🏢 FinTech & BI</div>', unsafe_allow_html=True)
    
    st.markdown('<span class="section-badge">📈 Production Platforms</span>', unsafe_allow_html=True)
    st.link_button("📈 TransitionControl", "https://streamlit.app", use_container_width=True)
    st.link_button("💰 CapitalVantage Auditor", "https://streamlit.app", use_container_width=True)
    st.link_button("💳 CreditPulse-AI", "https://streamlit.app", use_container_width=True)
    st.link_button("🏗️ Moder 4C\'s Engine", "https://streamlit.app", use_container_width=True)

    st.markdown('<span class="section-badge">📊 Analytics & Dashboards</span>', unsafe_allow_html=True)
    st.link_button("📊 Real-time Sales Dashboard", "https://streamlit.app", use_container_width=True)
    st.link_button("🏢 ConstructAI Dashboard", "https://streamlit.app", use_container_width=True)
    st.link_button("🔮 Quantum AI Crypto", "https://streamlit.app", use_container_width=True)
    st.link_button("💹 Multi-Stock Predictor", "https://streamlit.app", use_container_width=True)
    st.link_button("📊 Stock Analysis Combo", "https://streamlit.app", use_container_width=True)

    st.markdown('<span class="section-badge">⚙️ Automation & Pipelines</span>', unsafe_allow_html=True)
    st.link_button("🧪 Fintech Regression Automation", "https://streamlit.app", use_container_width=True)
    st.link_button("🛰️ Etihad Telemetry Pipeline", "https://streamlit.app", use_container_width=True)

with col2:
    st.markdown('<div class="column-title">🧠 GenAI & Operations</div>', unsafe_allow_html=True)
    
    st.markdown('<span class="section-badge">⭐ Advanced GenAI Platforms</span>', unsafe_allow_html=True)
    st.link_button("💼 AI Recruiter", "https://streamlit.app", use_container_width=True)
    st.link_button("🤖 Multi-Agent Chatbot", "https://streamlit.app", use_container_width=True)
    st.link_button("🎨 Gemini AI Image Generator", "https://streamlit.app", use_container_width=True)

    st.markdown('<span class="section-badge">📊 Specialized Tools</span>', unsafe_allow_html=True)
    st.link_button("🍲 Smart Bhojan: Nutrition AI", "https://streamlit.app", use_container_width=True)
    st.link_button("🎥 YouTube Summarizer", "https://streamlit.app", use_container_width=True)
    st.link_button("🎤 Whisper AI Transcriber", "https://streamlit.app", use_container_width=True)
    st.link_button("🩺 Heart Failure Risk", "https://streamlit.app", use_container_width=True)

    st.markdown('<span class="section-badge">⚙️ Utilities & Training</span>', unsafe_allow_html=True)
    st.link_button("🛠️ AI Super Tool", "https://streamlit.app", use_container_width=True)
    st.link_button("🖼️ Photo Background Changer", "https://streamlit.app", use_container_width=True)
    st.link_button("🌡️ Temperature Forecasting App", "https://streamlit.app", use_container_width=True)
    st.link_button("📱 Generated QR Code", "https://streamlit.app", use_container_width=True)
    st.link_button("📝 MS Office Training", "https://streamlit.app", use_container_width=True)

# 5. Honors & Recognition Section
st.markdown('<div class="column-title">🏆 Honors & Recognition</div>', unsafe_allow_html=True)
st.success("🥉 **Bronze Medal** - Santa 2024: The Perplexity Permutation Puzzle (Kaggle)")
st.success("🥉 **Bronze Medal** - Predict Podcast Listening Time Challenge (Kaggle)")
st.info("🎓 **AI/ML for Geodata Analysis Certification** - Issued by IIRS / ISRO (September 2024)")

# 6. Live Automated Master QR Generator Engine
st.markdown('<div class="column-title">📱 Share My Digital Card</div>', unsafe_allow_html=True)

# OPTIONAL: Once you get your final card URL from Streamlit Cloud, replace the link below!
live_card_url = "https://linkedin.com"

qr = qrcode.QRCode(version=1, box_size=10, border=2)
qr.add_data(live_card_url)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="#1e3a8a", back_color="#ffffff")

# Render image layout
buf = BytesIO()
qr_img.save(buf, format="PNG")
byte_im = buf.getvalue()

q_col1, q_col2 = st.columns([1, 2])
with q_col1:
    st.image(byte_im, width=150)
with q_col2:
    st.write("Open this card on your laptop or smartphone screen during professional networking events. Anyone can scan this code to load your entire application portfolio instantly.")
    st.download_button(label="📥 Download QR Code Image", data=byte_im, file_name="srinivas_card_qr.png", mime="image/png")
