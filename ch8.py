def display_message():
    print("Hi. I'm learning how to make functinos in Python")


display_message()


def get_formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix", "mateo")
print(musician)

# 8.9
magician = ["nibus", "rudini", "merlin"]


def show_magicians(list):
    i = 0
    for element in list:
        i += 1
        print("The " + str(i) + "º magician is " + element.title())


show_magicians(magician)


# 8.10
def make_great(list):
    for element in list:
        aux = list.pop()
        aux = "Great " + aux
        list.insert(0, aux)
    return list


print("\n\n")
# show_magicians(magician)

# 8.11
magician = ["nibus", "rudini", "merlin"]
great_magicians = make_great(magician[:])
show_magicians(great_magicians)
print("\n")
show_magicians(magician)
print("\n\n")


# 8.12
def sandwiches(*items):
    print("Items asked: ")
    for item in items:
        print("-" + item)


sandwiches("bread", "tomatoes")
print("\n\n")


# 8.13
def user_profile(first_name, last_name, **infos):
    profile = {}
    profile["first_name"] = str(first_name).title()
    profile["last_name"] = str(last_name).title()
    for key, value in infos.items():
        profile[key] = value
    return profile


leandro = user_profile("leandro", "arcanjo", sexuality="gay", tall="1,72")

print(leandro)
print("\n\n")


# 8.14
def make_car(manufacter, model, **values):
    car = {}
    car["manufacter"] = manufacter
    car["model"] = model
    for key, value in values.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)