def solution(n, words):
    answer = []
    words_set = set()
    
    for i in range(len(words)):
        if words[i] in words_set or (i > 0 and words[i - 1][-1] != words[i][0]):
            return [(i % n) + 1, (i // n) + 1]
        words_set.add(words[i])

    return [0, 0]