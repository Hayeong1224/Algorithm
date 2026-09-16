def solution(numbers):
    new_numbers = sorted(map(str, numbers),key= lambda x: x*3, reverse=True) # 문자열로 변경 -> 3자리 붙인 기준 내림차순 정렬
    answer = ''.join(new_numbers)
    return answer if answer[0] != '0' else '0'