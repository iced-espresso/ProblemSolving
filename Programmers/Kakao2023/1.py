from datetime import date, timedelta

def strToDate(myStr):
    strSplit = myStr.split('.')
    intList = list(map(int,strSplit))
    return date(intList[0], intList[1], intList[2])

def solution(today, terms, privacies):
    termDict = {term.split()[0]:int(term.split()[1]) for term in terms}
    todayDate = strToDate(today)
    answer = []
    for i, privacy in enumerate(privacies):
        privacyDate, term = privacy.split()
        strSplit = privacyDate.split('.')
        intList = list(map(int,strSplit))
        intList[1] += termDict[term]
        newYear, newMonth = (intList[1]-1)//12, (intList[1] -1) % 12
        intList[0] += newYear
        intList[1] = newMonth+1
        privacyDate = date(intList[0], intList[1], intList[2])
        if privacyDate <= todayDate:
            answer.append(i+1)

    
    return answer


solution(
"2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])

