from faker import Faker
import random
fake = Faker("ru_Ru")

def fake_company(n):                                                   # n - количество людей
    name_firm = ["firm_"+str(x+1) for x in range(n)]
    name_firm_prefix = [fake.company_prefix() for _ in range(n)]
    profit = [round(random.uniform(10000,   90000),2) for x in range(10)]
    minus = [round(random.uniform(10000, 90000), 2) for x in range(10)]
    with open("for_task_7.txt", 'w', encoding='utf-8') as file:
        for i in range(len(name_firm_prefix)):
            file.write(f"{name_firm[i]} {str(name_firm_prefix[i])} {str(profit[i])} {str(minus[i])} \n")

