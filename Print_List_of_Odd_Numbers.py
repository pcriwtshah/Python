# INPUT NUMBER OF ODD NUMBERS

n=int(input('Amount: '))
start=1

for i in range(n):
  start+=2
  if start > n:
      break
  print(start)
