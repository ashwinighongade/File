a=10
b=5
c=6
a,b,c=b,c,a
print(a,b,c)
# print(10//2%1**4*5+2-5)


# print(True not False and False)
# a=int(input("Enter the number"))
# b=int(input("Enter the number"))
# c=int(input("Enter the number"))
# d=int(input("Enter the number"))
# e=int(input("Enter the number"))
# if (a>c or b>c or c<d or c<e):
#     print(c,"is middle number")
# elif (a>b or b>c  or b<d or b<e): 
#     print(b,"is middle number")
# elif(a>c or a>b or a<d or a<e):
#     print(a,"is middle number")
# elif(d>e or d>e or d<a or d<b):
#     print(d,"is middle number")
# else:
#     print(e,"is middle number")
# num=int(input("Enter the Number :"))
# i=1
# a=[]
# while i <=num:
#     name=input("Enter the Name :")
#     a.append(name)
#     i+=1
# print(a)
    
# num=int(input("Enter the Number :"))
# i=1
# a=""
# while i <=num:
#     name=input("Enter the Name :")
#     a+=name
#     a+=" "
#     i+=1
# print(a)

# list1=[10,101,110,1011,101011]
# i=0

# list=[]
# while i<len(list1):
#     b=str(list1[i])
#     e=len(b)
#     print(e,end=" ")
#     # length.append(e)
#     c=""
#     j=0
#     while j<len(b):
#         if b[j]!="0":
#             c+=b[j]
#         j+=1
#     list.append(int(c))
#     i+=1
# print(list)

# list2=[]  
# i=0

# while i<len(list):
#     a=str(list[i])
#     sum=0
    
#     j=0
#     while j<len(a):
#         sum=sum+int(a[j])
#         j+=1
#     list2.append(sum)
#     i+=1
# print(list2)


list=[1,2,3,4,5,6]
num=int(input("Enter the number :"))
list1=[]
k=2
i=0
while i<len(list):
    if i==k:
        list1.append(num)
        k+=2
    list1.append(list[i])
    i+=1
# list1.append(num)
print(list1)

# x=lambda a:a+10
# print(x(5))

