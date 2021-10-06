from array import *

# for else loop
# else block is executed when there is no break statement executed

num = 3
for i in range(2, num):
    if num%i==0:
        print("Not Prime")
        break

else:
    print("Prime")
