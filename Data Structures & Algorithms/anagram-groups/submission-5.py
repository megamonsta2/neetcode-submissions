class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        found: dict[int, list[str]] = {}
        for s in strs:
            chars = self.getCharacters(s)
            if chars in found:
                found[chars].append(s)
            else:
                found[chars] = [s]

        result: list[list[str]] = []
        for f in found:
            result.append(found[f])
        return result

    def getCharacters(self, s: str) -> int:
        found = [0] * 26
        for c in s:
            found[self.getChar(c)] += 1
        return hash(tuple(found))

    def getChar(self, c: str) -> int:
        return ord(c.lower()) - 97