class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        for word in strs:
            # If word is "hello", this becomes "5#hello"
            encoded_list.append(str(len(word)) + "#" + word)
    
        return "".join(encoded_list)

    def decode(self, s: str) -> List[str]:
        final_strs = []
        i = 0
    
        while i < len(s):
            # 1. Find where the '#' is to grab the length
            j = i
            while s[j] != '#':
                j += 1
            
            # 2. Extract the length (the numbers between i and j)
            length = int(s[i:j])
        
            # 3. The actual word starts right after the '#' (j + 1)
            start = j + 1
            end = start + length
        
            # 4. Slice out the exact word and save it
            final_strs.append(s[start:end])
        
            # 5. Move our pointer 'i' to the beginning of the next block
            i = end
        
        return final_strs


