tuple=(2,3,4,5,2,1,3)
print(tuple.index(3))#first time the element occur
print(tuple.count(2))#number of times the number occur

a=input("Movie 1-")
b=input("Movie 2-")
c=input("Movie 3-")
print("Your 3 fav films-",(a,b,c))

add_tuple=(a,b,c), tuple
print(add_tuple)
print(add_tuple[0][1])#accessing the second element of the first tuple

name = ("addx","adxacw","accwwc")
print(tuple+name)#adding two tuples

fruit1=input("Enter first fruit:")
fruit2=input("Enter second fruit:")
fruit3=input("Enter third fruit:")
fruit4=input("Enter forth fruit:")
fruit5=input("Enter fifth fruit:")

fruits = (fruit1,fruit2,fruit3,fruit4,fruit5)
print("\nThe fruits are:",fruits)
print("Total number of fruits are:",len(fruits))
print("The first fruit:",fruits[0])
print("The last fruit:",fruits[-1])
