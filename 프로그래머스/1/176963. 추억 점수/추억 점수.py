def solution(name, yearning, photo):
    answer = []
    yearning_dict = dict(zip(name, yearning))
    
    for group in photo:
        total = 0
        
        for name in group:
            if name in yearning_dict: total += yearning_dict[name]
        answer.append(total)
    
    return answer