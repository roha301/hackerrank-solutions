# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/check-palindrome-filter-non-letters/problem?isFullScreen=true
# Problem     Check Palindrome by Filtering Non-Letters
# Difficulty  Easy
# Subdomain   Software Engineer Prep Kit
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-16, 08:47 a.m.
# Technique   list-comprehension-filtering-reversal
# Time        O(N)
# Space       O(N)
# Insight     The implementation filters the input string for alphabetic characters, converts them to lowercase, and compares the resulting list with its reverse to determine if it is a palindrome.
# Interview   Before: "I would iterate through the string with two pointers to check for a palindrome." After: "Using list comprehension and slicing is more idiomatic in Python, achieving O(N) time and space complexity while correctly handling the 1000-character constraint."
# Pitfalls    (1) Failing to account for non-alphabetic characters like digits or symbols which must be ignored per the problem statement.  (2) Neglecting the case-insensitive requirement by failing to convert characters to lowercase before comparison.  (3) Assuming the input string is empty or contains only letters, which contradicts the constraint that it may contain symbols and digits.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#

def isAlphabeticPalindrome(code: str) -> bool:
    filtered_chars = [char.lower() for char in code if char.isalpha()]
    return filtered_chars == filtered_chars[::-1]
    # Write your code here

if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
