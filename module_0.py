import numpy as np


def game_core_v1(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    left = 1
    rigth = 101
    predict = 50
    while number != predict:
        count += 1
        if predict < number:
            left = predict
        elif predict > number:
            rigth = predict
        predict = (rigth-left)//2 + left

    return(count)  # выход из цикла, если угадали


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    left = 1
    rigth = 101
    predict = np.random.randint(left, rigth)
    while number != predict:
        count += 1
        if predict < number:
            left = predict
        elif predict > number:
            rigth = predict
        predict = np.random.randint(left, rigth)

    return(count)  # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = float(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v1)
score_game(game_core_v2)

