basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print(type(basket))
print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a-b)
print(a|b)
print(a&b)
print(a^b)

set1 = {"Python", "Java", "C++", "SQL"}
set2 = {"Python", "JavaScript", "SQL", "AI"}

print("All unique technologies:",set1|set2)
print("Technologies common to both sets:",set1&set2)
print("Technologies only in set1:",set1-set2)
print("Technologies only in set2:",set2-set1)
print("Technologies that are in one set but not both:",set1^set2)
