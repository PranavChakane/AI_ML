# ​ Multilingual FAQ Bot – Semantic Best-Match Retrieval

A lightweight, interactive FAQ bot that returns the single most relevant answer to your question—across multiple languages—using **semantic vector search** with Sentence Transformers.

---

##  Project Structure


multilingual_faq_bot/
├── app.py # Streamlit frontend for FAQ queries
├── utils.py # Embedding-based FAQ search logic
├── faq.json # Multilingual FAQ dataset (questions + answers)
└── README.md # Project documentation (this file)


---

##  Features

-  **Multilingual Support** — Handles English, Spanish, French, etc., seamlessly.
-  **Semantic “Best Match”** — Delivers the highest similarity FAQ for your query.
-  **Streamlit UI** — User-friendly web app to interact with your bot.
-  **Fast Retrieval** — Uses vector embeddings and FAISS for quick search.

---

🛠 Tools & Libraries Used
1. FAISS (Facebook AI Similarity Search)
Developed by Meta AI.

High-performance library for vector similarity search and clustering.

Used here to store FAQ embeddings and quickly find the most relevant FAQ to a user’s query.

Instead of searching text directly, FAISS compares semantic vector representations.

2. Sentence Transformers
Python framework for state-of-the-art embeddings.

Here, we use the paraphrase-multilingual-MiniLM-L12-v2 model.

Converts questions and answers into vector embeddings so that semantically similar queries match, even if the wording is different.

3. JSON
Simple format to store FAQs (faq.json).

Easy to extend for more questions and languages.

##  ⚙️ How It Works
1. Load Data
    Read faq.json into memory.

2. Create Embeddings
    Use Sentence Transformers to create vector embeddings for all questions.

3. Index with FAISS
    Store embeddings in a FAISS index for fast nearest-neighbor search.

4. User Query
    When a user asks a question, embed it and search FAISS for the closest match.

5. Return Answer
    Return the matching answer from the dataset.


---

##  Installation & Setup

```bash
# Clone this project or navigate to the multilingual_faq_bot folder
cd multilingual_faq_bot

# (Optional) Set up a virtual environment
python -m venv venv
source venv/bin/activate  # (or use venv\Scripts\activate on Windows)

# Install dependencies
pip install streamlit sentence-transformers faiss-cpu

or 

pip install -r requirements.txt

### Run the App
streamlit run app.py

Example Usage
User Query:¿Cómo puedo cambiar mi contraseña?
Bot Output:

Question: ¿Cómo puedo cambiar mi contraseña?

Answer: Vaya a la configuración y haga clic en 'Restablecer contraseña'.

Similarity: 1.00


Why Semantic Search?
Rather than matching keywords, this approach understands meaning across languages. So even phrasing or languages change, the FAQ with the closest semantic intent is returned.


🔍 Architecture Diagram
flowchart TD
    A[faq.json] --> B[Load FAQs in utils.py]
    B --> C[Generate Multilingual Embeddings]
    C --> D[Store in FAISS Index]
    E[User Query in Any Language] --> F[Generate Embedding for Query]
    F --> G[FAISS Similarity Search]
    G --> H[Find Closest FAQ]
    H --> I[Return Answer]






Next Enhancements
Show top 3 matches instead of just the best match.

Add Visual Feedback like similarity bars or confidence coloring.

Plugin a live FAQ source (like Google Sheets, Airtable, or a database).

Expand to include multilingual answer generation using LLMs.

Credits & License
Created by Pranav as part of the LLM learning journey.
Powered by Sentence Transformers and Streamlit — great tools for building semantic apps.

MIT License — feel free to fork, tweak, and extend!