class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        for i in range(10):
            divisor = 10**i
            left = n // (divisor * 10)
            current = (n // divisor) % 10
            right = n % divisor
            # print('iteration = ', i, '{ left: ', left, ', current: ', current, ', right: ', right, ' }')

            if current == 0:
                count += left * divisor
            elif current == 1:
                count += left * divisor + right + 1
            else:
                count += (left + 1) * divisor
        return count

# sol = Solution()
# result = sol.countDigitOne(13)
# print(result)