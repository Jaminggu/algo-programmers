def solution(data, ext, val_ext, sort_by):
    answer = []
    data_codes = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    c1 = data_codes[ext]
    c2 = data_codes[sort_by]
        
    for item in data:
        if item[c1] < val_ext:
            answer.append(item)
        
        answer.sort(key=lambda x: x[c2])
            
    
    return answer