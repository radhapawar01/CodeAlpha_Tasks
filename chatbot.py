import json

# Load predefined responses from a JSON file
with open("responses.json", "r") as file:
    responses = json.load(file)

def get_response(user_input):
    """
    Returns a predefined response for the user input.
    If no exact match, returns a default message.
    """
    user_input = user_input.lower().strip()
    return responses.get(user_input, "Sorry, I don't understand that. Can you try something else?")

def start_chat():
    """
    Main function to start the chatbot conversation.
    """
    print("Chatbot: Hello! I am your friendly chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        if user_input.lower() == "bye":
            break

if __name__ == "__main__":
    start_chat()
