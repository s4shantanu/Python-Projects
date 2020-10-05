while(True):
    print("Press q to quit")
    a = input("Enter a Number: ")
    if a == 'q' :
        break
    try:
        print("Trying...")
        a = int(a)
        if a > 6:
            print("You Entered a number greater than 6")
    except Exception as e:
                print(f"Your input result as error: {e}")

print("Thanks for playing this game")