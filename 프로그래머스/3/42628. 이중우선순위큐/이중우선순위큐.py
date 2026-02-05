def solution(operations):
    arr = []
    
    for o in operations:
        cmd, num = o.split()
        num = int(num)
        
        if cmd == 'I':
            arr.append(num)
            arr.sort()
        elif len(arr) != 0 and cmd == 'D' and num == 1:
            arr.pop()
        elif len(arr) != 0 and cmd == 'D' and num == -1:
            arr.pop(0)
            
    if len(arr) != 0:
        return [arr[-1], arr[0]]
    return [0,0]
    