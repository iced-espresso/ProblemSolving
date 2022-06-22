def solution(s):
    answerList = [len(s)]
    answerList += [compress(s, splitLen) for splitLen in range(1, int(len(s)/2 + 1))]
    return min(answerList)

def compress(s, splitLen):
    splitedStrs = [s[i:i+splitLen] for i in range(0, len(s), splitLen)]
    return getCompressedStrLen(splitedStrs)

def getCompressedStrLen(splitedStrs):
    compressedStrLen = 0
    refWord = splitedStrs[0]
    cnt = 1
    for _, s in enumerate(splitedStrs[1:] + ['']):
        if refWord == s:
            cnt += 1
        else:
            compressedStrLen = compressedStrLen + getMergedLen(refWord, cnt)
            refWord = s
            cnt = 1
    return compressedStrLen

def getMergedLen(refWord, cnt):
    if cnt == 1:
        return len(refWord)
    return len(str(cnt) + refWord)

a = [
    "a",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))