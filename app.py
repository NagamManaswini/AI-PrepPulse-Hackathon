import streamlit as st
st.markdown(
    """
    <style>
    /* Main container */
    .block-container {
        border: 4px solid #000000;
        border-radius: 16px;
        padding: 30px;
        background-color: #ffffff;
        color: #000000;
    }

    /* Force text color */
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #000000 !important;
    }

    /* Card style */
    .card {
        border: 2px solid #000000;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 25px;
        background-color: #f9f9f9;
    }

    /* Quote style */
    .quote {
        text-align: center;
        font-style: italic;
        color: #333333 !important;
        margin-top: 10px;
    }

    /* Background outside */
    body {
        background-color: #0e1117;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI PrepPulse",
    page_icon="🚀",
    layout="centered"
)

# ---------------- FULL SCREEN DARK BORDER + UI ----------------
st.markdown(
    """
    <style>
    /* Full screen container */
    .block-container {
        border: 4px solid #000000;
        border-radius: 16px;
        padding: 30px;
        background-color: #ffffff;
    }

    body {
        background-color: #f2f2f2;
    }

    /* Card style */
    .card {
        border: 2px solid #333333;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 25px;
        background-color: #fafafa;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }

    /* Quote style */
    .quote {
        text-align: center;
        font-style: italic;
        color: #555;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- TITLE ----------------
st.title("🚀 AI PrepPulse")
st.subheader("Interview Readiness Analyzer (2-Minute Assessment)")
st.write("Answer honestly. This tool helps you prepare **before** real interviews.")

st.markdown(
    '<p class="quote">“Success is where preparation meets opportunity.”</p>',
    unsafe_allow_html=True
)

st.divider()

# ---------------- INPUT SECTION ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("📝 Quick Profile")

tech = st.slider("Technical Skill Level (0 = Beginner, 10 = Strong)", 0, 10, 5)
dsa = st.slider("DSA Confidence (0 = None, 10 = Confident)", 0, 10, 5)

resume = st.selectbox("Resume Quality", ["Basic", "Good", "Strong"])
projects = st.selectbox("Projects / Portfolio", ["None", "1–2 Projects", "3+ Projects"])

communication = st.slider("Communication Confidence", 0, 10, 5)
mock = st.selectbox("Mock Interviews Taken", ["0", "1–3", "4+"])

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- SCORING LOGIC ----------------
resume_score = {"Basic": 5, "Good": 10, "Strong": 15}[resume]
project_score = {"None": 5, "1–2 Projects": 12, "3+ Projects": 20}[projects]
mock_score = {"0": 5, "1–3": 10, "4+": 15}[mock]

score = (
    tech * 3 +
    dsa * 2 +
    resume_score +
    project_score +
    communication * 2 +
    mock_score
)

# ---------------- RESULT SECTION ----------------
if st.button("🔍 Calculate Interview Readiness"):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📊 Your Results")

    st.metric("Interview Readiness Score", f"{score}/100")

    if score < 40:
        level = "Beginner 🔴"
        timeline = "6–8 weeks"
        quote = "“Every expert was once a beginner.”"
    elif score < 70:
        level = "Intermediate 🟡"
        timeline = "3–4 weeks"
        quote = "“You are closer than you think.”"
    else:
        level = "Interview Ready 🟢"
        timeline = "1–2 weeks"
        quote = "“Confidence comes from preparation.”"

    st.subheader(f"Level: {level}")
    st.markdown(f'<p class="quote">{quote}</p>', unsafe_allow_html=True)

    st.subheader("✅ Strengths")
    if tech >= 7:
        st.write("• Strong technical foundation")
    if projects != "None":
        st.write("• Good project exposure")
    if communication >= 7:
        st.write("• Confident communication skills")

    st.subheader("⚠️ Gaps to Improve")
    if dsa < 5:
        st.write("• Revise core DSA concepts")
    if resume == "Basic":
        st.write("• Improve resume bullet points")
    if mock == "0":
        st.write("• Start mock interview practice")

    st.subheader("🎯 Personalized Improvement Plan")
    st.write("• Practice 5–7 mock interviews")
    st.write("• Revise DSA daily")
    st.write("• Improve resume using STAR method")
    st.write("• Practice communication regularly")

    st.subheader("⏳ Estimated Time to Become Interview-Ready")
    st.success(timeline)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        '<p class="quote">“Don’t wait for opportunity. Create it.”</p>',
        unsafe_allow_html=True
    )
