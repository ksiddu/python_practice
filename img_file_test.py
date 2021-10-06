
f1 = open("DC.jpg", "rb")
f2 = open("DC2.jpg", "wb")
for data in f1:
    print(data)
    f2.write(data)