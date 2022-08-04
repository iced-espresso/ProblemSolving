class Person:
    def __init__(self, referral):
        self.money = 0
        self.referral = referral
    
    def Distribute(self, profit):
        if self.referral == None:
            self.money += profit
            return
        referralProfit = int(profit * 0.1)
        myProfit = profit - referralProfit
        self.money += myProfit
        if referralProfit > 0:
            self.referral.Distribute(referralProfit)

center = Person(None)
personDict = {'-':center}

def makeTree(enroll, referral):
    for (personName,referralName) in zip(enroll, referral):
        personDict[personName] = Person(personDict[referralName])
    return

def calculateMoney(seller, amount):
    for (s, a) in zip(seller, amount):
        personDict[s].Distribute(a*100)
    return

def getResult(enroll):
    result = [personDict[myName].money for myName in enroll]
    return result

def solution(enroll, referral, seller, amount):
    makeTree(enroll, referral)
    calculateMoney(seller, amount)
    answer = getResult(enroll)
    return answer