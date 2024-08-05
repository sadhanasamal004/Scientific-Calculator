                      # PROJECT 1: BUILDING CALCULATOR APP USING TKINTER

from tkinter import *
import ast
root=Tk()

i=0
def displaynumber(n):   #function for display the digits clicked
    global i
    display.insert(i,n)
    i+=1

def displayoperators(o):#function for display the operators clicked
    global i
    l=len(o)
    display.insert(i,o)
    i+=l

def clear():            #function for executing all clear
    display.delete(0,END)

def calculate():        #function for executing '='
    entire_string=display.get()
    try:
        node=ast.parse(entire_string,mode='eval')
        result=eval(compile(node,'<string>','eval'))
        clear()
        display.insert(0,result)
    except Exception:
        clear()
        display.insert(0,'Error')

def undo():         #function for backspace
    entire_string=display.get()
    if len(entire_string):
        new_string=entire_string[:-1]
        clear()
        display.insert(0,new_string)
    else:
        clear()
        display.insert(0,'')

display=Entry(root)
display.grid(row=0,columnspan=6,ipadx=5,ipady=5)

nums=[1,2,3,4,5,6,7,8,9]
count=0
for i in range(3):
    for j in range(3):
       num_text=nums[count]
       numbers=Button(root,text=num_text,width=4,height=2,command=lambda text=num_text:displaynumber(text))
       numbers.grid(row=i+2,column=j+1)
       count+=1
zerobutton=Button(root,text=0,width=4,height=2,command=lambda : displaynumber(0))
zerobutton.grid(row=5,column=2)

count1=0
operations=['+','-','*','/','%','**2','*3.14','(',')','**']
size=len(operations)
for i in range(4):
    for j in range(3):
        if count1<size:
            operators=Button(root,text=operations[count1],width=4,height=2,command=lambda text=operations[count1]:displayoperators(text))
            operators.grid(row=i+2,column=j+4)
            count1+=1

acbutton=Button(root,text='AC',height=2,width=4,command=clear)
acbutton.grid(row=5,column=1)
ebutton=Button(root,text='=',height=2,width=4,command=calculate)
ebutton.grid(row=5,column=3)
undobutton=Button(root,text='<-',width=4,height=2,command=undo)
undobutton.grid(row=5,column=5)

root.mainloop()