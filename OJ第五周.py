#%%
def find_num1(n):
    a=0
    while a <= n :                                #当a小于n时循环
        if int(a) % 7 != 0 and int(a) % 3 == 0:   #整除的判断   
            print(a)
            a+=1                             
        else :
            a+=1
    return

def find_num2(n):
    for a in range(n+1):                          #用for语句循环
        if int(a) % 7 != 0 and int(a) % 3 == 0:   #整除的判断   
            print(a)
            a+=1                             
        else :
            a+=1
    return

target=int(input())
find_num1(target)
find_num2(target)

#%%
s = input()
c = input()
def count(s, c):
    i=0
    ans=0
    while i <= len(s) :
        if s[i:i+1] == c:
            ans +=1
            i +=1
        else :
            i+=1
    print(ans)
    return
count(s,c)
#%%
s = input()
w = input()
def has(s, w):
    i=t=0
    lenth,cut=len(s),len(w)
    while i+cut <= lenth :
        if s[i:i+cut]== w :
            t+=1
            i+=1
        else:
            i+=1
    if t!=0:
        print("Ture")
    else :
        print("False")
    return
has(s,w)
# %%
s = input()
w = input()
def has(s, w):
    t=0
    for letter in s.split( ):
        if letter == w:
            t+=1
    if t!= 0 :
        print("True")
    else :
        print("False")
    return
has(s,w)
            
# %%
sts=input()
list1=sts.rsplit()
i,t=0,len(list1)
for i in range(t):
    print(list1[i])

# %%
ch = input()
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"         #给定字母表
betalpha=alphabet[::-1]                       #给定倒序字母表
max=alphabet.index(ch)                        #找到输入字母的位置                                         #定义控制参量
def pyramid(ch):
    i=1
    if max==0 :                               #如果输入的是A 不用加空格
        print("A")
    else :
        print(" "*max+"A")
    while i <= max :                          #如果不是 则采用字符串拼接
        print(" "*(max-i)+alphabet[:i]+alphabet[i:i+1]+betalpha[-i:])
        i+=1
    return
pyramid(ch)

# %%