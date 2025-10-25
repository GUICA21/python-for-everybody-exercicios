def thing():
    print("Hello World")


thing()
print("Done")
thing()


def greet(lang):

    if lang == "English":
        print("Hello World")
    elif lang == "Spanish":
        print("Hola")
    else:
        print("Sorry, I don't understand that")


greet("English")
greet("Spanish")
greet("Portuguese")
