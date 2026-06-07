class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        arr = [0] * 26

        for letter in s:
            index = ord(letter) - ord('a')
            arr[index] += 1
        
        for letter in t:
            index = ord(letter) - ord('a')
            arr[index] -= 1
        
        for num in arr:
            if num != 0:
                return False
        
        return True
        

        
