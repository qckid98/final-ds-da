import streamlit as st

def show():
    st.markdown("<div class='page-title'>🤖 About Data Alchemist</div>", unsafe_allow_html=True)
    
    # Team Information Card
    st.markdown("""
    <div class='info-box'>
        <h3>🚀 Data Alchemist Team</h3>
        <p>Tim spesialis data yang mengubah data mentah menjadi insights berharga dengan kekuatan Machine Learning dan analitik canggih.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🎯 Our Mission
        Menghadirkan solusi Machine Learning yang accessible dan powerful untuk membantu bisnis memahami audiens mereka dengan lebih baik melalui analisis data yang mendalam dan prediksi yang akurat.
        
        ### 🔧 Technology Stack
        - **📊 Machine Learning** - Advanced algorithms dan predictive modeling
        - **📈 Data Processing** - Real-time data processing pipelines
        - **🎨 Data Visualization** - Interactive dashboard dengan modern visualization
        - **☁️ Cloud Infrastructure** - Scalable and reliable cloud architecture
        - **🔒 Security** - End-to-end encryption dan privacy protection
        """)
        
        st.markdown("""
        ### 👥 Meet The Data Alchemists
        Tim profesional yang berdedikasi dalam mengubah data menjadi solusi bisnis yang bernilai.
        """)
        
        # Team members in a grid
        team_col1, team_col2 = st.columns(2)
        
        with team_col1:
            st.markdown("""
            <div class='prediction-card' style='margin-bottom: 15px;'>
                <h4>👑 Ivan Febriand Muhammad</h4>
                <p><strong>Team Leader</strong></p>
                <p>Creating a model</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='prediction-card' style='margin-bottom: 15px;'>
                <h4>🔮 Juan Javier</h4>
                <p><strong>Data Scientist</strong></p>
                <p>UI/UX Specialist</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='prediction-card' style='margin-bottom: 15px;'>
                <h4>📊 Muhammad Naufal Rahmatullah</h4>
                <p><strong>Data Scientist</strong></p>
                <p>Creating EDA/p>
            </div>
            """, unsafe_allow_html=True)
        
        with team_col2:
            st.markdown("""
            <div class='prediction-card' style='margin-bottom: 15px;'>
                <h4>⚡ Rizki Insyani</h4>
                <p><strong>Data Scientist</strong></p>
                <p>Data Preprocessing</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='prediction-card' style='margin-bottom: 15px;'>
                <h4>🎨 Susiana Febriyanti Muqaromah</h4>
                <p><strong>Data Scientist</strong></p>
                <p>Feature Engineering</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='prediction-card' style='margin-bottom: 15px;'>
                <h4>🔍 Tika Iswari Larasati</h4>
                <p><strong>Data Scientist</strong></p>
                <p>Deployment Stage and helping streamlit</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        # Juan Javier Profile Card
        st.markdown("""
        <div class='prediction-card'>
            <div style="text-align: center; margin: 10px 0 20px 0;">
                <div style="width: 80px; height: 80px; border-radius: 50%; background: linear-gradient(135deg, #3b82f6, #1d4ed8); display: flex; align-items: center; justify-content: center; font-size: 2rem; margin: 0 auto;">
                    👨‍💻
                </div>
                <h3 style="margin: 15px 0 5px 0;">Juan Javier</h3>
                <p style="color: #10b981; font-weight: bold; margin: 0;">Junior Data Scientist</p>
            </div>
            <div style="background: rgba(59, 130, 246, 0.1); padding: 12px; border-radius: 8px; margin: 15px 0;">
                <p style="margin: 0; text-align: center; font-style: italic; font-size: 0.9rem;">
                    "Turning data into decisions through machine learning"
                </p>
            </div>
            <div style="display: grid; gap: 8px; margin-top: 15px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span>📧</span>
                    <span style="font-size: 0.9rem;">juan.javier@dataalchemist.com</span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span>🔗</span>
                    <span style="font-size: 0.9rem;">github.com/juanjavier</span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span>💼</span>
                    <span style="font-size: 0.9rem;">linkedin.com/in/juanjavier</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # System Specifications
        st.markdown("""
        <div class='prediction-card'>
            <h4>📈 System Specifications</h4>
            <div style="display: grid; gap: 12px; margin-top: 15px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span>🤖 ML Model:</span>
                    <span style="color: #10b981; font-weight: bold;">Advanced</span>
                </div>
                <div style="height: 6px; background: #334155; border-radius: 3px; overflow: hidden;">
                    <div style="height: 100%; width: 85%; background: #10b981;"></div>
                </div>
                
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span>⚡ Processing:</span>
                    <span style="color: #3b82f6; font-weight: bold;">Real-time</span>
                </div>
                <div style="height: 6px; background: #334155; border-radius: 3px; overflow: hidden;">
                    <div style="height: 100%; width: 92%; background: #3b82f6;"></div>
                </div>
                
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span>📊 Accuracy:</span>
                    <span style="color: #f59e0b; font-weight: bold;">95.2%</span>
                </div>
                <div style="height: 6px; background: #334155; border-radius: 3px; overflow: hidden;">
                    <div style="height: 100%; width: 95%; background: #f59e0b;"></div>
                </div>
                
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span>🔧 Status:</span>
                    <span style="color: #10b981; font-weight: bold;">🟢 Operational</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Contact Information
        st.markdown("""
        <div class='prediction-card'>
            <h4>📞 Contact Team</h4>
            <div style="display: grid; gap: 10px; margin-top: 15px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span>📧</span>
                    <span style="font-size: 0.9rem;">team@dataalchemist.com</span>
                </div>
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span>🔗</span>
                    <span style="font-size: 0.9rem;">dataalchemist.github.io</span>
                </div>
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span>💼</span>
                    <span style="font-size: 0.9rem;">linkedin.com/company/data-alchemist</span>
                </div>
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span>🐦</span>
                    <span style="font-size: 0.9rem;">@data_alchemist</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Project Statistics
    st.markdown("---")
    st.markdown("<div class='page-title'>📊 Project Statistics</div>", unsafe_allow_html=True)
    
    stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)
    
    with stats_col1:
        st.markdown("""
        <div class='prediction-card' style='text-align: center; height: 120px;'>
            <h3>🚀 15+</h3>
            <p>Projects Completed</p>
        </div>
        """, unsafe_allow_html=True)
    
    with stats_col2:
        st.markdown("""
        <div class='prediction-card' style='text-align: center; height: 120px;'>
            <h3>💼 12</h3>
            <p>Happy Clients</p>
        </div>
        """, unsafe_allow_html=True)
    
    with stats_col3:
        st.markdown("""
        <div class='prediction-card' style='text-align: center; height: 120px;'>
            <h3>📈 95.2%</h3>
            <p>Success Rate</p>
        </div>
        """, unsafe_allow_html=True)
    
    with stats_col4:
        st.markdown("""
        <div class='prediction-card' style='text-align: center; height: 120px;'>
            <h3>⏱️ 2.1s</h3>
            <p>Avg Response Time</p>
        </div>
        """, unsafe_allow_html=True)