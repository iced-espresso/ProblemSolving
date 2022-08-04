from os import listdir


def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=len)
    listDict = {}
    for x in s:
        for y in x.split(','):
            if y not in listDict:
              answer.append(int(y))
              listDict[y] = 1
    return answer