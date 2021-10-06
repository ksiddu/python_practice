
def square(a):
    return a*a
# anonymous expression : single line statements without function name
f1 = lambda a: a*a


result = square(5)
print(result)

result1 = f1(5)
print(result1)

# greater than
f2 = lambda a, b: a > b
result2 = f2(6, 2)

print(result2)

# even or odd with ternary
f3 = lambda a: "even" if a % 2 == 0 else "odd"
result3 = f3(6)

print(result3)
