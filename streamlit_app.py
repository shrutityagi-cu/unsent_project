import streamlit as st
import os
import joblib
import pickle
from transformers import pipeline
import matplotlib.pyplot as plt
from openai import OpenAI

# -------------------- UI STYLING --------------------
st.markdown("""
    <style>
    body {
        background-color: #0b0000;
        color: #f5e6e6;
    }
    .stApp {
        background-color: #0b0000;
    }
    textarea {
        background-color: #1a0000 !important;
        color: #f5e6e6 !important;
        border: 1px solid #660000 !important;
    }
    .stButton>button {
        background-color: #660000;
        color: white;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("unsent.")
st.caption("things you never said, but meant.")

# -------------------- LOAD BERT MODEL --------------------
@st.cache_resource
def load_bert():
    return pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base"
    )

classifier = load_bert()

# -------------------- LOAD CLASSICAL MODEL --------------------
@st.cache_resource
def load_classical():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(BASE_DIR, "data", "processed", "model.pkl")
    vectorizer_path = os.path.join(BASE_DIR, "data", "processed", "vectorizer.pkl")

    model = joblib.load(model_path)
    with open(vectorizer_path, "rb") as f:
        vectorizer = pickle.load(f)

    return model, vectorizer

classic_model, vectorizer = load_classical()

# -------------------- OPENAI SETUP --------------------
client = OpenAI(api_key="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")  # 🔴 replace later

def rewrite_text(text):
    prompt = f"""
    Rewrite this as a short, emotional, unsent message.
    Keep it poetic, raw, and minimal.

    Text: {text}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# -------------------- INPUT --------------------
user_input = st.text_area("write what you couldn't send...")

# -------------------- MAIN ACTION --------------------
if st.button("feel it"):
    if user_input.strip() != "":

        # 🔥 BERT prediction
        bert_result = classifier(user_input)[0]
        bert_pred = bert_result['label']
        bert_score = round(bert_result['score'], 2)

        # 🔥 Classical prediction
        vec = vectorizer.transform([user_input])
        classic_pred = classic_model.predict(vec)[0]

        # -------------------- OUTPUT --------------------
        st.markdown(f"### {bert_pred.lower()}")
        st.caption(f"confidence: {bert_score}")

        # -------------------- COMPARISON --------------------
        st.markdown("### comparison")

        col1, col2 = st.columns(2)

        with col1:
            st.write("BERT")
            st.success(bert_pred)

        with col2:
            st.write("Classical ML")
            st.info(classic_pred)

        # -------------------- VISUALIZATION --------------------
        fig, ax = plt.subplots()
        ax.bar([bert_pred], [bert_score])
        ax.set_ylabel("confidence")

        st.pyplot(fig)

    else:
        st.warning("you wrote nothing.")

# -------------------- REWRITE FEATURE --------------------
if st.button("rewrite it like it hurts"):
    if user_input.strip() != "":
        try:
            rewritten = rewrite_text(user_input)
            st.markdown("#### rewritten:")
            st.write(rewritten)
        except Exception as e:
            st.error(f"Rewrite failed: {e}")
    else:
        st.warning("you wrote nothing.")