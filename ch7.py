# 7.8
sandwich_orders = ["x-salad", "x-bacon", "x-egg"]
finished_sandwichs = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(sandwich + " finished.")
    finished_sandwichs.append(sandwich)

print(finished_sandwichs)
print("\n\n\n")

# 7.9
sandwich_orders = ["x-salad", "pastrami", "x-bacon", "pastrami", "x-egg"]
print(sandwich_orders)

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print(sandwich_orders)
print("\n\n\n")

# 7.10
aux = True
dreams = {}
while aux:
    name = input("What is your name? ")
    dream = input("What is your dream? ")
    dreams[name] = dream
    ans = input("Would you like someone else to ask? (Y/N)")
    if (ans == "N") or (ans == "n"):
        aux = False

print("\n")
for name in dreams.keys():
    print(name.title() + "'s dream is " + str(dreams[name]) + ".")

