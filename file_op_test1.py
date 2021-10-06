
print("***** read entire file contents *****")
f1 = open("MyData", "r")
print(f1.read())

print("***** read line by line *****")
f2 = open("MyData", "r")
line = f2.readline()
#print(line)

while line!="":
    print(line)
    line = f2.readline()


print("***** read line by line using readlines() method *****")
f3 = open("MyData", "r")
lines = f3.readlines()
print(lines)

for line in lines:
    print(line)
