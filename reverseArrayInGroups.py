# https://practice.geeksforgeeks.org/problems/reverse-array-in-groups0255/1

def reverseInGroups(arr, N, K):
    """
    Given an array arr[] of positive integers of size N. Reverse every 
    sub-array group of size K.
    """
  
    subs = N // K
    if N % K != 0:
        subs += 1
    solution = []
    for i in range(subs):
        solution += arr[K * i : (K * i) + K][::-1]    
    return solution
  
if __name__ == "__main__":
  reverseInGroups([1,2,3,4,5,6,7,8,9,10],10,3)
