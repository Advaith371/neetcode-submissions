from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required_chars = defaultdict(int)
        found_chars = defaultdict(int)
        smallest_str = None  # tupla (l, r)
        l = 0

        for c in t:
            required_chars[c] += 1

        for r in range(len(s)):
            if s[r] in required_chars:
                found_chars[s[r]] += 1

            valid_substring = True

            while valid_substring:        
                for k, v in required_chars.items():
                    if found_chars[k] < v:
                        valid_substring = False
                        break
                
                if valid_substring:
                    while s[l] not in required_chars:
                        l += 1
        
                    current_len = r - l + 1
        
                    if smallest_str is None or current_len < (smallest_str[1] - smallest_str[0] + 1):
                        smallest_str = (l, r)

                    found_chars[s[l]] -= 1
                    l += 1
    
        return "" if not smallest_str else s[smallest_str[0]:smallest_str[1] + 1]