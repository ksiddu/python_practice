# function definition and function call

# just print, nothing to return
def greetMorning():
    print("Hello")
    print("Good morning")

# just print, nothing to return
def greetAfterNoon():
    print("Hello")
    print("Good afternoon")

# return single value
def add(x, y):
    print(x+y)

# return single value
def sub(x, y):
    return x-y

# return multiple values as tuple
def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d

# call functions
greetMorning()
greetAfterNoon()
add(1, 2)
result = sub(10, 5)
print("Sub is :", result)

result1, result2 = add_sub(10, 4)

print("Add result is :", result1)
print("Sub result is :", result2)

result3 = add_sub(10, 2)

print("Add result is :", result3[0])
print("Sub result is :", result3[1])