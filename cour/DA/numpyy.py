import numpy as np
a = np.array([0,1,2,3,4])
b = np.array([3.1, 11.02, 6.2, 5.6,3.4])
c = np.array([20, 1, 2, 3, 4])

# Assign the first element to 100
c[0] = 100

# Slicing the numpy array
d = c[1:4]

# Set the fourth element and fifth element to 300 and 400
c[3:5] = 300, 400

print(type(a))
print(type(b))
print(a.dtype)
print(c)
print(d)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1:5:2])

#Print the even elements in the given array.
print(arr[1:8:2])

#Assign Value with List
select = [0, 2, 3, 4]
print(select)

# Use List to select elements
d = c[select]
print(d)

c[select] = 100000
print(d)

# Get the size of numpy array
print(a.size)

# Get the number of dimensions of numpy array
print(a.ndim)

# Get the shape/size of numpy array
print(a.shape)

# Get the mean of numpy array
mean = a.mean()
print(mean)

# Get the standard deviation of numpy array
standard_deviation=a.std()
print(standard_deviation)

min_b = b.min()
print(min_b)

max_b = b.max()
print(max_b)

#Array Addition
u = np.array([1, 0])
v = np.array([0, 1])
z = np.add(u, v)
#print(z)

# Plotting functions
import time 
import sys
import numpy as np 
import matplotlib.pyplot as plt
def Plotvec1(u, z, v):
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)
print(Plotvec1(u, z, v))

#try myself
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

#addition:
m = np.add(arr1, arr2)

#sub:
n = np.subtract(arr1, arr2)

# Numpy Array Multiplication
p = np.multiply(arr1, arr2)

#dividion
q = np.divide(a, b)

#Dot Product
X = np.array([1, 2])
Y = np.array([3, 2])
print(np.dot(X, Y))

#Elements of X
print(X[0])
print(X[1])

#Elements of Y
print(Y[0])
print(Y[1])

#Adding Constant to a Numpy Array
u = np.array([1, 2, 3, -1]) 
print(u + 1)

#Mathematical Functions
# The value of pi
print(np.pi)

#Linspace
#numpy.linspace(start, stop, num = int value)
#start : start of interval range
#stop : end of interval range
#num : Number of samples to generate

print(np.linspace(-2, 2, num=5))

x = np.linspace(0, 2*np.pi, num=100)
y = np.sin(x)
plt.plot(x, y)

#Iterating 1-D Arrays
arr1 = np.array([1, 2, 3])
print(arr1)

for x in arr1:
    print(x)

#Quiz on 1D Numpy Array
u = np.array([1, 0])
v = np.array([0, 1])
print(u-v)

z = np.array([2, 4])
print(-2*z)

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 0, 1, 0, 1])
print(a * b)

def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)
#new
a = np.array([-1, 1])
b = np.array([1, 1])
print(Plotvec2(a, b))
print("The dot product is", np.dot(a,b))

#hisdj
a = np.array([1, 0])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))

#nhona = np.array([1, 1])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))

arr1 = np.array([1, 2, 3])
arr2 = np.array([8, 9, 10])

arr3 = np.add(arr1, arr2)
print(arr3)

arr4 = np.subtract(arr1, arr2)
print(arr4)

arr5 = np.multiply(arr1, arr2)
print(arr5)

arr6 = np.divide(arr1, arr2)
print(arr6)

arr7 = np.dot(arr1, arr2)
print(arr7)

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

#Starting index in slice is 1 as first even element(2) in array1 is at index 1
even_arr1 = arr1[1:5:2]
print("even for array1",even_arr1)
    
#Starting index in slice is 0 as first odd element(1) in array1 is at index 0
odd_arr1=arr1[0:5:2]
print("odd for array1",odd_arr1)

#Starting index in slice is 0 as first even element(6) in array2 is at index 0
even_arr2 = arr2[0:5:2]
print("even for array2",even_arr2)
    
    
#Starting index in slice is 1 as first odd element(7) in array2 is at index 1
odd_arr2=arr2[1:5:2]
print("odd for array2",odd_arr2)

A=np.array([[1,0,1],[2,2,2]])
print(A[0,1])

a=np.array([-1,1])
b=np.array([1,1])
print(np.dot(a,b))

X=np.array([[1,0,1],[2,2,2]]) 
out=X[0,1:3]
print(out)


X=np.array([[1,0],[0,1]])
Y=np.array([[2,2],[2,2]])
Z=np.dot(X,Y)
print(Z)


with open("Example1.txt","r") as File1:
    file_stuff=File1.readline ()
    print(file_stuff)

with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)