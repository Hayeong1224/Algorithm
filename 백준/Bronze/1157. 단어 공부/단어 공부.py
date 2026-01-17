word = input()
word = word.upper()
arr = set(word)

max_count = 0
repeat_count = 0
answer = ''

for a in arr:
  c = word.count(a)

  if max_count == c:
    repeat_count = c
  else:
    if max_count < c:
      max_count = c
      answer = a

if repeat_count == max_count:
  print('?')
else:
  print(answer)