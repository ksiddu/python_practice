from functools import reduce

nums = [1, 3, 4, 6, 34, 8]

print(nums)

# filter
evens = list(filter(lambda n: n%2==0, nums))
print(evens)

# map
doubles = list(map(lambda n: n*2, evens))
print(doubles)

# reduce , functools
sum = reduce(lambda a,b: a + b, doubles)
print(sum)