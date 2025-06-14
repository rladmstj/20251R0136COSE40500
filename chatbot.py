def chatbot(input_text):
    if "hello" in input_text.lower():
        return "Hi there!"
    elif "bye" in input_text.lower():
        return "Goodbye!"
    else:
        return "I don't understand."


print(chatbot("Hello, bot!"))
