# # # # import streamlit as st
# # # # import numpy as np
# # # # import pandas as pd
# # # # import joblib
# # # # import plotly.graph_objects as go
# # # # import plotly.express as px
# # # # import time

# # # # # --- PAGE CONFIGURATION ---
# # # # st.set_page_config(
# # # #     page_title="Boston Housing Price Predictor AI",
# # # #     page_icon="🏡",
# # # #     layout="wide",
# # # #     initial_sidebar_state="expanded"
# # # # )

# # # # # --- MODERN GLASSMORPHISM & ANIMATION STYLING ---
# # # # st.markdown("""
# # # # <style>
# # # #     @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700;800&display=swap');

# # # #     * {
# # # #         font-family: 'Plus Jakarta Sans', sans-serif;
# # # #     }

# # # #     /* Animated Gradient Background */
# # # #     .stApp {
# # # #         background: radial-gradient(circle at 10% 20%, rgba(18, 24, 38, 1) 0%, rgba(10, 14, 23, 1) 90.2%);
# # # #         color: #f1f5f9;
# # # #     }

# # # #     /* Glassmorphism Cards */
# # # #     .glass-card {
# # # #         background: rgba(255, 255, 255, 0.04);
# # # #         backdrop-filter: blur(16px);
# # # #         -webkit-backdrop-filter: blur(16px);
# # # #         border: 1px solid rgba(255, 255, 255, 0.08);
# # # #         border-radius: 20px;
# # # #         padding: 24px;
# # # #         margin-bottom: 24px;
# # # #         box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
# # # #         transition: transform 0.3s ease, border-color 0.3s ease;
# # # #     }

# # # #     .glass-card:hover {
# # # #         transform: translateY(-3px);
# # # #         border-color: rgba(99, 102, 241, 0.4);
# # # #     }

# # # #     /* Gradient Hero Text */
# # # #     .hero-title {
# # # #         font-size: 2.8rem;
# # # #         font-weight: 800;
# # # #         background: linear-gradient(135deg, #60a5fa 0%, #a855f7 50%, #ec4899 100%);
# # # #         -webkit-background-clip: text;
# # # #         -webkit-text-fill-color: transparent;
# # # #         margin-bottom: 8px;
# # # #     }

# # # #     .hero-subtitle {
# # # #         color: #94a3b8;
# # # #         font-size: 1.1rem;
# # # #         margin-bottom: 24px;
# # # #     }

# # # #     /* Prediction Result Box */
# # # #     .price-badge {
# # # #         background: linear-gradient(135deg, rgba(99, 102, 241, 0.2) 0%, rgba(168, 85, 247, 0.2) 100%);
# # # #         border: 1px solid rgba(168, 85, 247, 0.4);
# # # #         border-radius: 16px;
# # # #         padding: 20px;
# # # #         text-align: center;
# # # #         animation: pulse 2s infinite ease-in-out;
# # # #     }

# # # #     @keyframes pulse {
# # # #         0%, 100% { box-shadow: 0 0 20px rgba(168, 85, 247, 0.2); }
# # # #         50% { box-shadow: 0 0 35px rgba(168, 85, 247, 0.5); }
# # # #     }

# # # #     /* Sidebar Customization */
# # # #     section[data-testid="stSidebar"] {
# # # #         background: rgba(15, 23, 42, 0.75);
# # # #         backdrop-filter: blur(20px);
# # # #         border-right: 1px solid rgba(255, 255, 255, 0.06);
# # # #     }
# # # # </style>
# # # # """, unsafe_allow_html=True)

# # # # # --- LOAD TRAINED ARTIFACTS ---
# # # # @st.cache_resource
# # # # def load_artifacts():
# # # #     try:
# # # #         model = joblib.load('model.joblib')
# # # #         scaler = joblib.load('scaler.joblib')
# # # #         return model, scaler, True
# # # #     except Exception:
# # # #         # Fallback simulation if files aren't in working directory
# # # #         return None, None, False

# # # # model, scaler, artifacts_loaded = load_artifacts()

# # # # # --- HEADER SECTION ---
# # # # st.markdown('<div class="hero-title">Boston Housing Valuation AI</div>', unsafe_allow_html=True)
# # # # st.markdown('<div class="hero-subtitle">State-of-the-art predictive analytics powered by machine learning</div>', unsafe_allow_html=True)

# # # # if not artifacts_loaded:
# # # #     st.info("ℹ️ Running in demo mode (Place `model.joblib` and `scaler.joblib` in the project root directory for live inference).")

# # # # # --- SIDEBAR: INPUT FEATURES ---
# # # # st.sidebar.markdown("### 🎛️ Feature Parameters")
# # # # st.sidebar.caption("Adjust housing attributes to evaluate market value:")

# # # # tab1, tab2 = st.sidebar.tabs(["📍 Area & Environment", "🏠 Property Details"])

# # # # with tab1:
# # # #     crim = st.number_input("CRIM (Per capita crime rate)", min_value=0.0, max_value=100.0, value=0.2, step=0.05)
# # # #     zn = st.slider("ZN (Residential land zoned > 25k sq.ft %)", 0.0, 100.0, 12.5, 0.5)
# # # #     indus = st.slider("INDUS (Non-retail business acres %)", 0.0, 30.0, 7.8, 0.1)
# # # #     chas = st.selectbox("CHAS (Tract bounds Charles River?)", options=[0, 1], format_func=lambda x: "Yes (1)" if x == 1 else "No (0)")
# # # #     nox = st.slider("NOX (Nitric oxides ppm)", 0.3, 0.9, 0.53, 0.01)
# # # #     dis = st.slider("DIS (Distance to employment centres)", 1.0, 13.0, 3.8, 0.1)
# # # #     rad = st.slider("RAD (Highway accessibility index)", 1, 24, 4, 1)

# # # # with tab2:
# # # #     rm = st.slider("RM (Average rooms per dwelling)", 3.0, 9.0, 6.2, 0.1)
# # # #     age = st.slider("AGE (Owner-occupied units built pre-1940 %)", 0.0, 100.0, 65.0, 1.0)
# # # #     tax = st.slider("TAX (Full-value property-tax rate per $10k)", 180, 720, 310, 10)
# # # #     ptratio = st.slider("PTRATIO (Pupil-teacher ratio by town)", 12.0, 23.0, 18.4, 0.1)
# # # #     b = st.number_input("B (1000(Bk - 0.63)^2 proportion)", min_value=0.0, max_value=400.0, value=390.0, step=1.0)
# # # #     lstat = st.slider("LSTAT (% Lower status of population)", 1.0, 40.0, 12.5, 0.1)

# # # # # Package inputs into dataframe
# # # # input_data = pd.DataFrame([[
# # # #     crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat
# # # # ]], columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'])

# # # # # Baseline averages for normalization comparisons
# # # # dataset_averages = {
# # # #     'CRIM': 3.61, 'ZN': 11.36, 'INDUS': 11.13, 'CHAS': 0.069, 'NOX': 0.55,
# # # #     'RM': 6.28, 'AGE': 68.57, 'DIS': 3.79, 'RAD': 9.54, 'TAX': 408.23,
# # # #     'PTRATIO': 18.45, 'B': 356.67, 'LSTAT': 12.65
# # # # }

# # # # # --- PREDICTION COMPUTATION ---
# # # # if artifacts_loaded:
# # # #     scaled_features = scaler.transform(input_data)
# # # #     predicted_price = float(model.predict(scaled_features)[0])
# # # # else:
# # # #     # Deterministic heuristic fallback for visual demo
# # # #     predicted_price = max(5.0, (rm * 9.0) - (lstat * 0.6) - (crim * 0.4) - (ptratio * 0.8) + 10.0)

# # # # # --- MAIN DASHBOARD LAYOUT ---
# # # # col_left, col_right = st.columns([1.2, 2.0], gap="large")

# # # # with col_left:
# # # #     st.markdown('<div class="glass-card">', unsafe_allow_html=True)
# # # #     st.markdown("### 🏷️ Estimated Valuation")
    
# # # #     st.markdown(f"""
# # # #     <div class="price-badge">
# # # #         <span style="font-size: 0.95rem; color: #cbd5e1; text-transform: uppercase; letter-spacing: 1px;">Predicted Value (MEDV)</span>
# # # #         <h1 style="font-size: 2.7rem; margin: 8px 0; color: #38bdf8;">${predicted_price * 1000:,.2f}</h1>
# # # #         <span style="font-size: 0.85rem; color: #a78bfa;">Index score: {predicted_price:.2f} ($1,000s)</span>
# # # #     </div>
# # # #     """, unsafe_allow_html=True)

# # # #     # Key Indicator Metrics
# # # #     m1, m2 = st.columns(2)
# # # #     m1.metric("Rooms (RM)", f"{rm:.1f}", delta=f"{rm - dataset_averages['RM']:.1f} vs Avg")
# # # #     m2.metric("Socioeconomic (LSTAT)", f"{lstat:.1f}%", delta=f"{lstat - dataset_averages['LSTAT']:.1f}%", delta_color="inverse")
# # # #     st.markdown('</div>', unsafe_allow_html=True)

