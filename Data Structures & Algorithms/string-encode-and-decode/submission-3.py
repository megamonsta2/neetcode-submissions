class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            for c in s:
                result += self.encodeOne(c)
            result += "é"
        return result

    def encodeOne(self, s: str) -> str:
        return chr((ord(s) + 1) % 256)

    def decode(self, string: str) -> List[str]:
        result = []
        for s in string.split():
            word = ""
            for c in s:
                if c == "é":
                    result.append(word)
                    word = ""
                else:
                    word += self.decodeOne(c)
        return result

    def decodeOne(self, s: str) -> str:
        return chr((ord(s) - 1) % 256)
