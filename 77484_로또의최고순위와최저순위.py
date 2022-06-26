def solution(lottos, win_nums):
    answer = []

    win_num_dict = dict.fromkeys(win_nums, 1)
    matchList = [x for x in lottos if x in win_num_dict]
    
    lowMatchCnt = len(matchList)
    highMatchCnt = lowMatchCnt + lottos.count(0)
    
    rankHash = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    answer.append(rankHash[highMatchCnt])
    answer.append(rankHash[lowMatchCnt])

    return answer