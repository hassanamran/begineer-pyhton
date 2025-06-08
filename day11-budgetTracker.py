def addIncome(pbalance, plog):
    print("Add amount to be added to the income please")
    amount = float(input(">"))
    pbalance += amount
    print("enter description please")
    userdesc = input(">")
    plog.append({"type": "income", "desc": userdesc, "amount": amount})
    return pbalance


def addexpense(pbalance, plog):
    userexpense = float(input("Enter expense\n>"))
    pbalance = pbalance - userexpense
    userdesc = input("Enter description of the expense please\n>")
    plog.append({"type": "expense", "desc": userdesc, "amount": -userexpense})
    return pbalance


def main():
    balance = 0
    log = []
    print("Welcome. Please enter what you would like to do:")
    print("Type addinc to add income\nType addexp to add expense\nType balance to view balance\nType log to view transaction log.\nOr type exit to end program ")

    while True:
        useropt = input(">")
        if useropt == "addinc":
            balance = addIncome(balance, log)
        elif useropt == "addexp":
            balance = addexpense(balance, log)
        elif useropt == "balance":
            print(balance)
        elif useropt == "log":
            for transactions in log:
                print(transactions)
        elif useropt == "exit":
            break
