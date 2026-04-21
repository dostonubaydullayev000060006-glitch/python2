import os
os.system("cls")
# 1-misol
# a = int(input("Hafat kunini krgizing: "))

# if a==1:
#     print("Duyshanba: ")
# elif a==2:
#     print("Seshanba: ")
# elif a==3:
#     print("chorshanba: ")
# elif a==4:
#     print("Payshanba: ")
# elif a==5:
#     print("Juma: ")
# elif a==6:
#     print("Shanba: ")
# elif a==7:
#     print("Yakshanba: ")
# else: 
#     print("Bunday hafta kuni yoq ")


# # 2-misol
# a = int(input("Son kriting: "))

# if a%2==0:
#     print("Juft son: ",a)
# else:
#     print("Toq son: ",a)


# 3-misol
# a = int(input("Yosh kriting: "))

# if a>=0 and a<=6:
#     print("Bola ")
# elif a>=7 and a<=17:
#     print("O'quvchi ")
# elif a>=18 and a<=59:
#     print("Katta ")
# elif a>=60:
#     print("Keksalar ")
# else:
#     print("To'g'ri yosh kriting: ")


# 4-misol
# a = int(input("1-son kriting: "))
# s = int(input("2- son kriting: "))
# d = int(input("3-son kriting: "))

# if a>=s and s>=d:
#     print("Eng kattasi : ",a)
# elif a>=d and d>=s:
#     print("Eng kattasi : ",a)
# elif d >=a and a>=s:
#     print("Eng kattasi : ",d)
# elif d>=s and s>=a:
#     print("Eng kattasi : ",d)
# elif s>=d and d>=a:
#     print("Eng kattasi : ",s)
# elif s>=a and a>=d:
#     print("Eng kattasi : ",s)


# 5-misol
# a = int(input("son kriting: "))

# if a>=0:
#     print(a*a)
# else:
#     print(a*(-1))


# 6-misol
# a = int(input("son kriting: "))

# for i in range(1,a+1):
#     print(i*i,end=" ")


# 7-misol
# a = int(input("son kritng: "))
# for i in range(1,a+1):
#     if i%3==0:
#         print(i,end=" ")

# 8-misol
# a = int(input("son kriting: "))
# sum=1
# for i in range(1,a+1):
#     sum*=i
# print(sum)

# # 9-misol
# a = int(input("son kriting:  "))
# for i in range(a,0,-1):
#     print(i,end=" ")

# 10-misol
# a = int(input("son kriting: "))
# sum=0
# while a!=0:
#     s=a%10
#     sum+=s
#     a=a//10
# print(sum)

# 11-misol
# a = int(input("son kriting: "))
# sum=0
# while a!=0:
#     s=a%10
#     sum+=1
#     a=a//10
# print(sum)

# 12-misol
# a = int(input("son krit: "))
# for i in range(1,a+1):
#     if i%2!=0:
#         print(i,end=" ")


# 13-misol
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# 14-misol
# for i in range(1,6):
#     print("*"*5)
# print()

# 15-misol
a = int(input("son kriting: "))

for i in range(2,a+1):
    tub = True
    for j in range(2,i):
        if i%j == 0:
            tub = False
            break

    if tub:
        print(i,end=" ")


