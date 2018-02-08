from functools import reduce as f
input()
t=sorted([int(i)for i in input().split()])
a=0
if t!=[]:
 a=f(lambda x,y:x if abs(y)>abs(x)else y,t)
print(a)
