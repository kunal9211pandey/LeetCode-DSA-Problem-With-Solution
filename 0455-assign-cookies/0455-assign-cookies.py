class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = 0  # child pointer
        j = 0  # cookie pointer

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1      # child satisfied
            j += 1          # move to next cookie

        return i
