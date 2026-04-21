#!/usr/bin/env python3
"""
Main entry point for the LLM project.
Executes LLM functions in a defined sequence.
"""

from src.token import tokenizer

def main():
    """Main function to run LLM operations in sequence."""
    print("Starting LLM operations...")

    # Example 1: Tokenize a simple string
    text1 = "Hello, world!"
    tokens1 = tokenizer(text1)
    print(f"Tokens for '{text1}': {tokens1}")

    # Example 2: Tokenize an empty string
    text2 = ""
    tokens2 = tokenizer(text2)
    print(f"Tokens for empty string: {tokens2}")

    # Example 3: Tokenize a longer text
    text3 = "This is a test of the tokenizer."
    tokens3 = tokenizer(text3)
    print(f"Tokens for '{text3}': {tokens3}")

    print("LLM operations completed.")

if __name__ == "__main__":
    main()