# # # #     # Gauge Chart
# # # #     fig_gauge = go.Figure(go.Indicator(
# # # #         mode="gauge+number",
# # # #         value=predicted_price,
# # # #         domain={'x': [0, 1], 'y': [0, 1]},
# # # #         title={'text': "Valuation Tier ($k)", 'font': {'size': 16, 'color': '#f8fafc'}},
# # # #         gauge={
# # # #             'axis': {'range': [0, 50], 'tickcolor': "#64748b"},
# # # #             'bar': {'color': "#8b5cf6"},
# # # #             'bgcolor': "rgba(255, 255, 255, 0.05)",
# # # #             'steps': [
# # # #                 {'range': [0, 20], 'color': 'rgba(239, 68, 68, 0.2)'},
# # # #                 {'range': [20, 35], 'color': 'rgba(234, 179, 8, 0.2)'},
# # # #                 {'range': [35, 50], 'color': 'rgba(34, 197, 94, 0.2)'}
# # # #             ]
# # # #         }
# # # #     ))
# # # #     fig_gauge.update_layout(
# # # #         paper_bgcolor='rgba(0,0,0,0)',
# # # #         plot_bgcolor='rgba(0,0,0,0)',
# # # #         font={'color': "#f8fafc"},
# # # #         height=240,
# # # #         margin=dict(l=20, r=20, t=30, b=10)
# # # #     )
# # # #     st.plotly_chart(fig_gauge, use_container_width=True)

# # # # with col_right:
# # # #     st.markdown('<div class="glass-card">', unsafe_allow_html=True)
# # # #     st.markdown("### 📊 Input Profile & Feature Visualizer")
    
# # # #     chart_tabs = st.tabs(["Radar Profile", "Relative Feature Deviation", "Raw Input Data"])

# # # #     # 1. Radar Profile
# # # #     with chart_tabs[0]:
# # # #         radar_categories = ['RM', 'DIS', 'PTRATIO', 'LSTAT', 'INDUS', 'NOX']
# # # #         # Normalize relative to benchmark
# # # #         input_norm = [
# # # #             (input_data['RM'].values[0] / 9.0) * 100,
# # # #             (input_data['DIS'].values[0] / 13.0) * 100,
# # # #             (input_data['PTRATIO'].values[0] / 23.0) * 100,
# # # #             (input_data['LSTAT'].values[0] / 40.0) * 100,
# # # #             (input_data['INDUS'].values[0] / 30.0) * 100,
# # # #             (input_data['NOX'].values[0] / 0.9) * 100
# # # #         ]
        
# # # #         fig_radar = go.Figure()
# # # #         fig_radar.add_trace(go.Scatterpolar(
# # # #             r=input_norm,
# # # #             theta=radar_categories,
# # # #             fill='toself',
# # # #             fillcolor='rgba(99, 102, 241, 0.3)',
# # # #             line=dict(color='#818cf8', width=2),
# # # #             name='Current Configuration'
# # # #         ))
# # # #         fig_radar.update_layout(
# # # #             polar=dict(
# # # #                 radialaxis=dict(visible=True, range=[0, 100], color="#94a3b8", gridcolor="rgba(255,255,255,0.1)"),
# # # #                 angularaxis=dict(color="#f8fafc", gridcolor="rgba(255,255,255,0.1)")
# # # #             ),
# # # #             paper_bgcolor='rgba(0,0,0,0)',
# # # #             plot_bgcolor='rgba(0,0,0,0)',
# # # #             height=340,
# # # #             margin=dict(l=40, r=40, t=20, b=20),
# # # #             showlegend=False
# # # #         )
# # # #         st.plotly_chart(fig_radar, use_container_width=True)

# # # #     # 2. Deviation Chart
# # # #     with chart_tabs[1]:
# # # #         features_to_compare = ['CRIM', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'TAX', 'PTRATIO', 'LSTAT']
# # # #         pct_deviation = [
# # # #             ((input_data[feat].values[0] - dataset_averages[feat]) / dataset_averages[feat]) * 100
# # # #             for feat in features_to_compare
# # # #         ]

# # # #         df_dev = pd.DataFrame({'Feature': features_to_compare, 'Deviation (%)': pct_deviation})
# # # #         df_dev['Direction'] = df_dev['Deviation (%)'].apply(lambda x: 'Above Benchmark' if x >= 0 else 'Below Benchmark')

# # # #         fig_bar = px.bar(
# # # #             df_dev,
# # # #             x='Feature',
# # # #             y='Deviation (%)',
# # # #             color='Direction',
# # # #             color_discrete_map={'Above Benchmark': '#38bdf8', 'Below Benchmark': '#f43f5e'}
# # # #         )
# # # #         fig_bar.update_layout(
# # # #             paper_bgcolor='rgba(0,0,0,0)',
# # # #             plot_bgcolor='rgba(0,0,0,0)',
# # # #             font=dict(color='#f8fafc'),
# # # #             xaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
# # # #             yaxis=dict(gridcolor="rgba(255,255,255,0.1)"),
# # # #             height=340,
# # # #             margin=dict(l=20, r=20, t=20, b=20)
# # # #         )
# # # #         st.plotly_chart(fig_bar, use_container_width=True)

# # # #     # 3. Raw Data
# # # #     with chart_tabs[2]:
# # # #         st.dataframe(input_data.T.rename(columns={0: "Input Values"}), use_container_width=True)

# # # #     st.markdown('</div>', unsafe_allow_html=True)

# # # import streamlit as st
# # # import numpy as np
# # # import pandas as pd
# # # import joblib
# # # import plotly.graph_objects as go
# # # import plotly.express as px

# # # # --- PAGE CONFIGURATION ---
# # # st.set_page_config(
# # #     page_title="Boston Housing Valuation AI",
# # #     page_icon="🏡",
# # #     layout="wide",
# # #     initial_sidebar_state="expanded"
# # # )

# # # # --- LIGHT PROFESSIONAL THEME & HIGH-CONTRAST CSS ---
# # # st.markdown("""
# # # <style>
# # #     @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

# # #     * {
# # #         font-family: 'Plus Jakarta Sans', sans-serif;
# # #     }

# # #     /* Light Clean Slate Background */
# # #     .stApp {
# # #         background-color: #f8fafc;
# # #         color: #0f172a;
# # #     }

# # #     /* Professional Card Containers */
# # #     .pro-card {
# # #         background: #ffffff;
# # #         border: 1px solid #e2e8f0;
# # #         border-radius: 14px;
# # #         padding: 24px;
# # #         margin-bottom: 20px;
# # #         box-shadow: 0 4px 12px -2px rgba(15, 23, 42, 0.05), 0 2px 6px -2px rgba(15, 23, 42, 0.03);
# # #         transition: box-shadow 0.2s ease;
# # #     }

# # #     .pro-card:hover {
# # #         box-shadow: 0 10px 25px -3px rgba(15, 23, 42, 0.08), 0 4px 6px -4px rgba(15, 23, 42, 0.03);
# # #         border-color: #cbd5e1;
# # #     }

# # #     /* Main Typography */
# # #     .hero-title {
# # #         font-size: 2.4rem;
# # #         font-weight: 800;
# # #         color: #0f172a;
# # #         margin-bottom: 4px;
# # #         letter-spacing: -0.5px;
# # #     }

# # #     .hero-subtitle {
# # #         color: #475569;
# # #         font-size: 1.05rem;
# # #         font-weight: 500;
# # #         margin-bottom: 24px;
# # #     }

# # #     /* Prediction Result Showcase */
# # #     .price-display-box {
# # #         background: linear-gradient(135deg, #f0fdf4 0%, #e0f2fe 100%);
# # #         border: 1.5px solid #0284c7;
# # #         border-radius: 12px;
# # #         padding: 22px;
# # #         text-align: center;
# # #         margin-bottom: 16px;
# # #     }

# # #     .price-label {
# # #         font-size: 0.85rem;
# # #         font-weight: 700;
# # #         color: #0369a1;
# # #         text-transform: uppercase;
# # #         letter-spacing: 0.08em;
# # #     }

# # #     .price-value {
# # #         font-size: 2.6rem;
# # #         font-weight: 800;
# # #         color: #0c4a6e;
# # #         margin: 6px 0;
# # #     }

# # #     .price-index {
# # #         font-size: 0.9rem;
# # #         color: #0284c7;
# # #         font-weight: 600;
# # #     }

# # #     /* Sidebar Background & Contrast */
# # #     section[data-testid="stSidebar"] {
# # #         background-color: #ffffff;
# # #         border-right: 1px solid #e2e8f0;
# # #     }

# # #     /* Clean Metric overrides */
# # #     div[data-testid="stMetricValue"] {
# # #         color: #0f172a !important;
# # #         font-weight: 700 !important;
# # #     }
    
# # #     div[data-testid="stMetricLabel"] {
# # #         color: #475569 !important;
# # #         font-weight: 600 !important;
# # #     }
# # # </style>
# # # """, unsafe_allow_html=True)

# # # # --- LOAD ARTIFACTS ---
# # # @st.cache_resource
# # # def load_artifacts():
# # #     try:
# # #         model = joblib.load('model.joblib')
# # #         scaler = joblib.load('scaler.joblib')
# # #         return model, scaler, True
# # #     except Exception:
# # #         return None, None, False

# # # model, scaler, artifacts_loaded = load_artifacts()

# # # # --- HEADER SECTION ---
# # # st.markdown('<div class="hero-title">Boston Housing Valuation Engine</div>', unsafe_allow_html=True)
# # # st.markdown('<div class="hero-subtitle">Interactive pricing evaluation system & feature diagnostic suite</div>', unsafe_allow_html=True)

