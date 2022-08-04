import re
import string

def solution(new_id:string):
    answer = str.lower(new_id)
    answer = re.sub("[^_.\-a-z0-9]", "", answer)
    answer = re.sub("\.{2,}", ".", answer)
    answer = re.sub("^[.]|[.]$", "", answer)
    if answer == "":
        answer = "a"
    if len(answer) >= 16:
        answer = answer[:15]
    answer = re.sub("[.]$", "", answer)
    if len(answer) <= 2:
        answer += answer[-1] * (3-len(answer))
    return answer
