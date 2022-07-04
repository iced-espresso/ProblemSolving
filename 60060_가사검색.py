class Node:
    def __init__(self):
        self.nodeDict = {}
        self.lenDict = {}
        
originalRoot = Node()
reverseRoot = Node()
def updateTrie(root, myStr, reverse=False):
    node = root
    lenStr = len(myStr)
    if reverse == True:
        myStr = reversed(myStr)
    for i, c in enumerate(myStr):
        key = lenStr-i
        node.lenDict[key] = node.lenDict.setdefault(key, 0) + 1

        if c in node.nodeDict:
            node = node.nodeDict[c]
            
        else:
            node.nodeDict[c] = Node()
            node = node.nodeDict[c]
    return

def findEndNode(root, myStr):
    node = root
    for c in myStr:
        if c in node.nodeDict:
            node = node.nodeDict[c]
        else:
            return None
    return node

def getCount(query):
    s = query.split("?")
    if query[0] == '?':
        node = findEndNode(reverseRoot, reversed(s[-1]))
    else:
        node = findEndNode(originalRoot, s[0])
    if node == None:
        return 0 # trie에 없는 케이스
    cnt = node.lenDict.setdefault(query.count("?"),0)
    return cnt


def solution(words, queries):
    for word in words:
        updateTrie(originalRoot, word)
        updateTrie(reverseRoot, word, True)
    answer = [getCount(q) for q in queries]
    return answer

