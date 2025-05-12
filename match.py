
todos =[]
while True:
     user_action = input("Enter add or view :")
     match user_action:
         case "add":
            todo = input("Enter a todo item: ")
            todos.append(todo)
         case "view":
             for todo in todos:
                 print(todo)
             print("Your todos are:",todos)
         case "exit":
                print("Exiting the program.")
                break