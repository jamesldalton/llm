from src.embedding_matrix import *
import numpy as np

# Create training examples
input_file = "train_data/tokenized_shakespeare_pairs.txt"
batch_size = 16
print(f"Creating training examples from {input_file}...")
print("\tbatch_size:", batch_size)
with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
X = np.array(eval(lines[0].strip())) 
Y = np.array(eval(lines[1].strip()))

idx = np.random.choice(len(X), batch_size, replace=False)
print(f"Randomly selected indices for batch: {idx}")
x_batch = X[idx]  # shape: (batch_size, context_length)
y_batch = Y[idx]  # shape: (batch_size, context_length)

print("Sample input batch (token IDs):", x_batch)
print("Sample output batch (token IDs):", y_batch)

# Create the initial embedding matrix
vocab_size = 96
embed_dim = 32
print("Creating initial embedding matrix...")
initial_embedding_matrix = create_initial_embedding_matrix(vocab_size, embed_dim)
print("Embedding matrix created with shape:", initial_embedding_matrix.shape)
print("\tvocab_size:", vocab_size)
print("\tembed_dim:", embed_dim)

# TODO: understand this part
x_embedded = initial_embedding_matrix[x_batch]  # shape: (batch_size, context_length, embed_dim)
print("Sample embedded input batch shape:", x_embedded.shape)