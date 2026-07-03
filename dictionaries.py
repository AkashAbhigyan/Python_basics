tel = {'jack': 4098, 'sape': 4139}#dict(sape=4139, guido=4127, jack=4098),dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
tel['guido'] = 4127#adds or updates a key-value pair
print(tel)#prints the dictionary
print('jack' in tel)#checks if 'jack' is a key in the dictionary
print('msd' in tel)#checks if 'msd' is a key in the dictionary
print(tel.get('jack'))#returns the value for the key 'jack' if it exists, otherwise returns None
print(tel.get('msd'))#returns the value for the key 'msd' if it exists, otherwise returns None
del tel['sape']#removes the key-value pair with key 'sape' from the dictionary
tel['irv'] = 4127#adds or updates a key-value pair
print(tel)#prints the dictionary
print(list(tel))#prints a list of the keys in the dictionary
print(sorted(tel))#prints a sorted list of the keys in the dictionary
print(len(tel))#prints the number of key-value pairs in the dictionary
print(type(tel))

square = {x: x**2 for x in (2, 4, 6)}
print(square)#prints the dictionary of squares

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  -It is {1}.'.format(q, a))

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

for f in sorted(set(basket)):
    print(f)
