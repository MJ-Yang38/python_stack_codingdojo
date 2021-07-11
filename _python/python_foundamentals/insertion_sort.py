#implementing insertion sort: number of iteration is len(arr), need to rebuild the 
#array from the very first item, comparing the arr[i] to the ones on the left of it

arr=[7,4,5,2,1,13,11,9]
def insertionSort(arr):
    for j in range(1,len(arr)):
        for i in range(j):
            if arr[i]>arr[i-j]:
               arr[i],arr[i-j]=arr[i-j],arr[i]
    return arr
    
print(insertionSort(arr))


