def main ():
    print ("#############################################")
    print ("Pycalc 1.0")
    print ("Add, subtract, multiply, and divide user provided variables [X] & [Y]")
    print ("----------")
    print ("Operations:")
    print("+", "-", "*", "/")
    
    choice = input(">>Choose operation & press ENTER: ")

    num1 = int(input("Enter variable [X]: "))
    num2 = int(input("Enter variable [Y]: "))

    print ("------------------------")

    if choice == '+':
       print(num1,"+",num2,"=", (num1 + num2))

    elif choice == '-':
       print(num1,"-",num2,"=", (num1 - num2))

    elif choice == '*':
       print(num1,"*",num2,"=", (num1 * num2))

    elif choice == '/':
       print(num1,"/",num2,"=", (num1 / num2))
       
    else:
       print("Invalid input")

    again = input("Run Again (y/n)?")
    if again == "y":
        main()
    elif again == "n":
        print("Closing Application...")
    else:
        print("Invalid Entry. Closing Application...")
    
main() 
