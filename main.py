from pathlib import Path
import os

def readfilelandfolder():
    path= Path('')
    items=list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1}:{items} ")
   
def createfile():
        try:
            readfilelandfolder()
            name= input("Please tell Number: ")
            p =Path(name)
            if not p.exists():
                with open(p,"w") as fs:
                    data =input("what you want to write: ")
                    fs.write(data)

                print(F"File created")
            else:
                print("already exists")
        except Exception as err:
         print(f"error occured as {err}")   

def readfile():
    try:
        readfilelandfolder()
        name=input("which file you want to read")
        p= Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data =fs.read()
                print(data)

            print("readed")
        else:
            print("doesnot exists file")  
    except Exception as err:
         print(f"error occured as {err}")   

def updatefile():
    try:
        readfilelandfolder()  
        name=input("Tell which file you want to update: ")
        p=Path('name')
        if p.exists() and p.is_file():
            print ("Press 1 change name of the file ")
            print ("Press 2 overwrite of the file ")
            print ("Press 3 appending of the file ")

            res= int(input("tell response"))

            if res==1:
                name2=input("tell your file name")
                p2=Path(name2)
                p.rename(p2)

            if res==2:
                with open(p,'w')as fs:
                    data=input("tell what you want to overwrite") 
                    fs.write(data)   


            if res==3:
                with open(p,'a')as fs:
                    data=input("tell what you want to append") 
                    fs.write("" +data)  

    except Exception as err:
             print(f"error occured as {err}")   

def deletefile():
    try:
        readfilelandfolder()
        name=input("which file you want to delete")
        p= Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("removed")
        else:
            print("doesnot exists file")  
    
    except Exception as err:
         print(f"error occured as {err}")       

print("Press 1 create")
print("Press 2 read")
print("Press 3 update")
print("Press 4 delete")

check=int(input("Tell response:"))
if check ==1:
    createfile()

if check==2:
    readfile()

if check==3:
    updatefile()  

if check==4:
    deletefie()

