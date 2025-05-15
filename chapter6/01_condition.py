user_input = int(input("Enter your age"))

if user_input >= 18:
    print("You are not eligible to vote")
elif user_input < 0:
    print("Wrong input")
else:
    print("Above the mentioned Age")
