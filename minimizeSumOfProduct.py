# You are given two arrays, A and B, of equal size N. The task is to find the minimum
# value of A[0] * B[0] + A[1] * B[1] +…+ A[N-1] * B[N-1], where shuffling of elements
# of arrays A and B is allowed.

def minValue(a, b, n):
    a.sort()
    b.sort(reverse = True)
    sum_of_product = 0
    for i in range(n):
        sum_of_product += a[i] * b[i]
    return sum_of_product
