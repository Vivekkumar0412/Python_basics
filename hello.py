# # # print("Vivek is here")
# # # a = 10
# # # b = 10
# # # print("The sum of a and b is : ", a + b)
# # # print(id(a),id(b))
# # # c = "Vivek"
# # # print(c)
# # #
# # # print(a+b)
# # # print(a-b)
# # # print(a*b)
# # # print(a%b)
# # # print(a/b)
# # # print(a**2) #10 to the power
# # # print(a//b) # floor division means it will neflect the decimal value only integer part will be printed
# # # a+=59
# # # print(a)
# # a = 10
# # b = 10
# # # b = "11111"
# # print(b)
# # str1 = "vivek"
# # print('wwk' in str1)
# # print(type(b))
# # print(5 + (2*b))
# # a = 2 + 5j
# #
# # v = [1,2,3,4,"vivek","singh"]
# # print(13 in v)
# # print(v[4])
# # print("iv" in v[4])
# #
# # vk = (1,2,3,4,"vuic","989")
# # d = {
# #     "first" : 1,
# #     "second" : 2,
# #     "name" : "vivek singh rajput"
# # }
# # print(vk[5])
# # t = (10)
# # print(t, type(t))
# # d1 = {
# #     "first" : 1,
# #     "second" : 2,
# #     "name" : "vivek singh rajput"
# # }
# # print(d1, type(d1))
# # # print(d.second)
# # d1["name"] = "vivek"
# # print(d1["name"])
# # s = {1,1,2,2,3,3,4,4,}
# # print(s)
# # print(s,"s is here", type(s))
# #
# # print("New day new code")
# strr = "Vivek"
# # this is an error we can not do this thing we can assing anything multiple timees but we can not update it.
# strr = "vicek kr"
# # # strr[0] = "z"
# # a = (1,1,1,1,)
# # # print(a[0])
# # # print(strr[0])
# # a = int(input("Enter : -"))
# # b = int(a)
# # print(a,"after ", type(a))
# # print(b, type(b))
# #
# # c = eval(input("enyter c"))
# # # d = eval(input("enter d"))
# # # e = eval(input("endter d"))
# # # print(c + d + e)
# # if c % 2 == 0:
# #     print("even hai bhai")
# # else:
# #     print("odd hai bhai")
# #
# # d = eval(input("Enter the marks"))
# # if d >= 75:
# #     print("GREAT")
# # elif d >= 60:
# #     print(("V.GOOD"))
# # elif d >= 50:
# #     print("good need improvement")
# # else:
# #     print(("FAIL"))
#
# # for v in range(0,6,2):
# #     print(v)
# # for b in range(1,11):
# #     print("2 x ",b," = ", 2*b)
# #
# for j in range(10,0,-1):
#     print(j)
#
# i = 10
# while i > 0:
#     print(i, "Vivek")
#     i -= 1
#
# s = "vivek"
# # print("i" in strr)
# print(s[0:])
#
# print(s[-1::-1])
# st = "nitin jha hai naam"
# stt = s[-1::-1]
# print(stt , " stt is here")
# if st == stt:
#     print("Palindrome")
# else:
#     print("not a palindorm")
#
# # for i in range(len(st)):
# #     for j in range(len(stt)):
# #         if st[i] == stt[j]:
# #             print("Palindrome")
# #         else:
# #             print("Palindrome not hshehee")
# print(st.upper())
# print(st.lower())
# print(st.title())
# print(st.capitalize())
# print(st.index("jha"))
# print(st.lower().find("Jha"))
#
# jk = "123 hlhhi"
# print(jk.isalnum())
# print(chr(65))
#
# v = "VIVEK {} RAJPUT".format("SINGH")
# print(v)
#
# print("NEW DAY A NEW BEGAINING STREAK SAVED")
# sci = eval(input("ENTER SCIENCE MARKS : - "))
# maths = eval(input("ENTER SCIENCE MARKS : - "))
# eng = eval(input("ENTER SCIENCE MARKS : - "))
# avg = (sci + maths + eng)/3
# print(avg)
#
# for d in range(1,11):
#     pass
# print(d*d)/
l1 = [1,1,1,2,3,[9,8,0],4,5,6,78]
print(l1[4])
for i in range(len(l1)):
    print(l1[i], end = " ")

print()
print(l1[1::2])
l2 = [3,4,6,4,2,46,7,8,88,9,0]
c = 0
for i in range(len(l2)):
    if c < l2[i]:
        c = l2[i]
