a = {1, 2, 3, 4, 5, 4}
print(a)

a = {1, 2, 3} #add elements
a.add(6)
print(a)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b), "....", a | b) #union operations can be done
print(a.intersection(b), '...', a & b)
print(a.difference(b), '...', a - b)
print(a.symmetric_difference(b),'...', a ^ b)
a.clear()
print(a)

superset = {1, 2, 3, 4, 5, 6, 7, 8}
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 == s2)
print(s1 != s2)
print(s1 <= superset)
print(s1 >= s2)
print(s1 > s2)
