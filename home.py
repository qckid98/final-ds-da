import streamlit as st

def show():
    st.markdown("<div class='main-title'>🚀 Social Media Engagement Analyzer</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtext'>Platform analisis canggih untuk menganalisis dan memprediksi engagement media sosial dengan teknologi Machine Learning terdepan oleh Data Alchemist Team.</div>", unsafe_allow_html=True)

    # Stats Overview
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class='prediction-card' style='text-align: center; height: 120px;'>
            <h3>📈 95%</h3>
            <p>Accuracy</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='prediction-card' style='text-align: center; height: 120px;'>
            <h3>⚡ 2.3s</h3>
            <p>Prediction Time</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='prediction-card' style='text-align: center; height: 120px;'>
            <h3>🔢 15+</h3>
            <p>Features</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class='prediction-card' style='text-align: center; height: 120px;'>
            <h3>🎯 99.9%</h3>
            <p>Uptime</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Main Features Cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='card'>
            <h4>📊 Advanced Analytics</h4>
            <p>Teknologi Machine Learning canggih untuk analisis engagement yang mendalam dan prediksi akurat real-time oleh Data Scientist Team.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='card'>
            <h4>📈 Real-time Dashboard</h4>
            <p>Monitor performa media sosial dengan dashboard interaktif yang menampilkan metrik penting secara live.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='card'>
            <h4>🎯 Smart Predictions</h4>
            <p>Prediksi engagement masa depan dengan algoritma canggih untuk optimisasi strategi konten.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Additional content
    st.markdown("<div class='page-title'>🚀 Getting Started</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class='info-box'>
            <h3>💡 Selamat Datang di Data Science Platform!</h3>
            <p>Platform ini menggabungkan kekuatan Machine Learning dengan analitik media sosial untuk memberikan insights yang belum pernah ada sebelumnya, dikembangkan oleh Juan Javier dan Data Scientist Team.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        ### 🎯 Fitur Unggulan
        - **📊 Advanced Prediction** - Prediksi engagement dengan akurasi tinggi
        - **📈 Real-time Analytics** - Analisis mendalam dengan visualisasi interaktif
        - **⚡ Batch Processing** - Proses data dalam skala besar dengan cepat
        - **🔒 Secure & Private** - Data Anda terlindungi dengan enkripsi end-to-end
        """)
        
        st.markdown("""
        ### 🚀 Mulai Sekarang
        1. Navigasi ke tab **Prediction**
        2. Input teks atau upload file CSV
        3. Dapatkan insights berbasis data instan
        """)
        
    with col2:
        st.markdown("""
        <div class='prediction-card' style='text-align: center;'>
            <h4>🎮 Quick Actions</h4>
            <br>
            <div style='display: grid; gap: 10px;'>
                <button style='background: linear-gradient(135deg, #3b82f6, #1d4ed8); color: white; border: none; padding: 12px; border-radius: 10px; cursor: pointer;'>📤 Upload Data</button>
                <button style='background: linear-gradient(135deg, #10b981, #059669); color: white; border: none; padding: 12px; border-radius: 10px; cursor: pointer;'>📊 View Reports</button>
                <button style='background: linear-gradient(135deg, #8b5cf6, #7c3aed); color: white; border: none; padding: 12px; border-radius: 10px; cursor: pointer;'>⚙️ Settings</button>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='prediction-card'>
            <h4>👨‍💻 UI Develop</h4>
            <div style="display: flex; align-items: center; gap: 15px; margin: 15px 0;">
                <div style="width: 60px; height: 60px; border-radius: 50%; background: linear-gradient(135deg, #3b82f6, #1d4ed8); display: flex; align-items: center; justify-content: center; font-size: 1.5rem;">
                    👨‍💻
                </div>
                <div>
                    <strong>Juan Javier</strong><br>
                    <span style="color: #cbd5e1; font-size: 0.9rem;">Junior Data Scientist</span>
                </div>
            </div>
            <p>Spesialis dalam Machine Learning dan analitik media sosial dengan pengalaman 5+ tahun.</p>
        </div>
        """, unsafe_allow_html=True)