#sum of 100 number using reduce 
from functools import reduce
result = reduce(lambda x,y:x+y,range(1,101))
print(result)