# # # if not artifacts_loaded:
# # #     st.warning("⚠️ Running in heuristic demonstration mode. Place `model.joblib` and `scaler.joblib` in the project directory for actual model inference.")

# # # # --- SIDEBAR INPUTS ---
# # # st.sidebar.markdown("### 🎛️ Input Controls")
# # # st.sidebar.caption("Adjust residential metrics to run valuation:")

# # # tab1, tab2 = st.sidebar.tabs(["📍 Area & Environment", "🏠 Property Structure"])

# # # with tab1:
# # #     crim = st.number_input("CRIM (Crime Rate per capita)", min_value=0.0, max_value=100.0, value=0.2, step=0.05)
# # #     zn = st.slider("ZN (Large Lots % > 25k sq ft)", 0.0, 100.0, 12.5, 0.5)
# # #     indus = st.slider("INDUS (Non-Retail Land %)", 0.0, 30.0, 7.8, 0.1)
# # #     chas = st.selectbox("CHAS (Tract Bounds River?)", options=[0, 1], format_func=lambda x: "Yes (1)" if x == 1 else "No (0)")
# # #     nox = st.slider("NOX (Nitric Oxide Concentration ppm)", 0.3, 0.9, 0.53, 0.01)
# # #     dis = st.slider("DIS (Distance to Employment Hubs)", 1.0, 13.0, 3.8, 0.1)
# # #     rad = st.slider("RAD (Radial Highway Access Index)", 1, 24, 4, 1)

# # # with tab2:
# # #     rm = st.slider("RM (Average Rooms per Unit)", 3.0, 9.0, 6.2, 0.1)
# # #     age = st.slider("AGE (Units Built Pre-1940 %)", 0.0, 100.0, 65.0, 1.0)
# # #     tax = st.slider("TAX (Full Property Tax Rate / $10k)", 180, 720, 310, 10)
# # #     ptratio = st.slider("PTRATIO (Pupil-Teacher Ratio)", 12.0, 23.0, 18.4, 0.1)
# # #     b = st.number_input("B (Demographic Distribution Index)", min_value=0.0, max_value=400.0, value=390.0, step=1.0)
# # #     lstat = st.slider("LSTAT (% Lower Socioeconomic Status)", 1.0, 40.0, 12.5, 0.1)

# # # # Package Input Data
# # # input_data = pd.DataFrame([[
# # #     crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat
# # # ]], columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'])

# # # dataset_averages = {
# # #     'CRIM': 3.61, 'ZN': 11.36, 'INDUS': 11.13, 'CHAS': 0.069, 'NOX': 0.55,
# # #     'RM': 6.28, 'AGE': 68.57, 'DIS': 3.79, 'RAD': 9.54, 'TAX': 408.23,
# # #     'PTRATIO': 18.45, 'B': 356.67, 'LSTAT': 12.65
# # # }

# # # # --- PREDICTION LOGIC ---
# # # if artifacts_loaded:
# # #     scaled_features = scaler.transform(input_data)
# # #     predicted_price = float(model.predict(scaled_features)[0])
# # # else:
# # #     predicted_price = max(5.0, (rm * 9.0) - (lstat * 0.6) - (crim * 0.4) - (ptratio * 0.8) + 10.0)

# # # # --- MAIN DASHBOARD ---
# # # col_left, col_right = st.columns([1.2, 2.0], gap="large")

# # # with col_left:
# # #     st.markdown('<div class="pro-card">', unsafe_allow_html=True)
# # #     st.markdown("<h4 style='color: #0f172a; margin-top: 0;'>Valuation Output</h4>", unsafe_allow_html=True)
    
# # #     st.markdown(f"""
# # #     <div class="price-display-box">
# # #         <div class="price-label">Estimated Median Value</div>
# # #         <div class="price-value">${predicted_price * 1000:,.2f}</div>
# # #         <div class="price-index">Raw Prediction: {predicted_price:.2f} ($k)</div>
# # #     </div>
# # #     """, unsafe_allow_html=True)

# # #     # Core Metrics
# # #     m1, m2 = st.columns(2)
# # #     m1.metric("Rooms (RM)", f"{rm:.1f}", delta=f"{rm - dataset_averages['RM']:.1f} vs Avg")
# # #     m2.metric("Socioeconomic (LSTAT)", f"{lstat:.1f}%", delta=f"{lstat - dataset_averages['LSTAT']:.1f}%", delta_color="inverse")
# # #     st.markdown('</div>', unsafe_allow_html=True)

# # #     # Gauge Chart (Light/Crisp Theme)
# # #     fig_gauge = go.Figure(go.Indicator(
# # #         mode="gauge+number",
# # #         value=predicted_price,
# # #         domain={'x': [0, 1], 'y': [0, 1]},
# # #         title={'text': "Market Valuation Tier ($k)", 'font': {'size': 14, 'color': '#334155'}},
# # #         number={'font': {'color': '#0f172a', 'size': 28}},
# # #         gauge={
# # #             'axis': {'range': [0, 50], 'tickcolor': "#94a3b8", 'tickfont': {'color': '#64748b'}},
# # #             'bar': {'color': "#0284c7"},
# # #             'bgcolor': "#f1f5f9",
# # #             'borderwidth': 1,
# # #             'bordercolor': "#cbd5e1",
# # #             'steps': [
# # #                 {'range': [0, 20], 'color': '#fee2e2'},
# # #                 {'range': [20, 35], 'color': '#fef3c7'},
# # #                 {'range': [35, 50], 'color': '#dcfce7'}
# # #             ]
# # #         }
# # #     ))
# # #     fig_gauge.update_layout(
# # #         paper_bgcolor='rgba(0,0,0,0)',
# # #         plot_bgcolor='rgba(0,0,0,0)',
# # #         height=220,
# # #         margin=dict(l=20, r=20, t=30, b=10)
# # #     )
# # #     st.plotly_chart(fig_gauge, use_container_width=True)

# # # with col_right:
# # #     st.markdown('<div class="pro-card">', unsafe_allow_html=True)
# # #     st.markdown("<h4 style='color: #0f172a; margin-top: 0;'>Diagnostic Visualizations</h4>", unsafe_allow_html=True)
    
# # #     tab_radar, tab_bar, tab_table = st.tabs(["Radar Profile", "Benchmark Deviation", "Raw Attributes"])

# # #     # 1. High Contrast Radar Chart
# # #     with tab_radar:
# # #         radar_categories = ['RM', 'DIS', 'PTRATIO', 'LSTAT', 'INDUS', 'NOX']
# # #         input_norm = [
# # #             (input_data['RM'].values[0] / 9.0) * 100,
# # #             (input_data['DIS'].values[0] / 13.0) * 100,
# # #             (input_data['PTRATIO'].values[0] / 23.0) * 100,
# # #             (input_data['LSTAT'].values[0] / 40.0) * 100,
# # #             (input_data['INDUS'].values[0] / 30.0) * 100,
# # #             (input_data['NOX'].values[0] / 0.9) * 100
# # #         ]
        
# # #         fig_radar = go.Figure()
# # #         fig_radar.add_trace(go.Scatterpolar(
# # #             r=input_norm,
# # #             theta=radar_categories,
# # #             fill='toself',
# # #             fillcolor='rgba(2, 132, 199, 0.15)',
# # #             line=dict(color='#0284c7', width=2.5),
# # #             name='Input Profile'
# # #         ))
# # #         fig_radar.update_layout(
# # #             polar=dict(
# # #                 radialaxis=dict(visible=True, range=[0, 100], color="#64748b", gridcolor="#e2e8f0"),
# # #                 angularaxis=dict(color="#0f172a", gridcolor="#e2e8f0", tickfont=dict(size=12, color="#0f172a", family="Plus Jakarta Sans"))
# # #             ),
# # #             paper_bgcolor='rgba(0,0,0,0)',
# # #             plot_bgcolor='rgba(0,0,0,0)',
# # #             height=340,
# # #             margin=dict(l=40, r=40, t=20, b=20),
# # #             showlegend=False
# # #         )
# # #         st.plotly_chart(fig_radar, use_container_width=True)

# # #     # 2. High Contrast Benchmark Deviation
# # #     with tab_bar:
# # #         features_to_compare = ['CRIM', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'TAX', 'PTRATIO', 'LSTAT']
# # #         pct_deviation = [
# # #             ((input_data[feat].values[0] - dataset_averages[feat]) / dataset_averages[feat]) * 100
# # #             for feat in features_to_compare
# # #         ]

# # #         df_dev = pd.DataFrame({'Feature': features_to_compare, 'Deviation (%)': pct_deviation})
# # #         df_dev['Direction'] = df_dev['Deviation (%)'].apply(lambda x: 'Above Benchmark' if x >= 0 else 'Below Benchmark')

# # #         fig_bar = px.bar(
# # #             df_dev,
# # #             x='Feature',
# # #             y='Deviation (%)',
# # #             color='Direction',
# # #             color_discrete_map={'Above Benchmark': '#0284c7', 'Below Benchmark': '#e11d48'}
# # #         )
# # #         fig_bar.update_layout(
# # #             paper_bgcolor='rgba(0,0,0,0)',
# # #             plot_bgcolor='rgba(0,0,0,0)',
# # #             font=dict(color='#0f172a', family="Plus Jakarta Sans"),
# # #             legend=dict(title=None, orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
# # #             xaxis=dict(gridcolor="#f1f5f9", tickfont=dict(color="#334155")),
# # #             yaxis=dict(gridcolor="#e2e8f0", tickfont=dict(color="#334155")),
# # #             height=340,
# # #             margin=dict(l=20, r=20, t=20, b=20)
# # #         )
# # #         st.plotly_chart(fig_bar, use_container_width=True)

