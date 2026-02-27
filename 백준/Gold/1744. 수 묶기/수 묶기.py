n = int(input())
arr = [int(input()) for _ in range(n)]

pos, neg, ones, zeros = [], [], 0, 0

for num in arr:
  if num > 1:
    pos.append(num)
  elif num == 1:
    ones += 1
  elif num == 0:
    zeros += 1
  else:
    neg.append(num)

pos.sort(reverse=True)
neg.sort()

result = ones # 1은 다 더하고 시작

# 양수 묶기
for i in range(0, len(pos) - 1, 2):
  result += pos[i] * pos[i+1]
if len(pos) % 2 == 1:
  result += pos[-1]

# 음수 묶기
for i in range(0, len(neg) - 1, 2):
  result += neg[i] * neg[i+1]
if len(neg) % 2 == 1:
  if zeros == 0:
    result += neg[-1]

print(result)