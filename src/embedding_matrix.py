import numpy as np

def create_initial_embedding_matrix(vocab_size, embed_dim):
    """Creates an initial embedding matrix with small random values."""
    return np.random.randn(vocab_size, embed_dim) * 0.01


#TODO: Add embedding matrix creation functions here