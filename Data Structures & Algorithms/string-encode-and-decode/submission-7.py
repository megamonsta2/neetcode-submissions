class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += s + "é"
        return result

    def decode(self, s: str) -> List[str]:
        if s == "": return []
        return s.split("é")[:-1]
