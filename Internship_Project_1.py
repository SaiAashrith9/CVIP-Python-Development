import math
import tkinter as tk
root=tk.Tk()
#string
string=""
global BODMAS
BODMAS={"/":1,"*":2,"+":3,"-":4}
def one():
    #tk.Label(f1,text="1").pack()
    global string
    string+="1"
def two():
    #tk.Label(f1,text="2").pack()
    global string
    string+="2"
def three():
    #tk.Label(f1,text="3").pack()
    global string
    string+="3"
def four():
    #tk.Label(f1,text="4").pack()
    global string
    string+="4"
def five():
    #tk.Label(f1,text="5").pack()
    global string
    string+="5"
def six():
    #tk.Label(f1,text="6").pack()
    global string
    string+="6"
def seven():
    #tk.Label(f1,text="7").pack()
    global string
    string+="7"
def eight():
    #tk.Label(f1,text="8").pack()
    global string 
    string+="8"
def nine():
    #tk.Label(f1,text="9").pack()
    global string
    string+="9"
def zero():
    #tk.Label(f1,text="0").pack()
    global string
    string+="0" 
#def add(a,b):
#    return a+b
def add():
    global string
    string+="+"
#def substract(a,b):
#    return a-b
def substract():
    global string
    string+="-"
#def multiply(a,b):
#    return a*b
def multiply():
    global string
    string+="*"
#def divide(a,b):
#    return a/b
def divide():
    global string
    string+="/"
#def power(a,b):
#    return a**b
def power():
    global string
    string+="^"
def fact():
    global string
    string+="!"
def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)  
def indices_of_operators_function():
    number_of_operators=0
    indices_of_operators=[]
    division=[]
    multiplication=[]
    addition=[]
    substraction=[]
    exponentiation=[]
    factorial=[]
    for i in range(len(string)):
        if string[i]=="+":
            number_of_operators+=1
            addition.append(i)
            indices_of_operators.append(i)
        elif string[i]=="-":
            number_of_operators+=1
            substraction.append(i)
            indices_of_operators.append(i)  
        elif string[i]=="*":
            number_of_operators+=1
            multiplication.append(i)
            indices_of_operators.append(i)
        elif string[i]=="/":
            number_of_operators+=1
            division.append(i)
            indices_of_operators.append(i)
        elif string[i]=="^":
            number_of_operators+=1
            exponentiation.append(i)
            indices_of_operators.append(i)
        elif string[i]=="!":
            number_of_operators+=1
            factorial.append(i)
            indices_of_operators.append(i)
def decimal():
    global string
    string+="."

def open_bracket():
    global string
    string+="("

def close_bracket():
    global string
    string+=")"

  
def backspace():
    global string
    string=string[:-1]

def clear():
    global string
    string=""


