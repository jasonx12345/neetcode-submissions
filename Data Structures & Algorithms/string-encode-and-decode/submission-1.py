class Solution:
    HashMap = {}
    def encode(self, strs: List[str]) -> str:
        combined = ""

        for word in strs:
            combined += str(len(word)) + "#" + word

        return combined


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the separator after the length
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1

            # Read exactly this many characters
            result.append(s[start:start + length])

            # Move to the next length
            i = start + length

        return result