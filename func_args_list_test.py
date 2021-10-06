import sys

list = [1, 2, 3, 4, 5]

def printEven(list):
    for i in list:
        if i % 2 == 0:
            print(i)

        else:
            pass

printEven(list)


list1 = [1, 2, 3, 4, 5]

def printSquare(list):
    for i in list:
        if i % 2 == 0:
            print(i * i)

printSquare(list1)

# can modify the list passed by value since list is mutable
list2 = [1, 2, 3, 4, 5]
def update(length):
    length = len(list2)
    print(length)
    for i in range(0, length):
        if list2[i] % 2 == 0:
            print("even")
            list2[i] = "even"

update(list2)
print(list2)

# to pass list as argument and return multiple values
def CountEvenOrOdd(list):
    even = 0
    odd = 0
    for i in list:
        if i % 2 == 0:
            even += 1

        else:
            odd += 1
    return even, odd

list3 = [1, 2, 3, 4, 5]

even, odd = CountEvenOrOdd(list3)

print("Even count ", even)
print("Odd count ", odd)

list4 = ["Siddu", "Yuvraj", "Sachin", "Navin", "Kampli"]

def count(list):
    count = 0
    for i in list:
        length = len(i)
        if length > 5:
            count+=1
    return count


result = count(list4)
print("No of names {}".format(result))