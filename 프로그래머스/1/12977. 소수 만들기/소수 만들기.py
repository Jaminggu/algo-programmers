from itertools import combinations

def solution(nums):
    answer = 0

    coms = list(combinations(nums, 3))
    
    for com in coms:
        total = sum(com)
        cnt = 0
        for j in range(2, total):
            if total % j == 0: cnt += 1
        if cnt == 0: answer += 1

    return answer