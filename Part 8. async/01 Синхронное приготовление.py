import time
from datetime import datetime

# в нашей программе одна минута реального времени будет соответствовать одной секунде времени работы программы
# если установить коэффициент в 0.5, то половине секунды времени работы программы
COEFF = 1


def dish(name, prepare, wait):
    """
    функция имитирует приготовление одного блюда
    :param name: название блюда
    :param prepare: сколько минут на подготовку
    :param wait: сколько минут на ожидание готовности
    :return:
    """
    print(f"start {datetime.now().strftime('%H:%M:%S')} prepare dish {name} {prepare} min")
    time.sleep(COEFF * prepare)
    print(f"start {datetime.now().strftime('%H:%M:%S')} wait dish {name} {wait} min")
    time.sleep(COEFF * wait)
    print(f"{datetime.now().strftime('%H:%M:%S')} dish {name} is ready")


def main():
    """
    функция запускает "приготовление" блюд
    :return:
    """
    dish('закуска', 2, 3)
    dish('основное блюдо', 5, 10)
    dish('десерт', 3, 5)


if __name__ == '__main__':
    t0 = time.time()  # запоминаем время начала работы
    main()  # запускаем приготовление
    delta = int((time.time() - t0) / COEFF)  # считаем затраченное время
    print(f"{datetime.now().strftime('%H:%M:%S')} It took {delta} min")