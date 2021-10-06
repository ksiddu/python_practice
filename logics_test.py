
# first 50 fibonacci numbers
fib1 = 0
fib2 = 1
print(fib1)
print(fib2)
list = [];
list.append(fib1)
list.append(fib2)
for i in range(2, 50,1):
    fib = fib1 + fib2
    fib1 = fib2;
    fib2 = fib
    list.append(fib)
    print(fib)

print("Length of list")
print(len(list))
print(list)

# check a given number is prime or not: 3, 8
x = 3
flag = True
for i in range(2, x/2 + 1, 1):
    print(i)
    if(x%i==0):
        flag = False
        break;

if flag:
    print("Prime")

else:
    print("Not Prime")



# stars logic

#i = 5
for i in range(1, 6, 1):
    if(i <= 5):
        j = 1
        for j in range(1, i+1, 1):
            print("*"),

    print("")

# numbers logic
for i in range(1, 5, 1):
    for j in range(5-i):
        print(j + 1),

    print("")
