import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Iris Vision AI",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>

/* =======================================================
   GLOBAL
======================================================= */

.stApp {
    background:
        radial-gradient(
            circle at 5% 5%,
            rgba(139, 92, 246, 0.20),
            transparent 25%
        ),
        radial-gradient(
            circle at 95% 10%,
            rgba(6, 182, 212, 0.18),
            transparent 25%
        ),
        radial-gradient(
            circle at 50% 100%,
            rgba(236, 72, 153, 0.12),
            transparent 30%
        ),
        #070b14;

    color: #f8fafc;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* =======================================================
   SIDEBAR
======================================================= */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #0b1020,
            #111827
        );

    border-right: 1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] * {
    color: #e2e8f0;
}

section[data-testid="stSidebar"] .stRadio > label {
    color: #94a3b8;
    font-weight: 700;
}


/* =======================================================
   TOP HEADER
======================================================= */

.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;

    background: rgba(15,23,42,0.72);
    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 22px;
    padding: 18px 25px;

    margin-bottom: 20px;

    box-shadow:
        0 20px 50px rgba(0,0,0,0.25);

    backdrop-filter: blur(18px);
}

.brand {
    font-size: 22px;
    font-weight: 900;

    background:
        linear-gradient(
            90deg,
            #22d3ee,
            #8b5cf6,
            #ec4899
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.status {
    background: rgba(34,197,94,0.12);
    color: #4ade80;

    border: 1px solid rgba(34,197,94,0.25);

    padding: 7px 13px;
    border-radius: 999px;

    font-size: 12px;
    font-weight: 700;
}


/* =======================================================
   HERO
======================================================= */

.hero {
    position: relative;
    overflow: hidden;

    background:
        linear-gradient(
            135deg,
            #111827 0%,
            #1e1b4b 50%,
            #0f172a 100%
        );

    border: 1px solid rgba(139,92,246,0.25);

    border-radius: 30px;

    padding: 42px;

    margin-bottom: 25px;

    box-shadow:
        0 25px 70px rgba(0,0,0,0.35),
        0 0 50px rgba(139,92,246,0.08);
}

.hero::before {
    content: "";

    position: absolute;

    width: 300px;
    height: 300px;

    right: -80px;
    top: -100px;

    background: #8b5cf6;

    filter: blur(100px);

    opacity: 0.20;
}

.hero::after {
    content: "✦";

    position: absolute;

    right: 70px;
    top: 25px;

    font-size: 120px;

    color: #22d3ee;

    opacity: 0.08;
}

.hero-title {
    position: relative;

    font-size: 44px;
    font-weight: 950;

    letter-spacing: -2px;

    margin: 0;

    background:
        linear-gradient(
            90deg,
            #ffffff,
            #c4b5fd,
            #67e8f9
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-text {
    position: relative;

    color: #94a3b8;

    font-size: 16px;

    max-width: 700px;

    line-height: 1.7;

    margin-top: 10px;
}


/* =======================================================
   SECTION TITLE
======================================================= */

.section-title {
    font-size: 25px;
    font-weight: 850;

    color: #f8fafc;

    margin: 12px 0 5px;
}

.section-subtitle {
    color: #64748b;

    font-size: 14px;

    margin-bottom: 18px;
}


/* =======================================================
   GLASS CARD
======================================================= */

.glass-card {
    background:
        rgba(15,23,42,0.72);

    border:
        1px solid rgba(255,255,255,0.08);

    border-radius: 24px;

    padding: 25px;

    box-shadow:
        0 15px 45px rgba(0,0,0,0.22);

    backdrop-filter: blur(18px);

    margin-bottom: 20px;
}

.card-heading {
    font-size: 20px;
    font-weight: 850;

    color: #f8fafc;

    margin-bottom: 5px;
}

.card-description {
    color: #64748b;
    font-size: 13px;
    margin-bottom: 20px;
}


/* =======================================================
   FEATURE BOX
======================================================= */

.feature-box {
    background:
        linear-gradient(
            135deg,
            rgba(30,41,59,0.85),
            rgba(15,23,42,0.65)
        );

    border:
        1px solid rgba(255,255,255,0.07);

    border-radius: 17px;

    padding: 14px 17px;

    margin-top: 13px;

    color: #cbd5e1;

    font-weight: 700;

    transition: 0.2s;
}

.feature-box:hover {
    border-color: rgba(139,92,246,0.45);

    transform: translateX(3px);

    box-shadow:
        0 0 25px rgba(139,92,246,0.08);
}


/* =======================================================
   SLIDER
======================================================= */

.stSlider label {
    color: #94a3b8 !important;
}

.stSlider [data-baseweb="slider"] {
    margin-top: -5px;
}


/* =======================================================
   INPUT TABLE
======================================================= */

div[data-testid="stDataFrame"] {
    border-radius: 17px;

    border: 1px solid rgba(255,255,255,0.07);

    overflow: hidden;
}


/* =======================================================
   RESULT
======================================================= */

.result-box {
    position: relative;

    overflow: hidden;

    background:
        linear-gradient(
            135deg,
            rgba(34,211,238,0.10),
            rgba(139,92,246,0.15)
        );

    border:
        1px solid rgba(103,232,249,0.25);

    border-radius: 24px;

    padding: 30px;

    text-align: center;

    margin-top: 20px;

    box-shadow:
        0 0 45px rgba(34,211,238,0.08);
}

.result-box::before {
    content: "";

    position: absolute;

    width: 180px;
    height: 180px;

    left: -80px;
    bottom: -100px;

    background: #ec4899;

    filter: blur(80px);

    opacity: 0.18;
}

.result-caption {
    color: #67e8f9;

    font-size: 12px;

    font-weight: 800;

    letter-spacing: 2px;

    text-transform: uppercase;
}

.result-species {
    font-size: 35px;

    font-weight: 950;

    margin-top: 8px;

    background:
        linear-gradient(
            90deg,
            #22d3ee,
            #a78bfa,
            #f472b6
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.result-description {
    color: #94a3b8;

    font-size: 13px;

    margin-top: 7px;
}


/* =======================================================
   PROBABILITY CARDS
======================================================= */

.prob-card {
    background:
        rgba(15,23,42,0.78);

    border:
        1px solid rgba(255,255,255,0.08);

    border-radius: 20px;

    padding: 20px;

    text-align: center;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.20);

    transition: 0.2s;
}

.prob-card:hover {
    transform: translateY(-4px);

    border-color: rgba(139,92,246,0.35);

    box-shadow:
        0 15px 35px rgba(0,0,0,0.30);
}

.prob-emoji {
    font-size: 28px;
}

.prob-name {
    color: #94a3b8;

    font-size: 13px;

    margin-top: 6px;
}

.prob-value {
    font-size: 25px;

    font-weight: 900;

    margin-top: 5px;
}


/* =======================================================
   METRICS
======================================================= */

.metric {
    background:
        linear-gradient(
            145deg,
            rgba(15,23,42,0.9),
            rgba(30,41,59,0.7)
        );

    border:
        1px solid rgba(255,255,255,0.08);

    border-radius: 22px;

    padding: 25px;

    text-align: center;

    box-shadow:
        0 12px 35px rgba(0,0,0,0.20);
}

.metric-icon {
    font-size: 27px;
}

.metric-value {
    font-size: 34px;

    font-weight: 950;

    margin-top: 5px;

    background:
        linear-gradient(
            90deg,
            #22d3ee,
            #a78bfa
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.metric-label {
    color: #64748b;

    font-size: 13px;

    margin-top: 5px;
}


/* =======================================================
   DATASET
======================================================= */

.dataset-header {
    background:
        linear-gradient(
            135deg,
            rgba(139,92,246,0.15),
            rgba(6,182,212,0.08)
        );

    border:
        1px solid rgba(139,92,246,0.18);

    border-radius: 22px;

    padding: 22px 25px;

    margin-bottom: 20px;
}

.dataset-title {
    font-size: 23px;

    font-weight: 900;

    color: #f8fafc;
}

.dataset-text {
    color: #64748b;

    font-size: 13px;

    margin-top: 5px;
}


/* =======================================================
   RADIO NAVIGATION
======================================================= */

div[data-testid="stRadio"] {
    background:
        rgba(15,23,42,0.75);

    border:
        1px solid rgba(255,255,255,0.08);

    padding: 12px 18px;

    border-radius: 18px;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.18);

    margin-bottom: 25px;
}

div[data-testid="stRadio"] label {
    color: #cbd5e1 !important;
}


/* =======================================================
   CHART
======================================================= */

div[data-testid="stVegaLiteChart"],
div[data-testid="stArrowVegaLiteChart"] {
    background: transparent !important;
}


/* =======================================================
   BUTTON
======================================================= */

.stButton > button {
    border-radius: 14px;

    background:
        linear-gradient(
            135deg,
            #7c3aed,
            #2563eb
        );

    color: white;

    border: 1px solid rgba(255,255,255,0.12);

    font-weight: 800;
}


/* =======================================================
   FOOTER
======================================================= */

.footer {
    text-align: center;

    color: #475569;

    font-size: 12px;

    padding: 35px 0 10px;
}


/* =======================================================
   HIDE STREAMLIT UI
======================================================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD MODEL
# =========================================================
@st.cache_resource
def load_model():
    return joblib.load("iris_model.pkl")


model = load_model()


# =========================================================
# LOAD DATASET
# =========================================================
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["target"] = iris.target

target_names = iris.target_names

df["species"] = df["target"].map(
    lambda x: target_names[x]
)


# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:

    st.markdown("""
    <div style="
        text-align:center;
        padding:15px 0 25px;
    ">
        <div style="font-size:48px;">🔮</div>

        <div style="
            font-size:22px;
            font-weight:900;
            color:#f8fafc;
        ">
            Iris Vision
        </div>

        <div style="
            color:#64748b;
            font-size:12px;
            margin-top:5px;
        ">
            AI Classification System
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div style="
        background:rgba(34,211,238,0.07);
        border:1px solid rgba(34,211,238,0.15);
        padding:15px;
        border-radius:15px;
    ">
        <div style="
            color:#22d3ee;
            font-weight:800;
            font-size:13px;
        ">
            ⚡ MODEL STATUS
        </div>

        <div style="
            color:#94a3b8;
            font-size:12px;
            margin-top:7px;
        ">
            Model loaded successfully
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="
        color:#64748b;
        font-size:12px;
        line-height:1.8;
    ">
        <b style="color:#cbd5e1;">Model Input</b><br>
        • Sepal Length<br>
        • Sepal Width<br>
        • Petal Length<br>
        • Petal Width
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# TOP BAR
# =========================================================
st.markdown("""
<div class="topbar">

    <div class="brand">
        🔮 IRIS VISION AI
    </div>

    <div class="status">
        ● MODEL ONLINE
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================
st.markdown("""
<div class="hero">

    <div class="hero-title">
        Iris Classification
    </div>

    <div class="hero-text">
        ระบบ Machine Learning สำหรับวิเคราะห์และจำแนกสายพันธุ์
        ดอก Iris จากลักษณะของกลีบและกลีบเลี้ยง
        พร้อมแสดงความน่าจะเป็นของผลการทำนายแบบ Real-time
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# NAVIGATION
# =========================================================
selected_tab = st.radio(
    "Navigation",
    [
        "🎯 AI Prediction",
        "📊 Dataset Analytics"
    ],
    horizontal=True,
    label_visibility="collapsed"
)


# =========================================================
# PREDICTION PAGE
# =========================================================
if selected_tab == "🎯 AI Prediction":

    left, right = st.columns(
        [0.95, 1.25],
        gap="large"
    )


    # =====================================================
    # LEFT
    # =====================================================
    with left:

        st.markdown("""
        <div class="glass-card">

            <div class="card-heading">
                🎛️ Feature Controls
            </div>

            <div class="card-description">
                ปรับค่าของดอก Iris เพื่อส่งเข้าสู่โมเดล
                Machine Learning
            </div>

        </div>
        """, unsafe_allow_html=True)


        # -------------------------------------------------
        # SEPAL LENGTH
        # -------------------------------------------------
        st.markdown(
            '<div class="feature-box">🌱 Sepal Length</div>',
            unsafe_allow_html=True
        )

        sl = st.slider(
            "Sepal Length",
            float(df["sepal length (cm)"].min()),
            float(df["sepal length (cm)"].max()),
            5.8,
            step=0.1,
            label_visibility="collapsed"
        )


        # -------------------------------------------------
        # SEPAL WIDTH
        # -------------------------------------------------
        st.markdown(
            '<div class="feature-box">🍃 Sepal Width</div>',
            unsafe_allow_html=True
        )

        sw = st.slider(
            "Sepal Width",
            float(df["sepal width (cm)"].min()),
            float(df["sepal width (cm)"].max()),
            3.0,
            step=0.1,
            label_visibility="collapsed"
        )


        # -------------------------------------------------
        # PETAL LENGTH
        # -------------------------------------------------
        st.markdown(
            '<div class="feature-box">🌸 Petal Length</div>',
            unsafe_allow_html=True
        )

        pl = st.slider(
            "Petal Length",
            float(df["petal length (cm)"].min()),
            float(df["petal length (cm)"].max()),
            4.3,
            step=0.1,
            label_visibility="collapsed"
        )


        # -------------------------------------------------
        # PETAL WIDTH
        # -------------------------------------------------
        st.markdown(
            '<div class="feature-box">🌺 Petal Width</div>',
            unsafe_allow_html=True
        )

        pw = st.slider(
            "Petal Width",
            float(df["petal width (cm)"].min()),
            float(df["petal width (cm)"].max()),
            1.3,
            step=0.1,
            label_visibility="collapsed"
        )


        # -------------------------------------------------
        # INPUT TABLE
        # -------------------------------------------------
        st.markdown("""
        <div class="section-title">
            📋 Current Input
        </div>

        <div class="section-subtitle">
            ค่าที่กำลังถูกส่งเข้าสู่โมเดล
        </div>
        """, unsafe_allow_html=True)


        input_df = pd.DataFrame({
            "Sepal Length": [sl],
            "Sepal Width": [sw],
            "Petal Length": [pl],
            "Petal Width": [pw]
        })


        st.dataframe(
            input_df,
            use_container_width=True,
            hide_index=True
        )


        # -------------------------------------------------
        # MODEL INPUT
        # -------------------------------------------------
        input_data = np.array([
            [sl, sw, pl, pw]
        ])


        # -------------------------------------------------
        # PREDICTION
        # -------------------------------------------------
        prediction = model.predict(input_data)

        result_name = target_names[
            prediction[0]
        ].capitalize()


        # -------------------------------------------------
        # RESULT
        # -------------------------------------------------
        st.markdown(f"""
        <div class="result-box">

            <div class="result-caption">
                AI PREDICTION
            </div>

            <div class="result-species">
                Iris {result_name}
            </div>

            <div class="result-description">
                โมเดลจำแนกจาก Feature ทั้งหมด 4 ตัว
            </div>

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # RIGHT
    # =====================================================
    with right:

        # -------------------------------------------------
        # PROBABILITY
        # -------------------------------------------------
        st.markdown("""
        <div class="glass-card">

            <div class="card-heading">
                📡 Prediction Probability
            </div>

            <div class="card-description">
                ความน่าจะเป็นที่โมเดลประเมินสำหรับแต่ละสายพันธุ์
            </div>

        """, unsafe_allow_html=True)


        prediction_proba = model.predict_proba(
            input_data
        )


        proba_df = pd.DataFrame(
            prediction_proba * 100,
            columns=[
                name.capitalize()
                for name in target_names
            ]
        ).T


        proba_df.columns = [
            "Probability (%)"
        ]


        st.bar_chart(
            proba_df,
            color="#8b5cf6",
            height=350
        )


        st.markdown("</div>", unsafe_allow_html=True)


        # -------------------------------------------------
        # PROBABILITY CARDS
        # -------------------------------------------------
        st.markdown("""
        <div class="section-title">
            🎯 Probability Details
        </div>

        <div class="section-subtitle">
            ค่าความมั่นใจของโมเดลในแต่ละสายพันธุ์
        </div>
        """, unsafe_allow_html=True)


        p1, p2, p3 = st.columns(3)


        probabilities = prediction_proba[0] * 100


        species_colors = [
            ("🌸", "#fb7185"),
            ("🌼", "#facc15"),
            ("🌿", "#4ade80")
        ]


        for col, name, probability, color_info in zip(
            [p1, p2, p3],
            target_names,
            probabilities,
            species_colors
        ):

            emoji, color = color_info

            with col:

                st.markdown(f"""
                <div class="prob-card">

                    <div class="prob-emoji">
                        {emoji}
                    </div>

                    <div class="prob-name">
                        {name.capitalize()}
                    </div>

                    <div
                        class="prob-value"
                        style="color:{color};"
                    >
                        {probability:.2f}%
                    </div>

                </div>
                """, unsafe_allow_html=True)


# =========================================================
# DATASET PAGE
# =========================================================
else:

    # -----------------------------------------------------
    # HEADER
    # -----------------------------------------------------
    st.markdown("""
    <div class="dataset-header">

        <div class="dataset-title">
            📊 Dataset Analytics
        </div>

        <div class="dataset-text">
            สำรวจ Iris Dataset พร้อมข้อมูลสถิติและการกระจายของข้อมูล
        </div>

    </div>
    """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # METRICS
    # -----------------------------------------------------
    m1, m2, m3 = st.columns(3)


    with m1:

        st.markdown(f"""
        <div class="metric">

            <div class="metric-icon">
                📦
            </div>

            <div class="metric-value">
                {len(df)}
            </div>

            <div class="metric-label">
                จำนวนข้อมูลทั้งหมด
            </div>

        </div>
        """, unsafe_allow_html=True)


    with m2:

        st.markdown(f"""
        <div class="metric">

            <div class="metric-icon">
                🧬
            </div>

            <div class="metric-value">
                {len(iris.feature_names)}
            </div>

            <div class="metric-label">
                จำนวน Features
            </div>

        </div>
        """, unsafe_allow_html=True)


    with m3:

        st.markdown(f"""
        <div class="metric">

            <div class="metric-icon">
                🌺
            </div>

            <div class="metric-value">
                {len(target_names)}
            </div>

            <div class="metric-label">
                จำนวนสายพันธุ์
            </div>

        </div>
        """, unsafe_allow_html=True)


    st.markdown("<br>", unsafe_allow_html=True)


    # -----------------------------------------------------
    # DATASET TABLE
    # -----------------------------------------------------
    st.markdown("""
    <div class="glass-card">

        <div class="card-heading">
            🗃️ Iris Dataset Explorer
        </div>

        <div class="card-description">
            ข้อมูลทั้งหมดที่ใช้สำหรับการวิเคราะห์
        </div>

    """, unsafe_allow_html=True)


    st.dataframe(
        df,
        use_container_width=True,
        height=500
    )


    st.markdown("</div>", unsafe_allow_html=True)


    # -----------------------------------------------------
    # ANALYTICS
    # -----------------------------------------------------
    st.markdown("""
    <div class="section-title">
        📈 Data Analytics
    </div>

    <div class="section-subtitle">
        สถิติพื้นฐานของ Dataset
    </div>
    """, unsafe_allow_html=True)


    stat1, stat2 = st.columns(2, gap="large")


    # -----------------------------------------------------
    # MEAN
    # -----------------------------------------------------
    with stat1:

        st.markdown("""
        <div class="glass-card">

            <div class="card-heading">
                📏 Feature Mean
            </div>

            <div class="card-description">
                ค่าเฉลี่ยของแต่ละ Feature
            </div>

        """, unsafe_allow_html=True)


        mean_df = df[
            iris.feature_names
        ].mean().to_frame("Mean")


        st.dataframe(
            mean_df,
            use_container_width=True
        )


        st.markdown("</div>", unsafe_allow_html=True)


    # -----------------------------------------------------
    # SPECIES COUNT
    # -----------------------------------------------------
    with stat2:

        st.markdown("""
        <div class="glass-card">

            <div class="card-heading">
                🌺 Species Distribution
            </div>

            <div class="card-description">
                จำนวนข้อมูลของแต่ละสายพันธุ์
            </div>

        """, unsafe_allow_html=True)


        species_count = (
            df["species"]
            .value_counts()
            .rename("จำนวน")
        )


        st.bar_chart(
            species_count,
            color="#06b6d4"
        )


        st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="footer">

    🔮 Iris Vision AI
    &nbsp;•&nbsp;
    Machine Learning Dashboard
    <br>

    Powered by Python + Streamlit + Scikit-learn

</div>
""", unsafe_allow_html=True)
