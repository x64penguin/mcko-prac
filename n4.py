import csv


with open("history_mirror.csv", encoding="utf8") as f:
    data = list(csv.reader(f, delimiter=","))[1:]


years = {}
for date, *_ in data:
    year = date.split("-")[0]
    if year not in years:
        years[year] = 1
    else:
        years[year] += 1

# Выводим года в отсортированном порядке
for y, cnt in sorted(years.items(), key=lambda x: int(x[0])):
    print(f"В {y} году зеркало было использовано {cnt}.")