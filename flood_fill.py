class Solution: 
    def fill(self, image: List[List[int]], sr: int, sc: int, currentColor: int, color: int):
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != currentColor:
            return
        image[sr][sc] = color
        self.fill(image, sr + 1, sc, currentColor, color)
        self.fill(image, sr - 1, sc, currentColor, color)
        self.fill(image, sr, sc + 1, currentColor, color)
        self.fill(image, sr, sc - 1, currentColor, color)
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        self.fill(image, sr, sc, image[sr][sc], color)
        return image
        
