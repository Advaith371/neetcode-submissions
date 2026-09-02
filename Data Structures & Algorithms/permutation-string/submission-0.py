class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = {}
        comp = {}
        if len(s1) > len(s2): return False
        for i in s1:
            target[i] = 1 + target.get(i, 0)
        for i in range(len(s1)):
            comp[s2[i]] = 1 + comp.get(s2[i], 0)
        r = len(s1)
        while r < len(s2):
            if comp == target:
                return True
            else:
                comp[s2[r]] = 1 + comp.get(s2[r], 0)
                if comp[s2[r-len(s1)]] > 1:
                    comp[s2[r-len(s1)]] -= 1
                else:
                    del comp[s2[r-len(s1)]]
            r += 1
        if comp == target:
                return True
        return False