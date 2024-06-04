#!/bin/python3

import math
import os
import random
import re
import sys
import datetime 
# Complete the time_delta function below.
def time_delta(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.datetime.strptime(t1,format)
    time2 = datetime.datetime.strptime(t2,format)
    timedif = (time1 -time2)
    ans =(abs(int(timedif.total_seconds())))
    return ans

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        print(delta)
        # fptr.write(delta + '\n')

    # fptr.close()
