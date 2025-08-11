import json, os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class FAQSearchEngine:
    def __init__(self, faq_file, model_name="sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
                 index_path="faq_index.faiss", emb_path="faq_embeddings.npy", device="cpu"):
        self.model_name = model_name
        self.device = device
        self.model = SentenceTransformer(self.model_name, device=device)

        # load faqs
        with open(faq_file, "r", encoding="utf-8") as f:
            self.faqs = json.load(f)

        # try load embeddings & index from disk if present
        if os.path.exists(emb_path) and os.path.exists(index_path):
            self.embeddings = np.load(emb_path)
            self.index = faiss.read_index(index_path)
        else:
            questions = [faq["question"] for faq in self.faqs]
            # batch/normalize embeddings (float32)
            self.embeddings = self.model.encode(questions, show_progress_bar=True, batch_size=64, normalize_embeddings=True)
            if self.embeddings.dtype != np.float32:
                self.embeddings = self.embeddings.astype("float32").copy()
            dim = self.embeddings.shape[1]
            self.index = faiss.IndexFlatIP(dim)
            self.index.add(self.embeddings)
            # persist
            np.save(emb_path, self.embeddings)
            faiss.write_index(self.index, index_path)

    def search(self, query, top_k=3):
        q_emb = self.model.encode([query], normalize_embeddings=True)
        if q_emb.dtype != np.float32:
            q_emb = q_emb.astype("float32")
        distances, indices = self.index.search(q_emb, top_k)
        results = []
        for i, dist in zip(indices[0], distances[0]):
            faq = self.faqs[int(i)]
            results.append({"question": faq["question"], "answer": faq["answer"], "similarity": float(dist)})
        return results
