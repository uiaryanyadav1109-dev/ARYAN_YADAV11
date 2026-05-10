while True:
    #INPUTS
    a=float(input("ENTER A NUMBER_1:"))
    b=float(input("ENTER A NUMBER_2:"))
    option=input("ENTER A FUNCTION(+,-,*,/):")
    #FUNTIONS AND OUTPUTS

    #FOR ADDITION
    if option=='+':
        sum=a+b
        print("ADDITION OF",a,"+",b,":",sum)
    
    #FOR SUBTRACTION
    elif option=='-':
        sub=a-b
        print("SUBTRACTION OF",a,"-",b,":",sub)
        sub2=b-a
        print("SUBTRACTION OF",b,"-",a,":",sub2)
    
    #FOR DIVISION
    elif option=='/':
            if b!=0:
                div2 = b/a
                print("DIVISION OF",b,"/",a,":",div2)
            else:
                print("CANNOT DIVIDE BY ZERO")
                div1 = a/b
                print("DIVISION OF",a,"/",b,":",div1)
                
    #FOR MULTIPLICATION    
    elif option=='*':
        mulp=a*b
        print("MULTIPLICATION OF",a,"*",b,":",mulp)
    else:
        print("INVALID OPTION")
    
    #ON/OFF SWITCH
    cont=input("DO YOU WANT TO CONTINUE(YES/NO):").lower()
    if option=="no":
        print("Calculator closed")
        break