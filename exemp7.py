# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def insert_full(**data_set) :
    data_set = (f"name_1 {name_1}; name_2 {name_2}; bern_date {bern_date}; sity_live {Sity_live}; adress_mail {adress_mail}; phone_numb {phone_numb}", )
    print(data_set)
print(insert_full(name_1=str(input("input name")),
                  name_2=str(input("input soname")),
                  bern_date=str(input("bern date")),
                  Sity_live=str(input("input sity")),
                  adress_mail=str(input("input email")),
                  phone_numb=str(input("input phone"))))


from sys import argv

def salary(hours, stav, bounty):
    return int((hours * stav) + pr)

try:
    file, w_hours, h_stav, b_pr = argv
except ValueError:
    print("Введите аргументы через пробел - кол-во отработанных часов, ставку, премию")
    exit()

print(w_hours, h_stav, b_pr)
s = salary(int(w_hours), int(h_stav), int(b_pr))

print(f"Зарплата за отработанные часы + премия : {s}")
