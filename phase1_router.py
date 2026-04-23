from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

model = SentenceTransformer('all-MiniLM-L6-v2')

personas = {
    "bot_A": "I love AI, crypto, and future tech",
    "bot_B": "I hate tech monopolies and care about privacy",
    "bot_C": "I care only about money and markets"
}

ids = list(personas.keys())
texts = list(personas.values())

embeddings = model.encode(texts)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))


def route_post(post):
    emb = model.encode([post])
    D, I = index.search(np.array(emb), k=3)

    for i, idx in enumerate(I[0]):
        sim = 1 / (1 + D[0][i])
        print(ids[idx], "→", round(sim, 2))


route_post("AI replacing developers")