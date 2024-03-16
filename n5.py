import csv


with open("history_mirror.csv", encoding="utf8") as f:
    data = list(csv.reader(f, delimiter=","))[1:]


def hash_name(name: str) -> int:
    '''
    Хэшериет строку и возвращает хэш
    :param name: строка которую нужно хэшировать
    :return: хэш
    '''
    p = 67
    m = 10e9 + 9

    result = 0
    p_pow = 1
    for x in name:
        result += (ord(x) * p_pow) % m
        p_pow *= p
    return int(result)


# Добавляем хеш и записываем в файл
with open("users_with_hash.csv", "w", encoding="utf8", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(("ID", "date", "username", "vedict"))
    for x in data:
        writer.writerow((hash_name(x[1]), *x))
