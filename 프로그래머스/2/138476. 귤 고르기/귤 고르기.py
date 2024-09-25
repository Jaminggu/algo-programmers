def solution(k, tangerine):
    answer = 0
    tangerine_dict = {};
    
    for size in tangerine:
        if size in tangerine_dict:
            tangerine_dict[size] = tangerine_dict[size] + 1
        else:
            tangerine_dict[size] = 1
    tangerine_dict = sorted(tangerine_dict.items(), key=lambda x: x[1], reverse=True)
    
    for size, count in tangerine_dict:
        k = k - count
        answer += 1
        
        if k <= 0:
            return answer