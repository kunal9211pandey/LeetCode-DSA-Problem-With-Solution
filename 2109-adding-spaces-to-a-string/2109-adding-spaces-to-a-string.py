class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        space_idx = 0

        for i in range(len(s)):
            if space_idx < len(spaces) and i == spaces[space_idx]:
                result.append(' ')
                space_idx += 1

            result.append(s[i])

        return "".join(result)
