class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        found: dict[int, list[str]] = {}
        for s in strs:
            charList = [0] * 26
            for c in s:
                charList[ord(c.lower()) - 97] += 1
            chars = hash(tuple(charList))
            
            if chars in found:
                found[chars].append(s)
            else:
                found[chars] = [s]

        result: list[list[str]] = []
        for f in found:
            result.append(found[f])
        return result