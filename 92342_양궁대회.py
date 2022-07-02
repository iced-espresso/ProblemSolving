from functools import cmp_to_key
diffMax = 0
candiList = []



def calDiff(apeachInfo, lionInfo):
    scoreApeach = 0
    scoreLion = 0
    for idx, a, l in zip(range(11), apeachInfo, lionInfo):
        if a >= l:
            if a != 0:
                scoreApeach += 10-idx
        else:
            scoreLion += 10-idx
    return scoreLion - scoreApeach

def myCompare(info1, info2):
    for i1, i2 in list(zip(info1, info2))[::-1]:
        if i2 > i1: return -1
        if i1 > i2: return 1


# n = 남은화살갯수
def dfs(idx, n, apeachInfo:list, lionInfo:list):
    if n == 0:
        diff = calDiff(apeachInfo, lionInfo)
        global candiList
        global diffMax
        if diff == diffMax and diff != 0:   
            newList = [x for x in lionInfo]
            candiList = max((candiList, newList), key=cmp_to_key(myCompare))
        elif diff > diffMax:
            candiList = [x for x in lionInfo]
            

            diffMax = diff
        return
    
    if idx == 10:
        lionInfo[idx] = n
        dfs(idx+1, 0, apeachInfo, lionInfo)
        lionInfo[idx] = 0
        return

    #지는 경우
    dfs(idx+1, n, apeachInfo, lionInfo)

    #이기는 경우
    if n > apeachInfo[idx] :
        lionInfo[idx] = apeachInfo[idx] + 1
        dfs(idx+1, n - lionInfo[idx], apeachInfo, lionInfo)
        lionInfo[idx] = 0



def solution(n, info):
    answer = []
    global apeachInfo
    apeachInfo = info
    global diffMax
    diffMax = 0
    dfs(0, n, info, [0]*11)
    
    if diffMax == 0:
        answer = [-1]
    else:
        answer = candiList[0]

        answer = candiList
    return answer

solution(9, [0,0,1,2,0,1,1,1,1,1,1]	)