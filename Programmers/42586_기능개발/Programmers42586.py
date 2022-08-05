import math
from platform import release


def calComplteDay(progress, speed) -> int:
    return math.ceil((100-progress)/speed)

def solution(progresses, speeds):
    completeDays = [calComplteDay(progress, speed) for (progress, speed) in zip(progresses, speeds)]
    
    answer = []

    refDay = completeDays[0]
    releaseCnt = 0
    for completeDay in completeDays + [101]:
        if refDay >= completeDay:
            releaseCnt += 1
        else:
            answer.append(releaseCnt)
            releaseCnt = 1
            refDay = completeDay
            
    return answer

solution([93, 30, 55],[1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])