# # #     # 3. Raw Data Summary
# # #     with tab_table:
# # #         st.dataframe(
# # #             input_data.T.rename(columns={0: "Selected Value"}),
# # #             use_container_width=True
# # #         )

# # #     st.markdown('</div>', unsafe_allow_html=True)


# # import streamlit as st
# # import numpy as np
# # import pandas as pd
# # import joblib
# # import plotly.graph_objects as go
# # import plotly.express as px

# # # --- PAGE CONFIGURATION ---
# # st.set_page_config(
# #     page_title="Boston Housing Valuation AI",
# #     page_icon="🏡",
# #     layout="wide",
# #     initial_sidebar_state="expanded"
# # )

# # # --- MODERN VIBRANT LIGHT THEME & MICRO-ANIMATIONS ---
# # st.markdown("""
# # <style>
# #     @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

# #     * {
# #         font-family: 'Plus Jakarta Sans', sans-serif;
# #     }

# #     /* Animated Multi-Gradient Mesh Background */
# #     .stApp {
# #         background-color: #f8fafc;
# #         background-image: 
# #             radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.08) 0px, transparent 50%),
# #             radial-gradient(at 100% 0%, rgba(236, 72, 153, 0.08) 0px, transparent 50%),
# #             radial-gradient(at 50% 100%, rgba(14, 165, 233, 0.08) 0px, transparent 50%);
# #         color: #0f172a;
# #     }

# #     /* Keyframe Animations */
# #     @keyframes slideUp {
# #         from { opacity: 0; transform: translateY(18px); }
# #         to { opacity: 1; transform: translateY(0); }
# #     }

# #     @keyframes glowPulse {
# #         0%, 100% { box-shadow: 0 4px 20px rgba(99, 102, 241, 0.15); }
# #         50% { box-shadow: 0 8px 30px rgba(236, 72, 153, 0.25); }
# #     }

# #     @keyframes floatBadge {
# #         0%, 100% { transform: translateY(0px); }
# #         50% { transform: translateY(-4px); }
# #     }

# #     /* Animated Glass & Depth Cards */
# #     .luminous-card {
# #         background: rgba(255, 255, 255, 0.88);
# #         backdrop-filter: blur(14px);
# #         -webkit-backdrop-filter: blur(14px);
# #         border: 1px solid rgba(226, 232, 240, 0.9);
# #         border-radius: 18px;
# #         padding: 24px;
# #         margin-bottom: 22px;
# #         box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.04), 0 8px 10px -6px rgba(15, 23, 42, 0.02);
# #         animation: slideUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
# #         transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
# #     }

# #     .luminous-card:hover {
# #         transform: translateY(-4px);
# #         border-color: #818cf8;
# #         box-shadow: 0 20px 30px -10px rgba(99, 102, 241, 0.12), 0 10px 10px -5px rgba(15, 23, 42, 0.04);
# #     }

# #     /* Gradient Hero Title */
# #     .hero-title {
# #         font-size: 2.7rem;
# #         font-weight: 800;
# #         letter-spacing: -0.8px;
# #         background: linear-gradient(135deg, #3b82f6 0%, #6366f1 40%, #ec4899 100%);
# #         -webkit-background-clip: text;
# #         -webkit-text-fill-color: transparent;
# #         margin-bottom: 4px;
# #         animation: slideUp 0.4s ease-out;
# #     }

# #     .hero-subtitle {
# #         color: #475569;
# #         font-size: 1.05rem;
# #         font-weight: 600;
# #         margin-bottom: 24px;
# #         animation: slideUp 0.5s ease-out;
# #     }

# #     /* Valuation Box with Vibrant Animated Glow */
# #     .price-display-box {
# #         background: linear-gradient(135deg, #eff6ff 0%, #faf5ff 50%, #fdf2f8 100%);
# #         border: 2px solid #818cf8;
# #         border-radius: 16px;
# #         padding: 24px 16px;
# #         text-align: center;
# #         margin-bottom: 18px;
# #         animation: glowPulse 3.5s infinite ease-in-out;
# #     }

# #     .price-pill {
# #         display: inline-block;
# #         background: #4f46e5;
# #         color: #ffffff;
# #         font-size: 0.75rem;
# #         font-weight: 700;
# #         text-transform: uppercase;
# #         letter-spacing: 0.08em;
# #         padding: 4px 14px;
# #         border-radius: 9999px;
# #         margin-bottom: 8px;
# #         animation: floatBadge 3s ease-in-out infinite;
# #     }

# #     .price-value {
# #         font-size: 2.8rem;
# #         font-weight: 800;
# #         color: #1e1b4b;
# #         margin: 6px 0;
# #         letter-spacing: -1px;
# #     }

# #     .price-index {
# #         font-size: 0.9rem;
# #         color: #6366f1;
# #         font-weight: 700;
# #     }

# #     /* Sidebar High-Contrast Styling */
# #     section[data-testid="stSidebar"] {
# #         background-color: rgba(255, 255, 255, 0.95);
# #         border-right: 1px solid #e2e8f0;
# #     }

# #     /* Metric Visual Contrast */
# #     div[data-testid="stMetricValue"] {
# #         color: #0f172a !important;
# #         font-weight: 800 !important;
# #     }
    
# #     div[data-testid="stMetricLabel"] {
# #         color: #334155 !important;
# #         font-weight: 700 !important;
# #     }
# # </style>
# # """, unsafe_allow_html=True)

# # # --- LOAD ARTIFACTS ---
# # @st.cache_resource
# # def load_artifacts():
# #     try:
# #         model = joblib.load('model.joblib')
# #         scaler = joblib.load('scaler.joblib')
# #         return model, scaler, True
# #     except Exception:
# #         return None, None, False

# # model, scaler, artifacts_loaded = load_artifacts()

# # # --- HEADER SECTION ---
# # st.markdown('<div class="hero-title">Boston Housing Valuation AI</div>', unsafe_allow_html=True)
# # st.markdown('<div class="hero-subtitle">✨ Interactive predictive analytics with real-time diagnostic visualizers</div>', unsafe_allow_html=True)

# # if not artifacts_loaded:
# #     st.info("💡 **Demo Mode Active:** Place `model.joblib` and `scaler.joblib` in the project root folder for live trained inference.")

# # # --- SIDEBAR INPUTS ---
# # st.sidebar.markdown("### 🎛️ INPUT CONTROLS")
# # st.sidebar.caption("Adjust residential attributes below:")

# # tab1, tab2 = st.sidebar.tabs(["📍 Area & Environment", "🏠 Property Structure"])

# # with tab1:
# #     crim = st.number_input("CRIM (Crime Rate per capita)", min_value=0.0, max_value=100.0, value=0.2, step=0.05)
# #     zn = st.slider("ZN (Large Lots % > 25k sq ft)", 0.0, 100.0, 12.5, 0.5)
# #     indus = st.slider("INDUS (Non-Retail Land %)", 0.0, 30.0, 7.8, 0.1)
# #     chas = st.selectbox("CHAS (Tract Bounds River?)", options=[0, 1], format_func=lambda x: "Yes (1)" if x == 1 else "No (0)")
# #     nox = st.slider("NOX (Nitric Oxide Concentration ppm)", 0.3, 0.9, 0.53, 0.01)
# #     dis = st.slider("DIS (Distance to Employment Hubs)", 1.0, 13.0, 3.8, 0.1)
# #     rad = st.slider("RAD (Highway Access Index)", 1, 24, 4, 1)

# # with tab2:
# #     rm = st.slider("RM (Average Rooms per Dwelling)", 3.0, 9.0, 6.2, 0.1)
# #     age = st.slider("AGE (Units Built Pre-1940 %)", 0.0, 100.0, 65.0, 1.0)
# #     tax = st.slider("TAX (Property Tax Rate / $10k)", 180, 720, 310, 10)
# #     ptratio = st.slider("PTRATIO (Pupil-Teacher Ratio)", 12.0, 23.0, 18.4, 0.1)
# #     b = st.number_input("B (Demographic Distribution Index)", min_value=0.0, max_value=400.0, value=390.0, step=1.0)
# #     lstat = st.slider("LSTAT (% Lower Status Population)", 1.0, 40.0, 12.5, 0.1)

# # # Package Input Data
# # input_data = pd.DataFrame([[
# #     crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat
# # ]], columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'])

# # dataset_averages = {
# #     'CRIM': 3.61, 'ZN': 11.36, 'INDUS': 11.13, 'CHAS': 0.069, 'NOX': 0.55,
# #     'RM': 6.28, 'AGE': 68.57, 'DIS': 3.79, 'RAD': 9.54, 'TAX': 408.23,
# #     'PTRATIO': 18.45, 'B': 356.67, 'LSTAT': 12.65
# # }

# # # --- PREDICTION COMPUTATION ---
# # if artifacts_loaded:
# #     scaled_features = scaler.transform(input_data)
# #     predicted_price = float(model.predict(scaled_features)[0])
# # else:
# #     # Heuristic demonstration formula
# #     predicted_price = max(5.0, (rm * 9.0) - (lstat * 0.6) - (crim * 0.4) - (ptratio * 0.8) + 10.0)

# # # --- MAIN DASHBOARD LAYOUT ---
# # col_left, col_right = st.columns([1.2, 2.0], gap="large")

