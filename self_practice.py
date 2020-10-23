def cal(a):
    ary = list(range(a))
    h = 0
    for i in ary:
        if(i%2 == 0):
            h+= i
    return h
a = 12
result = cal(a)
print(result)

#############################

a = list(range(1,12,3))
r = 0
for i in a[2:]:
    r+=i
print(r)

#############################

def add(a):
    c = list(a)
    for i in range(1, len(c)*2, 2):
        c.insert(i, 'E')
    return c

def prnt(st):
    for i in st:
        print(i, end='')

a = 'rfr'.upper()
st = add(a)
prnt(st)
print('NCE')

#############################

def bin(a):
    b = list()
    while(a!=0):
        b.append(a%2)
        a = int(a / 2)
    return b

def cpl(r):
    e = len(r) - 1
    for i in range(e, -1, -1):
        print(1 - r[i], end='')

a = int(10)
r = bin(a)
cpl(r)

#############################

a = list()
for i in range(10):
    a.append(int(input()))
dif = 99
for i in range(10):
    if(a[i]>33):
        t = a[i] - 33
    else:
        t = 33 - a[i]
    if (t<=dif):
        dif = t
        r = f"dif is {dif}, value is {a[i]}"
        print(r)
print("final result :"+r)
        

#############################

def init():
    lst = [ 0 ]
    for i in range(1,5):
        lst.append(lst[i - 1]+i)
    return lst

def sort(a):
    for i in range(1, 5):
        j = i - 1
        k = a[i]
        while(j >= 0 and a[j] < k):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = k
        
a = init()
sort(a)
for i in a:
    print(i, end =' ')
    
############################# 삽입정렬


