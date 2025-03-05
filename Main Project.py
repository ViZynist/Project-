# Хранилище данных
import sys

data = {}


def add_entry(date, participants, event):
    """Добавляет запись в хранилище"""
    if date not in data:
        data[date] = []
    data[date].append((participants, event))


def search_by_date_range(start_date, end_date):
    """Поиск записей по диапазону дат"""
    result = []
    for date in sorted(data.keys()):
        if start_date <= date <= end_date:
            result.extend(data[date])
    return result


def search_by_keyword(keyword):
    """Поиск записей по ключевому слову среди участников или событий"""
    result = []
    for entries in data.values():
        for entry in entries:
            if keyword.lower() in entry[0].lower() or keyword.lower() in entry[1].lower():
                result.append(entry)
    return result


def calculate_statistics():
    """
    Функция для расчета статистики:
    1. Общее количество событий.
    2. Наиболее часто упоминаемые участники.
    """
    total_events = sum(len(entries) for entries in data.values())

    participant_frequencies = {}
    for entries in data.values():
        for entry in entries:
            participants = entry[0]
            for participant in participants:
                participant_frequencies[participant] = participant_frequencies.get(participant, 0) + 1

    most_common_participants = sorted(
        participant_frequencies.items(), key=lambda item: item[1], reverse=True
    )

    return total_events, most_common_participants


def display_statistics(total_events, most_common_participants):
    """Отображает статистику"""
    print("\nСтатистика:")
    print(f"Общее количество событий: {total_events}")
    print("\nНаиболее часто упоминаемые участники:")
    for index, (participant, count) in enumerate(most_common_participants[:5]):
        print(f"{index + 1}. {participant}: {count} раз")


def user_input():
    """Запрашивает данные у пользователя и добавляет их в хранилище"""
    while True:
        print("\nВыберите действие:")
        print("1. Добавить новую запись")
        print("2. Найти записи по диапазону дат")
        print("3. Найти записи по ключевому слову")
        print("4. Вывод статистики по записанной информации")
        print("0. Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            # Запрашиваем данные для новой записи
            date = input("Введите дату (YYYY-MM-DD): ")
            participants = input("Введите участников через запятую: ").split(", ")
            event = input("Введите название события: ")

            # Добавляем запись
            add_entry(date, participants, event)
            print("Запись добавлена.")

        elif choice == "2":
            # Запрашиваем диапазон дат для поиска
            start_date = input("Введите начальную дату (YYYY-MM-DD): ")
            end_date = input("Введите конечную дату (YYYY-MM-DD): ")

            # Выполняем поиск
            results = search_by_date_range(start_date, end_date)
            if results:
                print("\nЗаписи за указанный период:")
                for record in results:
                    print(f"Дата: {start_date}, Участники: {record[0]}, Событие: {record[1]}")
            else:
                print("Нет записей за указанный период.")

        elif choice == "3":
            # Запрашиваем ключевое слово для поиска
            keyword = input("Введите ключевое слово: ")

            # Выполняем поиск
            results = search_by_keyword(keyword)
            if results:
                print("\nЗаписи, соответствующие запросу:")
                for record in results:
                    print(f"Участники: {record[0]}, Событие: {record[1]}")
            else:
                print("Нет записей, соответствующих запросу.")

        elif choice == "4":
            # Расчитываем и выводим статистику
            total_events, most_common_participants = calculate_statistics()
            display_statistics(total_events, most_common_participants)

        elif choice == "0":
            print("Завершение программы...")
            sys.exit(0)

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    user_input()