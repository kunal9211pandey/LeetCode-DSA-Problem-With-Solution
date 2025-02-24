class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        st={}
        ts={}
        for i , j in zip(s,t):
            if i in st:
                if st[i] != j:
                    return False
            else:
                st[i]=j

            if j in ts:
                if ts[j] != i:
                    return False
            else:
                ts[j]=i
        return True