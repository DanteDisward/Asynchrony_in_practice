from asyncio import *


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        await sleep(1/power)
        print(f'Силач {name} поднял {i+1}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = create_task(start_strongman('Тики', 2))
    task2 = create_task(start_strongman('Ник', 3))
    task3 = create_task(start_strongman('Нил', 4))
    await task1
    await task2
    await task3

run(start_tournament())
