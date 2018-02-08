a=[]
b=[]
n,w,nb,ef,ep,c,d,f=[int(i) for i in input().split()]
for i in range(f):
 x, y = [int(j) for j in input().split()]
 a.append(x)
 b.append(y)
a.append(ef)
b.append(ep)
while True:  
 c,d,dr = input().split()
 cf=int(c)
 cp=int(d)
 if cf!=-1:
  y=b[a.index(cf)]
  if y>cp and dr=="LEFT" or y<cp and dr=="RIGHT":print("BLOCK")
  else:print("WAIT")
 else:print("WAIT")
