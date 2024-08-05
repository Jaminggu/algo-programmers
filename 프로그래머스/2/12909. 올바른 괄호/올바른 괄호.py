def solution(s):
    n = 0
    
    if s[0] == ")" or s[-1] == "(": return False

    for char in s:
        n += 1 if char == "(" else - 1
        if n < 0: break

    return n == 0