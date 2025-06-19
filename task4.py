'''Task 4.
Longest Consecutive Sequence
Given an unsorted list of integers, find the length of the longest consecutive
sequence.
def longest_consecutive(nums: list) -> int:
 pass
Example:
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums)) Output: 4 (because [1,2,3,4] is the longest)
'''

def longest_consecutive(nums: list) -> int:
    nums.sort()
    temp = 1
    longest = 0

    for i in range(len(nums)-1):
        if nums[i] - nums[i+1] == -1:
            temp +=1
        elif temp > longest:
            longest = temp
    return longest

nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))
