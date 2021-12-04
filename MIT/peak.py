# PEAK FINDING

a = [4, 15, 17, 20, 9, 7]
m = len(a)

def peak(a, m):
    if a[0] >= a[1]:
        return 0
    if a[m-1] >= a[m-2]:
        return m -1
    for i in range (1, m-1):
        if a[i] >= a[i-1] and a[i] >= a[i+1]:
            return i

print("The index of peak is", peak(a, m))