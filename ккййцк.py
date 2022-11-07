F = open("27.txt")
N = int( F.readline() )
K = 43
totalSum = 0
for i in range(1,N+1):
  x = int( F.readline() )
  totalSum += x
  r = totalSum % K