num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
op = input("Choose the operation (+, -, *, /):")

match op:
    case '+':
        print("The result is ", num1+num2,".", sep="")
    case '-':
        print("The result is ", num1-num2,".", sep="")
    case '*':
        print("The result is ", num1*num2,".", sep="")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print("The result is ", num1/num2,".", sep="")