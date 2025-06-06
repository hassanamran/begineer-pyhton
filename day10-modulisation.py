
def add(parafile):
    print("Enter your todo:")
    usertodo = input("> ")

    with open(parafile, "a") as f:
        f.write(usertodo + "\n")
        print("Todo added.")


def show(parafile):
    print("here are your todos mate: ")
    with open(parafile, "r") as f:
        todos = f.readlines()
        # using enumerate. its used to index directly. we made todo to store each element from list todos
        for i, todo in enumerate(todos):
            print(f"{i + 1}. {todo.strip()}")


def delete(parafile):
    print("enter the number of Todo to delete")
    with open(parafile, "r") as f:
        todos = f.readlines()
        # we display list again for user to select the number
        for i, todo in enumerate(todos):
            print(f"{i + 1}. {todo.strip()}")

        choice = int(input(">"))
    if 1 <= choice <= len(todos):
        # subtract 1 because there a zero based indexing in the todos list
        todos.pop(choice - 1)

        # Now rewrite the entire file with the remaining todos
        with open(parafile, "w") as f:
            for todo in todos:
                f.write(todo)
                print("Todo deleted.")
    else:
        print("Invalid number!")


def search(parafile):
    print("enter keyword to search for")
    keyword = input("> ")
    with open(parafile, "r") as f:
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

    else:
        print("invalid option. kindly select from the given ones above")


def main():
    while True:
        print("\nChoose an action: add / show / delete / search / exit")
        useroption = input(">")
        filename = "todos2.txt"
        if useroption == 'add':
            add(filename)
        elif useroption == 'show':
            show(filename)
        elif useroption == 'delete':
            delete(filename)
        elif useroption == 'search':
            search(filename)
        elif useroption == "exit":
            exit()
