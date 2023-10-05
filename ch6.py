# 6.1
person = {
    "name": "leandro",
    "age": 22,
    "hair": "brown",
}
print(person)
print("\n\n\n")

# 6.2
favorite_numbers = {
    "leandro": 36,
    "bison": 54,
    "leticia": 16,
    "thais": 17,
}
for person in favorite_numbers.keys():
    print(person.title() + ": " + str(favorite_numbers[person]))
print("\n\n\n")

# 6.3/ 6.4
glossary = {
    "list": "an amout of elements",
    "loop": "a repetition structure",
    "conditional": "a struture who verifies if a condition is true or false",
}
for item in glossary.keys():
    print(str(item).title() + ": " + str(glossary[item]) + ". ")

print("\n")
glossary["int"] = "a variable that keeps a integer number"
for item in glossary.keys():
    print(str(item).title() + ": " + str(glossary[item]) + ". ")
print("\n\n\n")

# 6.5
rivers = {
    "nile": "egypt",
    "amazonas": "brazil",
    "sena": "france",
}
for river in rivers:
    print(
        "The "
        + str(river).title()
        + " runs trought "
        + str(rivers[river]).title()
        + " ."
    )
print("\n\n\n")

# 6.6
favorite_numbers = {
    "leandro": 36,
    "bison": 54,
    "leticia": 16,
    "thais": 17,
}
people = ["leandro", "bison", "leticia", "thais", "vini"]
for person in people:
    if person in favorite_numbers.keys():
        print(str(person).title() + " thanks for responding.")

    elif person not in favorite_numbers.keys():
        print(str(person).title() + " please respond our pool.")
print("\n\n\n")

# 6.7
tmers = {
    "thais": "tiny",
    "vini": "style",
    "gustavo": "beaultiful",
    "ana": "smart",
}
si_babies = {
    "bison": "funny",
    "let": "happy",
    "nat": "jealous",
    "thais": "talkative",
}
friends = [tmers, si_babies]

for group in friends:
    for people in group.items():
        print(people[0].title() + " is " + people[1] + ". ")
print("\n\n\n")

# 6.9
favorite_places = {
    "leandro": ["Sao Paulo", "Rio de Janeiro", "barcelona"],
    "othon": ["bahia", "irlanda"],
    "marcelo": ["barcelona", "rio de janeiro", "sao joao del rei"],
}
for (
    people,
    places,
) in (
    favorite_places.items()
):  # in this case, the first variable kepps the key, and the second keeps the value
    print(people.title() + " favorite place(s) are: ")
    for place in places:
        print(place.title())
    print("\n")
print("\n\n\n")
# 6.11
cities = {
    "divinopolis": {
        "population": "280k",
        "state": "mg",
    },
    "sao paulo": {
        "population": "12m",
        "state": "sp",
    },
}

for city, points in cities.items():
    print("City: " + str(city).title() + " . Points:")
    for point in points:
        print("\t" + point + " : " + points[point])
