# import sys
# sys.stdin = open("input.txt", "r")
rules = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  n, m = map(int, input().split())
  target_line = ""
  
  for _ in range(n):
    line = input().strip()
    if not target_line and '1' in line:
        # 56자리 암호 추출
        i = line.rfind('1')
        target_line = line[i-55:i+1]
      
  # 7자리씩 끊어서 테이블 규칙대로 변환
  codes = [target_line[i:i+7] for i in range(0, 56, 7)]
  password = list()
  for c in codes:
    for i in range(len(rules)):
      if c == rules[i]:
        password.append(i)

  #올바른 암호인지 확인
  odd_sum = even_sum = 0
  for i in range(len(password)):
    if i%2 != 0: #0부터 시작이니까
      even_sum += password[i]
    else:
      odd_sum += password[i]

  if (odd_sum*3 + even_sum) % 10 == 0:
    print(f"#{test_case} {odd_sum+even_sum}")
  else:
    print(f"#{test_case} 0")