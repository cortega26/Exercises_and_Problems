# https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/0/

def check(A, B, N):
    """
    Given two arrays A and B of equal size N, the task is to find if given
    arrays are equal or not. Two arrays are said to be equal if both of
    them contain same set of elements, arrangements (or permutation) of
    elements may be different though.
    Note: If there are repetitions, then counts of repeated elements
    must also be same for two array to be equal.
    Time complexity must be O(n)
    """
    
    dict_a, dict_b = {}, {}
    for i in A:
        if i in dict_a:
            dict_a[i] += 1
        else:
            dict_a[i] = 1
    for j in B:
        if j in dict_b:
            dict_b[j] += 1
        else:
            dict_b[j] = 1
                
    if dict_a == dict_b:
        return 1
    else:
        return 0

if __name__ == "__main__":
    check([1, 2, 6, 5, 4, 4],[4, 5, 2, 1, 6, 4], 6)
