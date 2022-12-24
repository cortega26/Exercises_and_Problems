# https://practice.geeksforgeeks.org/problems/reverse-array-in-groups0255/1

def reverse_in_groups(arr: List[int], N: int, K: int) -> List[int]:
    """
    Given a list of positive integers arr of size N, reverse every 
    sub-list of size K.
    """
    # Calculate the number of sub-lists
    num_sublists = N // K
    if N % K != 0:
        num_sublists += 1
    
    # Reverse each sub-list and append it to the result list
    result = []
    for i in range(num_sublists):
        result += arr[K * i : (K * i) + K][::-1]    
    return result
  
if __name__ == "__main__":
    reverse_in_groups([1,2,3,4,5,6,7,8,9,10], 10, 3)
