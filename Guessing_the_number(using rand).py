import random

#no guessing limit 
def generate(a):
    x = random.randint(0,a)
    answer = 0
    while answer != x: 
       answer = int(input("Guess the number: "))
       if answer > x:
        print("\n Your guess is too high, Try again!")
       elif answer < x:
        print("\n Your guess is too low, Try again!")
       else:
        print("Congratulations you got it right!")


generate(100)


