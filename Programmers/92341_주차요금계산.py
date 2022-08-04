import math
from collections import defaultdict

inTimeMap = dict()
accTimeMap = defaultdict(lambda:0)

def timeStrToNum(timeStr):
    h,m = timeStr.split(":")
    minuateNum = int(h)*60 + int(m)
    return minuateNum

def carIn(carNumStr, timeStr):
    inTimeMap[carNumStr] = timeStrToNum(timeStr)

def carOut(carNumStr, timeStr):
    accTimeMap[carNumStr] += timeStrToNum(timeStr) - inTimeMap[carNumStr]
    del inTimeMap[carNumStr]

def calculateTotalTimes(records):
    for record in records:
        s = record.split()
        if s[2] == "IN":
            carIn(s[1], s[0])
        elif s[2] == "OUT":
            carOut(s[1], s[0])
    noOutList = [carnum for carnum in inTimeMap.keys()]
    for carNum in noOutList:
        carOut(carNum, "23:59")

def calcuateFees(fees):
    feeList = []
    for carNum, time in zip(accTimeMap, accTimeMap.values()):
        fee = fees[1]
        if fees[0] < time:
            fee += math.ceil( (time -fees[0])/fees[2])*fees[3]
        feeList.append((carNum,fee))
    feeList.sort(key=lambda x:int(x[0]))
    feeList = [x[1] for x in feeList]
    return feeList
    
def solution(fees, records):
    calculateTotalTimes(records)
    answer =  calcuateFees(fees)
    return answer

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])