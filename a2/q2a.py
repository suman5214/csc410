student = [1,2,3,4,5]
pairing = [(1,2),(1,3),(1,4),(2,1),(2,3),(2,5),(3,2),(3,1),(4,1),(5,2)]
d = []
asrt = '(assert (not (or'
for i in student:
    for j in student:
        if i != j:
            d.append((i,j))
c = []

for i in d:
    print('(declare-const '+'s'+str(i[0])+'s'+str(i[1])+' Bool)')
for i in student:
    print('(declare-const '+'s'+str(i)+' Bool)')
for i in d:
    a = i[0]
    b = i[1]
    s = asrt
    for j in d:
        if i !=j:
            if (a in j) or (b in j):
                temp = ' (and '+'s'+str(a)+'s'+str(b)+' '+'s'+str(j[0])+'s'+str(j[1])+')'
                s+=(temp)
    s += ' (and '+'s'+str(a)+'s'+str(b)+' '+'s'+str(a)+')'
    s += ' (and '+'s'+str(a)+'s'+str(b)+' '+'s'+str(b)+')'
    s += ')))'
    print(s)

for i in student:
    s = '(assert (not (or'
    for j in d:
        if i in j:
            temp = ' (and '+'s'+str(i)+' '+'s'+str(j[0])+'s'+str(j[1])+')'
            s+=(temp)
    s += ')))'
    print(s)
    
for i in d:
    a = i[0]
    b = i[1]
    s = asrt
    if i in pairing:
        print('(assert-soft '+'s'+str(a)+'s'+str(b)+' :weight 3 )')
    else:
        print('(assert-soft '+'s'+str(a)+'s'+str(b)+' :weight 2 )')
    
for i in student:
    s = asrt
    print('(assert-soft '+'s'+str(i)+' :weight 1 )')    
    
print('(check-sat)')
print('(get-model)')