import sys

n, q = raw_input().strip().split(' ')
n, q = [int(n),int(q)]
l = []
last_ans = 0
for i in range(n):
    l.append([])
    
for i in range(q):
    que_typ, y, val_inp = raw_input().strip().split(' ')
    que_typ,y,val_inp = [int(que_typ),int(y),int(val_inp)]
    if que_typ == 1:
        index = ((y^last_ans)%n)
        l[index].append(val_inp)
    if que_typ ==2:
        index = ((y^last_ans)%n)
        last_ans = l[index][len(l[index])-1]
        print(last_ans)