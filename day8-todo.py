f = open("todos.txt", "a")

print("enter data. type exit to finish ")
while True:
    userinput = input()
    if userinput == "exit":
        break
    f.write(userinput + "\n")
    print("add the next letter or type exit: ")
print("data added and file succesfully closed")
f.close()



print("do you want the data. [y/n]")
userinput = input()
if userinput == "y":
    print("these are the data in file")
    f = open("todos.txt", "r")
    for line in f.readlines():
        print(line.strip())
    f.close()







