from array import *

# array concepts: to store same data type

vals = array('i', [2, 9, 7, -8, 6])

print(vals)
print("Array Size: " + str(vals.buffer_info()[1]))

for val in vals:
    print(val),

print("")

print("Using for loop with index")
for i in range(len(vals)):
    print(vals[i]),

print("")

# copy array in python
newArray = array(vals.typecode, (a for a in vals))

print("Using for each loop")
for e in newArray:
    print(e),

print("")

print("Using while loop")
i = 0
while i<len(newArray):
    print(newArray[i]),
    i+=1

print("")
# factorial logic
num = 5
fact = 1
for i in range(1, num+1):
    fact = fact * i

print("Factorial: ", fact)

