from collections import Counter
import heapq
from string import ascii_lowercase



class Solution:

    def getMaxAlphabet(self, prevChar):
        maxChar = '-'
        searchList = [x for x in self.s_count.items() if x[0] != prevChar]
        if len(searchList) == 0:
            return '-'
        return max(searchList, key=lambda x:x[1])[0]

    def reorganizeString(self, s: str) -> str:
        self.s_count = Counter(s)
        c = '-'
        ret = []
        for i in range(len(s)):
            c = self.getMaxAlphabet(c)
            if c == '-':
                return ""
            self.s_count[c] -= 1
            if self.s_count[c] <= 0:
                del(self.s_count[c])
            ret.append(c)
        return "".join(ret)

print(Solution().reorganizeString("aab"))
print(Solution().reorganizeString("aaab"))