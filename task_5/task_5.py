# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить ее на экран.

#Отдадим все на волю рендома ^__^

import random
with open("for_task_5.txt", 'w', encoding='utf-8') as file:
    for i in range(random.randint(0,100)):
        file.write(str(random.randint(0,200)))
        file.write(" ")
with open("for_task_5.txt", 'r', encoding='utf-8') as file:
    foo = [int(i) for i in file.readline().split()]
print(sum(foo))

