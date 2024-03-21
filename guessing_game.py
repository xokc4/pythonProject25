import sys
import logging
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def guess_number():
    # Загадываем число
    secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    logger.info(f"Загаданное число: {secret_number}")

    print("Программа загадала число от 0 до 1000. Угадайте его за 10 попыток.")
    logger.info("Игра началась.")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            guess = int(input(f"Попытка {attempt}. Введите ваше предположение: "))
        except ValueError:
            logger.error("Ошибка: Неверный формат числа. Пожалуйста, введите целое число.")
            print("Ошибка: Введите целое число.")
            continue

        if guess < secret_number:
            logger.info("Предложенное число меньше загаданного.")
            print("Загаданное число больше.")
        elif guess > secret_number:
            logger.info("Предложенное число больше загаданного.")
            print("Загаданное число меньше.")
        else:
            logger.info(f"Игрок угадал число {secret_number} за {attempt} попыток.")
            print(f"Поздравляем! Вы угадали число {secret_number} за {attempt} попыток.")
            return

    logger.info(f"Игрок не угадал число за {MAX_ATTEMPTS} попыток. Было загадано число {secret_number}.")
    print(f"К сожалению, вы не угадали число за {MAX_ATTEMPTS} попыток. Было загадано число {secret_number}.")

if __name__ == "__main__":
    guess_number()