# # with col_left:
# #     st.markdown('<div class="luminous-card">', unsafe_allow_html=True)
# #     st.markdown("<h4 style='color: #0f172a; font-weight: 700; margin-top: 0;'>🏷️ Valuation Output</h4>", unsafe_allow_html=True)
    
# #     st.markdown(f"""
# #     <div class="price-display-box">
# #         <div class="price-pill">Estimated Market Value</div>
# #         <div class="price-value">${predicted_price * 1000:,.2f}</div>
# #         <div class="price-index">Model Target (MEDV): {predicted_price:.2f} ($k)</div>
# #     </div>
# #     """, unsafe_allow_html=True)

# #     # Core Metrics with High Contrast Cards
# #     m1, m2 = st.columns(2)
# #     m1.metric("Rooms (RM)", f"{rm:.1f}", delta=f"{rm - dataset_averages['RM']:+.1f} vs Avg")
# #     m2.metric("Socioeconomic (LSTAT)", f"{lstat:.1f}%", delta=f"{lstat - dataset_averages['LSTAT']:+.1f}%", delta_color="inverse")
# #     st.markdown('</div>', unsafe_allow_html=True)

# #     # Vibrant Gauge Chart
# #     fig_gauge = go.Figure(go.Indicator(
# #         mode="gauge+number",
# #         value=predicted_price,
# #         domain={'x': [0, 1], 'y': [0, 1]},
# #         title={'text': "Market Valuation Tier ($k)", 'font': {'size': 14, 'color': '#1e293b', 'family': 'Plus Jakarta Sans'}},
# #         number={'font': {'color': '#0f172a', 'size': 32, 'family': 'Plus Jakarta Sans'}},
# #         gauge={
# #             'axis': {'range': [0, 50], 'tickcolor': "#64748b", 'tickfont': {'color': '#334155', 'size': 11}},
# #             'bar': {'color': "#4f46e5", 'thickness': 0.28},
# #             'bgcolor': "#f8fafc",
# #             'borderwidth': 1.5,
# #             'bordercolor': "#cbd5e1",
# #             'steps': [
# #                 {'range': [0, 20], 'color': '#fee2e2'},
# #                 {'range': [20, 35], 'color': '#fef08a'},
# #                 {'range': [35, 50], 'color': '#bbf7d0'}
# #             ]
# #         }
# #     ))
# #     fig_gauge.update_layout(
# #         paper_bgcolor='rgba(0,0,0,0)',
# #         plot_bgcolor='rgba(0,0,0,0)',
# #         height=230,
# #         margin=dict(l=20, r=20, t=35, b=10)
# #     )
# #     st.plotly_chart(fig_gauge, use_container_width=True)

# # with col_right:
# #     st.markdown('<div class="luminous-card">', unsafe_allow_html=True)
# #     st.markdown("<h4 style='color: #0f172a; font-weight: 700; margin-top: 0;'>📊 Feature Visualizers & Diagnostics</h4>", unsafe_allow_html=True)
    
# #     tab_radar, tab_bar, tab_table = st.tabs(["✨ Radar Profile", "📈 Benchmark Deviation", "📋 Input Table"])

# #     # 1. Vibrant Polar Radar Chart
# #     with tab_radar:
# #         radar_categories = ['RM', 'DIS', 'PTRATIO', 'LSTAT', 'INDUS', 'NOX']
# #         input_norm = [
# #             (input_data['RM'].values[0] / 9.0) * 100,
# #             (input_data['DIS'].values[0] / 13.0) * 100,
# #             (input_data['PTRATIO'].values[0] / 23.0) * 100,
# #             (input_data['LSTAT'].values[0] / 40.0) * 100,
# #             (input_data['INDUS'].values[0] / 30.0) * 100,
# #             (input_data['NOX'].values[0] / 0.9) * 100
# #         ]
        
# #         fig_radar = go.Figure()
# #         fig_radar.add_trace(go.Scatterpolar(
# #             r=input_norm,
# #             theta=radar_categories,
# #             fill='toself',
# #             fillcolor='rgba(99, 102, 241, 0.22)',
# #             line=dict(color='#4f46e5', width=3),
# #             marker=dict(size=6, color='#ec4899'),
# #             name='Input Profile'
# #         ))
# #         fig_radar.update_layout(
# #             polar=dict(
# #                 radialaxis=dict(visible=True, range=[0, 100], color="#64748b", gridcolor="#e2e8f0"),
# #                 angularaxis=dict(color="#0f172a", gridcolor="#e2e8f0", tickfont=dict(size=12, color="#0f172a", family="Plus Jakarta Sans", weight=600))
# #             ),
# #             paper_bgcolor='rgba(0,0,0,0)',
# #             plot_bgcolor='rgba(0,0,0,0)',
# #             height=340,
# #             margin=dict(l=45, r=45, t=25, b=25),
# #             showlegend=False
# #         )
# #         st.plotly_chart(fig_radar, use_container_width=True)

# #     # 2. Colorful Benchmark Deviation Chart
# #     with tab_bar:
# #         features_to_compare = ['CRIM', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'TAX', 'PTRATIO', 'LSTAT']
# #         pct_deviation = [
# #             ((input_data[feat].values[0] - dataset_averages[feat]) / dataset_averages[feat]) * 100
# #             for feat in features_to_compare
# #         ]

# #         df_dev = pd.DataFrame({'Feature': features_to_compare, 'Deviation (%)': pct_deviation})
# #         df_dev['Direction'] = df_dev['Deviation (%)'].apply(lambda x: 'Above Benchmark' if x >= 0 else 'Below Benchmark')

# #         fig_bar = px.bar(
# #             df_dev,
# #             x='Feature',
# #             y='Deviation (%)',
# #             color='Direction',
# #             color_discrete_map={'Above Benchmark': '#3b82f6', 'Below Benchmark': '#f43f5e'}
# #         )
# #         fig_bar.update_layout(
# #             paper_bgcolor='rgba(0,0,0,0)',
# #             plot_bgcolor='rgba(0,0,0,0)',
# #             font=dict(color='#0f172a', family="Plus Jakarta Sans"),
# #             legend=dict(title=None, orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(color="#1e293b", weight=600)),
# #             xaxis=dict(gridcolor="#f1f5f9", tickfont=dict(color="#0f172a", weight=600)),
# #             yaxis=dict(gridcolor="#e2e8f0", tickfont=dict(color="#0f172a", weight=600)),
# #             height=340,
# #             margin=dict(l=20, r=20, t=20, b=20)
# #         )
# #         st.plotly_chart(fig_bar, use_container_width=True)

# #     # 3. Clean Interactive Table
# #     with tab_table:
# #         st.dataframe(
# #             input_data.T.rename(columns={0: "Selected Value"}),
# #             use_container_width=True
# #         )

# #     st.markdown('</div>', unsafe_allow_html=True)
# import streamlit as st
# import numpy as np
# import pandas as pd
# import joblib
# import plotly.graph_objects as go
# import plotly.express as px

# # --- PAGE CONFIGURATION ---
# st.set_page_config(
#     page_title="Boston Housing Valuation AI",
#     page_icon="🏡",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # --- MODERN VIBRANT LIGHT THEME & MICRO-ANIMATIONS ---
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

#     * {
#         font-family: 'Plus Jakarta Sans', sans-serif;
#     }

#     /* Ambient Mesh Gradient Background */
#     .stApp {
#         background-color: #f8fafc;
#         background-image: 
#             radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.08) 0px, transparent 50%),
#             radial-gradient(at 100% 0%, rgba(236, 72, 153, 0.08) 0px, transparent 50%),
#             radial-gradient(at 50% 100%, rgba(14, 165, 233, 0.08) 0px, transparent 50%);
#         color: #0f172a;
#     }

#     /* Keyframe Animations */
#     @keyframes slideUp {
#         from { opacity: 0; transform: translateY(16px); }
#         to { opacity: 1; transform: translateY(0); }
#     }

#     @keyframes glowPulse {
#         0%, 100% { box-shadow: 0 4px 18px rgba(99, 102, 241, 0.15); }
#         50% { box-shadow: 0 8px 28px rgba(236, 72, 153, 0.22); }
#     }

#     /* Glass Cards */
#     .luminous-card {
#         background: rgba(255, 255, 255, 0.92);
#         backdrop-filter: blur(14px);
#         -webkit-backdrop-filter: blur(14px);
#         border: 1px solid rgba(226, 232, 240, 0.95);
#         border-radius: 18px;
#         padding: 24px;
#         margin-bottom: 22px;
#         box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.04);
#         animation: slideUp 0.5s ease forwards;
#         transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
#     }

#     .luminous-card:hover {
#         transform: translateY(-3px);
#         border-color: #818cf8;
#         box-shadow: 0 18px 30px -10px rgba(99, 102, 241, 0.12);
#     }

#     /* Hero Typography */
#     .hero-title {
#         font-size: 2.6rem;
#         font-weight: 800;
#         letter-spacing: -0.8px;
#         background: linear-gradient(135deg, #2563eb 0%, #4f46e5 45%, #db2777 100%);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         margin-bottom: 4px;
#     }

#     .hero-subtitle {
#         color: #475569;
#         font-size: 1.05rem;
#         font-weight: 600;
#         margin-bottom: 24px;
#     }

