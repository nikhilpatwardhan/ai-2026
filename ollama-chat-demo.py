import ollama


def main():
    response = ollama.chat(model='smollm2', messages=[
        {
            'role': 'user',
            'content': 'Why is the sky blue?'
        }
    ])
    print(response['message']['content'])


if __name__ == "__main__":
    main()
