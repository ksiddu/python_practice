
def printMsg(name):
    print("Hi", name)


#printMsg("Siddu")

def smart_func(func):
    def inner(name):
        print("Good morning")
        return func(name)
    return inner

f1 = smart_func(printMsg)

# with decorators, passing function to another function
f1(("gavi"))

# without decorators
printMsg("Siddu")
