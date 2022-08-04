
def solution(numbers, hand):
    answer = ""
    leftHand = [3,0]
    rightHand = [3,2]
    for n in numbers:
        n = 11 if n == 0 else n
        if n in (1,4,7): # left hand
            moveHand = leftHand
        elif n in (3,6,9):
            moveHand = rightHand
        else:
            
            numPos =  [(n-1)//3, (n-1) % 3]
            leftDis = sum([abs(x-y) for x,y in zip(leftHand,numPos)])
            righttDis = sum([abs(x-y) for x,y in zip(rightHand,numPos)])
            if leftDis < righttDis:
                moveHand = leftHand
            elif leftDis > righttDis:
                moveHand = rightHand
            else:
                if hand == "left":
                    moveHand = leftHand
                else:
                    moveHand = rightHand

        moveHand[0] = (n-1)//3
        moveHand[1] = (n-1) % 3
        answer += "L" if moveHand is leftHand else "R"
    return answer


solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")