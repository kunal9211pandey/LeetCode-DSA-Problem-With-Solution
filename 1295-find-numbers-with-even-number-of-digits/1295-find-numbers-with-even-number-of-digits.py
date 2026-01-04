class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digit_count = 0

        def number_has_even_digits(number: int) -> bool:
            digit_count = 0
            while number != 0:
                number //= 10
                digit_count += 1
            return digit_count % 2 == 0

        for number in nums:
            if number_has_even_digits(number):
                even_digit_count += 1

        return even_digit_count
