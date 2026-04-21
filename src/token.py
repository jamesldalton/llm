def tokenizer(text):
    """A simple tokenizer that converts a string into a list of ASCII-like values."""
    chars = list(text) 
    tokens = [encode(x) for x in chars] 
    return tokens

def encode(ch):
    """Encodes a single character into its corresponding token."""
    if ch == '\n':
        return 0 # reserve 0 for newline
    return ord(ch) - 31 # offset to reduce vocab size