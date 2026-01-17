n = int(input())

level = 1
max_num = 1
increment = 6

while n > max_num:
  max_num += increment
  increment += 6
  level += 1

print(level)