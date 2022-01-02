a = {}
b = dict()
print(a)
print(b)

a = {1: 'python', 2: 'java'}
b = dict({1: 'C++', 2: 'ruby'})
print(a)
print(b)

a = {'1st': 'python', '2nd': 'java'}
print(a['1st'])
print(a.get('2nd'))

a = {'1st': 'python', '2nd': 'java'}
print(a)
a['2nd'] = 'C++'
print(a)
a['3rd'] = 'ruby'
print(a)

a = {'1st': 'python', '2nd': 'C++', '3rd': 'ruby'}
print(a)
p = a.pop('3rd') #remove the key and return value
print('\nValue: ', p)
print('Dictionary: ', a)

q = a.popitem() #remove a key value pair and retun them as a tuple
print('\nKey: ', q)
print('Dictionary: ', a)

a.clear() #clear all

a = {'1st': 'python', '2nd': 'C++', '3rd': 'ruby'}
print(a.keys())
print(a.values())
print(a.items())
print(a.get('1st'))