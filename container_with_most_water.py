# https://leetcode.com/problems/container-with-most-water/

 def maxArea(height):
    """
    You are given an integer array height of length n. There are n vertical 
    lines drawn such that the two endpoints of the ith line are (i, 0) and 
    (i, height[i]).
    Find two lines that together with the x-axis form a container, such 
    that the container contains the most water.
    Return the maximum amount of water a container can store.
    """
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        current_area = (right - left) * min(height[left], height[right])
        if current_area > max_area:
            max_area = current_area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

if __name__ == "__main__":
    maxArea([1,8,6,2,5,4,8,3,7])
