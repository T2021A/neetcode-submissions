from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counter = {}
        t_counter = {}
        for i in range(len(s)):
            if s[i] in s_counter:
                s_counter[s[i]] += 1
            else:
                s_counter[s[i]] = 1
            if t[i] in t_counter:
                t_counter[t[i]] += 1
            else:
                t_counter[t[i]] = 1
        return t_counter == s_counter 
