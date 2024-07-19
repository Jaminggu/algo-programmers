def solution(s):
    status = 0

    for char in s:
        if char == 'p' or char == 'P':
            status += 1
        elif char == 'y' or char == 'Y':
            status -= 1

    return status == 0