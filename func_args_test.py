# four kinds: index, keyword, default, variable length arguments

# type1: index
def add(x, y):
    c = x + y
    return c

result = add(10, 5)

print("result ", result)

# type1: index
def person1(name, age):
    print(name)
    print(age)
    print(age - 5)

person1("Siddu", 33)


# type2: keyword
def person2(name, age):
    print(name)
    print(age)
    print(age - 5)

person2(age=33, name="Siddu")

# type3: default even if age is not passed, it will take default value
def person3(name, age=18):
    print(name)
    print(age)

person3("Siddu")

# type4: variable length arguments
def sum1(a, *b):
    c = a
    for i in b:
        c = c + i
    print("Sum ", c)

sum1(1)
sum1(1, 2)
sum1(1, 2, 3)

# type4: variable length arguments
def sum2(*a):
    c = 0
    for i in a:
        c = c + i
    print("Sum ", c)

sum2(1)
sum2(1, 2)
sum2(1, 2, 3)


# keyworded variable length arguments
def person4(name, **data):
    print(name)
    #print(data)
    for i,j in data.items():
        print(i,j)

person4("Siddu1", age=23, city='Singapore')

person4("Siddu2", age=23, city='Singapore', mob=123455)