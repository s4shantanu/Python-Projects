#  Faulty Calculator
print("Enter 1st Number")
num1 = int(input())
print("So what you want? +,_,*,/")
num3 = (input())
print("Enter 2nd Number")
num2 = int(input())
print("The Answer is " "")



if num1 == 45 and  num2 == 3 and num3 == '*':
    print("555")
elif num1 == 50 and  num2 == 9 and num3 == '+':
    print("55")
elif num1 == 34 and num2 == 7 and num3 == '/':
    print("7")
elif num3 == '*':
    num4 = num1 * num2
    print(num4)
elif num3 == '+':
    plus = num2 + num1
    print(plus)
elif num3 == '/':
    Dev = num2 / num1
    print(Dev)
elif num3 == '-':
    sub = num2 - num1
    print(sub)
elif num3 == '%':
    percent = num2 % num1
    print(percent)
else:
    print("Error! Please check your input")

