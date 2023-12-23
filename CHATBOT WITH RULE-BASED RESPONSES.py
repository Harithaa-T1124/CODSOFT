print("WELCOME TO HTCHATBOT")
def get_response(user_input):
    # Convert user input to lowercase
    user_input = user_input.lower()

    # Defining rules and responses
    if "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "good morning" in user_input:
        return "Good Morning! How can I assist you today?"
    elif "good afternoon" in user_input:
        return "Good Afternoon! How can I assist you today?"
    elif "good evening" in user_input:
        return "Good Evening! How can I assist you today?"
    elif "good night" in user_input:
        return "Good Night! If you have any more questions or need assistance in the future, feel free to reach out. Have a restful sleep! Take care!. Now you can 'exit' the ongoing session."
    elif "how are you" in user_input or "how are you doing" in user_input:
        return "I'm just a chatbot,I don't have feelings but thanks for asking! How can I help you?"
    elif "what is your name" in user_input or "who are you" in user_input:
        return "I am HTchatbot."
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome!"
    elif "who made you" in user_input:
        return "I was coded by Ms. Harithaa"
    elif "are you a human" in user_input or "are you a robot" in user_input:
        return "I am a Chatbot.My purpose is to assist and provide information to the best of my abilities,I'm here to help with your questions or concerns you may have!"
    else:
        return "I'm sorry, I don't understand. Could you please rephrase your question?"


# To interact with the chatbot
def main():
    print("Chatbot: Hello! I hope you are doing great. How can I assist you today?")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)


if _name_ == "_main_":
    main()

'''
OUTPUT:

WELCOME TO HTCHATBOT
Chatbot: Hello! I hope you are doing great. How can I assist you today?
You: hello
Chatbot: Hello! How can I assist you today?
You: good morning
Chatbot: Good Morning! How can I assist you today?
You: good afternoon
Chatbot: Good Afternoon! How can I assist you today?
You: good evening
Chatbot: Good Evening! How can I assist you today?
You: how are you
Chatbot: I'm just a chatbot,I don't have feelings but thanks for asking! How can I help you?
You: what is your name
Chatbot: I am HTchatbot.
You: thanks
Chatbot: You're welcome!
You: who made you
Chatbot: I was coded by Ms. Harithaa
You: are you a robot
Chatbot: I am a Chatbot.My purpose is to assist and provide information to the best of my abilities,I'm here to help with your questions or concerns you may have!
You: how old are you
Chatbot: I'm sorry, I don't understand. Could you please rephrase your question?
You: exit
Chatbot: Goodbye! Have a great day!

'''
