print("***Python Calculator***")
print("         +-*/          ")

while True:
    ans=input("Do you want to perform a calculation Yes or No? ")
    ans=ans.lower()
    if ans == 'no':
        print("Have a Calculative Day!!!")
        break
        
     
    else:
        a=input("Enter the first number ")
        b=input("Enter the second number ")
        a=int(a)
        b=int(b)
        oper=input("Choose an operation from +,-,*,/ ")
        if oper == '+':
            answer=a+b
            print(f"Result:{answer}")
        elif oper == '-':
            answer=a-b
            print(f"Result:{answer}")
        elif oper == '*':
            answer=a*b
            print(f"Result:{answer}")
        elif oper == '/':
            answer=a/b
            print(f"Result:{answer}")

            
            
        
    
          
