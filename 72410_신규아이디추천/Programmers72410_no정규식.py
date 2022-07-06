import string

def solution(new_id:string):
    answer = str.lower(new_id)
    availableStr = "abcdefghijklmnopqrstuvwxyz-_.0123456789"
    answer = [x for x in answer if x in availableStr]
    answer = "".join(answer)
    while ".." in answer:
        answer = answer.replace("..",".")
    if answer != "" and answer[0] == '.':
        answer = answer[1:]
    if answer != "" and answer[-1] == ".":
        answer = answer[:-1]
    if answer == "":
        answer = "a"
    if len(answer) >= 16:
        answer = answer[:15]
    if answer != "" and answer[-1] == ".":
        answer = answer[:-1]
    if len(answer) <= 2:
        answer += answer[-1] * (3-len(answer))
    return answer

solution("...!@BaT#*..y.abcdefghijklm")