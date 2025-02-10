class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # Criando a tabela dp com (m+1) linhas e (n+1) colunas
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Caso base da subsequencia "" vazia
        for i in range(m + 1):
            dp[i][0] = 1

        # Preenchendo a tabela com as formas de formar t
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]
    
# sol = Solution()
# main, search = "babgbag", "bag"
# result = sol.numDistinct(main, search)
# print(result)