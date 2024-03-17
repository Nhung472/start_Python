x = 8
if x > 5:
   print('x is greater than five')
elif x < 5:
   print('x is less than five')
else:
   print('x is equal to five')

b = 0
while b<5:
    print("Not there yet, x = " + str(b))
    b = b+1
print("b = " + str(b))

def even(number):
    if number % 2 ==0:
        return True
    return False
even(5)

def hint(username):
    if len(username) <8:
        print("invalid. at least 8 char")
    elif len(username) >15:
        print("invalid. at max 14 char")
    else:
        print("valid")
hint(dsfesfsd)

x = 8
if x > 5:
   print('x is greater than five')
elif x < 5:
   print('x is less than five')
else:
   print('x is equal to five')
