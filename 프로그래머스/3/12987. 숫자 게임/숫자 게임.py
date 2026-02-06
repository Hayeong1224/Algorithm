import heapq
def solution(A, B):
    ans = 0
    A.sort(reverse= True)
    B.sort(reverse= True)
    a_idx, b_idx = 0, 0
    
    for i in range(len(A)):
        if B[b_idx] > A[a_idx]:
            a_idx += 1
            b_idx += 1
            ans += 1
        else:
            a_idx += 1
            B.pop()
        
    return ans