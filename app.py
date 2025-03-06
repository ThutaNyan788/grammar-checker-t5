import streamlit as st
from happytransformer import HappyTextToText, TTSettings

# Load model from Hugging Face
MODEL_NAME = "ThutaNyan/grammar-t5-model"  # Replace with your actual model repo
happy_tt = HappyTextToText("T5", MODEL_NAME)

# Set inference settings
beam_settings = TTSettings(num_beams=5, min_length=1, max_length=20)

st.title("Grammar Checker App")
st.write("Enter a sentence with incorrect grammar, and I will correct it!")

# User input
sentence = st.text_input("Enter a sentence:", "My cat have claws")

if st.button("Correct Grammar"):
    input_text = "grammar: " + sentence
    result = happy_tt.generate_text(input_text, args=beam_settings)
    st.write("✅ Corrected Sentence:", result.text)
