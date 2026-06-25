from ai import stream_response

print("Notes Assistant — ask me anything. Type 'quit' to exit.\n")

while True:
    question = input("You: ").strip()

    if question == "":
        continue

    if question.lower() == "quit":
        print("Goodbye!")
        break

    print("\nAssistant: ", end="")
    stream_response(question)
    print()