spam_list =["Make a lot of money","Buy now", "Limited time offer", "Subscribe this", "Click this"]
user_input = input("Enter your message: ")
if user_input.capitalize() in spam_list:
    print("This message is spam")