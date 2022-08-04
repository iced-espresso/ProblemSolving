def checkRightStr(u):
    leftCnt = 0
    rightCnt = 0
    for c in u:
        if c == '(':
            leftCnt += 1
        else:
            rightCnt += 1
        if leftCnt < rightCnt:
            return False
    return leftCnt == rightCnt

def flip(x):
    flipHash = {"(":")", ")":"("}
    return flipHash[x]

def change(w):
    if w == "": return w
    u, v = splitBalenced(w)
    if checkRightStr(u):
        return u + change(v)
    else:
        u = "".join([flip(x) for x in u[1:-1]])
        u = "(" + change(v) + ")" + u
        return u

    
def splitBalenced(w):
    leftCnt = 0
    rightCnt = 0
    for i, c in enumerate(w):
        if c == '(':
            leftCnt += 1
        else:
            rightCnt += 1
        if leftCnt == rightCnt:
            return (w[0:i+1], w[i+1:])

def solution(p):
    answer = change(p)
    return answer
