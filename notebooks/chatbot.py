
import ollama

messages = []

user_input = input("Message: ")

while user_input.lower() != "exit" and user_input.lower() != "quit" and user_input.lower() != "bye":
    messages.append({
        "role": "user",
          "content": user_input})

    response = ollama.chat(
        model="llama3.2:1b",
        messages=messages
    )

    ollama_reply = response["message"]["content"]

    messages.append({
        "role": "assistant",
          "content": ollama_reply})

    print(f"Ollama: {ollama_reply}")
    
    user_input = input("Message: ")

