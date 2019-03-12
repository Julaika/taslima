x,y=input().split()
x=int(x)
y=int(y)
for i in range(x,y):
  for num in range(2,i):
    if(i % num) == 0:
       continue
    else:
      print(num)
 
