def greet():
    print("hello")
    print("welcome")
    print("this is a function")

greet()

#function with parameters

def greet_with_name(name):
    print(f"hello {name}")
    print(f"welcome {name}")
    print("this is a function")

greet_with_name("Angela")

#functions with multiple parameters

def name_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in {location}")

name_with("Angela", "London")