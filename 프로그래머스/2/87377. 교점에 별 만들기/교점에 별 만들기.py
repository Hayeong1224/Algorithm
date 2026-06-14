def solution(line):
    # 1. 교점 구하기
    intersections = set() # (x,y) 형태로 저장
    for i in range(len(line)):
        A, B, E = line[i]
        for j in range(i, len(line)):
            C, D, F = line[j]
            
            denom = A*D - B*C
            if denom == 0: continue
            
            x = (B*F - E*D) / denom
            y = (E*C - A*F) / denom
            
            if int(x) != x or int(y) != y: continue # 정수 판별
            x, y = int(x), int(y)
            intersections.add((x,y))
    
    # 2. 영역 구하기 
    min_x = min(pos[0] for pos in intersections)
    min_y = min(pos[1] for pos in intersections)
    max_x = max(pos[0] for pos in intersections)
    max_y = max(pos[1] for pos in intersections)    
    
    #3. 별 만들기
    answer = []
    for y in range(max_y, min_y - 1, -1): # y가 작을수록 나중에 그려져야 함!
        row = ""
        for x in range(min_x, max_x + 1):
            if (x,y) in intersections:
                row += "*"
            else:
                row += "."
        answer.append(row)
    
    return answer