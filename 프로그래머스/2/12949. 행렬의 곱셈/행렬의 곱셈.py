def solution(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])
    answer = [[0] * c2 for _ in range(r1)]
    
    for r in range(r1):
        row = arr1[r]
        for c in range(c2):
            col = [arr2[i][c] for i in range(r2)]
            answer[r][c] = sum(a * b for a, b in zip(row, col))
    
    return answer