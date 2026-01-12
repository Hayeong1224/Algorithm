import sys
input = sys.stdin.readline

a, b = map(int, input().split())

MAX = 100001
is_prime = [True] * MAX
is_prime[0] = is_prime[1] = False

# 소수 판별
for i in range(2,int(MAX**0.5)+1):
  if is_prime[i]:
    for j in range(i*i,MAX,i):
      is_prime[j] = False

# 소인수 개수 DP -> f(n) = f(n/p) + 1
# 1. 가장 작은 소인수 찾기
min_prime = [0] * MAX
for i in range(2,MAX):
  if min_prime[i] == 0:
    for j in range(i,MAX,i):
      if min_prime[j] == 0:
        min_prime[j] = i

# 2. 소인수 개수 찾기
f_count = [0] * MAX
for i in range(2,MAX):
  f_count[i] = f_count[i // min_prime[i]] + 1
        
# 최종 - 언더프라임인지 판별
count = 0
for i in range(a,b+1):
  if is_prime[f_count[i]]:
    count += 1

print(count)