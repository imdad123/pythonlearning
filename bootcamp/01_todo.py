todos = []

while True:
    user_input = input("Enter you Option  add view delete exit:  ")
    match user_input:
        case "add":
            todo = input("Enter a new todo: ")
            todos.append(todo)
            print(f"Todo '{todo}' added.")
        case "view":
            if todos:
                print("Your todos:")
                for i, todo in enumerate(todos, start=1):
                    print(f"{i}. {todo}")
            else:
                print("No todos found.")
        case "delete":
            if todos:
                for i, todo in enumerate(todos, start=1):
                    print(f"{i}. {todo}")
                index = int(input("Enter the number of the todo to delete: ")) - 1
                
                if 0 <= index < len(todos):
                    removed_todo = todos.pop(index)
                    print(f"Todo '{removed_todo}' deleted.")  
                else:
                    print("Invalid index. No todo deleted.")
        case "exit":
            print("Exiting the todo application.")
            break
       