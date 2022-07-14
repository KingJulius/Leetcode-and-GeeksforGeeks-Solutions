class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        l, r = 0, len(products)-1
        res = []
        products.sort()
        for i in range(len(searchWord)):
            c = searchWord[i]
            while l<=r and (len(products[l])<=i or c!=products[l][i]):
                l += 1
            while l<=r and (len(products[r])<=i or c!=products[r][i]):
                r -= 1
            res.append([])
            for j in range(min(r-l+1, 3)):
                res[-1].append(products[l+j])
        return res
        