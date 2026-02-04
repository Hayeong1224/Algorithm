n = int(input())
arr = []

for _ in range(n):
  line = input()
  opt = list(line.split())
  is_added = False

  if len(opt) > 1: # 여러 단어인 경우
    # 1. 단어 첫 글자 가능한 지 위치 찾기
    idx = 0    
    for i in range(len(opt)):
      if not is_added and arr.count(opt[i][0].capitalize()) == 0:
        arr.append(opt[i][0].capitalize())
        is_added = True
        break
      else:
        idx += len(opt[i]) + 1 # 공백 포함

    # 2. 출력
    if not is_added: # 첫 글자에 없다면 앞에서부터 찾아보기
      for i in range(len(line)):
        if not is_added and line[i] != ' ' and arr.count(line[i].capitalize()) == 0:
          arr.append(line[i].capitalize())
          is_added = True
          print(f'[{line[i]}]', end='')
        else:
          print(line[i], end='')

    else: # 첫 글자에 있다면
      for i in range(len(line)):
        if i == idx:
          print(f'[{line[i]}]', end='')
        else:
          print(line[i], end='')
      
  else: # 한 단어인 경우
    for o in line:
      if not is_added and o != ' ' and arr.count(o.capitalize()) == 0:
        arr.append(o.capitalize())
        is_added = True
        print(f'[{o}]', end='')

      else:
        print(o, end='')

  print()