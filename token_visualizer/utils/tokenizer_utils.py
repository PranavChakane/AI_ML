from transformers import AutoTokenizer

def tokenize_text(text, model_name="gpt2"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Encode text with special tokens
    encoding = tokenizer(text, return_tensors="pt", return_attention_mask=False, add_special_tokens=True)

    input_ids = encoding["input_ids"][0].tolist()
    tokens = tokenizer.convert_ids_to_tokens(input_ids)

    # Classify each token
    token_types = []
    for tok in tokens:
        if tok in tokenizer.all_special_tokens:
            token_types.append("special")
        elif tok.startswith("##") or tok.startswith("▁"):
            token_types.append("subword")
        else:
            token_types.append("word")

    return tokens, input_ids, token_types

def get_tokenizer_description(model_name):
    descriptions = {
        "gpt2": """
**GPT-2 Tokenizer**  
- Byte-Pair Encoding (BPE)  
- No special tokens like `[CLS]` or `[SEP]`  
- Uses raw text format  
""",
        "bert-base-uncased": """
**BERT Tokenizer (base-uncased)**  
- WordPiece encoding  
- Lowercases input  
- Adds `[CLS]` at start and `[SEP]` at end  
""",
        "roberta-base": """
**RoBERTa Tokenizer**  
- Byte-Pair Encoding with whitespace marker (`▁`)  
- No `[CLS]` or `[SEP]`, uses special tokens like `<s>`, `</s>`  
"""
    }
    return descriptions.get(model_name, "No description available.")
