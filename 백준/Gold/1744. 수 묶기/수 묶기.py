n = int(input())
arr = [int(input()) for _ in range(n)]

if n == 1:
  print(arr[0])

else:
  arr_pos = sorted([num for num in arr if num > 1], reverse = True)
  sum_one = arr.count(1)
  arr_zero = [num for num in arr if num == 0]
  arr_neg = sorted([num for num in arr if num < 0])
  
  result = sum_one # 1은 다 더하고 시작
  
  if arr_pos: # 양수
    if len(arr_pos) % 2 == 0: # 짝수개
      result += sum([arr_pos[i] * arr_pos[i+1] for i in range(0, len(arr_pos), 2)])
    else: # 홀수개
      result += sum([arr_pos[i] * arr_pos[i+1] for i in range(0, len(arr_pos)-1, 2)])
      result += arr_pos[-1]

  if arr_neg: # 음수
    if len(arr_neg) % 2 == 0: # 짝수개
      result += sum([arr_neg[i] * arr_neg[i+1] for i in range(0, len(arr_neg), 2)])
    else: # 홀수개
      result += sum([arr_neg[i] * arr_neg[i+1] for i in range(0, len(arr_neg)-1, 2)])
      if not arr_zero:
        result += arr_neg[-1]
  
  print(result)