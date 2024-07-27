import re

def chatbot_response(user_input, context):
    # Convert the user input to lowercase to make the matching case-insensitive
    user_input = user_input.lower()

    # Personalization: remember user's name
    name_match = re.search(r'\bmy name is (\w+)', user_input)
    if name_match:
        name = name_match.group(1)
        context['name'] = name
        return f"Nice to meet you, {name}!"
    
    # Define responses for specific user inputs
    if "hello" in user_input or "hi" in user_input:
        if 'name' in context:
            return f"Hello, {context['name']}! How can I assist you today?"
        else:
            return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm functioning as expected. How about you?"
    elif "your name" in user_input:
        return "I am a simple rule-based chatbot."
    elif "help" in user_input:
        return "Sure! What do you need help with?"
    elif "joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "weather" in user_input:
        return "I'm not equipped to provide weather updates, but you can check a weather app for that!"
    elif "thank you" in user_input:
        return "You're welcome!"
    elif "codsoft" in user_input:
        return "Codsoft is an IT services and IT consultancy company that specializes in creating innovative solutions."
    elif "bye" in user_input:
        if 'name' in context:
            return f"Goodbye, {context['name']}! Have a great day!"
        else:
            return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Main loop to interact with the user
if __name__ == "__main__":
    context = {}
    print("Chatbot: Hi! I am a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            if 'name' in context:
                print(f"Chatbot: Goodbye, {context['name']}! Have a great day!")
            else:
                print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input, context)
        print(f"Chatbot: {response}")
