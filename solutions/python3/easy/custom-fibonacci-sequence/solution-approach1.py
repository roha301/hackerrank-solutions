# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/custom-fibonacci-sequence/problem?isFullScreen=true
# Problem     Custom Fibonacci Sequence
# Difficulty  Easy
# Subdomain   Software Engineer Prep Kit
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-16, 07:31 p.m.
# Technique   iterative-fibonacci-sequence
# Time        O(n)
# Space       O(1)
# Insight     The function iteratively computes the n-th Fibonacci number by maintaining the two most recent values in the sequence starting from F(0)=1 and F(1)=2.
# Interview   Before: "I could use recursion to solve this." After: "Recursion would be inefficient due to redundant calculations. An iterative approach with O(n) time and O(1) space is optimal, especially since the problem defines F(0)=1 and F(1)=2, requiring careful handling of the base cases up to n=92."
# Pitfalls    (1) Failing to handle the base cases n=0 and n=1 correctly, which return 1 and 2 respectively.  (2) Using an incorrect loop range, such as range(n), which would miss the final addition required for the n-th index.  (3) Assuming standard Fibonacci indexing where F(0)=0 and F(1)=1, which contradicts the problem's specific definition.
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
