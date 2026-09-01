def solution(participant, completion):
    dic = dict()
    temp = 0
    
    for part in participant:
        dic[hash(part)] = part
        temp += hash(part)
    
    for comp in completion:
        temp -= hash(comp)
    
    return dic[temp] 