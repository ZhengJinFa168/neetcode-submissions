class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        output=""
        for phrases in strs:
            output = output + "€" + phrases

        return output

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        return s.split("€")[1:]
