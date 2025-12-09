from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sorted_char = sorted(freq.items() , key = lambda x:x[1] , reverse = True)
        results = ''.join(i * j for i , j in sorted_char)
        return results