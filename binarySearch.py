# Level: Basic
# Given a sorted array of size n and an integer number, find the
# position at which number is present in the array using binary search.

def binary_search(arr, n, number):
    left = 0
    right = n - 1
    while left <= right:
        m = (left + right) // 2
        if arr[m] < number:
            left = m + 1
        elif arr[m] > number:
            right = m - 1
        else:
            return m
    return -1
