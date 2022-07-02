import math
def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    return convert_notation(q, base) + T[r] if q else T[r]

def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True

def splitNum(nStr):

    splited = []
    word = ""
    for i, c in enumerate(nStr):
        if c == '0':
            if word != "":
                splited.append((i,word))
            word = ""       
        else:
            word += c
    return splited
def solution(n, k):
    convertNum = convert_notation(n,k)
    s = convertNum.split('0')
    s = [x for x in s if x != ""]
    primeList = [x for x in s if is_prime_number(int(x))]
    answer = len(primeList)
    return answer

solution(437674, 3)
solution(110011	, 10)