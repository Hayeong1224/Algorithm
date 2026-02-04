s = input()
w = s.count('a')
s += s

min_b = 1000 # b가 가장 적은 구간
for i in range(len(s) - w):
  b = s[i:i+w].count('b')
  min_b = min(min_b, b)

print(min_b)