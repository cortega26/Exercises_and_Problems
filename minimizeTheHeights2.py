# Given an array arr[] denoting heights of n towers and a positive integer k, you have
# to modify the height of each tower either by increasing or decreasing them by K only
# once. After modifying, height should be a non-negative integer. 
# Find out the minimum possible difference of the height of shortest and longest
# towers after you have modified each tower.
# Note: It is compulsory to increase or decrease by k to each tower.

def getMinDiff(arr, n, k):
    arr = list(set(arr))
    arr.sort(reverse = True)
    arr = [i + k for i in arr]
    min_diff = arr[0] - arr[-1]
    for idx, value in enumerate(arr):
        if value - 2 * k >= 0 and idx+1 < len(arr):
            arr[idx] = arr[idx] - 2 * k
            current_diff = max([arr[0]] + [arr[idx+1]]) - min([arr[idx]] + [arr[-1]])
            if current_diff < min_diff:
                min_diff = current_diff    
    return min_diff
