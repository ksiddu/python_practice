
#print("Siddu")

# while loop
i = 1
while( i <= 5):
    print("Siddu")
    i+=1



# for loop
string_list = ["Siddu", "Ravi", "Arjun", "Ram", "Ajith"]

print(string_list)

for i in string_list:
    print(i)

integer_list = [10, 20, 30, 40, 50]

print(integer_list)

for i in integer_list:
    print(i)

# https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/

for i in range(len(integer_list)):
    print(i)
    print(integer_list[i])


# a number not divisible by 5
for i in range(1, 21, 1):
    if(i%5 != 0):
        print(i)


# 1 to 100 , not divisible by 3
for i in range(1, 101):
    if(i%3==0):
        continue
    print(i)

print("Bye")

# 1 to 100 , not divisible by 3 and  not divisible by 5
for i in range(1, 101):
    if(i%3==0 or i%5==0):
        continue
    print(i)

print("Bye")

# use pass statement to do nothing, empty braces in other languages
for i in range(1, 101):
    if(i%2!=0):
        pass
    else:
        print(i)

print("Bye")