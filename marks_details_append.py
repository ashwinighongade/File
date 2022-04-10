obj1=open("marks.det",'a')
for i in range(2):
    roll=int(input("Enter the roll"))
    name=input("Enter name")
    marks=float(input("Enter marks"))
    rec=str(roll)+","+ name+","+str(marks)+'\n'
    obj1.write(rec)
obj1.close()
