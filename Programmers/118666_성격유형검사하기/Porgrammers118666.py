def solution(survey, choices):
    personalityScore = {"RT":0, "CF":0, "JM":0, "AN":0}
    for s, c in zip(survey, choices):
        score = c - 4
        if s in personalityScore.keys():
            personalityScore[s] += score
        else:
            personalityScore[s[::-1]] -= score
    answer = ""
    for k, v in zip(personalityScore.keys(), personalityScore.values()):
            answer += k[0] if v <= 0 else k[1]
    return answer


solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])