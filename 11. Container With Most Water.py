class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area
            current_width = right - left
            current_height = min(height[left], height[right])
            current_area = current_width * current_height
            
            # Update max area if current is larger
            if current_area > max_area:
                max_area = current_area
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area