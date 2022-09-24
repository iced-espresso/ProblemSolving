def solution(cap, n, deliveries, pickups):
    answer = 0

    delCap = 0
    pickCap = 0

    for i in range(n)[::-1]: 
        if deliveries[i] == 0 and pickups[i] == 0:
            continue

        answer += (i+1)*2

        pickCap = pickups[i]
        pickups[i] = 0
        delCap = deliveries[i]
        deliveries[i] = 0
        for j in range(i)[::-1]:
            pickCap += pickups[j]
            if pickCap > cap:
                pickups[j] = pickCap-cap
                break
            pickups[j] = 0
            

        for j in range(i)[::-1]:
            delCap += deliveries[j]
            if delCap > cap:
                deliveries[j] = delCap-cap
                break
            deliveries[j] = 0
    return answer


solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])