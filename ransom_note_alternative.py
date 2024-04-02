class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}

        for char in magazine:
            if char in mag:
                mag[char] += 1
            else:
                mag[char] = 1

        # subtract the letters of ransomNote from mag dictionary
        for char in ransomNote:
            if char not in mag or mag[char] <= 0:
                return False
            mag[char] -= 1

        return True
