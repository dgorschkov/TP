import os
import time
import asyncio
from datetime import datetime

COEFF = 1


async def dish(name, prepare, wait):
    print(f"start {datetime.now().strftime('%H:%M:%S')} prepare dish {name} {prepare} min")
    time.sleep(COEFF * prepare)
    print(f"start {datetime.now().strftime('%H:%M:%S')} wait dish {name} {wait} min")
    await asyncio.sleep(COEFF * wait)
    print(f"{datetime.now().strftime('%H:%M:%S')} dish {name} is ready")


async def main():
    tasks = [
        asyncio.create_task(dish('закуска', 2, 3)),
        asyncio.create_task(dish('основное блюдо', 5, 10)),
        asyncio.create_task(dish('десерт', 3, 5)),
    ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time.time()  # запоминаем время начала работы
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main()) # запускаем асинхронное приготовление
    delta = int((time.time() - t0) / COEFF)  # считаем затраченное время
    print(f"{datetime.now().strftime('%H:%M:%S')} It took {delta} min")