import streamlit as st
from utils import FAQSearchEngine


@st.cache_resource
def get_engine():
    return FAQSearchEngine("faq.json")

st.set_page_config(page_title="🌍 Multilingual FAQ Search Bot", page_icon="🤖")

st.title("🌍 Multilingual FAQ Search Bot")
st.write("Ask your question in **any language**. We'll find the best matching FAQ.")


faq_bot = get_engine()

query = st.text_input("❓ Enter your question here:")

if query:
    results = faq_bot.search(query)
    
    if results:
        best_match = results[0]  # Assuming results are already sorted by similarity
        st.subheader("🔍 Best Match")
        st.write(f"**Question:** {best_match['question']}")
        st.write(f"**Answer:** {best_match['answer']}")
        st.write(f"**Similarity:** {best_match['similarity']:.4f}")
    else:
        st.warning("No similar question found.")