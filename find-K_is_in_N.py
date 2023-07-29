N=list(map(int,input().split()))
K=list(map(int,input().split()))
for i in range(0,len(K)):
    if K[i] in N:
      print("yes")
      break
    else:
      print("no")
      break
