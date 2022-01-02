a = 10
b = 15
if a == b:
    print('they are equal')
elif a >b:
    print('a is larger')
else:
    print('b is larger')

n = int(input('enter a number:'))
if n >= 0:
    if n == 0:
        print('entered number is zero')
    else:
        print('entered a positive number')
else:
    print('entered a pnegative number')


fruits = ['apple', 'orange', 'banana']
for fruit in fruits:
    print(fruit)

number = [1, 2, 3, 4]
sum = 0
for i in number:
    sum += i
print(sum)

for i in range (10):
    print(i)
print('\n')

cakes = ['pineapple', 'chocolate', 'banana']
for cake in cakes:
    print(cake)
else:
    print('no more cakes left to eat')

second = 10
while second >= 0:
    print(second, end = '-> ')
    second -= 1
print('blastoff!')


counter = 0
while counter < 3:
    print('hello?')
    counter = counter + 1
else: 
    print('why you are not replying bro?')


count = 1
for i in range(10):
    print(str(i) * i)
    for j in range(0, i):
        count = count + 1
        