for j in range(len(l2)-1, -1, -1):
    print(l2[j], end = " ")
print(c)
for j in  l2:
    if j >3 and j<8:
        print(j)

s = "vivek"
for k in range(len(s)):
    print(s[k], end = " ")
print()
s = "vivek singh"
print(s)

dis = {
    "name" : "vivek",
    "age": 24,
    "employe" : "true"
}
print(dis)
print(dis["name"],dis["age"])
print(s[len(s)-1::-1])
# del l1
# l1.pop(3)
# print(l1)
l3 = [1,2,3,4,5,5,6,7,8,9]
# for m in range(len(l3)):
# #     print(m, end = "The index is : ")
# #     print(l3.pop(m))
#
# for k in range(len(l3)):
#     l3[k] = l3[k]*l3[k]
#
# print(l3)
# # l3.insert(2,99)
# print(l3)
# l4 = [40,90]
# l3.extend(l4)
# print(l3)
# l4 = []
# for i in range(100):
#     l4.append(i)
# print(l4)
# print(max(l3))
#
# vi = "vivek singh rajput"
# vk = vi.split()
# print(vk)
# el = []
# for mk in range(3):
#     a = input("ENTER THE DATA " + str(mk))
#     el.append(a)
# print(el)
# print(el.pop())

# eq = []
# while True:
#     inp = int(input('''
#         1 ENTER THE VALUE TO QUESUE
#         2 REMOVE AN ITEM FROM
#         3 GET FRONT ELEMNET
#         4 GET THE LAST ELEMENT
#         5 EXIT
#     '''))
#     if inp == 1:
#         data = int(input("enter the value : - "))
#         # eq.insert(0,data)
#         eq.append(data)
#         print(eq)
#     elif inp == 2:
#         if len(eq) == 0:
#             print("The queue is empty")
#         else:
#             a = eq.pop(0)
#             print(a)
#             print(eq)
#     elif inp == 3:
#         if len(eq) == 0:
#             print("The queue is empty")
#         else:
#             print(eq[0])
#             print(eq)
#     elif inp == 4:
#         if len(eq) == 0:
#             print("The queue is empty")
#         else:
#             print(eq[-1])
#             print(eq)
#     elif inp == 5:
#         break
#     else:
#         print("INVALID ")
d = {
    'name':'vivek singh',
    'salary':20000000
}
d['age'] = 24
d['name'] = 'vivek singh rajput'
for val in d:
    print("The key is : - ",val," and its value is :-", d[val])

course = {
    'java': {'duration': '2 months', 'fee': 10000},
    'python': {'duration': '2 months', 'fee': 10000},
    'c++':{'duration': '2 months', 'fee': 10000}
}
print(course['java'])
for itm in course:
    print('the key is ', itm, 'the value is : ',course[itm]['duration'])

def fn():
    print("hi i am function")
fn()

def fnn (a,b):
    return a + b
data = fnn(30,29)
print(data)

import check

print(check.mult(5,5))
print(check.summ(98,2))

class Check:
    a = 59
    def __init__(self):
        print("hi this is constructor")
    def summ(self):
        print(80 + 90)

    # def mult(c,b):
    def hihi(self,b,c):
        self.c = self.a + b+c
        print(self.c)
data1 = Check()
data1.summ()
data1.hihi(10,10)

class T:
    def __init__(self):
        self.name = ""
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name

objt = T()
objt.setName('Vivek')
viv = objt.getName()
print(viv)


a = 0
b = 1
print(0)
print(1)
for i in range(10):
    temp = a + b
    print(temp)
    a = b
    b = temp

# rectangel
for i in range(1,6):
    for j in range(1,6):
        print(" * ",end="")
    print()

# holoow rec
for i in range(1,6):
    for j in range(1,6):
        if(i == 1 or i == 5
                or j == 1 or j == 5 ):
            print("*",end="")
        else:
            print(" ")
    print()

for i in range(1,6):
    for j in range(1,6):
        if (i == 1 or i == n) or (j == 1 or j == m):
            print("*",end="")
        else:
            print(" ")
    print()


a = "abcd"
b = "cdba"
if(sorted(a) == sorted(b)):
    print("hi")
print(sorted(a))

for i in range(4):
    for j in range(i,5):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    for l in range(i+1):
        print("*",end="")
    print()
