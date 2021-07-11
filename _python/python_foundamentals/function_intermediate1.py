#randint function, consider edge cases when min>max, max<0
import random
def rand_int(min=0,max=100):
        num=random.random()*(max-min)+min
        return round(num)
#print(rand_int())
#print(rand_int(max=50))
#print(rand_int(min=50))    
print(rand_int(min=1,max=-2))
