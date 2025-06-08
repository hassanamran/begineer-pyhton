

with open("dev/hello-world/python-practice/expenses.csv") as file:
    lines = file.readlines()
total = 0
with open("cleanedexpenses.csv", "w") as f:
    for line in lines[1:]:
        parts = line.strip().split(",")
        if len(parts) == 3 and parts[1] != "" and parts[2].isdigit():
            # only the correct pages may pass
            total += int(parts[2])
            cleanstr = str(f"{parts[1]}: {parts[2]}")
            f.write(cleanstr + "\n")

print("the data is succesfully cleaned and added to the new file titles cleanedexpenses.csv.")
print(f"the sum of total valid entries is: {total}")

View = input("Do you want to see the cleaned file data [y/n] ?\n>")
if View == "y":
    with open("./cleanedexpenses.csv", "r") as read:
        for data in read:
            print(data)
elif View == "n":
    exit()
