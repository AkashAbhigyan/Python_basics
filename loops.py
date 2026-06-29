for num1 in range(11):
    print(num1)

num2=0
while num2 <= 10:
    print(num2)
    num2 += 1


for num3 in range(10,-1,-1):
    print(num3)

num4 = 10
while num4 >= 0:
    print(num4)
    num4 -= 1


num5 = 0
while num5 <= 7:
    print("#"*num5)
    num5 += 1


num6 = 0
while num6 <= 8:
    print("#"*8)
    num6 += 1

num7 = 1
while num7 <= 10:
    print(num7,"x",num7,"=",num7*num7)
    num7+=1


list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for library in list:
    print(library)


for evennum8 in range(0,101,2):
    print(evennum8)


    for oddnum9 in range(1,101,2):
        print(oddnum9)


num8 = 1
for l in range(0,100):
    num8 += l
    print(l)
print("The sum of all the numbers is=",l+num8)


m = 0
o = 0
for n in range(0,101):
    if n%2 == 0:
        m += n
    else:
        o += n
print("Sum of even numbers is-",m)
print("Sum of odd numbers is-",o)