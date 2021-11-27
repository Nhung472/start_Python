
s = "10010"
c = int(s, 2)
print("After converting to integer base 2: %d" %c, end = "\n")

e = float(s)
print("After converting to float: %f" %e, end = "\n")

s = '4'
c = ord(s)
print("After converting character to integer: %c" %c, end = "\n")

c = hex(56)
print("After converting 56 to hexadecimal string: " + c, end = "\n")

c = oct(56)
print("After converting 56 to octal string: " + c, end = "\n")

s = 'hello'
c = tuple(s)
print('After converting string to tuple: ', c, end = "\n")

c = set(s)
print('After converting string to set: ', c, end = "\n")

tuple1 = ()
tuple2 = ("python", 'for', 256)
print(tuple1)
print(tuple2)
tuple1 = tuple1 + (1, 2, 'get', 'it')
print(tuple1)
tuple3 = 'example'
print(type(tuple3))
print(tuple1[0])
print(tuple1[:])
print(tuple1[3][1])

tuple3 = (1, 2, 3, ['hindi', 'python'])
print(tuple3.count(2))
print(tuple3.index(['hindi', 'python']))