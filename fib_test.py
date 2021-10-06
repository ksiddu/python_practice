import sys

# nth fibonacci
def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)

fib(10)


# factorial using for loop
def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i

    return f


res= fact(5)
print(res)

# factorial using recursion
def fact_recursion(n):
    if n == 0:
        return 1

    return n * fact_recursion(n - 1)

res1= fact_recursion(4)
print(res1)


print("============================")

# fibonacci < n
def fib_max(n):
    max_count = sys.maxsize
    print(max_count)
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, max_count):
        c = a + b
        if c >=n:
            break;
        else:
            a = b
            b = c
            print(c)

fib_max(100)
print("============================")