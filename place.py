file1=open("people1-exercise.txt","r")
# data = file.read()
for i in file1 :
    print(i)
    print("#")
    if "delhi" in i:
        a=open("delhi.txt","a")
        a.write(i)
    elif "shimla" in i:
        a=open("shimla.txt","a")
        a.write(i)
    else:
        a=open("other.txt","a")
        a.write(i)


