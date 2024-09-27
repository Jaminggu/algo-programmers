def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount) - 9):
        discount_dict = {}
        checked = True
        for j in range(i, i + 10):
            if discount[j] in discount_dict:
                discount_dict[discount[j]] += 1
            else:
                discount_dict[discount[j]] = 1
        
        for j in range(len(want)):
            if discount_dict.get(want[j], 0) != number[j]:
                checked = False
                break
        
        if checked: 
            answer += 1
    
    return answer
