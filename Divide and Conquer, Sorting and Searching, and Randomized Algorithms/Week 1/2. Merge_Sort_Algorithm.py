# Merge Sort Algorithm

# Define Merge Function to merge two unsorted array
def merge(a, b):
    c = []
    i = 0
    j = 0
    
    while(i<len(a) and j<len(b)):
        if(a[i]>=b[j]):
            c.append(b[j])
            j = j+1
        else:
            c.append(a[i])
            i = i+1
    
    if(i==len(a)):
        while(j<len(b)):
            c.append(b[j])
            j = j+1
    else:
        while(i<len(a)):
            c.append(a[i])
            i = i+1
    return c

# Merge Sort Function
def merge_sort(a):
    if(len(a)//2 == 0):
        return a
    partition = len(a)//2
    left = merge_sort(a[:partition])
    right = merge_sort(a[partition:])
    return merge(left,right)
    
unsort = [2,15,22,1,36,9,13,11,100,99,98,97,96,95]
print(merge_sort(unsort))

