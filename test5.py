import sys
x = 8
r = x % 2


if r == 0:
    print("Even")
    if(x > 5):
        print("Greater than 5")
    else:
        print("Not Greater than 5")
else:
    print("Odd")

print("Bye")