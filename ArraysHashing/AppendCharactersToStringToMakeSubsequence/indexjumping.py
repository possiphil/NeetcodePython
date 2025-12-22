class Solution(object):
    def appendCharacters(self, s, t):
        n, m = len(t), len(s)
        a = ord('a')

        if (m == 0):
            return n == 0

        store = [[m+1] * 26 for _ in range(m)]
        store[m-1][ord(s[m-1]) - a] = m-1

        for i in range(m-2, -1, -1):
            store[i] = store[i+1][:]
            store[i][ord(s[i]) - a] = i
        
        i, j = 0, 0

        while i < n and j < m:
            j = store[j][ord(t[i]) - a] + 1
            if j > m:
                break
            i+=1

        return n - i
        