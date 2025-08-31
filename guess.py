import random

print("🎲 welcome to the number Guessing game 🎲")

print(" I am thinking of a number between 1 and 50 ")

secrete_number = random.randint(1,50)

attempts = 0

while True:
    guess = int(input("enter your Guess :"))
    attempts+=1
    
    if guess < secrete_number:
        print("Too low 📉 Try again.")
        
    elif guess > secrete_number:
        print(" To High 📈 Try again.")
        
    else:
        print(f"🎉 Correct! the number was {secrete_number}")
        print(f"you Gussed it in {attempts} attempts 🏆")
        break