x = 1
while x < 100:
   print(x)
   x = x*2


y = 1
i = 0
while y < 100:
   if i == 5:
       break
   print(i, y)
   y = y*2
   i += 1

m = 0
while m<10:
   if m % 3!=0:
      print(m)
      m +=1
      continue
   m +=1