def solution(ingredient):
    answer = 0
    hamburger = []
    
    for item in ingredient:
        hamburger.append(item)
        
        if len(hamburger) >= 4 and hamburger[-4:] == [1, 2, 3, 1]:
            answer += 1
            del hamburger[-4:]
    
    return answer