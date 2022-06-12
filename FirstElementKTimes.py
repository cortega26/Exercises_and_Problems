# Given an array of N integers. Find the first element that occurs at least K 
# number of times. Return -1 if no element ocurr K times.


def firstElementKTime(arr, n, k):
        dict_counter = {}
        for i in range(n):
            if arr[i] in dict_counter.keys():
                dict_counter[arr[i]] += 1
            else:
                dict_counter[arr[i]] = 1
            if dict_counter[arr[i]] == k:
                return arr[i]
        return -1
