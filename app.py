import asyncio
import streamlit as st
from happytransformer import HappyTextToText, TTSettings

# Fix event loop issue
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Load your model
MODEL_NAME = "ThutaNyan/grammar-t5-model"  # Replace with your Hugging Face model name
happy_tt = HappyTextToText("T5", MODEL_NAME)

beam_settings = TTSettings(num_beams=5, min_length=1, max_length=20)

st.title("Grammar Checker App")
st.write("Enter a sentence with incorrect grammar, and I will correct it!")

sentence = st.text_input("Enter a sentence:", "My cat have claws")

if st.button("Correct Grammar"):
    input_text = "grammar: " + sentence
    result = happy_tt.generate_text(input_text, args=beam_settings)
    st.write("✅ Corrected Sentence:", result.text)
