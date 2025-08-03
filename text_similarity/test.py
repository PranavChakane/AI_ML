from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("paraphrase-multilingual-mpnet-base-v2")
text1 = "I'm going to the market"
text2 = "Voy al mercado"

emb1 = model.encode(text1, convert_to_tensor=True, normalize_embeddings=True)
emb2 = model.encode(text2, convert_to_tensor=True, normalize_embeddings=True)

similarity = util.cos_sim(emb1, emb2).item()
print(f"Cosine Similarity: {similarity:.4f}")
