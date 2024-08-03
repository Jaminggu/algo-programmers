def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for participant_person in participant:
        if participant_person in completion: completion.remove(participant_person)
        else: return participant_person
