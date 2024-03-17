product = 1
for n in range(1,10):
    product = product * n
print(product)


def to_celsius(x):
    return(x-32) * 5/9

for x in range(0, 101, 10): #start: 0. end: 100, step: 10
    print(x, to_celsius(x))

num = 5
y = [1, 2, 3]
for num in y:
   print(num)

print(num)

students = [['Igor', 'Sokolov'], ['Riko', 'Miyazaki'], ['Tuva', 'Johansen']]
for student in students:
   for name in student:
       print(name)
   print()