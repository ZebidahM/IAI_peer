def test_chatbot():
    """Runs basic test cases to validate chatbot responses."""
    test_cases = [
        "Which crypto is trending?",
        "What’s the most sustainable coin?",
        "Tell me about long-term investment options.",
        "How does crypto work?",
        "exit"
    ]
    
    for query in test_cases:
        print(f"User: {query}")
        print(f"CryptoBuddy: {chatbot_response(query)}")
        print("-" * 50)

# Run test cases
test_chatbot()
