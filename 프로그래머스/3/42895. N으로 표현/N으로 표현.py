def solution(N, number):
    
    d = [set() for _ in range(9) ]
    
    for i in range(1,9):
        d[i].add(int(str(N)*i))
        
        for j in range(1,i):
            for op1 in d[j]:
                for op2 in d[i-j]:
                    d[i].add(op1 + op2)
                    d[i].add(op1 - op2)
                    d[i].add(op1 * op2)
                    if op2 != 0:
                        d[i].add(op1 // op2)
                        
        if number in d[i]:
            return i
        
    return -1