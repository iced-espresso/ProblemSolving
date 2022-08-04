import collections
from typing import List


def toMagicWords(word) -> str:

    for idx in range(len(word)):
        yield word[:idx] + "*" + word[idx+1:]

class MagicDictionary:
    def __init__(self):
        self.lenBucket = collections.defaultdict(lambda : collections.defaultdict(list))
        return

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            magicDict = self.lenBucket[len(word)]
            for magicWord in toMagicWords(word):
                magicDict[magicWord].append(word)
        return

    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self.lenBucket:
            return False

        magicDict = self.lenBucket[len(searchWord)]
        searchLists = [magicDict[magicWord] for magicWord in toMagicWords(searchWord) if magicWord in magicDict]
                
        return any(len(searchList) > 1 or searchWord != searchList[0] for searchList in searchLists)


# Your MagicDictionary object will be instantiated and called as such:
dictionary = ["hello","leetcode"]
searchWords = ["hello", "hhllo", "hell", "leetcoded"]
obj = MagicDictionary()
obj.buildDict(dictionary)

results = [obj.search(searchWord) for searchWord in searchWords]
print(results)