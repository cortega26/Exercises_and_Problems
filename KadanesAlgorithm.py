# Given an array arr[] of N integers. Find the contiguous sub-array
# (containing at least one number) which has the maximum sum and
# return its sum.

def maxSubArraySum(arr, N):
    max_sum = 0
    current_sum = 0
    if max(arr) <= 0:
        return max(arr)
    for i in arr:
        current_sum += i
        if current_sum > max_sum:
            max_sum = current_sum
        elif current_sum < 0:
            current_sum = 0
    return max_sum
