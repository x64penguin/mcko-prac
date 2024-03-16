import csv


with open("history_mirror.csv", encoding="utf8") as f:
    data = list(csv.reader(f, delimiter=","))[1:]

msg = input()
while msg != "stop":
    name, last_name = msg.split()

    found = False
    for date, username, verdict in data:
        current_name = username.split()

        if current_name[1] == name and current_name[2] == last_name:
            print(f"Предсказание для {current_name[0]} {current_name[1][0]}.{current_name[2][0]} - {verdict}")
            found = True

    if not found:
        print("Вас не нашлось в записях")

    msg = input()