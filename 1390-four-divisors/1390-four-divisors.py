class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0

        for num in nums:
            count = 0
            div_sum = 0

            d = 1
            while d * d <= num:
                if num % d == 0:
                    other = num // d

                    if d == other:
                        count += 1
                        div_sum += d
                    else:
                        count += 2
                        div_sum += d + other

                    # Early break: more than 4 divisors
                    if count > 4:
                        break
                d += 1

            if count == 4:
                total_sum += div_sum

        return total_sum
