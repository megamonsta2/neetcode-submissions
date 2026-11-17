class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        SFound = self.getFound(s)
        TFound = self.getFound(t)

        for i in SFound:
            if i not in TFound or SFound[i] != TFound[i]:
                return False
        return True

    def getFound(self, s: str) -> dict[str, int]:
        found = {}
        for i in s:
            if i in found:
                found[i] += 1
            else:
                found[i] = 1
        return found
