class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        ans = []
        digits = "123456789"

        for length in range(2, 10):
            for start in range(0, 10 - length):
                
                temp = digits[start:start + length]
                num = int(temp)

                if low <= num <= high:
                    ans.append(num)

        ans.sort()

        return ans
