print("Press show edit or add to manage your todo list")
todos = []
while True:
    user_action = input("Enter add, show, edit, or exit: ")
    match user_action:
        case "add":
            todo = input("Enter a todo item: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "edit":
            print("Your current todos are:",todos)
            todo=int(input("Enter the index of the todo item to edit: "))
            number = todo-1
            new_todo = input("Enter the new todo item: ")
            todos[number]=new_todo
        case "exit":
            print("Exiting the program.")
            break
             