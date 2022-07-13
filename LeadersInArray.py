# https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1

def leaders(arr, n):
    """
    Find the leaders in the array
    An element of array is leader if it is greater than or equal to all the 
    elements to its right side. The rightmost element is always a leader. 
    """
    
    arr = arr[::-1]
    sol = []
    high = -float("Inf")
    for i in arr:
        if i >= high:
            sol.append(i)
            high = i    
    return sol[::-1]

if __name__ == "__main__":
    leaders([1,5,2,8,0,4,3,-2], 8)

