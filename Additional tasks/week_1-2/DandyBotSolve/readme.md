!!! Решение для игры находятся в user_bot.py
    Для запуска игры запустить main.py  !!!


Скачайте игру DandyBot. Код для своего игрока записывается в файле user_bot.py. Игра запускается с помощью main.py.

Вот простой пример содержимого user_bot.py:

def script(check, x, y):
    return 'right'
Игровая логика записывается исключительно в теле функции script. В нашем случае игрок будет постоянно двигаться вправо.

Полный список действий, которые можно возвращать из функции script, задающей "интеллект" игрока:

	'up'. Двигаться вверх на клетку.
	'down'. Двигаться вниз на клетку.
	'left'. Двигаться влево на клетку.
	'right'. Двигаться вправо на клетку.
	'pass'. Ничего не делать.
	'take'. Взять золото.
Для изучения среды есть функция check:

	check('player', x, y). True, если какой-то игрок в позиции (x, y).
	check('gold', x , y). Если золото в позиции (x, y), то вернуть его количество, иначе вернуть 0.
	check('wall', x, y). True, если стена в позиции (x, y).
	check('empty', x, y). True, если пусто в позиции (x, y).
	check('level'). Вернуть номер текущего уровня.
Ваша задача — пройти 4 уровня. Дополнительно устанавливаемыми библиотеками и глобальными данными пользоваться нельзя.