# https://practice.geeksforgeeks.org/problems/minimize-the-sum-of-product1525/1

def minValue(a, b, n):
    """
    You are given two arrays, A and B, of equal size N. The task is to find 
    the minimum value of A[0] * B[0] + A[1] * B[1] + ... + A[N-1] * B[N-1], 
    where shuffling of elements of arrays A and B is allowed.
    """
    a.sort()
    b.sort(reverse = True)
    return sum([a[i] * b[i] for i in range(n)])

if __name__ == "__main__":
    minValue([1,6,2],[14,19,8],3)
