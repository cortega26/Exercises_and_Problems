# Level: Basic
# Given an array, rotate the array by one position in clock-wise direction.

def rotate(arr, n):
    return [arr[n-1]] + arr[:-1] 
