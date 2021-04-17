
def random_number_location(target, max_value=1000, difficulty=60):
    for place in range(difficulty):
        if target < ((place + 1) * max_value / difficulty):
            print("Случайное число где-то здесь:")
            print("0", ("-" * place) + "x" + "-" * (difficulty - place), str(max_value))
            break





def CheckYourLuck(AttemptsValue = 7):
    import random
    from colorama import Fore
    max_random = 1000
    target = random.randint(0, max_random)
    guess = 0
    attempts = 0
    PreviousGuess = 0
    dificalt = 0
    advanced_mode = None
    print("Уровни сложности:" + Fore.GREEN + "\n 1 - Легко" + Fore.CYAN + "\n 2 - Среднe" + Fore.YELLOW + "\n 3 - Сложно"
          + Fore.BLUE + "\n 4 - Очень Сложно" + Fore.MAGENTA + "\n 5 - Боль и Страдание" + Fore.RED + "\n 6 - НАСМЕРТЬ " + Fore.RESET)
    print("Подсказки будут даваться в зависимости от выбраного уровня сложности.")
    while dificalt > 6 or dificalt < 1:
        try:
            dificalt = int(input("Введите число соответствующее уровеню сложности:"))
# except срабатывает вместе со следующим if =( Попытаться это исправить .)
        except Exception:
            print("Пожалуйста введите числовое значение соответствующее желаемому уровню сложности.")
        else:
            if dificalt > 6 or dificalt < 1:
                print("Уровень сложности должен сответствовать числам от 1 до 6")

    if dificalt == 1:
        random_number_location(target, max_random, 60)
        advanced_mode = False
        print(Fore.GREEN)
    elif dificalt == 2:
        random_number_location(target, max_random, 50)
        advanced_mode = False
        print(Fore.CYAN)
    elif dificalt == 3:
        random_number_location(target, max_random, 40)
        advanced_mode = False
        print(Fore.YELLOW)
    elif dificalt == 4:
        random_number_location(target, max_random, 30)
        advanced_mode = True
        print(Fore.BLUE)
    elif dificalt == 5:
        random_number_location(target, max_random, 20)
        advanced_mode = True
        print(Fore.MAGENTA)
    elif dificalt == 6:
        print("Я в тебя верю!")
        advanced_mode = True
        print(Fore.RED)
    while guess != target:
        if attempts == AttemptsValue:
            print("Игра окончена, число попыток исчерпано")
            break
        try:
            guess = float(input("Угадай моё число от 0 до 1000: "))
        except Exception:
            attempts += 1
            print("Ты ввел не число, а текст. Осталось опыток:", AttemptsValue - attempts)
            continue
        if guess > 1000 or guess < 0:
            attempts += 1
            print("Ты указал число больше 1000, или меньше 0. Осталось опыток:", AttemptsValue - attempts)
            continue
        elif advanced_mode == False:
            if guess > target:
                attempts += 1
                print("Попробуй поменьше. Осталось опыток:", AttemptsValue - attempts)
            elif guess < target:
                attempts += 1
                print("Попробуй побольше. Осталось опыток:", AttemptsValue - attempts)
        elif advanced_mode == True:
            if attempts > 0:
                difference = abs(target - guess)
                PreviousDifference = abs(target - PreviousGuess)
                if difference < PreviousDifference and guess != target:
                    attempts += 1
                    print("Теплее. Осталось опыток:", AttemptsValue - attempts)
                    PreviousGuess = guess
                elif difference > PreviousDifference and guess != target:
                    attempts += 1
                    print("Холоднее. Осталось опыток:", AttemptsValue - attempts)
                    PreviousGuess = guess
                elif difference == PreviousDifference:
                    attempts += 1
                    print("Не стоит вводить одно и тоже число 2 раза подряд. Осталось опыток:", AttemptsValue - attempts)
                    PreviousGuess = guess
            else:
                if guess > target:
                    attempts += 1
                    print("Попробуй поменьше. Осталось опыток:", AttemptsValue - attempts)
                    PreviousGuess = guess
                elif guess < target:
                    attempts += 1
                    print("Попробуй побольше. Осталось опыток:", AttemptsValue - attempts)
                    PreviousGuess = guess
    else:
        print("Ты угадал!")







CheckYourLuck(13)