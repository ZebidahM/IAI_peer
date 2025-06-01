def validate_input(user_input):
    """Checks if user input contains valid keywords."""
    valid_keywords = ["trending", "sustainable", "investment", "crypto"]
    
    if any(keyword in user_input.lower() for keyword in valid_keywords):
        return True
    else:
        return False

def chatbot_response(user_input):
    """Provides recommendations or prompts user for better queries."""
    if validate_input(user_input):
        return parse_user_query(user_input)
    else:
        return "🤔 I didn't quite get that. Try asking about trends or sustainability!"
