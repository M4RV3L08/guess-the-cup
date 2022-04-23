import os,random

os.system('cls')

NUmber_of_cups =int( input("How many cups?: (ENter Just Number)"))

if NUmber_of_cups > 0:
    chances = int (input("How many chances?: "))
    j = 1

    chosen_one = random.randint(1,NUmber_of_cups)
    while j <= chances:
        User_chose = int(input("Guess the cup number :"))

        if User_chose == chosen_one:
            print("Yes , thats right")
            break

        else:
            print("No , wrong choise")
            
        j += 1
        
else:
    print("Invalid input !")

print(25*'-',"\nEnd of the game...")