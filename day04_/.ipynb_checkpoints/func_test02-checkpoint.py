def add(*args):
    total = 0    
    for i in args:
        total += i
    return total

total = add(1,2,3,4,5,6,7,8,9)
print(total)


def mul(a,b,c,d):
    print(a*b*c*d)

mul(*1,2,3,4)