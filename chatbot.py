# ============================================================
# Rule-Based AI Chatbot
# Artificial Intelligence - Project 1
# ============================================================


def get_response(user_input):
    """
    Generate a response based on predefined rules.
    """

    # Convert user input to lowercase and remove extra spaces
    text = user_input.lower().strip()

    # --------------------------------------------------------
    # GREETINGS
    # --------------------------------------------------------

    if text in ["hello", "hi", "hey"]:
        return "Hello! How can I help you today?"

    elif text in ["good morning", "morning"]:
        return "Good morning! Have a great day!"

    elif text == "good afternoon":
        return "Good afternoon! How can I help you?"

    elif text == "good evening":
        return "Good evening! What can I do for you?"

    # --------------------------------------------------------
    # BASIC CONVERSATION
    # --------------------------------------------------------

    elif "how are you" in text:
        return "I am fine! Thank you for asking."

    elif "your name" in text:
        return "My name is RuleBot. I am a rule-based AI chatbot."

    elif "who are you" in text:
        return "I am RuleBot, a simple chatbot created using Python."

    # --------------------------------------------------------
    # ARTIFICIAL INTELLIGENCE
    # --------------------------------------------------------

    elif "what is ai" in text:
        return (
            "AI stands for Artificial Intelligence. "
            "It is the ability of machines to perform tasks "
            "that normally require human intelligence."
        )

    elif "what is artificial intelligence" in text:
        return (
            "Artificial Intelligence is a technology that enables "
            "machines to perform intelligent tasks."
        )

    # --------------------------------------------------------
    # CHATBOT
    # --------------------------------------------------------

    elif "what is chatbot" in text:
        return (
            "A chatbot is a computer program that communicates "
            "with users through text or voice."
        )

    elif "rule based ai" in text:
        return (
            "Rule-based AI uses predefined rules and conditions "
            "to decide what response should be given."
        )

    # --------------------------------------------------------
    # PYTHON
    # --------------------------------------------------------

    elif "what is python" in text:
        return (
            "Python is a popular programming language known "
            "for its simple syntax and readability."
        )

    elif "why python" in text:
        return (
            "Python is widely used because it is easy to learn "
            "and useful in AI, data science, and web development."
        )

    # --------------------------------------------------------
    # HELP
    # --------------------------------------------------------

    elif "what can you do" in text:
        return (
            "I can respond to predefined questions about AI, "
            "chatbots, Python, and basic conversation."
        )

    elif "help" in text:
        return (
            "You can ask me about AI, chatbots, Python, "
            "or basic conversation."
        )

    # --------------------------------------------------------
    # THANK YOU
    # --------------------------------------------------------

    elif "thank you" in text or text == "thanks":
        return "You're welcome! I am happy to help."

    # --------------------------------------------------------
    # EXIT COMMANDS
    # --------------------------------------------------------

    elif text in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Thank you for chatting with me."

    # --------------------------------------------------------
    # UNKNOWN INPUT
    # --------------------------------------------------------

    else:
        return (
            "Sorry, I don't understand that question. "
            "Please try another question."
        )


# ============================================================
# MAIN CHATBOT PROGRAM
# ============================================================

def start_chatbot():

    print("=" * 55)
    print("              RULE-BASED AI CHATBOT")
    print("=" * 55)

    print("Hello! I am RuleBot.")
    print(
        "You can ask me about AI, chatbots, Python, "
        "or basic questions."
    )
    print("Type 'bye', 'exit', or 'quit' to end the conversation.")
    print("-" * 55)

    # Continuous conversation loop
    while True:

        user_input = input("You: ")

        response = get_response(user_input)

        print("RuleBot:", response)

        # Stop the chatbot when the user enters an exit command
        if user_input.lower().strip() in [
            "bye",
            "goodbye",
            "exit",
            "quit"
        ]:
            break

    print("-" * 55)
    print("Chatbot session ended.")
    print("=" * 55)


# ============================================================
# RUN THE CHATBOT
# ============================================================

if __name__ == "__main__":
    start_chatbot()