import re
vowels = {'a', 'e', 'i', 'o', 'u'}

while True:
  password = input()
  if password == "end":
    break

  check = True
  # 모음 반드시 하나 포함
  if not any(char in vowels for char in password):
    check = False
    
  # 모음이 3개 혹은 자음이 3개 연속
  v_cnt, c_cnt = 0, 0
  for c in password:
    if c in vowels:
      v_cnt += 1
      c_cnt = 0
    else:
      c_cnt += 1
      v_cnt = 0
      
    if v_cnt >= 3 or c_cnt >= 3:
      check = False
      break
    
  # 같은 글자 연속 x, ee와 oo는 허용
  prev = '.'
  for c in password:
    if c == prev:
      if c != 'e' and c != 'o':
        check = False
        break
    prev = c

  if check:
    print(f"<{password}> is acceptable.")
  else:
    print(f"<{password}> is not acceptable.")