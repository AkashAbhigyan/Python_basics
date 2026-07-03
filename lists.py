marks=[21,30,26.5,19.5]
print(marks,type(marks))
print(marks[0],marks[2])
marks[3]=20
print(marks)
marks.append(16)#adds one element at the end
marks.sort()#sorts in ascending order
marks.sort(reverse=True)#in descending order
marks.reverse()
marks.insert(1,25)
print(marks)
marks.remove(26.5)#removes first occuring element
marks.pop(1)#removes first element
print(marks)
print(len(marks))
print(20 in marks)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)  # letters in a but not in b
print(a | b)  # letters in a or b or both
print(a & b)  # letters in both a and b
print(a ^ b)  # letters in a or b but not both