import random

def checker(a,b):
    a = a.lower()
    b = b.lower()
    if (a == "rock" and b == 'paper') or (a == "scissors" and b == "rock") or (a == "paper" and b == "scissors"):
        print("The player wins")
    elif (b == "rock" and a == 'paper') or (b == "scissors" and a == "rock") or (b == "paper" and a == "scissors"):
        print("The computer wins")
    else:
        print("tie")
y = random.choice(["Rock","Paper","Scissors"])


match = input("Rock, Paper or Scissors: ")

print("The match goes as follows")
print("Computer: " + y + "\nPlayer: " + match)

checker(y,match)


