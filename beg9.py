x,y=input().split()
c=0
x=int(x)
y=int(y)
for i in range(x,y+1):
  for num in range(2,i):
    if(i % num) == 0:
       break
  else:
    c+=1
print(c) 

 
