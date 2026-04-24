import os
os.system("cls")

# 1.
# sum1=0
# sum2=0
# narhlar = (2,3,4,5,1,8,7)
# for i in narhlar:
#     if i%2==0:
#         sum1+=i
#     else:
#         sum2+=i
# print("Juft narxlar yig'indisi: ",sum1)
# print("Toq narxlar yig'indisi: ",sum2)


# 2.
# kelganlar = (1,2,6,4,3,7,9,10)

# for i in range(1,11):
#     if not i in kelganlar:
#         print(i,end=" ")



# 3.
# jamoa1 = (1,2,3,4)
# jamoa2 = (3,5,2,1)
# jamoa3 = (2,2,3,1)

# for i in range(4):
#     jamoa4 = jamoa1[i] + jamoa2[i] + jamoa3[i]
#     print(f"{i+1} - tur:",jamoa4)


# 4.

# shaharlar = ("Toshkent", "Samarqand", "Toshkent", "Buxoro", "Samarqand", "Toshkent")
# print(shaharlar)

# hisob={}
# for shahar in shaharlar:
#     if shahar in hisob:
#         hisob[shahar]+=1
#     else:
#         hisob[shahar]=1

# eng_kop_shahar = max(hisob, key=hisob.get)

# print(f"Eng ko'p tashrif: {eng_kop_shahar} ")

    


# 5.
# ertalab = (10,12,9,11,13,10,8)
# kechki = (18,20,17,22,19,16,15)

# for i in range(7):
#     farqlar = kechki[i] - ertalab[i]
#     print(farqlar,end=" ")


# 6.
# tuple = (1, 2, 3, 2, 1)
# if (tuple == tuple[::-1]):
#     print("palindrom")
# else:
#     print("palindrom emas")


# 7.
# ballar = (88,76,91,65,82)
# sum=0
# for i in ballar:
#     sum+=i
# sum1 = sum/5
# if sum1>=90:
#     print("O'rtacha ball: ",sum1,"----A'lo")
# elif sum1>=70 and sum1<=89:
#     print("O'rtacha ball: ",sum1,"----Yaxshi")
# elif sum1>=55 and sum1<=69:
#     print("O'rtacha ball: ",sum1,"----Qoniqarli")
# else:
#     print("O'rtacha ball: ",sum1,"----Qoniqarsiz")


# 8.
# ombor = (45,8,23,3,67,10,5)

# for i in range(len(ombor)):
#     if ombor[i]<=10:
#         print(f"{i} indeks: {ombor[i]} dona ---- Kam qolgan!")






                          # LIST

# lst1 = [1,2,3,4,"Salom", "Hello"]
# lst1[3] = "Good"
# print(lst1)
# print(lst1[3])



# lst1 = (1,2,3,4,"Salom", "Hello", 2,3,4,2,3,2)

# print(lst1.index("Salom"))

# print(lst1.count(4))


# t1 = (1,2,3,7,4,2,3,2,1,4,5,6,3,4,3)
# print(max(t1, key=t1.count))




# lst1 = ['Olma', 'Anor', 'Gilos', 'Nok', 'Anjir']

# lst1.append('Shaftoli')
# print(lst1)

# lst1.insert(1, 'Shaftoli')
# print(lst1)

# lst2 = [1,2,3,4,5]
# lst1.extend(lst2)
# lst1 += lst2
# print(lst1)

# lst1.remove('Gilos')
# print(lst1)

# a = lst1.pop(1)
# print(lst1)
# print(a)

# lst1.clear()
# print(lst1)

# lst1.sort()
# print(lst1)

# lst2 = lst1.copy()
# lst2.append("Banan")
# print(lst2)
# print(lst1)

# lst3 = lst1
# lst3.append("Banan")
# print(lst3)
# print(lst1)



# 1.
# lst = [2,24,4,3,6,15,20,30,8,1]
# lst1=lst.copy()

# for i in lst:
#     if i<=5:
#         lst1.remove(i)
#     else: 
#         print(i,end=" ")


# 2.
# lst = [2,3,32,22,43,25,87,45,9,34]

# a = max(lst)
# b = min(lst)
# print("Eng katta son: ",a)
# print("Eng kichik son: ",b)


# 3.
# lst = ['apple',5,True,'apple','banan','google',5,'banan',False,'banana']
# lst2 = []
# for i in lst:
#     if lst.count(i)>=2 and i not in lst2:
#         lst2.append(i)
    
# for i in lst2:
#     print(i,end=" ")


# 4.
# lst1 = ['friend','family','home','office','son']
# lst2 = ['wife','husband','friend','home','game','office']

# lst3 = []

# for i in lst1:
#     if i in lst2 and i not in lst3:
#         lst3.append(i)
# print(lst3,end=" ")

    

    