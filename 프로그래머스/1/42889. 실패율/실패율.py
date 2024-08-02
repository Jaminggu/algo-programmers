def solution(N, stages):
    answer = []
    failure_rate = {}
    users_cnt = len(stages)
    
    for i in range(1, N + 1):
        pass_user = stages.count(i)
        if pass_user:
            failure_rate[i] = pass_user / users_cnt
        else:
            failure_rate[i] = 0

        users_cnt -= pass_user
    
    return sorted(failure_rate, key = lambda x: failure_rate[x], reverse = True)