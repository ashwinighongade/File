size=int(input("How many student details"))
obj1=open("marks.det","w")
for i in range(size):
    roll=int(input("Enter the roll"))
    name=input("Enter name")
    marks=float(input("Enter marks"))
    rec=str(roll)+","+ name+","+str(marks)+'\n'
    obj1.write(rec)
obj1.close()