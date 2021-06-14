from DeleteData import Deletee
from DisplayData import Display
from InsertData import Insert
from UpdateData import Update

print("Book Project")
print("(1)--Insert.")
print("(2)--Display.")
print("(3)--Delete.")
print("(4)--Update.")
print("Enter your choice:")
s=int(input())
if(s==1):
    In=Insert()
    In.insert()
elif(s==2):
    D=Display()
    D.display()
elif(s==3):
    De=Deletee()
    De.delete()
elif(s==4):
    U=Update()
    U.update()
