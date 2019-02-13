x=int(input())
dig=0
n=x
while(x>0):
 c=x%10
 dig=dig*10+c
 x//=10
if(dig==n):
  print("yes")
else:
  print("no")

