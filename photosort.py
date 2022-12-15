import os


os.chdir(r"C:\Users\n.iliushin\Documents\Fakebelts\получение")
mylist = os.listdir()

for i in mylist:
    x = i.split("_")
    if len(x) > 6:
        x = x[1:]
        print(x)



   
##    if len(i) == 64:
##        os.rename(i, i[10:])
##    else:
##        continue



    
