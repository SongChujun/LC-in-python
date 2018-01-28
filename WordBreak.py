class Solution(object):
    mem=[]
    def wordBreak(self, s, wordDict):
        global mem
        mem=[-1 for _ in range(len(s)+1)]
        return self.dp(s,wordDict)
    def dp(self,s,wordDict):
        global mem
        if not s:
            mem[0]=1
            return True
        elif s in wordDict:
            mem[len(s)]=1
            return True
        elif mem[len(s)]!=-1:
            return bool(mem[len(s)])
        for i in range(1,len(s)):
            if s[:i] in wordDict:
                res=self.dp(s[i:],wordDict)
                if res==1:
                    mem[len(s)]=1
                    return True
        mem[len(s)]=0
        return False




