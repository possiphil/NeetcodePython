class Solution(object):
    def countSeniors(self, details):
        cnt = 0
        
        for p in details:
            if int(p[11:13]) > 60:
                cnt += 1
        
        return cnt
        