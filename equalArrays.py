# Level: Basic
# Given two arrays A and B of equal size N, the task is to find if given
# arrays are equal or not. Two arrays are said to be equal if both of
# them contain same set of elements, arrangements (or permutation) of
# elements may be different though.
# Note : If there are repetitions, then counts of repeated elements
# must also be same for two array to be equal.


def check(A,B,N):
    A.sort()
    B.sort()
    for i in range(N):
        if A[i] != B[i]:
            return 0
    return 1
