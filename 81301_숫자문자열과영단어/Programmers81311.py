def solution(s):
    for key, val in zip(["zero","one","two","three","four","five","six","seven","eight","nine"], range(0,10)):
        s = s.replace(key,str(val))
    answer = int(s)
    return answer