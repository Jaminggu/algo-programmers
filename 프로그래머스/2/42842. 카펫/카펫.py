def solution(brown, yellow):
    answer = []
    length = []
    
    if yellow == 1: return [3, 3]

    for i in range(1, int(yellow**0.5) + 1):
        if yellow % i == 0:
            width = max(i, int(yellow / i)) + 2
            height = min(i, int(yellow / i)) 
            if (width + height) * 2 == brown:
                return [width, height + 2]

    return answer