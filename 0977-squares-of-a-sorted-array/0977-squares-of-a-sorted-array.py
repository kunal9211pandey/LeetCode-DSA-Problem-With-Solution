class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # Function to square every element of an array
        def square(arr):
            for i in range(len(arr)):
                arr[i] = arr[i] * arr[i]
            return arr

        # Store positive and negative numbers separately
        positive = []
        negative = []

        # Divide the array into positive and negative parts
        for num in nums:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)

        # Square all elements of both arrays
        positive = square(positive)
        negative = square(negative)

        # Store the final sorted squared array
        final = []

        # Pointer for the last element of negative array
        left = len(negative) - 1

        # Pointer for the first element of positive array
        right = 0

        # Merge both squared arrays in sorted order
        while left >= 0 and right < len(positive):
            if negative[left] <= positive[right]:
                final.append(negative[left])
                left -= 1
            else:
                final.append(positive[right])
                right += 1

        # Add remaining elements from negative array
        while left >= 0:
            final.append(negative[left])
            left -= 1

        # Add remaining elements from positive array
        while right < len(positive):
            final.append(positive[right])
            right += 1

        # Return the final sorted squared array
        return final