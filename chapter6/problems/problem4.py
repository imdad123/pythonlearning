user_input = input("Enter username:  " )
if len(user_input) < 10:
    print("Username must be at least 10 characters long.")
else:
    print("Username is valid.")