import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Открытие файла для получения чтения словарей из сsv строк
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
