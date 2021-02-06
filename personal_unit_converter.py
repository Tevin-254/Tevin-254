user_name= input("Enter your user name: ")
print(f"Greetings Mr/Mrs/Miss {user_name}.Glad to have you back!")
print('\nkindly choose your conversion\n')

print( "a-convertion of cm into m")
print("b-convertion of m into km")
print("c-convertion of inch into ft")
print("d-convertion of m^3 into liters")
print("e-conversion of fahrenheit to celsius")
print("f-convertion of percentage to letter grade")


convertor= input("Enter your converter choice:")
if convertor =="a":
    print("Selection was made to a cm converter")
    
    a = int(input("Please enter your estimated distance in cm : "))
    m=a/100
    print("the distance in m is : " ,m)

elif convertor =="b":
    print("Selection was made to a m converter")
    m=int(input("enter distance in m : "))
    b=m/1000
    print(m,"m is equvalent to",b,"km")
elif convertor =="c":

    print("Selection was made to a inch converter")
    c=int(input("enter the length in inches : "))
    ft=c/12
    print("the length in feet is : " ,ft)

elif convertor == "d":
    print("Selection was made to a m^3 converter")
    m = int(input("Enter the capacity in m^3: "))
    liter=m*100
    print("Capaciy in liters is equal to ,",liter)

elif convertor =="e":

    print("Selection was made to a fahrenheit converter")
    Fr=float(input("Enter your temperature in fahrenheit : "))
    celsius=(5(Fr-32))/9
    print(Fr,"fahrenheit is equal to",celsius,"degrees Celsius")

elif convertor=="f":
 
    print("Selection was made to a percentage converter")
    f=int(input("Enter your grade in percentage: \n"))
    if  80<= f <=100:
        print("Your grade is A")
    elif 70<= f <=79:
        print ("Your grade is B")
    elif 60<= f <=69:
        print("Your grade is C")
    elif 50<= f <=59:
        print("Your grade is D")
    elif 20<= f <=49:
        print("Your grade is E")
    elif 0<= f <=19:
        print("Your grade is F")
    else:
        print("INVALID GRADE PERCENTAGE INPUT!") 
           
else:
    print("UNIDENTIFIED! Please select again:")

print("Thank you and Goodbye",user_name)      
