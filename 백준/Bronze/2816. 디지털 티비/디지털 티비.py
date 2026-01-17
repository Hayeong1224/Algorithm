n = int(input())
channels = list(input() for _ in range(n))
result = []

idx1 = channels.index('KBS1')
idx2 = channels.index('KBS2')

if idx1 > idx2:
  idx2 += 1

# KBS1
print('1' * idx1, end='')
print('4' * idx1, end='')

# KBS2
print('1' * idx2, end='')
print('4' * (idx2-1))