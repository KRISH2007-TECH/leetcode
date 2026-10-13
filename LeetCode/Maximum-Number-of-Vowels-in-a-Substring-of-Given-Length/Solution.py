1class Solution(object):
2    def maxVowels(self, s, k):
3        vowels = set("aeiou")
4        c = sum(1 for ch in s[:k] if ch in vowels)
5        ans = c
6
7        for i in range(k, len(s)):
8            if s[i] in vowels:
9                c += 1
10            if s[i - k] in vowels:
11                c -= 1
12
13            ans = max(ans, c)
14
15        return ans
16        """
17        :type s: str
18        :type k: int
19        :rtype: int
20        """
21        