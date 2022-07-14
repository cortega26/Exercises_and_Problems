# Given an array arr[] of size n, find the first repeating element.
# The element should occurs more than once and the index of its
# first occurrence should be the smallest.


def firstRepeated(arr, n):
    mp = {}
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]] += 1
            break
        else:
            mp[arr[i]] = 1
    for i in range(n):
        if mp[arr[i]] >= 2:
            return i
    return -1
