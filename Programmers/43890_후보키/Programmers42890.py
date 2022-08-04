from linecache import checkcache
from itertools import combinations

def makeRowToStr(row, colIdxList):
    return "".join([row[col] for col in colIdxList])

def isUniqueSet(relation, colIdxList):
    rowToStrs = [makeRowToStr(row, colIdxList) for row in relation]
    return len(set(rowToStrs)) == len(rowToStrs)

def getUniqueSetList(relation, r):
    candiKeySetList = []
    relationCols = {x for x in range(0, len(relation[0]))}
    candiKeySetList = [set(cols) for cols in combinations(relationCols, r) if isUniqueSet(relation, cols)]
    return candiKeySetList

def isMinimal(CandiKeySetList, keySet):
    for prevCandiKey in CandiKeySetList:
        if (prevCandiKey & keySet) == prevCandiKey:
            return False
    return True

def solution(relation):
    candiKeySetList = []
    for r in range(1, len(relation[0]) + 1):
        uniqueSetList = getUniqueSetList(relation, r)
        uniqueSetList = [keySet for keySet in uniqueSetList if isMinimal(candiKeySetList, keySet)]
        candiKeySetList += uniqueSetList

    return len(candiKeySetList)

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])