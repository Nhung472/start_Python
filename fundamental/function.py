def foo(bar):
    bar = 'new value'
    print(bar)

answer = 'old value'
foo(answer)
print(answer)

def add(x, y):
    print('The sum of a and b is:', (x + y))
def mul(x, y):
    print('The product of x and y is: ', (x * y))

add(5, 10)
mul(4, 6)

a = [1, 0, 5]
print(abs(-7))
print(all(a))
print(any(a))
print(len(a))
print(min(a))
print(max(a))
print(sum(a))
print(type(a))

