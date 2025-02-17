class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        rows = len(text1)
        cols = len(text2)
        
      
        dp = [[0 for col in range(cols + 1)] for row in range(rows + 1)]
        

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1  
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  

        return dp[rows][cols]