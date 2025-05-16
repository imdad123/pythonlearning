user_input1 = int(input("Enter number 1: "))
user_input2 = int(input("Enter number 2: "))
user_input3 = int(input("Enter number 3: "))
user_input4 = int(input("Enter number 4: "))

if user_input1 > user_input2 and user_input1 > user_input3 and user_input1 > user_input4:
    print("The largest number is: " + str(user_input1))
if user_input2 > user_input1 and user_input2 > user_input3 and user_input2 > user_input4:
    print("The largest number is: " + str(user_input2))
if user_input3 > user_input1 and user_input3 > user_input2 and user_input3 > user_input4:
    print("The largest number is: " + str(user_input3))
if user_input4 > user_input1 and user_input4 > user_input2 and user_input4 > user_input3:
    print("The largest number is: " + str(user_input4))