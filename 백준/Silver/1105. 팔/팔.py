import sys
L, R = input().split()
# 자릿수가 다르면 무조건 8이 없는 경우 있음!
if len(L) != len(R):
  print(0)
  sys.exit()

count = 0
for i in range(len(L)):
  if L[i] == R[i]:
    if L[i] == '8':
      count += 1
  else: # 두 숫자의 해당 자릿수가 달라지는 순간, 그 뒤는 8을 안 쓸 수 있음
    break

print(count)