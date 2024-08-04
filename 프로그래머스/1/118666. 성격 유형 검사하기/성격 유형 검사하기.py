def solution(survey, choices):
    answer = ''
    test_dict = {char: 0 for char in "RTCFJMAN"}
    
    for idx, item in enumerate(survey):
        choice = choices[idx]
        
        score = abs(choice - 4)
        
        if choice < 4:
            test_dict[item[0]] += score
        elif choice > 4:
            test_dict[item[1]] += score
        
    for char1, char2 in [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]:
        if test_dict[char1] >= test_dict[char2]:
            answer += char1
        else:
            answer += char2
        if len(answer) == 4: break
    
    return answer