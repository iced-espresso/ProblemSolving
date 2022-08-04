from collections import defaultdict

userDict = defaultdict(lambda:set())
reportCntDict = defaultdict(lambda:0)

def processReport(reports):
    for report in reports:
        s = report.split()
        if s[1] not in userDict[s[0]]:
            userDict[s[0]].add(s[1])
            reportCntDict[s[1]] += 1

def getSuccessCnt(id, k):
    return len([x for x in userDict[id] if reportCntDict[x] >= k])

def solution(id_list, report, k):
    processReport(report)
    answer = [getSuccessCnt(x,k) for x in id_list]
    return answer

solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)