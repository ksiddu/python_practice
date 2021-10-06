
# list is mutable and generic
# can contain multiple data type values
# https://www.programiz.com/python-programming/methods/list/index

list = [13, 1, 9, 2, 5]

print(list)

# using indexing
print(list[0])
print(list[4])

# to get the entire list
print(list)

# to get the entire list
print(list[0:])

# to get the entire list
print(list[:])

# to get the last element
print(list[-1])

# to get the last second element
print(list[-2])

# to get the minimum element
print(min(list))

# to get the maximum element
print(max(list))

# to get the sort element using sorted method which doesn't change the original list
print(sorted(list))

# original elements
print(list)

new_list = sorted(list, reverse=True)

# to get in descending order using sorted method which doesn't change the original list
print(new_list)

# to get in ascending & descending order using the list's sort method which changes the original list
list2 = [90, 1, 34, 36, 50]
print(list2)
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)

# tuple: its a list whose elements can't be changed [immutable], only 2 methods: count and index

values = (10, 3, 4, 6, 9, 4, 7, 4)

print(values)

print(values.index(4))

print(values.count(4))

# set: its a list whose elements are unique, doesn't maintain the order

my_set = {50, 5, 4, 8, 9}

print(my_set)

my_set.add(10)

print(my_set)

my_set.pop()

print(my_set)

# list methods
print("List methods")
list2 = [100, 10, 90, 20, 50]

print(list2)

# to add element at the end
list2.append(80)

print(list2)

# to add element at the specified index
list2.insert(1, 70)
print(list2)

list3 = [1, 2, 3, 4]

# to add another list at the end
list2.extend(list3)

print(list2)

# to delete last element
list2.pop()

# to delete specified element
list2.remove(70)

# to delete  element at the specified index
list2.pop(0)

print(list2)

# to reverse
list2.reverse()

print(list2)