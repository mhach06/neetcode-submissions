class Solution:

    def encode(self, strs: List[str]) -> str:
        # cannot use char to split since all chars may be used
        
        prefix = "prefix"

        for idx in range(len(strs)):
            strs[idx] = prefix + strs[idx]
        
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        s = s.split("prefix")
        return s[1:]


