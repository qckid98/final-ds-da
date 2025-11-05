import streamlit as st

# ========== PAGE CONFIGURATION ========== #
st.set_page_config(
    page_title="Social Media Engagement Dataset",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== MODERN BLUE-BLACK THEME ========== #
st.markdown("""
<style>
/* Reset default Streamlit - BACKGROUND GRADIENT */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
    color: #ffffff !important;
}

/* Main container styling */
.main .block-container {
    padding-top: 2rem;
}

/* Sidebar styling - DARK BLUE THEME */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #1e40af 100%) !important;
    border-right: 1px solid #334155;
}

[data-testid="stSidebar"] .stButton button {
    background: rgba(255, 255, 255, 0.1) !important;
    color: white !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 12px !important;
    padding: 12px 20px !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
    backdrop-filter: blur(10px);
    margin: 5px 0;
}

[data-testid="stSidebar"] .stButton button:hover {
    background: rgba(255, 255, 255, 0.2) !important;
    transform: translateX(8px) !important;
    border-color: #60a5fa !important;
    box-shadow: 0 4px 15px rgba(96, 165, 250, 0.3) !important;
}

/* Header title - MODERN GRADIENT */
.main-title {
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 50%, #1d4ed8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    margin-bottom: 1rem;
    text-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.page-title {
    font-size: 2.2rem;
    font-weight: 700;
    background: linear-gradient(135deg, #93c5fd 0%, #60a5fa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1.5rem;
    position: relative;
}

.page-title::after {
    content: '';
    position: absolute;
    bottom: -8px;
    left: 0;
    width: 60px;
    height: 3px;
    background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
    border-radius: 2px;
}

/* Subtext - LIGHT BLUE */
.subtext {
    font-size: 1.1rem;
    color: #cbd5e1 !important;
    margin-bottom: 2rem;
    text-align: center;
    line-height: 1.6;
}

/* FIX: Container untuk kolom - pastikan tinggi sama */
[data-testid="column"] {
    display: flex !important;
}

/* Modern Card Design */
.card {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.9) 100%);
    border: 1px solid #334155;
    border-radius: 20px;
    padding: 30px 25px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    height: 280px !important;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    backdrop-filter: blur(10px);
    position: relative;
    overflow: hidden;
}

.card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
}

.card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 40px rgba(59, 130, 246, 0.3);
    border-color: #60a5fa;
}

/* Card title - WHITE */
.card h4 {
    color: #ffffff !important;
    font-weight: 700;
    margin: 0 0 20px 0 !important;
    padding: 0 !important;
    font-size: 1.4rem !important;
    line-height: 1.3 !important;
    height: auto !important;
    display: flex;
    align-items: center;
    gap: 10px;
}

.card h4::before {
    font-size: 1.6rem;
}

/* Paragraph in card - LIGHT BLUE */
.card p {
    color: #cbd5e1 !important;
    font-size: 1rem !important;
    line-height: 1.6 !important;
    margin: 0 !important;
    padding: 0 !important;
    text-align: left;
}

/* MEMASTIKAN TINGGI KOLUM SAMA */
div[data-testid="column"] > div {
    height: 100%;
}

/* Prediction card style - DARK THEME */
.prediction-card {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.95) 0%, rgba(15, 23, 42, 0.95) 100%);
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 30px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    margin-bottom: 25px;
    backdrop-filter: blur(10px);
    position: relative;
}

.prediction-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    border-radius: 16px 16px 0 0;
}

.prediction-card, .prediction-card * {
    color: #ffffff !important;
}

/* Success message - MODERN GREEN */
.success-box {
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    color: white !important;
    padding: 25px;
    border-radius: 16px;
    margin: 20px 0;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 8px 32px rgba(16, 185, 129, 0.3);
    backdrop-filter: blur(10px);
}

.success-box, .success-box * {
    color: white !important;
    font-weight: 600;
}

/* Info box - MODERN BLUE */
.info-box {
    background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
    color: white !important;
    padding: 25px;
    border-radius: 16px;
    margin: 20px 0;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 8px 32px rgba(59, 130, 246, 0.3);
    backdrop-filter: blur(10px);
}

.info-box, .info-box * {
    color: white !important;
    font-weight: 600;
}

/* Footer text */
footer {
    visibility: hidden;
}

/* Tab styling - DARK THEME */
[data-testid="stTabs"] {
    background: rgba(15, 23, 42, 0.9);
    border-radius: 16px;
    padding: 8px;
    color: #ffffff !important;
    border: 1px solid #334155;
    backdrop-filter: blur(10px);
}

[data-testid="stTabs"] [data-baseweb="tab"] {
    color: #cbd5e1 !important;
    font-weight: 600;
    padding: 12px 24px;
    border-radius: 12px;
    transition: all 0.3s ease;
}

[data-testid="stTabs"] [data-baseweb="tab"][aria-selected="true"] {
    background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
    color: white !important;
}

/* Button styling - MODERN GRADIENT */
.stButton button {
    background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 28px !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    position: relative;
    overflow: hidden;
}

.stButton button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.5s;
}

.stButton button:hover::before {
    left: 100%;
}

.stButton button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 25px rgba(59, 130, 246, 0.5) !important;
}

/* ========== INPUT FIELDS STYLING ========== */
/* Input fields - DARK THEME */
.stTextInput input, 
.stTextArea textarea, 
.stNumberInput input,
.stSelectbox select,
.stMultiSelect span {
    color: #ffffff !important;
    background-color: rgba(15, 23, 42, 0.8) !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
    padding: 12px 16px !important;
    backdrop-filter: blur(10px);
}

.stTextInput input:focus, 
.stTextArea textarea:focus, 
.stNumberInput input:focus {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2) !important;
}

/* Placeholder text */
.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #64748b !important;
}

/* Dataframe - DARK THEME */
.stDataFrame {
    background: rgba(15, 23, 42, 0.8) !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
    overflow: hidden;
}

.stDataFrame, .stDataFrame * {
    color: #ffffff !important;
}

/* Expander - DARK THEME */
.streamlit-expanderHeader {
    color: #ffffff !important;
    background: rgba(15, 23, 42, 0.8) !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
    padding: 15px 20px !important;
}

.streamlit-expanderContent {
    color: #cbd5e1 !important;
    background: rgba(15, 23, 42, 0.6) !important;
    border: 1px solid #334155 !important;
    border-radius: 0 0 12px 12px !important;
    padding: 20px !important;
}

/* Radio buttons - DARK THEME */
.stRadio label {
    color: #ffffff !important;
}

/* Checkbox - DARK THEME */
.stCheckbox label {
    color: #ffffff !important;
}

/* Selectbox - DARK THEME */
.stSelectbox label {
    color: #ffffff !important;
}

/* File uploader - DARK THEME */
.stFileUploader label {
    color: #ffffff !important;
}

/* Metric - DARK THEME */
[data-testid="stMetricLabel"], 
[data-testid="stMetricValue"], 
[data-testid="stMetricDelta"] {
    color: #ffffff !important;
}

/* JSON - DARK THEME */
.stJson {
    color: #ffffff !important;
    background: rgba(15, 23, 42, 0.8) !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
    padding: 15px !important;
}

/* Sidebar title styling */
[data-testid="stSidebar"] h1 {
    color: #ffffff !important;
    text-align: center;
    margin-bottom: 2rem;
    font-size: 1.8rem;
    font-weight: 700;
}

[data-testid="stSidebar"] .stSubheader {
    color: #cbd5e1 !important;
}

[data-testid="stSidebar"] .stInfo {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 12px;
    color: #ffffff !important;
}

/* Footer styling */
.footer {
    text-align: center;
    color: #64748b !important;
    margin-top: 3rem;
    padding: 1rem;
    border-top: 1px solid #334155;
}

/* Decorative elements */
.decorative-circle {
    position: absolute;
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(59, 130, 246, 0.1) 0%, transparent 70%);
    pointer-events: none;
}

/* Team section styling */
.team-section {
    margin: 2rem 0;
}

.team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-top: 1rem;
}

</style>
""", unsafe_allow_html=True)

# ========== INITIALIZE SESSION STATE ========== #
if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"

# ========== SIDEBAR NAVIGATION ========== #
with st.sidebar:
    st.markdown("<h1>🚀 Navigation</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Navigation buttons dengan style yang konsisten
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🏠", use_container_width=True, key="home_btn"):
            st.session_state.current_page = "home"
        st.caption("Home")
    
    with col2:
        if st.button("🔮", use_container_width=True, key="prediction_btn"):
            st.session_state.current_page = "prediction"
        st.caption("Prediction")
    
    with col3:
        if st.button("ℹ️", use_container_width=True, key="about_btn"):
            st.session_state.current_page = "about"
        st.caption("About")
    
    st.markdown("---")
    
    # Informasi tambahan
    st.subheader("📊 Informasi")
    st.info("Dashboard ini menggunakan model Machine Learning canggih untuk memprediksi engagement media sosial dengan akurasi tinggi.")
    
    st.markdown("---")
    
    # Status indicator
    st.markdown("### 🟢 System Status")
    st.progress(85, text="Model Performance: 85%")
    
    st.markdown("---")
    
    # Team Members Section in Sidebar
    st.markdown("### 👥 Data Alchemist Members")
    st.markdown("**👑 Ivan Febriand Muhammad**  \n*Team Leader*")
    st.markdown("**🔮 Juan Javier**  \n*Data Scientist*")
    st.markdown("**📊 Muhammad Naufal Rahmatullah**  \n*Data Scientist*")
    st.markdown("**⚡ Rizki Insyani**  \n*Data Scientist*")
    st.markdown("**🎨 Susiana Febriyanti Muqaromah**  \n*Data Scientist*")
    st.markdown("**🔍 Tika Iswari Larasati**  \n*Data Scientist*")
    
    st.markdown("---")
    st.caption("🚀 Developed by **Data Alchemist Team**")

# ========== PAGE ROUTING ========== #
if st.session_state.current_page == "home":
    import home
    home.show()
elif st.session_state.current_page == "prediction":
    import prediction
    prediction.show()
elif st.session_state.current_page == "about":
    import about
    about.show()

# ========== TEAM SECTION IN MAIN APP ========== #
st.markdown("---")
st.markdown("<div class='page-title'>👥 Meet Our Data Alchemist Team</div>", unsafe_allow_html=True)

# Team members grid
col1, col2 = st.columns(2)

with col1:
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
        <p>Creating EDA</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
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

# ========== FOOTER ========== #
st.markdown("---")
st.markdown("""
<div class="footer">
    <p>© 2025 | Social Media Analytics Dashboard by <strong>Data Alchemist Team</strong></p>
</div>
""", unsafe_allow_html=True)

# ========== DECORATIVE ELEMENTS ========== #
st.markdown("""
<div class="decorative-circle" style="top: 10%; right: 5%;"></div>
<div class="decorative-circle" style="bottom: 20%; left: 3%; width: 150px; height: 150px;"></div>
""", unsafe_allow_html=True)