'''
정확성: 30.0
효율성: 0.0
합계: 30.0 / 100.0
'''

def solution(participant, completion):
    answer = ''
    for person in completion:
        for sub_person in participant:
            if sub_person == person:
                participant.remove(person)
                continue
    answer = ''.join(participant)
    return answer