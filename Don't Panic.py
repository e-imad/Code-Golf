a=[]
n,w,z,m,p,c,d,f=[int(i) for i in input().split()]
for i in range(f):a.append([int(j)for j in input().split()])
a.append([m,p])
a.sort(key=lambda x:x[0])
while 1:c,d,r=input().split();p=int(d);y=a[int(c)][1];print("BLOCK"if y>p and r=="LEFT"or y<p and r=="RIGHT"else"WAIT")
