# Whats happening ? --> How to create generator using "yield" keyword
# When you are developing memory efficient applications, you can use generators to create iterators in memory.
# If the body of a def contains yield, the function automatically becomes a generator function. 
# if you use list or something else it will load all the bulkier data into memory, but if you use yield it will load one data at a time into memory.

def getEven(n):
    for i in range (2, n+1, 2):
        yield i 
        
x=getEven(10)
print(x,type(x))

for value in x:         # x is a generator object, we can iterate over it using for loop & for loop avoids the stop iteration default Exception to occure.
    print(value)    