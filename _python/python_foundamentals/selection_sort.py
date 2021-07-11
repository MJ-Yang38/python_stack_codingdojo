#write the algorithm for selection sort
list1=[7,4,5,2,1,13,11,9]
def selection_sort(list):
    count=0
    for j in range(len(list)):
        min=j
        for i in range(j+1,len(list)):
            count+=1
            if list[min]>list[i]:
                min=i
        list[min],list[j]=list[j],list[min]
    print(count)
    return list
print(selection_sort(list1))