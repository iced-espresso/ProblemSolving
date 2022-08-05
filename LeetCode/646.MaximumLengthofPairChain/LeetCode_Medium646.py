from itertools import chain
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        lastChain = pairs[0][1]
        chainCnt=1
        for pair in pairs:
            if lastChain < pair[0]:
                lastChain = pair[1]
                chainCnt += 1

        return chainCnt



Solution().findLongestChain( [[1,2],[2,3],[3,4]])