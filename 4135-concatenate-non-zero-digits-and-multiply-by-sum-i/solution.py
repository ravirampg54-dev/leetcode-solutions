class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        digit_sum = 0
        place = 1

        # Extract digits from right to left
        while n > 0:
            digit = n % 10
            n //= 10

            if digit != 0:
                x = digit * place + x
                place *= 10
                digit_sum += digit

        return x * digit_sum
