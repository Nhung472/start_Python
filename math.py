a = 10
b = 20
print('add: ', a + b)
print('sub: ', a - b)
print('mul: ', a * b)
print('div: ', a / b)
print('rem: ', a % b)
print('expo: ', a ** b)

c = 10
add, sub, mul, div, rem, expo = 0, 0, 0, 1, 1, 1
add += c
sub -= c
mul *= c
div /= c
rem %= c
expo **= c

p = 5
q = 10
print(p == q)
print(p != q)
print(p > q)
print(p < q)
print(p >= q)
print(p <= q)

e = 5
f = 0
print(e and f)
print( e or f)
print( not e)
print( not f)

g = 5
h = 6
print(g & h)
print(g | h)
print(g ^ h)
print(~g)
print(g << h)
print(g >> h)
