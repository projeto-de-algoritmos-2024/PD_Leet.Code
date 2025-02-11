class Solution:
    def maximalRectangle(self, matrix) -> int:
        # Extraindo linhas e colunas
        rows = len(matrix)
        cols = len(matrix[0])

        # Calculando vetor de maximas alturas para cada celula 
        heights = [0] * cols
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                # Adiciona a altura da celula caso encontre 1
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0

            # print('alturas atuais: ', heights)
            # Area maxima no escopo atual
            stack = []
            for idx, h in enumerate(heights + [0]):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = idx if not stack else idx - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(idx)

        return max_area


# s = Solution()
# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]] 
# area = s.maximalRectangle(matrix)
# print(area)