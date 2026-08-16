# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/custom-fibonacci-sequence/problem?isFullScreen=true
# Problem     Custom Fibonacci Sequence
# Difficulty  Easy
# Subdomain   Software Engineer Prep Kit
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-16, 07:31 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getAutoSaveInterval' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER n as parameter.
#

def getAutoSaveInterval(n):
    if n==0:
        return 1
    if n==1:
        return 2
    a,b=1,2
    for i in range (2,n+1):
        a,b=b ,a+b
    return b            
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    result = getAutoSaveInterval(n)

    print(result)
