def greet(name):
    print(F"Hello {name}!")
    greet2(name)
    print("Getting ready to say bye...")
    bye()

def greet2(name):
    print(f"How are you {name}?")
def bye():
    print("Ok bye!")

greet("maggie")