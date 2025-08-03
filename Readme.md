# 🔍 Text Similarity App (Multilingual Powered by Transformers)

This is a simple and interactive Streamlit app that lets you compare **how semantically similar two texts are**, even if they're written in **different languages**. It uses powerful **sentence embeddings** to measure meaning — not just word overlap.

---

## 🌍 Features

✅ Compare meaning, not just keywords  
✅ Works in **multiple languages** (English, Hindi, Spanish, French, etc.)  
✅ Built with `sentence-transformers/paraphrase-multilingual-mpnet-base-v2`  
✅ Clean web UI using Streamlit  
✅ GPU-accelerated (if available)

---

## 🧠 What Are Sentence Embeddings?

Sentence embeddings are fixed-size vector representations of sentences that capture their **semantic meaning**.

We use:
```
sentence-transformers/paraphrase-multilingual-mpnet-base-v2
```
This model is fine-tuned to place **similar sentences in multiple languages closer together in vector space**.

### ✨ Example:
```
Text A: "The weather is great today."
Text B: "Aujourd’hui, il fait beau." (French)

✅ Cosine Similarity ≈ 0.85 (semantically close!)
```

---

## 🔧 Tech Stack

| Tool | Purpose |
|------|---------|
| `Streamlit` | UI framework for the app |
| `sentence-transformers` | Pretrained embedding model |
| `torch` | ML backend |
| `paraphrase-multilingual-mpnet-base-v2` | Cross-lingual semantic encoder |

---

## 🛠 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/text_similarity_app.git
cd text_similarity

# Create a virtual environment (optional but recommended)
python -m venv llm_env
source llm_env/bin/activate  # or llm_env\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then visit:  
👉 http://localhost:8501

---

## 🔬 How It Works

1. You enter two texts (in any supported language).
2. The model encodes them into 768-dimensional embeddings.
3. It calculates the **cosine similarity** between them.
4. The app shows a similarity score between **0 and 1**:
   - `1.0` → Perfect match
   - `0.0` → Totally unrelated

---

## 🧪 Sample Test Cases

| Text A | Text B | Language | Similarity |
|--------|--------|----------|------------|
| "I am going to the market" | "Voy al mercado" | English/Spanish | ~0.98 |
| "The cat is sleeping" | "Le chat dort" | English/French | ~0.98 |
| "Where are you?" | "How old are you?" | English/English | ~0.48 |

---

## 💡 Use Cases

- ✅ **Multilingual duplicate detection**
- ✅ **Cross-language plagiarism check**
- ✅ **Semantic search**
- ✅ **Cross-lingual Q&A matching**
- ✅ **Chatbot intent matching (multi-language)**

---

## 🧱 Requirements

| Package | Version |
|---------|---------|
| `streamlit` | ≥ 1.20 |
| `sentence-transformers` | ≥ 2.2.2 |
| `torch` | ≥ 1.12 |
| `transformers` | ≥ 4.24 |

---

## 📦 `requirements.txt`

```
streamlit
sentence-transformers
torch
transformers
```

---

## 🧠 Model Info: paraphrase-multilingual-mpnet-base-v2

- 🌍 Supports 50+ languages
- 🔬 Fine-tuned for paraphrase detection
- 🧠 Embedding size: 768
- 🐢 Speed: Moderate (fast on GPU)
- 🏋️ Training: SBERT on multilingual data

Model card: [Hugging Face link](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2)

---

## 📸 Screenshots

<sub><img width="1571" height="752" alt="image" src="https://github.com/user-attachments/assets/420b534d-6cb2-4754-9b6c-abeb84f8c485" />
</sub>

<sub><img width="1521" height="767" alt="image" src="https://github.com/user-attachments/assets/72bedcd6-bab4-408a-a23e-9c7f183e741f" />
</sub>
---

## 🙏 Credits

- [UKP Lab – TU Darmstadt](https://www.ukp.tu-darmstadt.de/) for Sentence Transformers
- [Hugging Face](https://huggingface.co/) for hosting awesome models

---
