def heapify(arr, n, i):
	largest = i
	l = 2 * i + 1	
	r = 2 * i + 2	 
#if left child of root exists and is greater than root
	if l < n and arr[i] < arr[l]:
		largest = l
#if right child of root exists and is greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r
	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i] 
# Heapify the root.
		heapify(arr, n, largest)
# The main function to sort an array of given size
def heapSort(arr):
	n = len(arr)
# Build a maxheap since last parent will be at ((n//2)-1) we can start at that location.
	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i)
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, i, 0)
arr = [ 1, 5, 4, 8, 9, 7, 6]
heapSort(arr)
n = len(arr)
print ("Sorted array is: ")
for i in range(n):
	print ("%d" %arr[i])
