print("welcome! \n Enter password please")
password = input()
# just learnt it from google very useful
hasupper = any(c.isupper() for c in password)
haslower = any(c.islower() for c in password)
# for checking 8 letters
has8char = False
if len(password) >= 8:
    has8char = True
# for checking special character. saw this one on google too wile looking up any()
hasspecial = any(not c.isalnum() for c in password)
# for checking digit. came up with this on my own through deduction
hasdigit = any(c.isdigit() for c in password)

if has8char and hasspecial and hasdigit and haslower and hasupper:
    print("Congrats, your password is valid")
else:
    print("password invalid. please try again")
