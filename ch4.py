# 4.3 Counting to Twenty
numbers = []
for number in range(1, 21):
    numbers.append(number)
print(numbers)
print("\n\n\n")
# 4.4 One Million
numbers = [value for value in range(1, 1000001)]
# print (numbers)
print("\n\n\n")


# 4.5 Summing a million
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print("\n\n\n")


# 4.6
odd = []
for num in range(1, 21, 2):
    odd.append(num)
print(odd)
print("\n\n\n")


# 4.7 Threes
three = [value for value in range(3, 31, 3)]
print(three)
print("\n\n\n")


# 4.8
cubes = []
for cube in range(1, 11):
    cubes.append(cube**3)
print(cubes)
print("\n\n\n")


# 4.9
cubes = [value**3 for value in range(1, 11)]
print(cubes)
print("\n\n\n")

# 4.10
print("The fisrt three items in the list are:" + str(cubes[0:3]))
n = int(len(cubes) / 2)
print("The three items from the middle of the list are: " + str(cubes[n - 1 : n + 2]))
print("The last three items in the list are: " + str(cubes[-3:]))
print("\n\n\n")

# 4.11
my_pizzas = ["marguerita", "calabresa", "bacon"]
friend_pizzas = my_pizzas[:]
friend_pizzas.append("portuguesa")
print("My favorite pizzas are: " + str(my_pizzas))
print("My friend's favorite pizzas are: " + str(friend_pizzas))
print("\n\n\n")


# 4.13
buffet=("arroz", "feijão", "mistura", "salada", "suquinho")
print("Original menu: ")
for food in buffet:
    print(food)
print("\n\n\n")

# 4.14
car="toyota"
print(car=="toyota")