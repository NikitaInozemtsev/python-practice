import random
import random_bot


def script(check, x, y):

    if check("level") == 1:
        # Собирание монеток прописано на каждом уровне
        if check("gold", x, y):
            return "take"
        # Идем направо до стены и по стенке идем вниз
        elif check("wall", x+2, y):
            return "down"
        return "right"

    elif check("level") == 2:
        if check("gold", x, y):
            return "take"

        # По умолчанию идем вверх
        # Уровень проходится по монеткам (мы идем в сторону монетки)
        if check("gold", x + 1, y):
            return  "right"
        elif check("gold", x - 1, y):
            return  "left"
        if check("gold", x, y - 1):
            return  "up"
        elif check("gold", x, y + 1):
            return  "down"

        # Условие для первого шага чтобы встать на линию с монетками
        if not check("wall",x+2,y):
            return "right"
        return "up"

    elif check("level") == 3:
        if check("gold", x, y):
            return "take"
        """
         Проверятся все блоки вокруг игрока и, в зависимости от этого, делается шаг
         Таким образом происходит обход локации против часовой стрелки
        """
        u = check("wall", x, y - 1)
        d = check("wall", x, y + 1)
        r = check("wall", x + 1, y)
        l = check("wall", x - 1, y)
        ur = check("wall", x + 1, y - 1)
        dr = check("wall", x + 1, y + 1)
        dl = check("wall", x - 1, y + 1)
        ul = check("wall", x - 1, y - 1)
        if l and d:
            return "right"
        if r and d:
            return "up"
        if u and r:
            return "left"
        if l and u:
            return "down"
        if d:
            return "right"
        if r:
            return "up"
        if u:
            return "left"
        if l:
            return "down"
        if ur:
            return "up"
        if dr:
            return "right"
        if dl:
            return "down"
        if ul:
            return "left"

    elif check("level") == 4:
        if check("gold", x, y):
            return "take"
        """
         Сохраняется логика из 3го уровня и добавляется "прыжок" на противоположную платформу
         2 прыжка в разных ситуациях:
            1 - когда над персонажем 3 блока и под персонажем находится один блок, то прыжок наверх
            2 - когда под персонажем 3 блока и над персонажем находится один блок, то прыжок вниз
        """
        if check("wall", x, y - 2) & check("wall", x + 1, y - 2) & check("wall", x + 2, y - 2) & check("wall", x, y + 1):
            return "up"
        if check("wall", x, y + 2) & check("wall", x - 1, y + 2) & check("wall", x - 2, y + 2) & check("wall", x, y - 1):
            return "down"
        u = check("wall", x, y - 1)
        d = check("wall", x, y + 1)
        r = check("wall", x + 1, y)
        l = check("wall", x - 1, y)
        ur = check("wall", x + 1, y - 1)
        dr = check("wall", x + 1, y + 1)
        dl = check("wall", x - 1, y + 1)
        ul = check("wall", x - 1, y - 1)
        if l and d:
            return "right"
        if r and d:
            return "up"
        if u and r:
            return "left"
        if l and u:
            return "down"
        if d:
            return "right"
        if r:
            return "up"
        if u:
            return "left"
        if l:
            return "down"
        if ur:
            return "up"
        if dr:
            return "right"
        if dl:
            return "down"
        if ul:
            return "left"

    return "pass"