#     /* Dynamic Price Box */
#     .price-display-box {
#         background: linear-gradient(135deg, #eff6ff 0%, #faf5ff 50%, #fdf2f8 100%);
#         border: 2px solid #818cf8;
#         border-radius: 16px;
#         padding: 20px 16px;
#         text-align: center;
#         margin-bottom: 18px;
#         animation: glowPulse 3.5s infinite ease-in-out;
#     }

#     .price-pill {
#         display: inline-block;
#         background: #4f46e5;
#         color: #ffffff;
#         font-size: 0.75rem;
#         font-weight: 700;
#         text-transform: uppercase;
#         letter-spacing: 0.08em;
#         padding: 4px 14px;
#         border-radius: 9999px;
#         margin-bottom: 8px;
#     }

#     .price-value {
#         font-size: 2.8rem;
#         font-weight: 800;
#         color: #1e1b4b;
#         margin: 4px 0;
#         letter-spacing: -1px;
#     }

#     .price-index {
#         font-size: 0.9rem;
#         color: #6366f1;
#         font-weight: 700;
#     }

#     /* Property Image Container */
#     .property-img-card {
#         border-radius: 14px;
#         overflow: hidden;
#         border: 1px solid #e2e8f0;
#         box-shadow: 0 4px 14px rgba(0, 0, 0, 0.06);
#         transition: transform 0.3s ease;
#     }
    
#     .property-img-card:hover {
#         transform: scale(1.015);
#     }

#     /* High-contrast Sidebar */
#     section[data-testid="stSidebar"] {
#         background-color: rgba(255, 255, 255, 0.96);
#         border-right: 1px solid #e2e8f0;
#     }
# </style>
# """, unsafe_allow_html=True)

# # --- LOAD ARTIFACTS ---
# @st.cache_resource
# def load_artifacts():
#     try:
#         model = joblib.load('model.joblib')
#         scaler = joblib.load('scaler.joblib')
#         return model, scaler, True
#     except Exception:
#         return None, None, False

# model, scaler, artifacts_loaded = load_artifacts()

# # --- HEADER SECTION ---
# st.markdown('<div class="hero-title">Boston Housing Valuation AI</div>', unsafe_allow_html=True)
# st.markdown('<div class="hero-subtitle">✨ Real-time machine learning valuation and architectural matching</div>', unsafe_allow_html=True)

# if not artifacts_loaded:
#     st.info("💡 **Demo Mode Active:** Place `model.joblib` and `scaler.joblib` in your directory for live inference.")

# # --- SIDEBAR INPUTS ---
# st.sidebar.markdown("### 🎛️ Feature Parameters")
# st.sidebar.caption("Fine-tune property & neighborhood features:")

# tab1, tab2 = st.sidebar.tabs(["📍 Area & Environment", "🏠 Property Structure"])

# with tab1:
#     crim = st.number_input("CRIM (Crime Rate per capita)", min_value=0.0, max_value=100.0, value=0.2, step=0.05)
#     zn = st.slider("ZN (Large Lots % > 25k sq ft)", 0.0, 100.0, 12.5, 0.5)
#     indus = st.slider("INDUS (Non-Retail Land %)", 0.0, 30.0, 7.8, 0.1)
#     chas = st.selectbox("CHAS (Tract Bounds River?)", options=[0, 1], format_func=lambda x: "Yes (1)" if x == 1 else "No (0)")
#     nox = st.slider("NOX (Nitric Oxide Concentration ppm)", 0.3, 0.9, 0.53, 0.01)
#     dis = st.slider("DIS (Distance to Employment Hubs)", 1.0, 13.0, 3.8, 0.1)
#     rad = st.slider("RAD (Highway Access Index)", 1, 24, 4, 1)

# with tab2:
#     rm = st.slider("RM (Average Rooms per Dwelling)", 3.0, 9.0, 6.2, 0.1)
#     age = st.slider("AGE (Units Built Pre-1940 %)", 0.0, 100.0, 65.0, 1.0)
#     tax = st.slider("TAX (Property Tax Rate / $10k)", 180, 720, 310, 10)
#     ptratio = st.slider("PTRATIO (Pupil-Teacher Ratio)", 12.0, 23.0, 18.4, 0.1)
#     b = st.number_input("B (Demographic Distribution Index)", min_value=0.0, max_value=400.0, value=390.0, step=1.0)
#     lstat = st.slider("LSTAT (% Lower Status Population)", 1.0, 40.0, 12.5, 0.1)

# # Package Input Data
# input_data = pd.DataFrame([[
#     crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat
# ]], columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'])

# dataset_averages = {
#     'CRIM': 3.61, 'ZN': 11.36, 'INDUS': 11.13, 'CHAS': 0.069, 'NOX': 0.55,
#     'RM': 6.28, 'AGE': 68.57, 'DIS': 3.79, 'RAD': 9.54, 'TAX': 408.23,
#     'PTRATIO': 18.45, 'B': 356.67, 'LSTAT': 12.65
# }

# # --- PREDICTION COMPUTATION ---
# if artifacts_loaded:
#     scaled_features = scaler.transform(input_data)
#     predicted_price = float(model.predict(scaled_features)[0])
# else:
#     predicted_price = max(5.0, (rm * 9.0) - (lstat * 0.6) - (crim * 0.4) - (ptratio * 0.8) + 10.0)

# # Property Tier Image Matching based on Predicted Price
# if predicted_price >= 35.0:
#     tier_label = "Luxury Executive Estate"
#     tier_color = "#059669"
#     img_url = "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80"
#     img_desc = "Luxury architectural estate with landscaped grounds & premium amenities."
# elif predicted_price >= 20.0:
#     tier_label = "Modern Suburban Family Home"
#     tier_color = "#2563eb"
#     img_url = "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=1200&q=80"
#     img_desc = "Classic multi-story suburban home with porch and private garden."
# else:
#     tier_label = "Entry-Level / Starter Home"
#     tier_color = "#d97706"
#     img_url = "https://images.unsplash.com/photo-1570129477492-45c003edd2be?auto=format&fit=crop&w=1200&q=80"
#     img_desc = "Compact residential residence with practical layout."

# # --- MAIN DASHBOARD LAYOUT ---
# col_left, col_right = st.columns([1.2, 2.0], gap="large")

# with col_left:
#     st.markdown('<div class="luminous-card">', unsafe_allow_html=True)
#     st.markdown("<h4 style='color: #0f172a; font-weight: 700; margin-top: 0;'>🏷️ Valuation Output</h4>", unsafe_allow_html=True)
    
#     st.markdown(f"""
#     <div class="price-display-box">
#         <div class="price-pill">Estimated Market Value</div>
#         <div class="price-value">${predicted_price * 1000:,.2f}</div>
#         <div class="price-index">Model Target (MEDV): {predicted_price:.2f} ($k)</div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Dynamic Realistic Property Representation
#     st.markdown(f"""
#     <div style="margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center;">
#         <span style="font-weight: 700; font-size: 0.9rem; color: #334155;">Representative Architecture</span>
#         <span style="font-size: 0.75rem; font-weight: 700; color: {tier_color}; background: #f1f5f9; padding: 3px 8px; border-radius: 6px;">{tier_label}</span>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.image(img_url, caption=img_desc, use_container_width=True)

#     # Metric Comparison
#     m1, m2 = st.columns(2)
#     m1.metric("Rooms (RM)", f"{rm:.1f}", delta=f"{rm - dataset_averages['RM']:+.1f} vs Avg")
#     m2.metric("Socioeconomic (LSTAT)", f"{lstat:.1f}%", delta=f"{lstat - dataset_averages['LSTAT']:+.1f}%", delta_color="inverse")
#     st.markdown('</div>', unsafe_allow_html=True)

# with col_right:
#     st.markdown('<div class="luminous-card">', unsafe_allow_html=True)
#     st.markdown("<h4 style='color: #0f172a; font-weight: 700; margin-top: 0;'>📊 Feature Visualizers & Diagnostics</h4>", unsafe_allow_html=True)
    
#     tab_radar, tab_bar, tab_gauge, tab_table = st.tabs(["✨ Radar Profile", "📈 Benchmark Deviation", "🎯 Valuation Tier", "📋 Raw Inputs"])

#     # 1. Polar Radar Chart
#     with tab_radar:
#         radar_categories = ['RM', 'DIS', 'PTRATIO', 'LSTAT', 'INDUS', 'NOX']
#         input_norm = [
#             (input_data['RM'].values[0] / 9.0) * 100,
#             (input_data['DIS'].values[0] / 13.0) * 100,
#             (input_data['PTRATIO'].values[0] / 23.0) * 100,
#             (input_data['LSTAT'].values[0] / 40.0) * 100,
#             (input_data['INDUS'].values[0] / 30.0) * 100,
#             (input_data['NOX'].values[0] / 0.9) * 100
#         ]
        
#         fig_radar = go.Figure()
#         fig_radar.add_trace(go.Scatterpolar(
#             r=input_norm,
#             theta=radar_categories,
#             fill='toself',
#             fillcolor='rgba(99, 102, 241, 0.22)',
#             line=dict(color='#4f46e5', width=3),
#             marker=dict(size=6, color='#ec4899'),
#             name='Input Profile'
#         ))
#         fig_radar.update_layout(
#             polar=dict(
#                 radialaxis=dict(visible=True, range=[0, 100], color="#64748b", gridcolor="#e2e8f0"),
#                 angularaxis=dict(color="#0f172a", gridcolor="#e2e8f0", tickfont=dict(size=12, color="#0f172a", weight=600))
#             ),
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             height=340,
#             margin=dict(l=45, r=45, t=25, b=25),
#             showlegend=False
#         )
#         st.plotly_chart(fig_radar, use_container_width=True)

