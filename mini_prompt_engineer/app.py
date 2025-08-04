import streamlit as st
from prompts.tone_templates import TONE_PROMPTS
from utils.llm_utils import rewrite_text



st.title("🛠️ Tone Emphasizer Engineer")
st.write("Rewriting FAQs or sentences into different tones using LLM prompt templates.")

text = st.text_area("Enter your FAQ or text to rewrite:")
tone = st.selectbox("Choose the tone:", list(TONE_PROMPTS.keys()))

if st.button("Rewrite"):
    if text:
        with st.spinner("Generating..."):
            output = rewrite_text(TONE_PROMPTS[tone], text)
        st.subheader("🔁 Rewritten Output:")
        st.success(output)
    else:
        st.warning("Please enter some text first.")
