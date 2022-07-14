def getPairsCount(arr, n, k):
    """
    Given an array of N integers, and an integer K, find 
    the number of pairs of elements in the array whose sum 
    is equal to K. Expected Time Complexity: O(n)
    """
    
    counter = 0
    dict_list = {}
    for i in range(n):
        if arr[i] in dict_list.keys():
            dict_list[arr[i]] += 1
        else:
            dict_list[arr[i]] = 1
        if (k - arr[i]) in dict_list.keys():
            if k - arr[i] != arr[i]:
                counter +=  dict_list[k - arr[i]]
            elif dict_list[arr[i]] > 1:
                counter += dict_list[arr[i]] - 1
    return counter
