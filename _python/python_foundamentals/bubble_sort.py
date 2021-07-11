arr=[8,1,4,2,0,9]
def bubble_sort(arr):
    count=0
    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):
            count+=1
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    print(count)
    return arr
print(bubble_sort(arr))