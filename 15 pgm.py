x,y=input().split()
x=int(x)
y=int(y)
h=list()
for x in range(x+1,y):
  if(x%2==0):
    h.append(x)
print(" " .join(str(x) for x in h))
