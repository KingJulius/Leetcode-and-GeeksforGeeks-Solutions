class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}
        
        def helper(sub):
            if sub in memo:
                return memo[sub]
            result = []
            for i in range(len(sub)):
                prefix = sub[:i+1]
                if prefix in wordSet:
                    if prefix == sub:
                        result.append(prefix)
                    else:
                        restofWords = helper(sub[i+1:])
                        for phrase in restofWords:
                            result.append(prefix+" "+phrase)
            memo[sub] = result
            return result
        return helper(s)