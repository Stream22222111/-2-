print("Задание 2")
A=int(input())
print(sum(range(1,A+1)))
print("Задание 4")
for i in range(10,21):
    print(i,i**2)
print("Задание 10")
print("Введите 10 пар чисел")
a=input("Введите 1 число из пары ")
b=input("Введите 2 число из пары ")
if a>b:
    print(a)
if a<b:
    print(b)
c=input("Введите 1 число из пары ")
d=input("Введите 2 число из пары ")
if c>d:
    print(c)
if c<d:
    print(d)
e=input("Введите 1 число из пары ")
f=input("Введите 2 число из пары ")
if e>f:
    print(e)
if e<f:
    print(f)
g=input("Введите 1 число из пары ")
h=input("Введите 2 число из пары ")
if g>h:
    print(g)
if g<h:
    print(h)
j=input("Введите 1 число из пары ")
k=input("Введите 2 число из пары ")
if j>k:
    print(j)
if j<k:
    print(k)
l=input("Введите 1 число из пары ")
m=input("Введите 2 число из пары ")
if l>m:
    print(l)
if l<m:
    print(m)
n=input("Введите 1 число из пары ")
o=input("Введите 2 число из пары ")
if n>o:
    print(n)
if n<o:
    print(o)
p=input("Введите 1 число из пары ")
q=input("Введите 2 число из пары ")
if p>q:
    print(p)
if p<q:
    print(q)
r=input("Введите 1 число из пары ")
s=input("Введите 2 число из пары ")
if r>s:
    print(r)
if r<s:
    print(s)
t=input("Введите 1 число из пары ")
u=input("Введите 2 число из пары ")
if t>u:
    print(t)
if t<u:
    print(u)
print("Вы ввели 10 пар чисел!")

print("Задание номер 9")
S=float(input("Введите первоначальную сумму вклада "))
N=float(input("Введите количество лет "))
AB=S*(1+(3/100)/365)**(N*365)
print("результат: "+str(AB))
print("Задание номер 8")
D=float(input("введите количество дюймов"))
F=D*(2+1/2)
print("Результат дюймы в сантиметры "+str(F))
print("Задание 1")
#1. Вводят 15 чисел. Определить, сколько среди них целых. задание 1
x=0
for i in range(1,6,1):
    A=float(input(f" введите A:"))
    int(A)==A
    if int(A)==A: x+=1
print(x)
print("Задание 3")
w=1
for i in range(1,8,1):
    A=float(input(f"введите A:"))
    if A>0:
        if int(A)==A: w*=A
print(round(w),)
print("Задание 5")
j=0
for i in range(1,6,1):
    N=float(input(f"Введите N:"))
    if N<0:
        if int(N)==N: j+=N
print(round(j),)
print("Задание 6")
z, p, n, counter=0,0,0,0

print("sisestage 5 num")
while counter<5:
    counter+=1
    a=int(input())
    if a>0:
        p+=1
    elif a<0:                  
        n+=1
    else:
        z+=1
print("позитивный",p)
print("негативный",n)
print("нули",z)
print("Задание 7")
for i in range(10,200,10):
    if i%10==0: 
        print(i)



