for i,x in enumerate(['A','B','C']):
    print(i,x)

# For loop example
dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])

# Exmaple of for loop, loop through list
for year in dates:  
    print(year)   

# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

# Loop through the list and iterate on both index and element value
squares=['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    print(i, square)

count = 1
while count <= 5:
    print(count)
    count += 1

# While Loop Example
dates = [1982, 1980, 1973, 2000]
i = 0
year = dates[0]
while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
print("It took ", i ,"repetitions to get out of loop.")

#Write a while loop to copy the strings 'orange' 
#of the list squares to the list new_squares. 
#Stop and exit the loop if the value on the list is not 'orange':

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)

for x in ['A','B','C']:
  print(x+'A')


