import streamlit as st

# =========================
# ตั้งค่าหน้าเว็บ
# =========================
st.set_page_config(
    page_title="Retro Calc",
    page_icon="🔢",
    layout="centered"
)

# =========================
# CSS - Retro / Y2K Calculator
# =========================
st.markdown("""
<style>

    /* =========================
       GLOBAL
    ========================= */
    .stApp {
        background:
            radial-gradient(circle at 20% 10%, #ffe8c2 0%, transparent 25%),
            radial-gradient(circle at 90% 90%, #ffb347 0%, transparent 25%),
            #f4ead5;
        color: #211a14;
    }

    .block-container {
        max-width: 430px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* =========================
       HEADER
       ========================= */
    .title {
        text-align: center;
        font-family: Impact, sans-serif;
        font-size: 46px;
        letter-spacing: 3px;
        color: #211a14;
        margin-bottom: 0;
        text-shadow: 3px 3px 0 #f59e0b;
    }

    .subtitle {
        text-align: center;
        font-family: monospace;
        font-size: 12px;
        font-weight: bold;
        letter-spacing: 3px;
        color: #7c5a3c;
        margin-bottom: 20px;
    }

    /* =========================
       CALCULATOR BODY
       ========================= */
    .calculator {
        background: #29231e;
        border: 4px solid #17130f;
        border-radius: 28px;
        padding: 20px;
        box-shadow:
            8px 8px 0 #17130f,
            0 20px 40px rgba(0,0,0,0.25);
    }

    /* =========================
       DISPLAY
       ========================= */
    .display {
        background: #b7c69b;
        border: 5px solid #17130f;
        border-radius: 12px;
        padding: 16px 18px;
        margin-bottom: 18px;

        box-shadow:
            inset 0 4px 0 rgba(255,255,255,0.25),
            inset 0 -5px 0 rgba(0,0,0,0.15);
    }

    .display-label {
        font-family: monospace;
        font-size: 10px;
        font-weight: bold;
        letter-spacing: 3px;
        color: #4b5739;
        margin-bottom: 4px;
    }

    .display-value {
        font-family: "Courier New", monospace;
        font-size: 34px;
        font-weight: 900;
        color: #17200e;
        text-align: right;

        min-height: 42px;
        overflow-x: auto;
        white-space: nowrap;
    }

    /* =========================
       BUTTON AREA
       ========================= */
    .stButton {
        margin-bottom: 8px;
    }

    .stButton > button {
        width: 100%;
        height: 58px;

        border-radius: 14px;
        border: 3px solid #17130f;

        background: #eee0c7;
        color: #211a14;

        font-family: Arial, sans-serif;
        font-size: 21px;
        font-weight: 900;

        box-shadow:
            0 5px 0 #17130f;

        transition:
            transform 0.08s ease,
            box-shadow 0.08s ease,
            background 0.08s ease;
    }

    .stButton > button:hover {
        background: #fff2dc;
        color: #211a14;
        transform: translateY(-2px);

        box-shadow:
            0 7px 0 #17130f;
    }

    .stButton > button:active {
        transform: translateY(4px);

        box-shadow:
            0 1px 0 #17130f;
    }

    /* =========================
       FIRST COLUMN - CLEAR
       ========================= */
    div[data-testid="column"]:nth-of-type(1)
    .stButton > button {
        background: #e85d4a;
        color: white;
    }

    div[data-testid="column"]:nth-of-type(1)
    .stButton > button:hover {
        background: #f47763;
        color: white;
    }

    /* =========================
       OPERATOR
       ========================= */
    div[data-testid="column"]:nth-of-type(4)
    .stButton > button {
        background: #f59e0b;
        color: #211a14;
    }

    div[data-testid="column"]:nth-of-type(4)
    .stButton > button:hover {
        background: #ffb52e;
    }

    /* =========================
       EQUAL
       ========================= */
    .equal-button button {
        background: #4f8f70 !important;
        color: white !important;
        border-color: #17130f !important;

        box-shadow:
            0 5px 0 #17130f !important;
    }

    .equal-button button:hover {
        background: #63aa87 !important;
    }

    .equal-button button:active {
        box-shadow:
            0 1px 0 #17130f !important;
    }

    /* =========================
       FOOTER
       ========================= */
    .footer {
        text-align: center;
        margin-top: 22px;

        font-family: monospace;
        font-size: 11px;
        font-weight: bold;

        color: #80684e;
        letter-spacing: 2px;
    }

</style>
""", unsafe_allow_html=True)


# =========================
# Session State
# =========================
if "display" not in st.session_state:
    st.session_state.display = "0"


# =========================
# Calculator Logic
# =========================
def click_btn(val):

    current = st.session_state.display

    # Clear
    if val == "C" or current == "Error":
        st.session_state.display = "0"

    # Calculate
    elif val == "=":
        try:

            expr = (
                current
                .replace("×", "*")
                .replace("÷", "/")
            )

            result = eval(
                expr,
                {"__builtins__": {}},
                {}
            )

            if isinstance(result, float) and result.is_integer():
                result = int(result)

            st.session_state.display = str(result)

        except:
            st.session_state.display = "Error"

    # Input
    else:

        if current == "0":

            if val in ["+", "-", "×", "÷"]:
                st.session_state.display += val

            else:
                st.session_state.display = val

        else:
            st.session_state.display += val


# =========================
# Header
# =========================
st.markdown(
    '<div class="title">RETRO CALC</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">/// SIMPLE • CLASSIC • FUN ///</div>',
    unsafe_allow_html=True
)


# =========================
# Calculator Container
# =========================
st.markdown(
    '<div class="calculator">',
    unsafe_allow_html=True
)


# =========================
# Display
# =========================
st.markdown(
    f"""
    <div class="display">
        <div class="display-label">CALCULATOR READY</div>
        <div class="display-value">
            {st.session_state.display}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# Buttons
# =========================
buttons = [
    ["C", "(", ")", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]


for row_index, row in enumerate(buttons):

    cols = st.columns(
        4,
        gap="small"
    )

    for i, char in enumerate(row):

        if char == "":
            continue

        with cols[i]:

            if char == "=":

                st.markdown(
                    '<div class="equal-button">',
                    unsafe_allow_html=True
                )

                clicked = st.button(
                    char,
                    key=f"btn_{row_index}_{i}"
                )

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )

            else:

                clicked = st.button(
                    char,
                    key=f"btn_{row_index}_{i}"
                )

            if clicked:
                click_btn(char)
                st.rerun()


# =========================
# Close Calculator
# =========================
st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================
# Footer
# =========================
st.markdown(
    '<div class="footer">◼ MADE WITH STREAMLIT ◼</div>',
    unsafe_allow_html=True
)