#     # 2. Benchmark Deviation Chart
#     with tab_bar:
#         features_to_compare = ['CRIM', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'TAX', 'PTRATIO', 'LSTAT']
#         pct_deviation = [
#             ((input_data[feat].values[0] - dataset_averages[feat]) / dataset_averages[feat]) * 100
#             for feat in features_to_compare
#         ]

#         df_dev = pd.DataFrame({'Feature': features_to_compare, 'Deviation (%)': pct_deviation})
#         df_dev['Direction'] = df_dev['Deviation (%)'].apply(lambda x: 'Above Benchmark' if x >= 0 else 'Below Benchmark')

#         fig_bar = px.bar(
#             df_dev,
#             x='Feature',
#             y='Deviation (%)',
#             color='Direction',
#             color_discrete_map={'Above Benchmark': '#3b82f6', 'Below Benchmark': '#f43f5e'}
#         )
#         fig_bar.update_layout(
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             font=dict(color='#0f172a', family="Plus Jakarta Sans"),
#             legend=dict(title=None, orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(color="#1e293b", weight=600)),
#             xaxis=dict(gridcolor="#f1f5f9", tickfont=dict(color="#0f172a", weight=600)),
#             yaxis=dict(gridcolor="#e2e8f0", tickfont=dict(color="#0f172a", weight=600)),
#             height=340,
#             margin=dict(l=20, r=20, t=20, b=20)
#         )
#         st.plotly_chart(fig_bar, use_container_width=True)

#     # 3. Gauge Tier Visualizer
#     with tab_gauge:
#         fig_gauge = go.Figure(go.Indicator(
#             mode="gauge+number",
#             value=predicted_price,
#             domain={'x': [0, 1], 'y': [0, 1]},
#             title={'text': "Market Valuation Tier ($k)", 'font': {'size': 14, 'color': '#1e293b'}},
#             number={'font': {'color': '#0f172a', 'size': 32}},
#             gauge={
#                 'axis': {'range': [0, 50], 'tickcolor': "#64748b", 'tickfont': {'color': '#334155', 'size': 11}},
#                 'bar': {'color': "#4f46e5", 'thickness': 0.28},
#                 'bgcolor': "#f8fafc",
#                 'borderwidth': 1.5,
#                 'bordercolor': "#cbd5e1",
#                 'steps': [
#                     {'range': [0, 20], 'color': '#fee2e2'},
#                     {'range': [20, 35], 'color': '#fef08a'},
#                     {'range': [35, 50], 'color': '#bbf7d0'}
#                 ]
#             }
#         ))
#         fig_gauge.update_layout(
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             height=320,
#             margin=dict(l=20, r=20, t=35, b=10)
#         )
#         st.plotly_chart(fig_gauge, use_container_width=True)

#     # 4. Raw Data Table
#     with tab_table:
#         st.dataframe(
#             input_data.T.rename(columns={0: "Selected Value"}),
#             use_container_width=True
#         )

#     st.markdown('</div>', unsafe_allow_html=True)


