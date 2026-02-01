class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return 0
        
        max_sum = 0
        current_sum = 0
        window = {}  # frequency map for current window
        
        # Build first window
        for i in range(k):
            current_sum += nums[i]
            window[nums[i]] = window.get(nums[i], 0) + 1
        
        # Check if first window has all distinct elements
        if len(window) == k:
            max_sum = current_sum
        
        # Slide the window
        for i in range(k, n):
            # Add new element
            current_sum += nums[i]
            window[nums[i]] = window.get(nums[i], 0) + 1
            
            # Remove old element
            left_element = nums[i - k]
            current_sum -= left_element
            window[left_element] -= 1
            if window[left_element] == 0:
                del window[left_element]
            
            # Check if current window has all distinct elements
            if len(window) == k:
                max_sum = max(max_sum, current_sum)
        
        return max_sum