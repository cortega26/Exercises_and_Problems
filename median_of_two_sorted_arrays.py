# https://leetcode.com/problems/median-of-two-sorted-arrays/

def findMedianSortedArrays(nums1, nums2):
    """
    Given two sorted arrays nums1 and nums2 of size m and n 
    respectively, return the median of the two sorted arrays.
    The overall run time complexity should be O(log(m+n)).
    """
    m = len(nums1)
    n = len(nums2)
    i, j = 0, 0
    median_idx = (m + n) // 2
    sol = []
    while i + j <= median_idx:
        if i == m:
            sol.extend(nums2[j:])
            break    
        if j == n:
            sol.extend(nums1[i:])
            break
        if nums1[i] < nums2[j]:
            sol.append(nums1[i])
            i += 1
        else:
            sol.append(nums2[j])
            j += 1      
    if (m + n) % 2 == 1:
        return sol[median_idx]
    else:
        return (sol[median_idx] + sol[median_idx - 1]) / 2.0
      
if __name__ = "__main__":
  findMedianSortedArrays([1, 2], [3, 4])
      
