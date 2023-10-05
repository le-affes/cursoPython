# 5.8 /  5.9
users = ["admin", "leandro", "othon", "marcelo"]

if users:
    for user in users:
        if user == "admin":
            print("Hello admin, would you like to see a status report? ")
        else:
            print("Hello " + str(user) + ", thanks for comming.")

else:
    print("Find some users.")
print("\n\n\n")

# 5.9 / 5.10
current_users = ["admin", "leandro", "othon", "marcelo"]
new_users = ["thais", "juliana", "Othon", "leaNdro"]

for nuser in new_users:
    avaliable = True

    for cuser in current_users:
        if nuser.casefold() == cuser.casefold():
            avaliable = False
    
    if avaliable:
        print(str(nuser) + " is avaliable.")
    else:
        print(str(nuser) + " is not avaliable.")
print("\n\n\n")

# 5.11
num=[number for number in range (1,10)]
for n in num:
    if(n==1):
        print(str(n)+"st")
    elif(n==2):
        print(str(n)+"nd")
    elif(n==3):
        print(str(n)+"rd")
    elif(n>3):
        print(str(n)+"th")