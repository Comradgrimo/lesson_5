from faker import Faker
import random
fake = Faker("ru_Ru")

def fake_data(n):                                                   # n - количество людей
    foo = [fake.last_name() for x in range(n)]
    bar = [round(random.uniform(8000,30000),2) for x in range(10)]
    with open("for_task_3.txt", 'w', encoding='utf-8') as file:
        for i in range(len(foo)):
            file.write(f"{foo[i]} {str(bar[i])} \n")

