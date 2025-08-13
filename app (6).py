import streamlit as st
import pandas as pd
from deep_translator import GoogleTranslator
from langdetect import detect
from difflib import get_close_matches
import os

# -----------------------------
# Setup custom cache to avoid permission errors
# -----------------------------
os.environ['TRANSFORMERS_CACHE'] = '/tmp/transformers_cache'
os.environ['HF_HOME'] = '/tmp/huggingface'

# -----------------------------
# Load dataset
# -----------------------------
DATA_PATH = "guvi dataset.xlsx"  # Place this in the same repo
df = pd.read_excel(DATA_PATH)
questions = df['Question'].tolist()
answers = df['Answer'].tolist()

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("GUVI Multilingual QA Chatbot")

user_input = st.text_area("Enter your question:")

if st.button("Get Answer"):
    if not user_input.strip():
        st.warning("Please enter a question!")
    else:
        try:
            # Detect input language
            detected_lang = detect(user_input)

            # Translate to English if necessary
            if detected_lang != 'en':
                input_in_english = GoogleTranslator(source=detected_lang, target='en').translate(user_input)
            else:
                input_in_english = user_input

            # Find closest question from dataset
            closest = get_close_matches(input_in_english, questions, n=1, cutoff=0.6)
            if closest:
                idx = questions.index(closest[0])
                final_answer_en = answers[idx]
            else:
                final_answer_en = "Sorry, no answer found in the dataset."

            # Translate answer back to input language
            if detected_lang != 'en':
                final_answer = GoogleTranslator(source='en', target=detected_lang).translate(final_answer_en)
            else:
                final_answer = final_answer_en

            # Display final answer
            st.subheader("Answer:")
            st.write(final_answer)

        except Exception as e:
            st.error(f"Error: {e}")