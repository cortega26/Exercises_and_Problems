# Level: Basic
# Given an array arr[] of positive integers of size N. Reverse every
# sub-array group of size K.


def reverseInGroups(arr, N, K):
  
    # Number of sub-arrays to reverse
    if N % K == 0:
        subs = N // K
    else:
        subs = (N // K) + 1
        
    solution = []
    for i in range(subs):
        solution += arr[K * i : (K * i) + K][::-1]    
    return solution
