#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    
    s_list = list(s)
    
    for i in range (len(s_list)):
        
        if i == 0 :
            s_list[i] = s_list[i].capitalize()
        
        if s_list[i] == " ":
            s_list[i+1] = s_list[i+1].capitalize()
    
    ans = ''.join(s_list)
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
