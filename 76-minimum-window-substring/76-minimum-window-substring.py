class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = defaultdict(int)
        
        for i in t:
            t_map[i] += 1
        
        dl_count = len(t_map)
        i, j, curr_count = 0, 0, 0
        ans = ""
        
        while j < len(s):
            
            t_map[s[j]] -= 1
            if t_map[s[j]] == 0:
                curr_count += 1
            
            while curr_count == dl_count:
                if not ans or len(ans) > j - i + 1:
                    ans = s[i:j+1]
                t_map[s[i]] += 1
                if t_map[s[i]] == 1:
                    curr_count -= 1
                i += 1
            j += 1
        return ans