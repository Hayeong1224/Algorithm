n, g = input().split()
n = int(n)
players = {input() for _ in range(n)}
min_p = {'Y': 1, 'F': 2, 'O': 3} # 임스 제외

count = 0
while len(players) >= min_p[g]:
  for i in range(min_p[g]):
    players.pop()
  count += 1

print(count)