class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        memo = [[False] * (len(t)+1) for _ in range(len(s)+1)]

        for j in range(len(t)+1):
            memo[len(s)][j] = True

        for i in range(len(s)-1, -1, -1):
            for j in range(len(t)-1, -1, -1):
                if s[i] == t[j]:
                    memo[i][j] = memo[i+1][j+1]
                else:
                    memo[i][j] = memo[i][j+1]

        return memo[0][0]
        