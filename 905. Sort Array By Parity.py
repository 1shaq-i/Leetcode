class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        for num in nums:
            rem = num % 2
            if rem == 0:
                even.append(num)
            else:
                odd.append(num)
        
        res = even + odd
        return res
