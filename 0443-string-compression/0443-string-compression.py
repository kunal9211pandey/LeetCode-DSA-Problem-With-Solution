class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        index = 0
        n = len(chars)

        while i < n:
            current_char = chars[i]
            count = 0

            while i < n and chars[i] == current_char:
                i += 1
                count += 1

            chars[index] = current_char
            index += 1

            if count > 1:
                for digit in str(count):
                    chars[index] = digit
                    index += 1

        return index
