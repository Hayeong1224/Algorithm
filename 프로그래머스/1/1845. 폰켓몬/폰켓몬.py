def solution(nums):
    
    # 종류에 따라 번호를 붙여 구분합니다. -> dict 느낌
    # 최대한 많은 종류의 폰켓몬을 포함하여 N/2마리 선택.
    count = dict()
    
    for i in nums:
        count[i] = count.get(i, 0) + 1
    
    return min(len(nums) // 2, len(count.keys()))