import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def check_prime(number):
    if number < 2 or number > 100000:
        logger.error("Неверный формат числа. Число должно быть от 2 до 100000.")
        return
    if is_prime(number):
        logger.info(f"{number} является простым числом.")
    else:
        logger.info(f"{number} является составным числом.")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            number = int(sys.argv[1])
            check_prime(number)
        except ValueError:
            logger.error("Неверный формат числа. Пожалуйста, введите целое число.")
    else:
        logger.error("Пожалуйста, передайте одно целое число в качестве аргумента командной строки.")
