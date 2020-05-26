# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("for_task_2.txt", 'r', encoding='utf-8') as file:
    foo = file.readlines()
print(f"Количество строк в файле: {len(foo)}")
for i in range(len(foo)):
    print(f"Количество слов в строке {i}: {len(foo[i].split())}" )