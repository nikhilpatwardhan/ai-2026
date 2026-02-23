import ollama


def run_prompt(model: str, prompt: str) -> str:
    response = ollama.chat(
        model=model, messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


if __name__ == "__main__":
    response = run_prompt("smollm2", "Why is the sky blue?")
    print(response)
