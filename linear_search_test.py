
list = [4, 2, 3, 56, 8, 9, 10]
n = 9
pos = -1

def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
    return False

result = search(list, n)
if result:
    print("Found at index", pos)
else:
    print("Not Found")
