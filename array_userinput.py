from array import *

num = input("enter the number of values")

arr = array('i', [])

for i in range(num):
    x = input("enter the next value")
    arr.append(x)

print(arr)

key = input("enter the key value")

# search for element index

for i in range(num):
    if(arr[i]==key):
        print("index is :", i)
        break

else:
    print("not found")

# search with index function
print(arr.index(key))