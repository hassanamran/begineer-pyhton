# first code of the day, its the even odd number checker
usernum = int(input("input a whole number to be checked please: "))
if usernum % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

    # the second code of today. its about a basic calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        # pretty smart chat, wouldnt have done it myself
        print("Can't divide by zero!")
    else:
        print(a / b)
else:
    print("Invalid operator.")

# third one. almost over, this code is about umm password verifier
# day5.py - Part 3
password = "codingomg"
attempt = input("Enter password: ")

if attempt == password:
    print("Access granted.")
else:
    print("Access denied.")
