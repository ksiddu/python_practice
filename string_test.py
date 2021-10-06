
str = "Siddu Kampli"
str1 = "Ilkal"
str2 = "Siddu"
str4 = "Siddu Kampli"


str3 = str + str1
print(str3)

result = str2 in str
print(result)

result1 = str1 in str
print(result1)

result2 = str4 is str
print(result2)


str5 = "  Siddu Kampli  "
print(str5.strip())
print(str5.lstrip())
print(str5.rstrip())