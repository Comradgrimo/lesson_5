# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
# собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
from generate_company import fake_company
import json
fake_company(10)

import re
with open("for_task_7.txt", 'r', encoding='utf-8') as file:
    foo = file.readlines()
str_ = [n.strip().split() for n in foo]             #Отсекаем пробелы переносы итд
name = [str_[n][0] for n in range(len(str_))]       #оставляем только название фирм
   #оставляем только цифры

profit = [round(float(i[2]) - float(i[3]), 2) for i in str_] #Прибыль
average = [x for x in profit if x > 0]
average = round(sum(average) / len(average), 2)                       #Средняя прибыль фирм с положительной выручкой

q = {name[i]:profit[i] for i in range(len(str_))}
total = [q, {"average_profit": average}]
print(total)

with open("for_task_7.json", 'w', encoding='utf-8') as file:
    json.dump(total, file)
