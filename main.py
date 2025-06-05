import random

print(" Я загадав число від 1 до 100. У тебе є 7 спроб, щоб вгадати його).")

number = random.randint(1, 100)
tries = 0

while tries < 7:
    guess = input("Введи число: ")
    guess = int(guess)

    tries += 1

    if guess < number:
        print("Твоє число менше загаданого.")
    elif guess > number:
        print("Твоє число більше загаданого.")
    else:
        print("Ти вгадав!!!")
        break

if guess != number:
    print("Спроби закінчились(. Я загадав число", number)
