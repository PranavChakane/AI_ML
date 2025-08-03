
import streamlit as st
#from utils import get_similarity_score

from sentence_transformers import SentenceTransformer, util
from torch import cuda

#model = SentenceTransformer("all-MiniLM-L6-v2")
device = "cuda" if cuda.is_available() else "cpu"
model = SentenceTransformer("paraphrase-multilingual-mpnet-base-v2", device=device)
def get_similarity_score(text1, text2):
    text1 = text1.strip().lower()
    text2 = text2.strip().lower()
    emb1 = model.encode(text1, convert_to_tensor=True, normalize_embeddings=True)
    emb2 = model.encode(text2, convert_to_tensor=True, normalize_embeddings=True)
    return util.cos_sim(emb1, emb2).item()




st.title("🔍 Text Similarity Checker")

text1 = st.text_area("Enter first text")
print(text1)
text2 = st.text_area("Enter second text")

text1 = text1.strip().lower()
text2 = text2.strip().lower()
if st.button("Compare"):
    score = get_similarity_score(text1.lower(), text2.lower())
    st.write(f"Cosine Similarity: {score:.4f}")

# ========================
# week1_text_similarity/utils.py

