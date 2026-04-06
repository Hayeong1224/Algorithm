from itertools import permutations

def solution(k, dungeons):
    for i in range(len(dungeons), 0, -1):
        for p in permutations(dungeons, i):
            cur_k = k
            success = True
            
            for need, spend in p:
                if cur_k >= need and cur_k - spend >= 0:
                    cur_k -= spend
                else: 
                    success = False
                    break
            
            if success: return i