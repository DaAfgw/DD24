# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter=","):
    # Разделяем строки на списки участников
    participants1 = group1.split(delimiter)
    participants2 = group2.split(delimiter)

    # Находим общие элементы
    common_participants = []
    for participant in participants1:
        if participant in participants2:
            common_participants.append(participant)

    # Сортируем результат
    return sorted(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print("Общие участники:", common)
