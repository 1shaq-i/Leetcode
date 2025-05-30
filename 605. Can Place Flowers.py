class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # Check left and right (handle edge cases)
                left_empty = (i == 0) or (flowerbed[i-1] == 0)
                right_empty = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
                
                if left_empty and right_empty:
                    flowerbed[i] = 1  # Plant a flower
                    n -= 1
                    if n == 0:
                        return True
        return n <= 0
