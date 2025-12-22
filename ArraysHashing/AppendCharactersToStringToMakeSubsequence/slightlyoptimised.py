class Solution(object):
    def appendCharacters(self, s, t):
        n, m = len(t), len(s)
        i, j = 0, 0

        while i < n and j < m:
            if t[i] == s[j]:
                i+=1
            j+=1

        return n - i
        