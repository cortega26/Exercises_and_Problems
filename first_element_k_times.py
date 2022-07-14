# https://practice.geeksforgeeks.org/problems/first-element-to-occur-k-times5150/1

def firstElementKTime(arr, n, k):
    """
    Given an array of N integers. Find the first element that
    occurs at least K number of times. Return -1 if no element 
    ocurr K times.
    """
    
    dict_counter = {}
    for i in range(n):
        if arr[i] in dict_counter.keys():
            dict_counter[arr[i]] += 1
        else:
            dict_counter[arr[i]] = 1
        if dict_counter[arr[i]] == k:
            return arr[i]
    return -1

if __name__ = "__main__":
    firstElementKtime([2, 5, 4, 7, 8, 7, 2, 1], 8, 2)
