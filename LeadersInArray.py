# Given an array A of positive integers. Your task is to find the leaders in the array.
# An element of array is leader if it is greater than or equal to all the elements to
# its right side. The rightmost element is always a leader. 

def leaders(A, N):
    sol = []
    max = 0
    for i in reversed(A):
        if i > max:
            sol.append(i)
            max = i    
    sol = sol[::-1]
    return sol
