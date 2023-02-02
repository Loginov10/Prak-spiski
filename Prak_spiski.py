from random import*
#6
while True:
    a=input("Введи имя: ")
    if a.isalpha():
        print(a)
        break
    else:
        print("Введи корректно")
print("Привет",a.capitalize())
b=len(a)
g=["a","e","i","o","u","y"]
so=["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
k=0
for i in a:
    if i in g:
        k+=1
    else:
       print("") 
o=0

for i in a:
    if i in so:
        o+=1
    else:
        print("")
print("количество букв",b, "количество гласных букв",k, "количество согласных букв",o)


print()
#5
a=['крот', 'белка', 'выхухоль']
b=['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
c=['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
max_a = len(max(a, key = len))
max_b = len(max(b, key = len))
max_c = len(max(c, key = len))
print(['_' * (max_a - len(x)) + x for x in a])
print(['_' * (max_b - len(x)) + x for x in b])
print(['_' * (max_c - len(x)) + x for x in c])



print()
#4 Сортировка
a=[6,9,4,3,2,7,34,3]
a.sort()
print(a)



#3   Бесконечные числа
arv=[]
kogus=int(input("Kogus:  "))
for i in range(kogus):
    arv.append(randint(-100,100))
print(arv)
max_arv=max(arv)
i=arv.index(max_arv)
print("позиция: ",i)
print("число: ",max_arv)
max_arv=round(max_arv/kogus,2)
arv.insert(i,max_arv)
arv.pop(i+1)
print(arv)
print()





#2  
num=[]
osa1=[]
osa2=[]
for i in range(20):
    num.append(randint(1,20))
if len(num)%2==0 and len(num)>=2:
    n=int(len(num)/2)
    for i in range(1,n+1):   #1,....n
        osa1.append(num[i-1])
    for j in range(n+1,len(num)+1):  #n+1,.... len()
        osa2.append(num[j-1])
    osa1.reverse()
    osa2.reverse()
    osa2.extend(osa1)
    print(osa2)
else:
    print("Viga")





spisok1=["pol1", "pol2"]
spisok2=["stena1","stean2"]
spi=[]
while True:
    print("1-развернкть первую половину списка")
    print("2-развернкть вторую половину списка")
    print("3-развернкть весь список")
    nom=int(input("Введи цифру:"))
    if nom==1:
        spisok1.reverse()
        spisok1.extend(spisok2)
        print(spisok1)
    elif nom==2:
        spisok2.reverse()
        spisok2.extend(spisok1)
        print(spisok2)
    elif nom==3:
       spi=spisok1.extend(spisok2)
       spi.reverse()
       print(spi)





#1
index=""
maa=["Tallinn","Narva","Kohtla-Järve","Ida-Võrumaa","Tartu","Tartumaa","Viljandi","Pärnumaa","Saaremaa"]
while True:
    try:
        index=int(input("Введи индекс: "))
        if index<99999 and index>10000:
            break
            
    except:
        print("Anna õige index")
i=index//10000  #1,2,3,4,5,6,7,8,9
print(f"{index} on {maa[i-1]}")   #0,1,2,3,4,5,6,7,8
if i in [1,2,3]:
    print("Jääta kodus")
else:
    print("Kanna maski")
