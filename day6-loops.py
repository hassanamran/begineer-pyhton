for i in range(5):
    print(f"stay locked in soldier. Day {i+1}")


command = ""
while command != "exit":
    command = input("enter exit to quit: ")

print("the program has ended")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    if num % 2 == 0:
        print(num)
