def addZeroToLeft(n, x):
    return '0'*(n-len(x)) + x

def solution(n, arr1, arr2):
    answer = [bin(x1|x2)[2:] for x1,x2 in zip(arr1,arr2)]
    answer = [addZeroToLeft(n, x) for x in answer]
    answer = [x.replace('1','#').replace('0',' ') for x in answer]
    return answer

solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])