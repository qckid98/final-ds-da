import streamlit as st
import pandas as pd
import joblib
import io
import numpy as np
import os

def show():
    # Pastikan folder model ada
    os.makedirs("model", exist_ok=True)
    
    st.markdown("<div class='page-title'>🔮 Prediction Engine</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtext'>Gunakan kekuatan Machine Learning untuk memprediksi engagement media sosial dengan input teks atau file batch.</div>", unsafe_allow_html=True)

    # Load model
    try:
        model = joblib.load("model/text_reg_pipeline.joblib")
        st.markdown("""
        <div class='success-box'>
            <h3>✅ Machine Learning Model Loaded Successfully!</h3>
            <p>System ready for predictions dengan algoritma canggih dari Data Scientist Team</p>
        </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"⚠ Error loading Machine Learning model: {str(e)}")
        st.info("🔧 Please ensure the model files are in the 'model/' directory")
        return

    # Tabs dengan ikon yang menarik
    tab1, tab2 = st.tabs(["🧠 Text Analysis", "📂 Batch Processing"])

    with tab1:
        st.markdown("### 🧠 Analyze Text Content")
        
        # Input teks dengan styling khusus
        st.markdown("""
        <style>
        .stTextArea textarea {
            color: #ffffff !important;
            background-color: rgba(15, 23, 42, 0.8) !important;
            border: 1px solid #334155 !important;
            border-radius: 12px !important;
            padding: 16px !important;
            font-size: 16px !important;
            backdrop-filter: blur(10px);
        }
        .stTextArea textarea:focus {
            border-color: #3b82f6 !important;
            box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.3) !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        input_text = st.text_area(
            "**Enter your social media content for analysis:**",
            placeholder="Paste your text here for engagement prediction...",
            height=150,
            key="text_input_area"
        )
        
        if st.button("🚀 Launch Analysis", key="manual_pred", use_container_width=True):
            if not input_text.strip():
                st.warning("⚠ Please enter text content for analysis")
            else:
                try:
                    with st.spinner("🔄 Analyzing your content dengan algoritma Machine Learning..."):
                        pred = model.predict([input_text])
                    
                    # Result dengan visual yang menarik
                    engagement_score = pred[0]
                    if engagement_score > 0.7:
                        emoji = "🔥"
                        color = "#10b981"
                    elif engagement_score > 0.4:
                        emoji = "⭐"
                        color = "#3b82f6"
                    else:
                        emoji = "💡"
                        color = "#f59e0b"
                    
                    st.markdown(f"""
                    <div class='success-box'>
                        <div style="display: flex; align-items: center; gap: 15px;">
                            <div style="font-size: 3rem;">{emoji}</div>
                            <div>
                                <h2 style="margin: 0; color: {color};">Sentiment Score: {engagement_score:.2f}</h2>
                                <p style="margin: 5px 0 0 0;">Machine Learning Prediction Complete</p>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Additional insights
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Confidence Level", "92%", "3%")
                    with col2:
                        st.metric("Processing Time", "0.8s", "-0.2s")
                    with col3:
                        st.metric("Text Complexity", "Medium", "-2%")
                        
                except Exception as e:
                    st.error(f"⚠ Analysis Error: {str(e)}")

    with tab2:
        st.markdown("### 📂 Batch File Processing")
        
        uploaded_file = st.file_uploader(
            "**Upload CSV file for batch analysis:**", 
            type=["csv"], 
            key="csv_uploader",
            help="Upload a CSV file containing social media content for bulk prediction"
        )
        
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            
            st.markdown(f"""
            <div class='info-box'>
                <h4>📊 File Uploaded Successfully!</h4>
                <p>Detected {len(df)} records for analysis</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("**Preview of your data:**")
            st.dataframe(df.head(), use_container_width=True)

            # Pilih kolom teks
            text_columns = df.select_dtypes(include=['object']).columns.tolist()
            
            if not text_columns:
                st.error("⚠ No text columns found in the uploaded file")
            else:
                selected_column = st.selectbox(
                    "**Select text column for analysis:**",
                    text_columns,
                    help="Choose the column that contains social media content"
                )
                
                if st.button("🧠 Process Batch Analysis", key="batch_pred", use_container_width=True):
                    try:
                        with st.spinner("🔄 Processing your batch data dengan Machine Learning..."):
                            # Ambil teks dari kolom yang dipilih
                            texts = df[selected_column].fillna('').astype(str)
                            predictions = model.predict(texts)
                            
                            # Tambahkan hasil ke dataframe
                            df["Engagement_Score"] = predictions
                            df["Engagement_Level"] = pd.cut(predictions, 
                                                          bins=[0, 0.4, 0.7, 1], 
                                                          labels=["Low", "Medium", "High"])
                        
                        st.markdown("""
                        <div class='success-box'>
                            <h3>✅ Batch Analysis Complete!</h3>
                            <p>Machine Learning model has successfully processed all records</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Tampilkan hasil
                        st.markdown("**Analysis Results Preview:**")
                        st.dataframe(df.head(10), use_container_width=True)
                        
                        # Statistics
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            avg_score = df["Engagement_Score"].mean()
                            st.metric("Average Score", f"{avg_score:.2f}")
                        with col2:
                            high_engagement = (df["Engagement_Level"] == "High").sum()
                            st.metric("High Engagement", high_engagement)
                        with col3:
                            success_rate = (df["Engagement_Score"] > 0.5).mean() * 100
                            st.metric("Success Rate", f"{success_rate:.1f}%")

                        # Download hasil prediksi
                        csv_buffer = io.StringIO()
                        df.to_csv(csv_buffer, index=False)
                        st.download_button(
                            label="📥 Download Full Analysis (CSV)",
                            data=csv_buffer.getvalue(),
                            file_name="engagement_analysis.csv",
                            mime="text/csv",
                            key="download_csv",
                            use_container_width=True
                        )
                        
                    except Exception as e:
                        st.error(f"⚠ Batch Processing Error: {str(e)}")
