
import streamlit as st
from utils import get_similarity_score

st.title("🔍 Text Similarity Checker")

text1 = st.text_area("Enter first text")
print(text1)
text2 = st.text_area("Enter second text")

if st.button("Compare"):
    score = get_similarity_score(text1, text2)
    st.write(f"Cosine Similarity: {score:.4f}")

# ========================
# week1_text_similarity/utils.py

from sentence_transformers import SentenceTransformer, util
from torch import cuda

#model = SentenceTransformer("all-MiniLM-L6-v2")
device = "cuda" if cuda.is_available() else "cpu"
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-mpnet-base-v2", device=device)
def get_similarity_score(text1, text2):
    emb1 = model.encode(text1, convert_to_tensor=True)
    emb2 = model.encode(text2, convert_to_tensor=True)
    return util.cos_sim(emb1, emb2).item()
