def solution(s):
    s_list = s.split(' ')
    answer = []
    
    for word in s_list:
        if word:
            word = word[0].upper() + word[1:].lower()
        answer.append(word)
    
    return ' '.join(answer)