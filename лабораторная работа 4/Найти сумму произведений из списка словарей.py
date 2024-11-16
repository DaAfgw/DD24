import json

filename = 'output.json'


def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    total_sum = sum(item["score"] * item["weight"] for item in data)

    # Округляем до 3 знаков
    return round(total_sum, 3)


print(task())
