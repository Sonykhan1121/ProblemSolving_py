import numpy

def arrays(arr):
    arr = arr[::-1]
    arr = numpy.array(arr,float)
    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)