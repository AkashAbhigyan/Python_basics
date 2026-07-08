file = open('D:\Learning\Github\simple.txt')
print(file.read())
file.close()

file = open('D:\Learning\Github\simple.txt', "r")
print(file.readline())
file.close()

file = open('D:\Learning\Github\simple.txt', "r")
print(file.readlines())
file.close()

file = open('D:\Learning\Github\simple.txt', "w")
file.write("Python Programming")
file.close()

file = open('D:\Learning\Github\simple.txt', "a")
file.write("\nFile Handling")
file.close()

with open('D:\Learning\Github\simple.txt', "r") as file:
    print(file.read())

with open('D:\Learning\Github\simple.txt', "w") as file:
    file.write("Hello Python")

