class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def solve(image, sr, sc, currColor, newColor):
            if sr >= len(image) or sr < 0 or sc < 0 or sc >= len(image[0]) or image[sr][sc] != currColor:
                return
            image[sr][sc] = newColor
            solve(image, sr+1, sc, currColor, newColor)
            solve(image, sr-1, sc, currColor, newColor)
            solve(image, sr, sc+1, currColor, newColor)
            solve(image, sr, sc-1, currColor, newColor)
        if image[sr][sc] != color:
            solve(image, sr, sc, image[sr][sc], color)
        return image