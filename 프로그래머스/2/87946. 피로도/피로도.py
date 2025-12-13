from itertools import permutations
def solution(k, dungeons):
    m = 0
    perms = permutations(dungeons,len(dungeons))
    for p in perms:
        count = 0
        tk = k
        for i in p:
            if tk >= i[0]:
                tk -= i[1]
                count += 1
        m = max(m, count)
    return(m)