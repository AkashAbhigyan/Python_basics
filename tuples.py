tuple=(2,3,4,5,2,1,3)
print(tuple.index(3))#first time the element occur
print(tuple.count(2))#number of times the number occur

a=input("Movie 1-")
b=input("Movie 2-")
c=input("Movie 3-")
print("Your 3 fav films-",[a,b,c])

d=[1,2,3]
e=d.copy()
e.reverse()
if(d==e):
    print("It is a palendrome")
else:
    print("It is not a palendrome")