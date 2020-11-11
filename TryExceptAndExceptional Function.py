print("Enter 1st Number")
num1 = input()
print("Enter 2nd Number")
num2 = input()

try:                            #Try function is for the avoid the error and try to continue the code
    print("Sum of these two number is",
          int(num1)+int(num2))              #If you add the string in the num1 or num2 you cant get the error
except Exception as e:          #error print karega as  a string becoz error was catch by the (e)
    print(e)

print("This is most important")            #function wrong ho error ho fir bhi ye line print hogi code nhi rukega.