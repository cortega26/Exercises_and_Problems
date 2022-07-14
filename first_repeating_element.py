# https://practice.geeksforgeeks.org/problems/first-repeating-element4018/1

def firstRepeated(arr, n):
    """
    Given an array arr[] of size n, find the first repeating element.
    The element should occurs more than once and the index of its
    first occurrence should be the smallest.
    """
    
    mp = {}
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    for i in range(n):
        if mp[arr[i]] >= 2:
            return i + 1
    return -1

if __name__ == "__main__":
    firstRepeated(arr, n)
