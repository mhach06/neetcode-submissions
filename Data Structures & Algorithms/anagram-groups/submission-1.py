import copy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_arr = []

        # Use enumerate to track the outer index (i)
        for i, word in enumerate(strs):
            in_final = False

            for row in final_arr:
                if word in row:
                    in_final = True
                    break
            
            if in_final:
                continue
            else:
                counts = [0] * 26
                for letter in word:
                    index = ord(letter) - ord('a')
                    counts[index] += 1
                
                cur_block = []
                cur_block.append(word)
                
                # Use enumerate to track the inner index (j)
                for j, cur_word in enumerate(strs):
                    # FIX: Only skip if it's the exact same index. 
                    # Do NOT skip just because the strings match in value.
                    if i == j or len(word) != len(cur_word):
                        continue

                    temp_count = copy.deepcopy(counts)
                    for letter in cur_word:
                        index = ord(letter) - ord('a')
                        temp_count[index] -= 1
                    
                    is_anagram = True
                    for count in temp_count:
                        if count != 0:
                            is_anagram = False
                    
                    if is_anagram:
                        cur_block.append(cur_word)

            final_arr.append(cur_block)
        
        return final_arr