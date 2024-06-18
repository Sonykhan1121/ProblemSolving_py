    #!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
print(matrix)
another = ""
for j in range(m):
    for i in range(n):
        try:
            another += matrix[i][j]
        except IndexError:
            pass

print(another)
decode_string = re.sub(r'(?<=\w)([^\w]+)(?=\w)',' ',another)
print(decode_string)