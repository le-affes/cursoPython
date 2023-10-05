# 3.1 Names
names = ["leandro", "othon", "marcelo"]
print(
    "Os moradores da casa são: "
    + names[0].title()
    + ", "
    + names[1].title()
    + " e "
    + names[2].title()
)
print("\n\n\n")

# 3.4 Guest List
names = ["Nat", "Let", "Byson", "Vini", "Pedro"]

for name in names:
    print("Hi " + name.title() + ", wanna come to my house?\n")
print("\n\n\n")

# 3.5 Changing guest list
names.remove("Vini")
names.append("Matheus")
for name in names:
    print("Hello " + name.title() + ", come for a dinner!\n")
print("\n\n\n")

# 3.6 More Guests
print("Hi y'all. I got a bigger dinner table!\n")
names.insert(1, "Kaue")
names.insert(0, "Rodrigo")
names.append("Davi")
for name in names:
    print("Hi " + name.title() + " come for a diner tomorrow!\n")
print("\n\n\n")

# 3.7 Shrinking Guest List
removed = [names.pop(0), names.pop(2), names.pop(3)]
for rem in removed:
    print("Hi " + rem.title() + " the dinner was cancelled.")
print("\n\n\n")

# 3.8
places = ["Barcelona", "Paris", "Egypt", "Argentina", "Veneza"]
print(places)
print("Sorted list: " + str(sorted(places)))
print("Original list" + str(places))
places.reverse()
print("Reversed list: " + str(places))
places.reverse()
print("Original list: " + str(places))
places.sort()
print("Sorted list: " + str(places))
places.sort(reverse=True)
print("Reverse sorted list: " + str(places))
print("\n\n\n")

# 3.9
print("O numero de convidados é: "+str(len(names)))
