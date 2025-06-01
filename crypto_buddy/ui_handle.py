def chat_loop():
    """Handles continuous user interaction."""
    print("Welcome to CryptoBuddy! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("CryptoBuddy: Thanks for chatting! 🚀 See you soon!")
            break
        else:
            response = chatbot_response(user_input)
            print(f"CryptoBuddy: {response}")

# Start chatbot loop
chat_loop()
