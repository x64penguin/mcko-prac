import csv


with open("history_mirror.csv", encoding="utf8") as f:
    data = list(csv.reader(f, delimiter=","))[1:]


# Сортируем сообщения по дате в порядке возрастания
data.sort(key=lambda x: x[0])

# Результат в виде csv файла с заголовком
result = [("date", "username")]

# Саммое раннее сообщение
oldest = None

for date, username, verdict in data:
    if verdict != "Победа над смертью":
        continue
    result.append((date, username))
    if oldest is None:
        oldest = (date, username)

# Записываем найденное в файл
with open("mirror_error.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter=",").writerows(result)

# Выводим самое ранне сообщение
surname, name, last_name = oldest[1].split()
print(f"Сообщение было зафиксировано: {oldest[0]} у пользователя {surname} {name[0]}.{last_name[0]}.")