print("choose an action from the following: add/ show/ delete/ search/ exit")
filename = "todos2.txt"
while True:

    useroption = input()

    # for adding
    if useroption == 'add':
        print("Enter your todo:")
        usertodo = input("> ")

        with open(filename, "a") as f:
            f.write(usertodo + "\n")
        print("Todo added.")

    # for showing.
    elif useroption == 'show':
        print("here are your todos mate: ")
        with open(filename, "r") as f:
            todos = f.readlines()
        # using enumerate. its used to index directly. we made todo to store each element from list todos
        for i, todo in enumerate(todos):
            print(f"{i + 1}. {todo.strip()}")

    elif useroption == "delete":
        print("enter the number of Todo to delete")
        with open(filename, "r") as f:
            todos = f.readlines()
            # we display list again for user to select the number
            for i, todo in enumerate(todos):
                print(f"{i + 1}. {todo.strip()}")

            choice = int(input(">"))
            if 1 <= choice <= len(todos):
                # subtract 1 because there a zero based indexing in the todos list
                todos.pop(choice - 1)

                # Now rewrite the entire file with the remaining todos
                with open(filename, "w") as f:
                    for todo in todos:
                        f.write(todo)
                        print("Todo deleted.")
            else:
                print("Invalid number!")

    elif useroption == "search":
        print("enter keyword to search for")
        keyword = input("> ")
        with open(filename, "r") as f:
            todos = f.readlines()
            # loop to find keyword
        flag = True
        for i, todo in enumerate(todos):
            if keyword in todo:
                print(f"{i+1}. {todo.strip()}")
                flag = False
                print("keyword found and deleted")

        if flag == True:
            print("keyword not find")

    elif useroption == 'exit':
        print("Goodbye!")
        break
    else:
        print("invalid option. kindly select from the given ones above")
