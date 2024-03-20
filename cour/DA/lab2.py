L = ["Michael Jackson", 10.1, 1982]
print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )

L = ["Michael Jackson", 10.1,1982,"MJ",1]
print(L[3:5])

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
print(L)

#append
L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
print(L)

#extend
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
print(L)

#nested lits
L.append(['a','b'])
print(L)

#change list:
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

#delete
print('Before change:', A)
del(A[0])
print('After change:', A)

#split()
print('hard rock'.split())

# Split the string by comma
print('A,B,C,D'.split(','))

#Copy and Clone List
A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

# Examine the copy by reference
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])

# Clone (clone by value) the list A
B = A[:]
B

#Now if you change A, B will not change:
print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])

#Print the first element in the second nested tuples
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
print(NestedT[2][1][0])
# Print the first element in the second nested tuples
print(NestedT[4][1][0])

