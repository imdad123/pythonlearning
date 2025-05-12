userinput = input("Enter a string: ")
print("You entered:", userinput)


while True:
     user_input = input("Enter a string: ")
     if user_input == "exit":
         print("Exiting the program.")
         break
     else:
         print("You entered:", user_input)
     
todos = []
while True:
    todo = input("Enter a todo item (or 'exit' to quit): ")
    if todo.lower() == 'exit':
        print("Exiting the program.")
        break
    else:
        todos.append(todo)
        print("Todo item added:", todo)