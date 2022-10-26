class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wordSet = set(wordlist)
        wordMapCapital = {}
        wordMapWildCard = {}
        res = []
        
        for word in wordlist:
            if word.upper() not in wordMapCapital:
                wordMapCapital[word.upper()] = word
            mask = ''.join(["*" if c.lower() in "aeiou" else c.upper() for c in word])
            if mask not in wordMapWildCard:
                wordMapWildCard[mask] = word
        
        
        for query in queries:
            curr = ""
            if query in wordSet:
                curr = query
            elif query.upper() in wordMapCapital:
                curr = wordMapCapital[query.upper()]
            else:
                mask = ''.join(["*" if c.lower() in "aeiou" else c.upper() for c in query])
                if mask in wordMapWildCard:
                    curr = wordMapWildCard[mask]
            res.append(curr)
        
        return res