import os
os.system("cls")

# 1.m
# tuple1 = (12,45,7,23,89,3)
# a = max(tuple1)
# b = min(tuple1)
# print("Eng kattasi: ",a)
# print("Eng kichik: ",b)

# 2.m
# tuple1 = (-2,5,-7,8,0,3,-1)
# a=0
# b=0

# for i in tuple1:
#     if i>0:
#         a+=1
#     elif i<0:
#         b+=1
# print("Musbat: ",a)
# print("Manfiy: ",b)

# 3.m
# tuple1 = (1,2,3,4)
# tuple2 = []
# a=1
# for i in tuple1:
#     a = i*i
#     tuple2.append(a)
# print(tuple2)


# 4.m
# tuple1 = (10,20,30,40,50,60)
# tuple2 = []
# for i in range(len(tuple1)):
#     if i%2==0:
#         tuple2.append(tuple1[i])
# print(tuple2)


# 5.m
# tuple1 = ('apple','banana','cherry')

# if 'banana' in tuple1:
#     print("bor ")
# else:
#     print("yoq ")


# LIST

# 1.m
# lst = [10,20,30,40,50,60,70]
# lst2 = []
# for i in range(len(lst)):
#     if i%2==0:
#         lst2.append(lst[i])
# print(lst2)


# 2.m
# lst = [1,2,3,4,5]
# print(lst[::-1])

# 3-m
# lst = ['a','b','a','c','b','d','a']
# lst2 = []
# for i in lst:
#     if lst.count(i)>=2 and i not in lst2:
#         lst2.append(i)
# print(lst2)


# 4-m
# lst = ['apple','banana','waterwelon','kiwi']
# uzun = lst[0]
# for i in lst:
#     if i>uzun:
#         uzun = i
# print(uzun)

# 1-m
# a = int(input("a = "))
# b = int(input("b = "))
# sonlar = []
# for i in range(a,b):
#     if i%2!=0:
#         sonlar.append(i)
# print("sonlar = ",sonlar)

# 2-m
# tuple1 = (3,8,1,10,6)
# a = max(tuple1)
# b = min(tuple1)
# j = a -b
# print(j)

# 3-m
# lst = [(5,2,3),(7,8,9),(1,4,6)]
# lst2 =[]
# for i in lst:
#     lst2.append((0,) + i[1:])
# print(lst2)

# 4-m
# a = "hello"
# t = tuple(a)

# print(t[::-1])

# 5-misol
# lst = [2,5,8,11,14,3,6]
# a=0
# for i in lst:
#     if i%2==0:
#         a+=1
# print("Juft sonlar soni: ",a)