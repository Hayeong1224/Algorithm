def solution(answers):
    n = len(answers)
    answer_sheets = [[1, 2, 3, 4, 5] * 2000, [2, 1, 2, 3, 2, 4, 2, 5] * 1250, [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000]
    
    result = []
    cnt = []
    for answer_sheet in answer_sheets:
        cnt.append(sum(choice == ans for choice, ans in zip(answer_sheet, answers)))
        
    max_cnt = max(cnt)
    for i, val in enumerate(cnt):
        if val == max_cnt:
            result.append(i+1)
    
    return result