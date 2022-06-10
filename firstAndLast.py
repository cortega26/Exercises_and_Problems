# Level: Basic
# Given a sorted array arr containing n elements with possibly duplicate
# elements, the task is to find indexes of first and last occurrences of
# an element x in the given array.
# If the element doesn't exist in the array return -1 -1


def find(arr, n, x):
    flag = True
    for idx, elem in enumerate(arr):
        if elem == x:
            if flag:
                minin = idx
                flag = False
            if flag == False and elem == x:
                maxin = idx
    if flag:
        return -1, -1
    return minin, maxin
