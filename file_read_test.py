
f1 = open("MyData", "r")

print(f1)
#print(f.read())

print(f1.readline(), end="")
print(f1.readline(), end="")
print(f1.readlines())

f2 = open("MyData", "r")

f3 = open("abc", "w")

for data in f2:
    f3.write(data)