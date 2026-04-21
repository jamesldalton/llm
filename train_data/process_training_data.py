import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from src.token import tokenizer

def process_text_file(input_file_path, output_file_path):
    """Read a text file line by line, tokenize each line, and save tokens to output file."""
    all_tokens = []
    with open(input_file_path, 'r', encoding='utf-8') as infile:
        for line in infile:
            # Strip whitespace and tokenize
            line = line.strip()
            if line:  # Skip empty lines
                tokens = tokenizer(line)
                all_tokens.extend(tokens)
                print(f"Processed: '{line}' -> {len(tokens)} tokens")
    
    # Write the combined array once
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        outfile.write(f"{all_tokens}")
    print(f"Tokenization complete. Total tokens: {len(all_tokens)}. Results saved to {output_file_path}")


def create_input_output_pairs(input_file_path, output_file_path, context_length):
    """Create input-output pairs from tokenized data for training."""
    X, Y = [], []
    with open(input_file_path, 'r', encoding='utf-8') as infile, \
         open(output_file_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            tokens = eval(line.strip())  # Convert string representation of list back to list
            for i in range(len(tokens) - context_length): 
                X.append(tokens[i : i + context_length])      # input sequence
                Y.append(tokens[i + 1 : i + context_length + 1])  # shifted by 1
        outfile.write(f"{X}\n")
        outfile.write(f"{Y}")
    print(f"Input-output pair creation complete. Total pairs: {len(X)}. Results saved to {output_file_path}")

if __name__ == "__main__":
    # Tokenize the training data
    input_file = "train_data/tiny_tinyshakespeare.txt"
    output_file = "train_data/tokenized_shakespeare.txt"
    process_text_file(input_file, output_file)

    # Create input-output pairs for training
    context_length = 8
    input_file = "train_data/tokenized_shakespeare.txt"
    output_file = "train_data/tokenized_shakespeare_pairs.txt"
    create_input_output_pairs(input_file, output_file, context_length)