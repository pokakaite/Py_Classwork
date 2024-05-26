import concurrent.futures
import time

start = time.perf_counter()


things = ['Вода', 'Еда']
doing = ['кипятится', 'греется']

def process(seconds, thing, doing):
    print(f'{thing} {doing} в течение {seconds} секунд...')
    time.sleep(seconds)

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [2, 3]
    result = executor.map(process, secs, things, doing)

finish = time.perf_counter()

print(f'\nПроцесс закончился спустя {round(finish - start, 2)} секунды')



start2 = time.perf_counter()


things = ['Овечка' for _ in range(5)]
doing = ['перепрыгивает забор' for _ in range(5)]

def process(seconds, count, thing, doing):
    print(f'\n{thing} {count} {doing} в течение {seconds} секунд...')
    time.sleep(seconds)

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [1, 2, 3, 4, 5]
    result2 = executor.map(process, secs, secs, things, doing)

finish2 = time.perf_counter()

print(f'\nПроцесс закончился спустя {round(finish2 - start2, 2)} секунды')