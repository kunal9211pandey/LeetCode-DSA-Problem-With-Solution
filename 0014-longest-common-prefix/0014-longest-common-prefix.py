class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()

        frist=strs[0]
        last=strs[-1]

        ans=""
        for i in range(min(len(frist),len(last))):
            if frist[i] != last[i]:
                return ans
            ans += frist[i]
        return ans