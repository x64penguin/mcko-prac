import csv


with open("history_mirror.csv", encoding="utf8") as f:
    data = list(csv.reader(f, delimiter=","))[1:]


# Проверка идет ли a раньше b по алфавиту
def compare(a, b):
    a_ = a.lower()
    b_ = b.lower()
    for i in range(min(len(a_), len(b_))):
        if a_[i] == b_[i]:
            continue
        return ord(a_[i]) < ord(b_[i])
    return False


for i in range(1, len(data)):
    key = data[i]
    j = i - 1
    while j >= 0 and compare(key[2], data[j][2]):
        j -= 1
    data[j] = key

