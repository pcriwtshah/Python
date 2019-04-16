# INPUT NUMBER OF EVEN NUMBERS

n=int(input('Amount: '))
start=0

for i in range(n):
  start+=2
  if start > n:
      break
  print(start)
