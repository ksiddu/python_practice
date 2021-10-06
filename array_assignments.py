from array import *
import time

start_time = time.time()

# to delete 2nd index value without inbuilt function
arr1 = array('i', [11, 22, 33, 44, 55])

print(arr1)

index = 2;
#arr.remove(30)

for i in range(len(arr1)):
    if(i==2):
        arr1.remove(arr1[i])

print(arr1)

# to reverse an array without inbuilt function

arr2 = array('i', [10, 20, 30, 40, 50])
length = len(arr2) - 1
print(arr2)


arr3 = array('i', [])
for i in range(length, -1, -1):
    arr3.append(arr2[i])

print(arr3)

# to reverse the range function

for i in reversed(range(10)):
    print(i)

print("--- %s seconds ---" % (time.time() - start_time))