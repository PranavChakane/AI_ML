import litellm

# Set LiteLLM to talk to Ollama
litellm.model_alias_map = {
    "local-llama": "ollama/llama3.1:8b"  # or mistral, gemma, etc.
}

def rewrite_text(prompt_template, text):
    full_prompt = prompt_template.format(text=text)

    response = litellm.completion(
        model="local-llama",
        messages=[
            {"role": "system", "content": "You are a tone rewriting assistant."},
            {"role": "user", "content": full_prompt}
        ],
        max_tokens=4000,
        temperature=0.7,
    )
    return response["choices"][0]["message"]["content"]