import streamlit as st
import numpy as np
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Boston Housing Valuation AI | Luxury Property Valuation & Intelligence",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MODERN PROPTECH AESTHETIC & SMOOTH CSS ANIMATIONS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap');

    * {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Ambient Aurora Gradient Background */
    .stApp {
        background-color: #fcfdfe;
        background-image: 
            radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.07) 0px, transparent 45%),
            radial-gradient(at 100% 0%, rgba(236, 72, 153, 0.07) 0px, transparent 45%),
            radial-gradient(at 50% 100%, rgba(14, 165, 233, 0.06) 0px, transparent 50%),
            radial-gradient(at 0% 100%, rgba(16, 185, 129, 0.05) 0px, transparent 45%);
        color: #0f172a;
    }

    /* Keyframe Animations */
    @keyframes subtleFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
    }

    @keyframes shimmerWave {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }

    @keyframes pulseGlow {
        0%, 100% { box-shadow: 0 8px 30px rgba(99, 102, 241, 0.12); }
        50% { box-shadow: 0 14px 45px rgba(236, 72, 153, 0.22); }
    }

    @keyframes cardFadeIn {
        from { opacity: 0; transform: translateY(18px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* PropTech Luxe Cards */
    .prop-card {
        background: rgba(255, 255, 255, 0.88);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        border: 1px solid rgba(226, 232, 240, 0.95);
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 22px;
        box-shadow: 0 10px 30px -10px rgba(15, 23, 42, 0.04);
        animation: cardFadeIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .prop-card:hover {
        transform: translateY(-4px);
        border-color: #a5b4fc;
        box-shadow: 0 20px 40px -12px rgba(99, 102, 241, 0.14);
    }

    /* Hero Typography */
    .hero-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 18px;
    }

    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.6rem;
        font-weight: 700;
        letter-spacing: -0.8px;
        background: linear-gradient(135deg, #1e1b4b 0%, #4338ca 40%, #db2777 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }

    .hero-badge {
        background: linear-gradient(135deg, #e0e7ff 0%, #fce7f3 100%);
        border: 1px solid #c7d2fe;
        color: #4338ca;
        padding: 6px 14px;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        animation: subtleFloat 3s ease-in-out infinite;
    }

    /* Valuation Box with Shimmer Animation */
    .valuation-box {
        background: linear-gradient(135deg, #ffffff 0%, #f5f3ff 50%, #eff6ff 100%);
        border: 2px solid #818cf8;
        border-radius: 18px;
        padding: 24px 18px;
        text-align: center;
        margin-bottom: 20px;
        animation: pulseGlow 4s infinite ease-in-out;
        position: relative;
        overflow: hidden;
    }

    .valuation-box::after {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.6), transparent);
        background-size: 200% 100%;
        animation: shimmerWave 4s infinite linear;
        pointer-events: none;
    }

    .val-tag {
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #4f46e5;
        background: rgba(99, 102, 241, 0.1);
        padding: 4px 12px;
        border-radius: 8px;
        display: inline-block;
        margin-bottom: 8px;
    }

    .val-amount {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.85rem;
        font-weight: 700;
        color: #0f172a;
        margin: 6px 0;
        letter-spacing: -1.5px;
    }

    .val-sub {
        font-size: 0.85rem;
        font-weight: 600;
        color: #6366f1;
    }

    /* PropTech KPI Grid */
    .kpi-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
        margin-top: 14px;
    }

    .kpi-item {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 12px 10px;
        text-align: center;
        transition: transform 0.2s ease;
    }

    .kpi-item:hover {
        transform: translateY(-2px);
        border-color: #cbd5e1;
    }

    .kpi-title {
        font-size: 0.72rem;
        font-weight: 600;
        color: #64748b;
        text-transform: uppercase;
    }

    .kpi-val {
        font-size: 1.15rem;
        font-weight: 800;
        color: #0f172a;
        margin-top: 2px;
    }

    /* Score Indicator Rings */
    .score-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-size: 0.85rem;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 8px;
    }

    /* High Contrast Sidebar */
    section[data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.96);
        border-right: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# --- LOAD TRAINED ARTIFACTS ---
@st.cache_resource
def load_artifacts():
    try:
        model = joblib.load('model.joblib')
        scaler = joblib.load('scaler.joblib')
        return model, scaler, True
    except Exception:
        return None, None, False

model, scaler, artifacts_loaded = load_artifacts()

# --- HEADER SECTION ---
st.markdown("""
<div class="hero-container">
    <div>
        <h1 class="hero-title"> BOSTON HOUSING VALUATION.AI</h1>
        <div style="color: #64748b; font-weight: 600; font-size: 1.05rem; margin-top: 2px;">
            Intelligent Valuation, Yield Forecaster & Spatial Quality Index
        </div>
    </div>
    <div class="hero-badge">⚡ Real-Time MLS Engine</div>
</div>
""", unsafe_allow_html=True)

if not artifacts_loaded:
    st.info("💡 **Interactive Simulation Mode:** Place `model.joblib` and `scaler.joblib` in the project root folder for production inference.")

# --- SIDEBAR INPUTS ---
st.sidebar.markdown("### 🎛️ Asset Parameters")
st.sidebar.caption("Adjust environmental & property parameters:")

tab1, tab2 = st.sidebar.tabs(["📍 Area & Environment", "🏠 Property Structure"])

with tab1:
    crim = st.number_input("CRIM (Crime Rate per capita)", min_value=0.0, max_value=100.0, value=0.2, step=0.05)
    zn = st.slider("ZN (Large Lots % > 25k sq ft)", 0.0, 100.0, 12.5, 0.5)
    indus = st.slider("INDUS (Non-Retail Land %)", 0.0, 30.0, 7.8, 0.1)
    chas = st.selectbox("CHAS (Charles River Waterfront?)", options=[0, 1], format_func=lambda x: "Yes (Waterfront)" if x == 1 else "No (Standard)")
    nox = st.slider("NOX (Air Pollution Index ppm)", 0.3, 0.9, 0.53, 0.01)
    dis = st.slider("DIS (Distance to Tech Hubs / Miles)", 1.0, 13.0, 3.8, 0.1)
    rad = st.slider("RAD (Transit & Highway Accessibility)", 1, 24, 4, 1)

with tab2:
    rm = st.slider("RM (Rooms / Dwellings)", 3.0, 9.0, 6.2, 0.1)
    age = st.slider("AGE (Historic Character / Units Pre-1940 %)", 0.0, 100.0, 65.0, 1.0)
    tax = st.slider("TAX (Property Tax Rate / $10k)", 180, 720, 310, 10)
    ptratio = st.slider("PTRATIO (School Student-Teacher Ratio)", 12.0, 23.0, 18.4, 0.1)
    b = st.number_input("B (Demographic Inclusion Index)", min_value=0.0, max_value=400.0, value=390.0, step=1.0)
    lstat = st.slider("LSTAT (% Lower Income Demographics)", 1.0, 40.0, 12.5, 0.1)

# Package Input Data
input_data = pd.DataFrame([[
    crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat
]], columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'])

dataset_averages = {
    'CRIM': 3.61, 'ZN': 11.36, 'INDUS': 11.13, 'CHAS': 0.069, 'NOX': 0.55,
    'RM': 6.28, 'AGE': 68.57, 'DIS': 3.79, 'RAD': 9.54, 'TAX': 408.23,
    'PTRATIO': 18.45, 'B': 356.67, 'LSTAT': 12.65
}

# --- PREDICTION LOGIC ---
if artifacts_loaded:
    scaled_features = scaler.transform(input_data)
    predicted_price = float(model.predict(scaled_features)[0])
else:
    predicted_price = max(5.0, (rm * 9.2) - (lstat * 0.62) - (crim * 0.35) - (ptratio * 0.75) + 8.5)

# --- CALCULATED PROPTECH METRICS ---
estimated_full_value = predicted_price * 1000
est_monthly_rent = estimated_full_value * 0.0072  # 0.72% monthly rent heuristic
est_cap_rate = ((est_monthly_rent * 12 * 0.70) / max(1, estimated_full_value)) * 100  # NOI / Value
walk_transit_score = int(np.clip(100 - (dis * 5) + (rad * 1.5), 30, 98))
school_rating = max(1.0, min(10.0, (24.0 - ptratio) * 0.9))
air_quality_score = int(np.clip((0.9 - nox) * 150, 40, 99))

# --- MAIN DASHBOARD LAYOUT ---
col_left, col_right = st.columns([1.15, 1.85], gap="large")

with col_left:
    st.markdown('<div class="prop-card">', unsafe_allow_html=True)
    st.markdown("<h4 style='color: #0f172a; font-weight: 700; margin: 0 0 12px 0;'>💎 Asset Valuation</h4>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="valuation-box">
        <div class="val-tag">Automated Valuation Model (AVM)</div>
        <div class="val-amount">${estimated_full_value:,.0f}</div>
        <div class="val-sub">Target Index: {predicted_price:.2f} ($1,000s)</div>
    </div>
    """, unsafe_allow_html=True)

    # PropTech Investment Calculator Card
    st.markdown("<h5 style='color: #1e293b; font-weight: 700; margin-bottom: 6px;'>📈 Projected Yield & Cash Flow</h5>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="kpi-grid">
        <div class="kpi-item">
            <div class="kpi-title">Est. Rent /mo</div>
            <div class="kpi-val" style="color: #4f46e5;">${est_monthly_rent:,.0f}</div>
        </div>
        <div class="kpi-item">
            <div class="kpi-title">Net Cap Rate</div>
            <div class="kpi-val" style="color: #059669;">{est_cap_rate:.1f}%</div>
        </div>
        <div class="kpi-item">
            <div class="kpi-title">5-Yr Apprec.</div>
            <div class="kpi-val" style="color: #db2777;">+24.8%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Neighborhood Eco & Quality Scores
    st.markdown("<h5 style='color: #1e293b; font-weight: 700; margin: 18px 0 8px 0;'>🌱 Neighborhood Livability Scores</h5>", unsafe_allow_html=True)
    
    col_s1, col_s2, col_s3 = st.columns(3)
    col_s1.markdown(f"""
    <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 8px; text-align: center;">
        <span style="font-size: 0.75rem; color: #166534; font-weight: 700;">🚶 Transit Score</span>
        <div style="font-size: 1.2rem; font-weight: 800; color: #15803d;">{walk_transit_score}/100</div>
    </div>
    """, unsafe_allow_html=True)

    col_s2.markdown(f"""
    <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 10px; padding: 8px; text-align: center;">
        <span style="font-size: 0.75rem; color: #1e40af; font-weight: 700;">🎓 School Tier</span>
        <div style="font-size: 1.2rem; font-weight: 800; color: #1d4ed8;">{school_rating:.1f}/10</div>
    </div>
    """, unsafe_allow_html=True)

    col_s3.markdown(f"""
    <div style="background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 10px; padding: 8px; text-align: center;">
        <span style="font-size: 0.75rem; color: #6b21a8; font-weight: 700;">🍃 Clean Air</span>
        <div style="font-size: 1.2rem; font-weight: 800; color: #7e22ce;">{air_quality_score}/100</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="prop-card">', unsafe_allow_html=True)
    st.markdown("<h4 style='color: #0f172a; font-weight: 700; margin: 0 0 12px 0;'>📊 Spatial Analytics & Feature Benchmarking</h4>", unsafe_allow_html=True)
    
    tab_radar, tab_bar, tab_gauge, tab_table = st.tabs([
        "✨ Property DNA Radar",
        "📈 Market Delta Benchmark",
        "🎯 Valuation Thermometer",
        "📋 Specification Matrix"
    ])

    # 1. Radar Profile (Property DNA)
    with tab_radar:
        radar_categories = ['Living Space (RM)', 'Employment Access (DIS)', 'School Quality (PTRATIO)', 'Affluence Index (LSTAT)', 'Commercial Proximity (INDUS)', 'Air Quality (NOX)']
        input_norm = [
            (input_data['RM'].values[0] / 9.0) * 100,
            (input_data['DIS'].values[0] / 13.0) * 100,
            ((23.0 - input_data['PTRATIO'].values[0]) / 11.0) * 100,
            ((40.0 - input_data['LSTAT'].values[0]) / 39.0) * 100,
            (input_data['INDUS'].values[0] / 30.0) * 100,
            ((0.9 - input_data['NOX'].values[0]) / 0.6) * 100
        ]
        
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=input_norm,
            theta=radar_categories,
            fill='toself',
            fillcolor='rgba(99, 102, 241, 0.20)',
            line=dict(color='#6366f1', width=3),
            marker=dict(size=7, color='#db2777'),
            name='Asset DNA Profile'
        ))
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100], color="#64748b", gridcolor="#e2e8f0"),
                angularaxis=dict(color="#0f172a", gridcolor="#e2e8f0", tickfont=dict(size=11, color="#0f172a", weight=700))
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=340,
            margin=dict(l=40, r=40, t=25, b=25),
            showlegend=False
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    # 2. Market Delta Deviation Chart
    with tab_bar:
        features_to_compare = ['CRIM', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'TAX', 'PTRATIO', 'LSTAT']
        pct_deviation = [
            ((input_data[feat].values[0] - dataset_averages[feat]) / dataset_averages[feat]) * 100
            for feat in features_to_compare
        ]

        df_dev = pd.DataFrame({'Feature': features_to_compare, 'Deviation (%)': pct_deviation})
        df_dev['Direction'] = df_dev['Deviation (%)'].apply(lambda x: 'Premium / Above Benchmark' if x >= 0 else 'Below Benchmark')

        fig_bar = px.bar(
            df_dev,
            x='Feature',
            y='Deviation (%)',
            color='Direction',
            color_discrete_map={'Premium / Above Benchmark': '#6366f1', 'Below Benchmark': '#f43f5e'}
        )
        fig_bar.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#0f172a', family="Plus Jakarta Sans"),
            legend=dict(title=None, orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(color="#0f172a", weight=700)),
            xaxis=dict(gridcolor="#f1f5f9", tickfont=dict(color="#0f172a", weight=700)),
            yaxis=dict(gridcolor="#e2e8f0", tickfont=dict(color="#0f172a", weight=700)),
            height=340,
            margin=dict(l=20, r=20, t=20, b=20)
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    # 3. Market Valuation Gauge
    with tab_gauge:
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=predicted_price,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Market Valuation Tier ($k MEDV)", 'font': {'size': 15, 'color': '#0f172a', 'family': 'Plus Jakarta Sans'}},
            number={'font': {'color': '#0f172a', 'size': 36, 'family': 'Space Grotesk'}, 'prefix': "$"},
            gauge={
                'axis': {'range': [0, 50], 'tickcolor': "#64748b", 'tickfont': {'color': '#334155', 'size': 11}},
                'bar': {'color': "#6366f1", 'thickness': 0.3},
                'bgcolor': "#f8fafc",
                'borderwidth': 1.5,
                'bordercolor': "#cbd5e1",
                'steps': [
                    {'range': [0, 20], 'color': '#fee2e2'},
                    {'range': [20, 35], 'color': '#fef08a'},
                    {'range': [35, 50], 'color': '#bbf7d0'}
                ]
            }
        ))
        fig_gauge.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=330,
            margin=dict(l=25, r=25, t=35, b=10)
        )
        st.plotly_chart(fig_gauge, use_container_width=True)

    # 4. Raw Specification Matrix
    with tab_table:
        st.dataframe(
            input_data.T.rename(columns={0: "Input Parameter Value"}),
            use_container_width=True
        )

    st.markdown('</div>', unsafe_allow_html=True)