def equal_to():
    global string
    #string+="="
    tk.Label(frame=f1,text=string).pack()
    tk.Label(frame=f1,text="=").pack()
    
    
    try:

        result=str(eval(string))
        '''
        #indices_of_operators_function()
        number_of_operators=0
        indices_of_operators=[]
        division=[]
        multiplication=[]
        addition=[]
        substraction=[]
        exponentiation=[]
        factorial=[]
        result=str(eval(string))
        for i in range(len(string)):
            if string[i]=="+":
                number_of_operators+=1
                addition.append(i)
                indices_of_operators.append(i)
            elif string[i]=="-":
                number_of_operators+=1
                substraction.append(i)
                indices_of_operators.append(i)  
            elif string[i]=="*":
                number_of_operators+=1
                multiplication.append(i)
                indices_of_operators.append(i)
            elif string[i]=="/":
                number_of_operators+=1
                division.append(i)
                indices_of_operators.append(i)
            elif string[i]=="^":
                number_of_operators+=1
                exponentiation.append(i)
                indices_of_operators.append(i)
            elif string[i]=="!":
                number_of_operators+=1
                factorial.append(i)
                indices_of_operators.append(i) 




















        results=[]
        if number_of_operators==1:
            a=string.split(string[indices_of_operators[0]])
            if string[indices_of_operators[0]]=="+":
                results.append(int(a[0])+int(a[1]))
            elif string[indices_of_operators[0]]=="-":
                results.append(int(a[0])-int(a[1]))
            elif string[indices_of_operators[0]]=="*":
                results.append(int(a[0])*int(a[1]))  
            elif string[indices_of_operators[0]]=="/":
                results.append(int(int(a[0])/int(a[1])))
            
        else:
            indices_of_operators_function() 
            #for n in range(len(indices_of_operators)):
            for i in range(len(division)):
                a=[]
                n=indices_of_operators.index(division[i])
                if n==0:
                    a.append(string[:indices_of_operators[n]])
                    if (len(indices_of_operators)>1):
                        a.append(string[indices_of_operators[n]+1:indices_of_operators[n+1]])
                    else:
                        a.append(string[indices_of_operators[n]+1:]) 
                elif n!=len(indices_of_operators)-1:
                    
                    a.append(string[indices_of_operators[n-1]+1:indices_of_operators[n]])
                    a.append(string[indices_of_operators[n]+1:indices_of_operators[n+1]])
                else:
                    a.append(string[indices_of_operators[n-1]+1:indices_of_operators[n]])
                    a.append(string[indices_of_operators[n]+1:])
                results.append(int(int(a[0])/int(a[1])))
            for r in results:
                for i in division:
                    index=indices_of_operators.index(i)
                    
                    if index!=len(indices_of_operators)-1 and index!=0:
                        string=string[:indices_of_operators[index-1]+1]+str(r)+string[indices_of_operators[index+1]:]
                    elif index!=0:
                        string=string[:indices_of_operators[index-1]+1]+str(r)
                    elif index!=len(indices_of_operators)-1:
                        string=str(r)+string[indices_of_operators[index+1]:]
                           
            results=[]

            #indices_of_operators_function()
            number_of_operators=0
            indices_of_operators=[]
            division=[]
            multiplication=[]
            addition=[]
            substraction=[]
            exponentiation=[]
            factorial=[]
            for i in range(len(string)):
                if string[i]=="+":
                    number_of_operators+=1
                    addition.append(i)
                    indices_of_operators.append(i)
                elif string[i]=="-":
                    number_of_operators+=1
                    substraction.append(i)
                    indices_of_operators.append(i)  
                elif string[i]=="*":
                    number_of_operators+=1
                    multiplication.append(i)
                    indices_of_operators.append(i)
                elif string[i]=="/":
                    number_of_operators+=1
                    division.append(i)
                    indices_of_operators.append(i)
                elif string[i]=="^":
                    number_of_operators+=1
                    exponentiation.append(i)
                    indices_of_operators.append(i)
                elif string[i]=="!":
                    number_of_operators+=1
                    factorial.append(i)
                    indices_of_operators.append(i)




























 
            for i in range(len(multiplication)):
                a=[]
                n=indices_of_operators.index(multiplication[i])
                if n==0:
                    a.append(string[:indices_of_operators[n]])
                    if (len(indices_of_operators)>1):
                        a.append(string[indices_of_operators[n]+1:indices_of_operators[n+1]])
                    else:
                        a.append(string[indices_of_operators[n]+1:]) 
                elif n!=len(indices_of_operators)-1:
                    a.append(string[indices_of_operators[n-1]+1:indices_of_operators[n]])
                    a.append(string[indices_of_operators[n]+1:indices_of_operators[n+1]])
                else:
                    a.append(string[indices_of_operators[n-1]+1:indices_of_operators[n]])
                    a.append(string[indices_of_operators[n]+1:])
                results.append(int(a[0])*int(a[1]))
            for r in results:
                for i in multiplication:
                     index=indices_of_operators.index(i)
                     if index!=len(indices_of_operators)-1 and index!=0:
                         string=string[:indices_of_operators[index-1]+1]+str(r)+string[indices_of_operators[index+1]:]
                     elif index!=0:
                         string=string[:indices_of_operators[index-1]+1]+str(r)
                     elif index!=len(indices_of_operators)-1:
                         string=str(r)+string[indices_of_operators[index+1]:]
                     
            results=[]
            
            #indices_of_operators_function()
            number_of_operators=0
            indices_of_operators=[]
            division=[]
            multiplication=[]
            addition=[]
            substraction=[]
            exponentiation=[]
            factorial=[]
            for i in range(len(string)):
                if string[i]=="+":
                    number_of_operators+=1
                    addition.append(i)
                    indices_of_operators.append(i)
                elif string[i]=="-":
                    number_of_operators+=1
                    substraction.append(i)
                    indices_of_operators.append(i)  
                elif string[i]=="*":
                    number_of_operators+=1
                    multiplication.append(i)
                    indices_of_operators.append(i)
                elif string[i]=="/":
                    number_of_operators+=1
                    division.append(i)
                    indices_of_operators.append(i)
                elif string[i]=="^":
                    number_of_operators+=1
                    exponentiation.append(i)
                    indices_of_operators.append(i)
                elif string[i]=="!":
                    number_of_operators+=1
                    factorial.append(i)
                    indices_of_operators.append(i)

















  
            for i in range(len(addition)):
                a=[]
                n=indices_of_operators.index(addition[i])
                if n==0:
                    a.append(string[:indices_of_operators[n]])
                    if (len(indices_of_operators)>1):
                        a.append(string[indices_of_operators[n]+1:indices_of_operators[n+1]])
                    else:
                        a.append(string[indices_of_operators[n]+1:]) 
                elif n!=len(indices_of_operators)-1:
                    a.append(string[indices_of_operators[n-1]+1:indices_of_operators[n]])
                    a.append(string[indices_of_operators[n]+1:indices_of_operators[n+1]])
                else:
                    a.append(string[indices_of_operators[n-1]+1:indices_of_operators[n]])
                    a.append(string[indices_of_operators[n]+1:])
                results.append(int(a[0])+int(a[1]))
            for r in results:
                for i in addition:
                    index=indices_of_operators.index(i)
                    if index!=len(indices_of_operators)-1 and index!=0:
                        string=string[:indices_of_operators[index-1]+1]+str(r)+string[indices_of_operators[index+1]:]
                    elif index!=0:
                        string=string[:indices_of_operators[index-1]+1]+str(r)
                    elif index!=len(indices_of_operators)-1:
                        string=str(r)+string[indices_of_operators[index+1]:]

            results=[]
            
            #indices_of_operators_function()
            number_of_operators=0
            indices_of_operators=[]
            division=[]
            multiplication=[]
            addition=[]
            substraction=[]
            exponentiation=[]
            factorial=[]
            for i in range(len(string)):
                if string[i]=="+":
                    number_of_operators+=1
                    addition.append(i)
                    indices_of_operators.append(i)
                elif string[i]=="-":
                    number_of_operators+=1
                    substraction.append(i)
                    indices_of_operators.append(i)  
                elif string[i]=="*":
                    number_of_operators+=1
                    multiplication.append(i)
                    indices_of_operators.append(i)
                elif string[i]=="/":
                    number_of_operators+=1
                    division.append(i)
                    indices_of_operators.append(i)
                elif string[i]=="^":
                    number_of_operators+=1
                    exponentiation.append(i)
                    indices_of_operators.append(i)
                elif string[i]=="!":
                    number_of_operators+=1
                    factorial.append(i)
                    indices_of_operators.append(i)














            for i in range(len(substraction)):
                a=[]
                n=indices_of_operators.index(substraction[i])
                if n==0:
                    a.append(string[:indices_of_operators[n]])
                    if len(indices_of_operators)>1:
                        a.append(string[indices_of_operators[n]+1:indices_of_operators[n+1]])
                    else:
                        a.append(string[indices_of_operators[n]+1:])  
                elif n!=len(indices_of_operators)-1:
                    a.append(string[indices_of_operators[n-1]+1:indices_of_operators[n]])
                    a.append(string[indices_of_operators[n]+1:indices_of_operators[n+1]])
                else:
                    a.append(string[indices_of_operators[n-1]+1:indices_of_operators[n]])
                    a.append(string[indices_of_operators[n]+1:])
                results.append(int(a[0])-int(a[1]))
            for r in results:
                for i in substraction:
                    index=indices_of_operators.index(i)
                    if index!=len(indices_of_operators)-1 and index!=0:
                        string=string[:indices_of_operators[index-1]+1]+str(r)+string[indices_of_operators[index+1]:]
                    elif index!=0:
                        string=string[:indices_of_operators[index-1]+1]+str(r)
                    elif index!=len(indices_of_operators)-1:
                        string=str(r)+string[indices_of_operators[index+1]:]

            results=[]

           

            operator=""
            for i in range(len(string)):
                if string[i]=="*" or string[i]=="/" or string[i]=="+" or string[i]=="-":
                    print(1)
                    operator=string[i]
                    print(operator)
                    break
            if operator!="":
                a=string.split(operator)
                if operator=="+":
                    results.append(int(a[0])+int(a[1]))
                if operator=="-":
                    results.append(int(a[0])-int(a[1]))
                if operator=="*":
                    results.append(int(a[0])*int(a[1]))
                if operator=="/":
                    results.append(int(a[0])/int(a[1]))        
           '''
         
    except():
        tk.Label(f1,text=e.message()).pack(side="right")
        print(e.message())
    finally:
        #for i in range(len(results)):
        #print(string)
        #print(result)
        #tk.Label(frame=f1,text=str(string)).pack()
        tk.Label(frame=f1,text=str(result)).pack()
        string=""
  
