
def f23(x):
    for i in x:
        i[0] = '{:,.2f}'.format(float(i[0]))
        i[1] = i[1].split(' ')[0]
        i[2] = i[2].title()
    result = list()
    for i in x:
        if i not in result:
            result.append(i)
    return result

#print(f23([['0.028', 'Кетолянц Ф.Г.', 'нет'], ['0.423', 'Наначев М.В.', 'да'], ['0.896', 'Кеций Н.Ф.', 'нет'], ['0.110', 'Кадко А.К.', 'да'], ['0.028', 'Кетолянц Ф.Г.', 'нет'], ['0.028', 'Кетолянц Ф.Г.', 'нет']]))