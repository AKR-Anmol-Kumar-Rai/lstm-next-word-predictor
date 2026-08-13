import streamlit as st
from functions.prediction import prediction, load_model, load_vocab


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="LSTM Next Word Predictor",
    page_icon="🧠",
    layout="wide"
)


# =========================================================
# LOAD MODEL
# =========================================================

model = load_model()
vocab = load_vocab()


# =========================================================
# CLEAR INPUT FUNCTION
# =========================================================

def clear_input():
    st.session_state["sentence"] = ""


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =====================================================
   MAIN BACKGROUND
===================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(120, 80, 255, 0.13),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 15%,
            rgba(0, 200, 255, 0.10),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #080b12 0%,
            #0d111c 50%,
            #090c14 100%
        );

    color: #f5f7ff;
}


/* =====================================================
   MAIN CONTAINER
===================================================== */

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}


/* =====================================================
   HERO
===================================================== */

.hero {
    text-align: center;
    padding: 30px 20px 35px 20px;
}

.hero-icon {
    font-size: 55px;
    margin-bottom: 5px;
}

.hero-title {
    font-size: 48px;
    font-weight: 800;
    letter-spacing: -1px;

    background: linear-gradient(
        90deg,
        #a78bfa,
        #38bdf8,
        #22d3ee
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 10px;
}

.hero-subtitle {
    color: #a7b0c0;
    font-size: 18px;
}


/* =====================================================
   SECTION TITLES
===================================================== */

.section-title {
    font-size: 25px;
    font-weight: 700;
    margin-top: 35px;
    margin-bottom: 18px;
}


/* =====================================================
   INFORMATION CARDS
===================================================== */

.info-card {
    background: rgba(20, 25, 38, 0.82);

    border: 1px solid rgba(148, 163, 184, 0.15);

    border-radius: 18px;

    padding: 25px;

    box-shadow:
        0 10px 40px rgba(0, 0, 0, 0.25);

    backdrop-filter: blur(12px);

    min-height: 230px;
}

.info-card h3 {
    margin-top: 0;
    color: #e5e7eb;
}

.info-card p {
    color: #aeb7c7;
    line-height: 1.7;
}


/* =====================================================
   ARCHITECTURE
===================================================== */

.architecture {
    display: flex;
    align-items: center;
    justify-content: center;

    gap: 12px;

    margin-top: 20px;
    margin-bottom: 35px;

    flex-wrap: wrap;
}

.arch-box {
    background: linear-gradient(
        145deg,
        #171d2b,
        #101521
    );

    border: 1px solid rgba(139, 92, 246, 0.35);

    border-radius: 14px;

    padding: 18px 22px;

    min-width: 150px;

    text-align: center;

    box-shadow:
        0 8px 25px rgba(0, 0, 0, 0.25);
}

.arch-icon {
    font-size: 28px;
}

.arch-name {
    font-weight: 700;
    margin-top: 6px;
}

.arch-desc {
    font-size: 12px;
    color: #8f9bad;
    margin-top: 4px;
}

.arrow {
    font-size: 25px;
    color: #7c3aed;
}


/* =====================================================
   INPUT AREA
===================================================== */

div[data-testid="stTextInput"] input {
    background-color: #161b26;
    color: #f5f7ff;

    border: 1px solid #30394d;

    border-radius: 10px;

    height: 48px;

    font-size: 16px;
}

div[data-testid="stTextInput"] input:focus {
    border-color: #7c3aed;
    box-shadow: 0 0 0 1px #7c3aed;
}


/* =====================================================
   BUTTONS
===================================================== */

.stButton > button {
    border-radius: 10px;

    border: 1px solid rgba(139, 92, 246, 0.5);

    background: linear-gradient(
        135deg,
        #6d28d9,
        #4f46e5
    );

    color: white;

    font-weight: 650;

    height: 45px;

    transition: 0.2s;
}

.stButton > button:hover {
    border-color: #a78bfa;

    transform: translateY(-1px);

    box-shadow:
        0 8px 25px rgba(99, 102, 241, 0.3);
}


/* =====================================================
   PREDICTION RESULT
===================================================== */

.result-card {
    background:
        linear-gradient(
            135deg,
            rgba(16, 185, 129, 0.14),
            rgba(34, 197, 94, 0.04)
        );

    border: 1px solid rgba(34, 197, 94, 0.35);

    border-radius: 18px;

    padding: 25px;

    text-align: center;

    margin-top: 25px;

    box-shadow:
        0 10px 30px rgba(0, 0, 0, 0.2);
}

.result-label {
    color: #9ca3af;

    font-size: 14px;

    text-transform: uppercase;

    letter-spacing: 1px;
}

.result-word {
    font-size: 42px;

    font-weight: 800;

    color: #4ade80;

    margin-top: 8px;
}


/* =====================================================
   MODEL STATS
===================================================== */

.stat-card {
    background: rgba(20, 25, 38, 0.8);

    border: 1px solid rgba(148, 163, 184, 0.15);

    border-radius: 15px;

    padding: 20px;

    text-align: center;
}

.stat-value {
    font-size: 27px;

    font-weight: 750;

    color: #60a5fa;
}

.stat-label {
    color: #8993a5;

    font-size: 13px;

    margin-top: 4px;
}


/* =====================================================
   FOOTER
===================================================== */

.footer {
    text-align: center;

    color: #7d8799;

    margin-top: 55px;

    padding-top: 25px;

    border-top: 1px solid rgba(148, 163, 184, 0.12);

    font-size: 14px;
}

.footer-name {
    color: #c4b5fd;

    font-size: 17px;

    font-weight: 700;

    margin-top: 8px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO SECTION
# =========================================================

st.markdown(
    "<h1 style='text-align: center;'>🧠 LSTM Next Word Predictor</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: #a7b0c0; font-size: 18px;'>"
    "Predict the next word using a trained Long Short-Term Memory neural network"
    "</p>",
    unsafe_allow_html=True
)


# =========================================================
# WHAT IS LSTM?
# =========================================================

st.markdown(
    '<div class="section-title">🧠 What is LSTM?</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:

    st.markdown("""
<div class="info-card">

<h3>Long Short-Term Memory</h3>

<p>
LSTM is a type of Recurrent Neural Network designed to
process sequential data such as text, speech and time-series data.
</p>

<p>
LSTMs use special gates to control which information should
be remembered, updated or forgotten. This allows them to
capture relationships between words across a sequence.
</p>

</div>
""", unsafe_allow_html=True)


with col2:

    st.markdown("""
<div class="info-card">

<h3>How This Project Works</h3>

<p>
The user enters a sentence. The text is tokenized and
converted into numerical word IDs.
</p>

<p>
The sequence is passed through an embedding layer, followed
by an LSTM network. The final hidden representation is passed
to a linear layer that produces scores for the vocabulary.
</p>

<p>
The word with the highest score is selected as the prediction.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# ARCHITECTURE
# =========================================================

st.markdown(
    '<div class="section-title">⚙️ Model Architecture</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="architecture">

<div class="arch-box">
    <div class="arch-icon">📝</div>
    <div class="arch-name">Input</div>
    <div class="arch-desc">Text sequence</div>
</div>

<div class="arrow">→</div>

<div class="arch-box">
    <div class="arch-icon">🔢</div>
    <div class="arch-name">Embedding</div>
    <div class="arch-desc">100 dimensions</div>
</div>

<div class="arrow">→</div>

<div class="arch-box">
    <div class="arch-icon">🧠</div>
    <div class="arch-name">LSTM</div>
    <div class="arch-desc">364 hidden units</div>
</div>

<div class="arrow">→</div>

<div class="arch-box">
    <div class="arch-icon">📊</div>
    <div class="arch-name">Linear</div>
    <div class="arch-desc">Vocabulary scores</div>
</div>

<div class="arrow">→</div>

<div class="arch-box">
    <div class="arch-icon">✨</div>
    <div class="arch-name">Prediction</div>
    <div class="arch-desc">Next word</div>
</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# TRY THE MODEL
# =========================================================

st.markdown(
    '<div class="section-title">🔮 Try the Model</div>',
    unsafe_allow_html=True
)


st.markdown(
    "Enter a sentence below and let the LSTM predict what comes next."
)


# Input
text = st.text_input(
    "Enter your sentence",
    placeholder="Example: hello how are",
    key="sentence"
)


# Buttons
col1, col2 = st.columns([3, 1])


with col1:

    predict_button = st.button(
        "🔮 Predict Next Word",
        use_container_width=True
    )


with col2:

    clear_button = st.button(
        "🗑️ Clear",
        use_container_width=True,
        on_click=clear_input
    )


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    if text.strip():

        result = prediction(
            model,
            vocab,
            text
        )

        # Extract predicted word
        predicted_word = result[len(text):].strip()


        # Prediction result
        st.markdown(
            f"""
<div class="result-card">

<div class="result-label">
Predicted Next Word
</div>

<div class="result-word">
{predicted_word}
</div>

</div>
""",
            unsafe_allow_html=True
        )


        # Complete sentence
        st.markdown("### 📝 Complete Prediction")

        st.info(result)

    else:

        st.warning("Please enter some text first.")


# =========================================================
# MODEL DETAILS
# =========================================================

st.markdown(
    '<div class="section-title">📊 Model Details</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)


with c1:

    st.markdown("""
<div class="stat-card">
<div class="stat-value">100</div>
<div class="stat-label">Embedding Dimension</div>
</div>
""", unsafe_allow_html=True)


with c2:

    st.markdown("""
<div class="stat-card">
<div class="stat-value">364</div>
<div class="stat-label">LSTM Hidden Units</div>
</div>
""", unsafe_allow_html=True)


with c3:

    st.markdown("""
<div class="stat-card">
<div class="stat-value">307</div>
<div class="stat-label">Max Sequence Length</div>
</div>
""", unsafe_allow_html=True)


with c4:

    st.markdown("""
<div class="stat-card">
<div class="stat-value">LSTM</div>
<div class="stat-label">Model Type</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

<div>
LSTM Next Word Prediction Project
</div>

<div class="footer-name">
Created by ANMOL KUMAR RAI
</div>

</div>
""", unsafe_allow_html=True)