#print(add(18,36))
f1=tk.Frame(root).pack(side="top")
f2=tk.Frame(root).pack(side="left")
f3=tk.Frame(root).pack(side="left")
f4=tk.Frame(root).pack(side="left")
f5=tk.Frame(root).pack(side="right")
#l=tk.Label(f1,text="\n\n\n")
#l.pack()
b=tk.Button(f2,text="1",command=one)
b1=tk.Button(f2,text="2",command=two)
b2=tk.Button(f2,text="3",command=three)
b3=tk.Button(f4,text="4",command=four)
b4=tk.Button(f4,text="5",command=five)
b5=tk.Button(f4,text="6",command=six)
b6=tk.Button(f3,text="7",command=seven)
b7=tk.Button(f3,text="8",command=eight)
b8=tk.Button(f3,text="9",command=nine)
b9=tk.Button(f3,text="0",command=zero)
b10=tk.Button(f3,text=".",command=decimal)
o1=tk.Button(f5,text="+",command=add)
o2=tk.Button(f5,text="-",command=substract)
o3=tk.Button(f5,text="*",command=multiply)
o4=tk.Button(f5,text="/",command=divide)
o5=tk.Button(f5,text="backspace",command=backspace)
o6=tk.Button(f5,text="clear",command=clear)
o7=tk.Button(f5,text="(",command=open_bracket)
o8=tk.Button(f5,text=")",command=close_bracket)
#o5=tk.Button(f5,text="^",command=power)
#o6=tk.Button(f5,text="n!",command=fact)
equalto=tk.Button(f3,text="=",command=equal_to)
#tk.Label(text="   ").pack()
b.pack(side="left")
b1.pack(side="left")
b2.pack(side="left")
#tk.Label(f2,text="\n\n").pack(side="left")
b3.pack(side="left")
b4.pack(side="left")
b5.pack(side="left")
#tk.Label(f3,text="\n\n").pack(side="left")
b6.pack(side="left")
b7.pack(side="left")
b8.pack(side="left")

#tk.Label(f4,text="\n\n").pack(side="left")
b9.pack(side="left")
o7.pack(side="left")
o8.pack(side="left")
b10.pack(side="left")
o6.pack(side="top")
o5.pack(side="top")
o1.pack(side="top")
o2.pack(side="top")
o3.pack(side="top")
o4.pack(side="top")

#o5.pack(side="top")
#o6.pack(side="top")
equalto.pack(side="top")
#print(b1+b2+b3)
tk.mainloop()


