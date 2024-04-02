class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans, mag = {},{}

        for char in ransomNote:
            if char in rans:
                rans[char] += 1
            else:
                rans[char] = 1
        
        for char in magazine:
            if char in mag:
                mag[char] += 1
            else:
                mag[char] = 1
        
        # compare the occurences of letters in ransomnote to magazine
        for key in rans:
            if key not in mag or rans[key] > mag[key]:
                return False
        
        return True
