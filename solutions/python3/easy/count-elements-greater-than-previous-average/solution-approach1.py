# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/count-elements-greater-than-previous-average/problem?isFullScreen=true
# Problem     Count Elements Greater Than Previous Average
# Difficulty  Easy
# Subdomain   Software Engineer Prep Kit
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-15, 05:43 p.m.
# Technique   running-sum-average-comparison
# Time        O(n)
# Space       O(1)
# Insight     The algorithm maintains a running sum of previous elements and compares the current element against the average by multiplying the current element by the count of previous elements to avoid floating-point precision issues.
# Interview   Before: "I would calculate the average at each step using division." After: "I optimized the comparison by multiplying the current element by the count of previous elements, achieving O(n) time and O(1) space while avoiding floating-point errors for inputs up to 10^9."
# Pitfalls    (1) Using floating-point division for the average calculation can lead to precision errors when comparing large integers.  (2) Failing to handle the n <= 1 case correctly, which results in an empty or single-element array that should return zero.  (3) Incorrectly updating the running sum before performing the comparison, which would include the current element in the average calculation.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    if len(responseTimes) <= 1:
        return 0
    count=0
    running_sum = responseTimes[0]
    for i in range(1, len(responseTimes)):
        if responseTimes[i] * i > running_sum:
            count +=1
        running_sum += responseTimes[i]
    return count            

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
