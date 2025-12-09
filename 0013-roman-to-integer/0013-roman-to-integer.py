class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000
        }
        total = 0
        prev = 0
        for char in s:
            current = roman_to_int[char]
            if current > prev:
                total += current - 2 * prev
            else:
                total += current
            prev = current
        return total
        