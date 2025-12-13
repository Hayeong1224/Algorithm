from itertools import permutations
def solution(k, dungeons):
    max_count = 0
    perms = permutations(dungeons,len(dungeons))
    for p in perms:
        temp_count = 0
        temp_k = k
        for required, consumed  in p:
            if temp_k >= required:
                temp_k -= consumed
                temp_count += 1
        max_count = max(max_count, temp_count)
    return(max_count)