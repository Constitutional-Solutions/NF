import time
from sentence_transformers import SentenceTransformer
import numpy as np

# Load MiniLM Locally (Sovereign AI)
# This will download once, then run offline forever.
print("Loading Cortex (MiniLM-L6-v2)...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Cortex Online.")

def get_embedding(text):
    """Converts text to vector for the Vector Database."""
    return model.encode(text)

def compare_resonance(text1, text2):
    """Calculates similarity between two thoughts."""
    vec1 = get_embedding(text1)
    vec2 = get_embedding(text2)
    # Cosine Similarity
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))