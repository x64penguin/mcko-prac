import csv


with open("history_mirror.csv", encoding="utf8") as f:
    data = list(csv.reader(f, delimiter=","))[1:]


def compare(a: str, b: str) -> bool:
    '''
    Возвращает True если строка a идет раньше по алфавиту чем b, иначе False
    '''

    a_ = a.lower()
    b_ = b.lower()
    for i in range(min(len(a_), len(b_))):
        if a_[i] == b_[i]:
            continue
        return ord(a_[i]) < ord(b_[i])
    return False


# Сортировка вставками по алфавиту по вердикту
for i in range(1, len(data)):
    key = data[i]
    j = i - 1
    while j >= 0 and compare(key[2], data[j][2]):
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = key


cnt = 0
for x in data:
    # Возможно, строки где verdict = "error" выводить не следует
    # if x[2] == "error":
    #    continue
    print(" - ".join(x))
    cnt += 1
    if cnt >= 4:
        break