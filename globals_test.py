
a = 10

def something():

    a = 15

    print("in function", a)

# with global keyword
def something1():
    global a
    a = 15

    print("in function", a)

# to maintain same variable a in local and global use globals() method
def something2():
    a = 8
    globals()['a'] = 15

    print("in function", a)

#something()
#print("outside function", a)
#something1()
#print("outside function", a)

something2()
print("outside function", a)