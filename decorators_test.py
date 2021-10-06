def div(a,b):
    if a<b:
        a,b=b,a
    return a/b



#result = div(8, 2)
#print(result)

#result = div(2, 8)
#print(result)

def division(a,b):
    return a/b

def smart_div(func):
    def inner(a,b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner
div = smart_div(division)

print(div(2, 4))