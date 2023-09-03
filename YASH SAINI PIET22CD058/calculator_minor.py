#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1.Importing libraries
import math
import simple_colors as color

#2.Startup Menu
print(color.black("WELCOME TO CALCULATOR🧮\n",['bold']))
print(color.blue("\nWHAT HELP DO YOU NEED??🔧\n"))
print(color.red('''
           1.PERFORM ADDITION
           2.PERFORM SUBTRACTION
           3.PERFORM DIVISON
           4.PERFORM MULTIPLICATION
           5.FIND EXPONENT
           6.FIND LOG
           7.TRIGONOMETRIC FUNCTIONS'''))

#3.Choice Input
ch=int(input("\nEnter your choice number: "))
print("\n\n")

#4.Addition
if ch==1:
    num=[]
    count=int(input("enter the qty. of numbers you want to add: "))
    print("\n")
    for k in range(count):
        num_k=float(input("enter your number: "))
        print("\n")
        num.append(num_k)
    sum_k=sum(num)
    print(color.green(f"\nThe Sum of your numbers {num} is: {sum_k}\n"))
    print(color.magenta(f"\nTHANK YOU FOR USING OUR SERVICES😄.....",['underlined','italic']))
    
#5.Subtraction    
elif ch==2:
        n1=float(input("\nEnter the first number: "))
        n2=float(input("\nEnter the second number: "))
        print(color.green(f"\nThe Difference of your numbers {n1} and {n2} is: {n1-n2}\n"))
        diff=n1-n2
        print(color.blue("\nDO YOU WANT TO ROUND THE Difference OFF??"))
        choice=input("\nEnter Yes or No: ")
        if choice =="Yes":
            digits=int(input("\nEnter the number of decimal places you want to round it off to: "))
            print("\nYour Difference is: ",round(diff,digits))
            print(color.magenta(f"\nTHANK YOU FOR USING OUR SERVICES😄.....",['underlined','italic']))
        else:
            print("\nYour Difference is: ",diff)
            print(color.magenta(f"\nTHANK YOU FOR USING OUR SERVICES😄.....",['underlined','italic']))

#6.Divison
elif ch==3:
        n1=float(input("\nEnter the Dividend: "))
        n2=float(input("\nEnter the Divisor: "))
        print(color.green(f"\nThe Quotient of division of {n1} and {n2} is: {n1/n2} and the Remainder is : {n1%n2}\n"))
        Q=n1/n2
        R=n1%n2
        print(color.blue("\nDO YOU WANT TO ROUND THE Quotient OFF??"))
        choice=input("\nEnter Yes or No: ")
        if choice =="Yes":
            digits=int(input("\nEnter the number of decimal places you want to round it off to: "))
            print("\nYour Quotient is: ",round(Q,digits))
            print(color.magenta(f"\nTHANK YOU FOR USING OUR SERVICES😄.....",['underlined','italic']))
        else:
            print("\nYour Quotient is: ",Q)
            print(color.magenta(f"\nTHANK YOU FOR USING OUR SERVICES😄.....",['underlined','italic']))

#7.Multiplication           
elif ch==4:
        n1=float(input("\nEnter the first number: "))
        n2=float(input("\nEnter the second number: "))
        prod=n1*n2
        print(color.green(f"\nThe Product of the numbers {n1} and {n2} is: {n1*n2}\n"))
        print(color.blue("\nDO YOU WANT TO ROUND THE Product OFF??"))
        choice=input("\nEnter Yes or No: ")
        if choice =="Yes":
            digits=int(input("\nEnter the number of decimal places you want to round it off to: "))
            print("\nYour Product is: ",round(prod,digits))
            print(color.magenta(f"\nTHANK YOU FOR USING OUR SERVICES😄.....",['underlined','italic']))
        else:
            print("\nYour Product is: ",prod)
            print(color.magenta(f"\nTHANK YOU FOR USING OUR SERVICES😄.....",['underlined','italic']))

#8.Exponent            
elif ch==5:
        n1=float(input("\nEnter the base value: "))
        n2=float(input("\nEnter the exponent: "))
        res=n1**n2
        print(color.green(f"\nThe Result of the numbers {n1} to the power {n2} is: {res}\n"))
        print(color.blue("\nDO YOU WANT TO ROUND THE Result OFF??"))
        choice=input("\nEnter Yes or No: ")
        if choice =="Yes":
            digits=int(input("\nEnter the number of decimal places you want to round it off to: "))
            print("\nYour Result is: ",round(res,digits))
            print(color.magenta(f"\nTHANK YOU FOR USING OUR SERVICES😄.....",['underlined','italic']))
        else:
            print("\nYour Result is: ",res)
            print(color.magenta(f"\nTHANK YOU FOR USING OUR SERVICES😄.....",['underlined','italic']))

#9.Logarithm
elif ch==6:
        n1=float(input("\nEnter the value: "))
        n2=float(input("\nEnter the base value: "))
        res=math.log(n1,n2)
        print(color.green(f"\nThe Result of the log of {n1} to the base {n2} is: {res}\n"))
        print(color.blue("\nDO YOU WANT TO ROUND THE Result OFF??"))
        choice=input("\nEnter Yes or No: ")
        if choice =="Yes":
            digits=int(input("\nEnter the number of decimal places you want to round it off to: "))
            print("\nYour Result is: ",round(res,digits))
            print(color.magenta(f"\nTHANK YOU FOR USING OUR SERVICES😄.....",['underlined','italic']))
        else:
            print("\nYour Result is: ",res)
            print(color.magenta(f"\nTHANK YOU FOR USING OUR SERVICES😄.....",['underlined','italic']))
            
#10.Trigonometric Ratios
elif ch==7:
    print('''
          YOU CAN FIND ALL 6 TRIGONOMETRIC RATIOS HERE:  ''')
    angle=float(input("\nEnter the value of angle :" ))
    ch=input("\nDo you want to work with DEGREES or RADIANS??: ")
    if ch=="DEGREES":
               print(color.blue(f'''
                 sin({angle}) = {round(math.sin(math.radians(angle)),3)}
                 cos({angle}) = {round(math.cos(math.radians(angle)),3)}
                 tan({angle}) = {round(math.tan(math.radians(angle)),3)}
                cosec({angle}) = {round(1/(math.sin(math.radians(angle))),3)}
                 sec({angle}) = {round(1/(math.cos(math.radians(angle))),3)}
                 cot({angle}) = {round(1/(math.tan(math.radians(angle))),3)}
                 
                 '''))
        
        
    elif ch=="RADIANS":
                print(color.blue(f'''
                 sin({angle}) = {round(math.sin(angle),3)}
                 cos({angle}) = {round(math.cos(angle),3)}
                 tan({angle}) = {round(math.tan(angle),3)}
                cosec({angle}) = {round(1/(math.sin(angle)),3)}
                 sec({angle}) = {round(1/(math.cos(angle)),3)}
                 cot({angle}) = {round(1/(math.tan(angle)),3)}
                 
                 '''))

    else:
        print(color.red(f"\nPLEASE ENTER A VALID CHOICE\n",['bold']))
else:
    print(color.red(f"\nPLEASE ENTER A VALID CHOICE BETWEEN 1 TO 7",{'bold'}))
        

    
    
    


# In[ ]:




