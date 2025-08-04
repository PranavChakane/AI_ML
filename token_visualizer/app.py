import streamlit as st
import pandas as pd
import altair as alt
from utils.tokenizer_utils import tokenize_text, get_tokenizer_description

st.set_page_config(page_title="Tokenization Visualizer", layout="wide")

st.title("🔤 Tokenization Visualizer")
st.markdown("""
This tool shows how different tokenizers split your text into pieces.  
Tokens are the building blocks language models use to process input.
""")

model_name = st.selectbox("Choose a tokenizer", ["gpt2", "bert-base-uncased", "roberta-base"])

with st.expander("📘 Tokenizer Introduction"):
    st.markdown(get_tokenizer_description(model_name))

text = st.text_area("✍️ Enter text to tokenize", placeholder="e.g. What's the best way to learn LLMs?")

if st.button("🔍 Tokenize"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        tokens, ids, types = tokenize_text(text, model_name)

        df = pd.DataFrame({
            "Token": tokens,
            "Token ID": ids,
            "Token Type": types,
            "Length": [len(tok) for tok in tokens],
        })

        st.subheader("🧱 Token Table")
        st.dataframe(df, use_container_width=True)

        st.subheader("📊 Token Length Chart")
        chart = alt.Chart(df.reset_index()).mark_bar().encode(
            x=alt.X("Token:N", sort=None),
            y="Length:Q",
            color="Token Type:N",
            tooltip=["Token", "Length", "Token Type"]
        ).properties(width=700, height=300)
        st.altair_chart(chart, use_container_width=True)

        st.markdown(f"**🔢 Total Tokens:** `{len(tokens)}`")
