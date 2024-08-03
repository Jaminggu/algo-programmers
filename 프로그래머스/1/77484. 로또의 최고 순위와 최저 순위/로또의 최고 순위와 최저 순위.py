def solution(lottos, win_nums):
    answer = []
    high = 0
    low = 0
    
    for num in lottos:
        if num != 0 and num in win_nums: low += 1
    
    if low == 6:
        answer.append(1)
    elif low == 5:
        answer.append(2)
    elif low == 4:
        answer.append(3)
    elif low == 3:
        answer.append(4)
    elif low == 2:
        answer.append(5)
    else:
        answer.append(6)
        
    high += low + lottos.count(0)
    
    if high == 6:
        answer.append(1)
    elif high == 5:
        answer.append(2)
    elif high == 4:
        answer.append(3)
    elif high == 3:
        answer.append(4)
    elif high == 2:
        answer.append(5)
    else:
        answer.append(6)
        
    answer.sort()
    
    return answer