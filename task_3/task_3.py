# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
# величины дохода сотрудников.

#т.к я ленив, то не хочу вбивать 10 человек с зарплатами вручную, поэтому я их сгенерирую, написав тем самым еще больше
# строк)), но они каждый раз разные ^__^
#надеюсь это не повлияет на оценку задания

from generate_name import fake_data
fake_data(10)                                                       #Инициализируем количесво человек (10)
with open("for_task_3.txt", 'r', encoding='utf-8') as file:
    foo = file.readlines()
bar = [i.strip().split() for i in foo]   #генерируем новый список с которым удобно работать
q=[]
for i in range(len(bar)):
    if (float(bar[i][1])) <= 20000:
        print(f"{bar[i][0]} {bar[i][1]}")
        q.append(float(bar[i][1]))

print(f"Средняя зарплата выбранных сотрудников - {round((sum(q)/len(q)),2)}")

