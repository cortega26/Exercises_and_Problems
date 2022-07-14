def maxSubArraySum(arr, N):
    """
    Given an array arr[] of N integers. Find the contiguous
    sub-array (containing at least one number) which has the 
    maximum sum and return its sum.
    """

    if max(arr) <= 0: return max(arr)
    
    max_sum = 0
    current_sum = 0
    for integer in arr:
        current_sum += integer
        if current_sum > max_sum:
            max_sum = current_sum
        elif current_sum < 0:
            current_sum = 0
    return max_sum

if __name__ == "__main__":
    maxSubArraySum([1,-2,3,5,6,-2,4,-4,0],9)
