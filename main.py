from chatbot import Chatbot

bot = Chatbot()


while True: 
    user_message = input("\n You: ")

    if user_message.lower()== "exit":
        
        print("Chat ended!")
        break
    answer= bot.chat(user_message)

    print("\n AI: ", answer)