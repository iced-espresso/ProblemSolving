def makeTable(info):
    myHash = dict()
    for i in info:
        s = i.split()
        for lang in (s[0],'-'):
            for job in (s[1], '-'):
                for career in (s[2], '-'):
                    for soulFood in (s[3], '-'):
                        myHash.setdefault((lang,job,career,soulFood), list()).append(int(s[4]))

    for key in myHash:
        myHash[key].sort()
    return myHash
def getHashKey(lang,job,career,soulFood):
    return (lang[0], job[0],career[0],soulFood[0])


def binary_search(sorted_list, searchnum):
    left = 0
    right = len(sorted_list)
    
    while(left < right):
        middle = (left+right)//2
        if searchnum <= sorted_list[middle]:
            right = middle
        else:
            left = middle + 1
    return left


def getQueryResult(myTable, query):
    q = query.split()
    qscore = int(q[7])
    candi = myTable.setdefault((q[0], q[2], q[4], q[6]), list())
    bbidx = binary_search(candi, qscore)
    return len(candi) - bbidx

def solution(info, query):
    answer = []
    myTable = makeTable(info)
    answer = [getQueryResult(myTable,  q) for q in query]
    return answer