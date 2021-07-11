class Underscore:
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i]=callback(iterable[i])
        return iterable
    
    def find(self, iterable, callback):
        for i in range(len(iterable)):
            temp=0
            if callback(iterable[i]) == True:
                temp=iterable[i]
                break
        return temp

    def filter(self, iterable, callback):
        newarr=[]
        for i in range(len(iterable)):
            if callback(iterable[i])==True:
                newarr.append(iterable[i])
        return newarr

    def reject(self, iterable, callback):
        newarr=[]
        for i in range(len(iterable)):
            if callback(iterable[i])==False:
                newarr.append(iterable[i])
        return newarr

_ = Underscore()

evens=_.map([1,2,3,4,5,6], lambda x: x*2)
print(evens)
find=_.find([1,2,3,4,5,6], lambda x: x>4)
print(find)
evens2=_.filter([1,2,3,4,5,6], lambda x: x%2==0)
print(evens2)
rejects=_.reject([1,2,3,4,5,6],lambda x: x%2==0)
print(rejects)
