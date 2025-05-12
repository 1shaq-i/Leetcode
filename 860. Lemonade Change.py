class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = {5: 0, 10: 0}

        for num in bills:
            if num == 5:
                counter[num] += 1
            if num == 10:
                if counter[5] > 0:
                    counter[5] -= 1
                    counter[num] += 1
                else:
                    return False
            if num == 20:
                if counter[5] > 0 and counter[10] > 0:
                    counter[5] -= 1
                    counter[10] -= 1
                elif counter[5] > 2:
                    counter[5] -= 3
                else:
                    return False
        return True
