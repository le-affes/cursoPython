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
