#1.Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def bigSize(list):
    for i in range(0,len(list),1):
        if list[i]>0:
            list[i]="big"
    return list
y=bigSize([-1,2,3,-4])
print(y)


#2.Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def countPositives(list):
    num=0
    for x in range(0,len(list),1):
        if list[x]>0:
            num=num+1
        list[len(list)-1]=num
    return list
y=countPositives([-1,1,1,1])
print(y)

#3.Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sumTotal(list):
    sum=0
    for x in range(0,len(list),1):
        sum=sum+list[x]
    return sum
y=sumTotal([1,2,3,4])
print(y)

#4.Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def average(list):
    avg=0
    sum=0
    for x in range(0,len(list),1):
        sum=sum+list[x]
        avg=sum/(len(list))
    return avg
print(average([1,2,3,4]))

#5.Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def lengthofList(list):
    return len(list)
y=lengthofList([])
print(y)

#6.Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def returnMin(list):
    if len(list)==0:
        return False
    minVal=0
    for x in range(0,len(list),1):
        if minVal>list[x]:
                minVal=list[x]
    return minVal
y=returnMin([33,2,7,-9])
print(y)

#7.Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def returnMax(list):
    if len(list)==0:
        return False
    maxVal=0
    for x in range(0,len(list),1):
        if maxVal<list[x]:
                maxVal=list[x]
    return maxVal
y=returnMax([])
print(y)

#8.Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def listToDict(list):
    if len(list)==0:
        return False
    maxVal=0
    sumTotal=0
    minVal=0
    avg=0
    for x in range(0,len(list),1):
        if maxVal<list[x]:
            maxVal=list[x]
        if minVal>list[x]:
            minVal=list[x]
        sumTotal=sumTotal+list[x]
        avg=sumTotal/(len(list))
    return {"sumTotal": sumTotal, "average": avg, "minimum": minVal, "Maximum": maxVal, "length": len(list)}
y=listToDict([37,2,1,-9])
print(y)

    
#9.Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverseList(list):
    for x in range(0,len(list)/2,1):
        temp=list[x]
        list[x]=list[len(list)-1-x]
        list[len(list)-1-x]=temp
    return list
y=reverseList([37,2,1,-9])
print(y)
