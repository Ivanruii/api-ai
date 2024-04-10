from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import pairwise_distances
import numpy as np

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# The differences between phrases are calculated, 
# first the embeddings are coded and the distance between them is calculated, 
# then the difference between each phrase is calculated.

def calculate_differences(sentences):
    embeddings = model.encode(sentences)
    embeddings = np.array([emb / np.linalg.norm(emb) for emb in embeddings])
    distances = pairwise_distances(embeddings, metric='cosine')
    differences = [float(distances[i, j]) for i in range(len(sentences)) for j in range(i+1, len(sentences))]
    return differences
