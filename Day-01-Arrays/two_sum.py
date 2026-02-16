"""
Day: 01
Problem: Two Sum
Concept: Arrays, HashMap
Time Complexity: O(n)
Space Complexity: O(n)
Date: 16-02-2026
"""

def two_sum(nums, target):
    hashmap = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i

# Example test
print(two_sum([2, 7, 11, 15], 9))
