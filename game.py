import random

print("Вітаю! Я загадав число від 1 до 100. Спробуйте вгадати його за 7 спроб.")

number = random.randint(1, 100)
tries = 0

while tries < 7:
    guess = input("Введіть ваше припушення: ")
    guess = int(guess)

    tries += 1

    if guess < number:
        print("Занадто маленьке!")
    elif guess > number:
        print("Занадто велике!")
    else:
        print("Ви вгадали! Це число")
        break

if guess != number:
    print("Спроби закінчились. Я загадав число", number)
