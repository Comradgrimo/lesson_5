# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

with open("for_task_4.txt", 'r', encoding='utf-8') as file:
    bar = [i.split() for i in file.readlines()]
name_ru = ["Один","Два","Три","Четыре"]
for i in range(len(bar)):
    bar[i][0] = name_ru[i]

with open("for_task_4(modyify).txt", 'w', encoding='utf-8') as file:
    for i in bar:
        file.write(" ".join(i))
        file.write("\n")