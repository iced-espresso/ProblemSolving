from collections import deque
from pickle import TRUE
from tkinter.tix import Tree
MAXR = 5
MAXC = 5

def getManDistance(r1,c1, r2,c2):
    return abs(r1-r2) + abs(c1-c2)

def isOutOfRange(r,c):
    return (r < 0 or r >= MAXR or c < 0 or c >= MAXC)

def hasClosePeople(place, row, col):
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    searchQ = deque()
    searchQ.append([row, col])
    while len(searchQ) > 0:
        currR, currC = searchQ.popleft()
        dis = getManDistance(row,col, currR, currC)

        if dis >= 2:
            continue
        searchPosList = [(currR+r,currC+c) for r,c in zip(dr,dc) if not isOutOfRange(currR+r, currC+c)]
        for nextR, nextC in searchPosList:
            if(nextR == row and nextC == col): continue
            if place[nextR][nextC] == 'P':
                return True
            
            if place[nextR][nextC] == 'O' and dis < getManDistance(row,col, nextR, nextC):
                searchQ.append([nextR, nextC])
            
    return False

def getSolByRoom(place):
    for row, rows in enumerate(place):
        for col, string in enumerate(rows):
            if(string == 'P'):
                if hasClosePeople(place, row, col):
                    return 0
    return 1

def solution(places):

    answer = [getSolByRoom(place) for place in places]
    print(answer)
    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)