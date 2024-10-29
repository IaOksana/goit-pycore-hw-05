from pathlib import Path
import re


""" Реалізуйте функцію load_logs(file_path: str) -> list для завантаження логів з файлу.
Завантаження лог-файлів виконує функція load_logs(file_path: str) -> list, що відкриває файл, читає кожен 
рядок і застосовує на нього функцію parse_log_line, зберігаючи результати в список. """
def load_logs(file_path: str) -> list:
    path = Path(file_path)
    result_list = []
    
    if path.exists():
        with open(file_path, "r") as file:
            result_list = [parse_log_line(line) for line in file if parse_log_line(line)]
            # так не подобається : result_list = list(map(lambda line: parse_log_line(line), file))
            return result_list
    else :
        print("No such file")
        return []


""" Реалізуйте функцію filter_logs_by_level(logs: list, level: str) -> list для фільтрації логів за рівнем.
Фільтрацію за рівнем логування виконує функція filter_logs_by_level(logs: list, level: str) -> list. 
Вона дозволить вам отримати всі записи логу для певного рівня логування. """
def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"] == level, logs))


""" Підрахунок записів за рівнем логування, проходить по всім записам і підраховує кількість записів для кожного 
рівня логування. """
def count_logs_by_level(logs: list) -> dict:
    result = {"INFO" : 0, "DEBUG" : 0, "ERROR" : 0, "WARNING" : 0}

    for item in logs:
        result[item["level"]] = result[item["level"]] + 1

    return result


""" Вивід результатів - форматує та виводить результати підрахунку в читабельній формі
Вона приймає результати виконання функції count_logs_by_level. """
def display_log_counts(counts: dict):

    print("Рівень логування | Кількість")
    print("----------------------------")
    print(f'INFO             | {counts["INFO"]}')
    print(f'DEBUG            | {counts["DEBUG"]}')
    print(f'ERROR            | {counts["ERROR"]}')
    print(f'WARNING          | {counts["WARNING"]}')


""" Парсинг рядка логу виконує ****функцію parse_log_line(line: str) -> dict, яка приймає рядок з логу як вхідний 
параметр і повертає словник з розібраними компонентами: дата, час, рівень, повідомлення. 
example: 2024-01-22 13:30:30 INFO Scheduled maintenance. """
def parse_log_line(line: str) -> dict:
    line_parts = line.split(maxsplit=3)

    if len(line_parts) < 4: 
        print ("Неправильний рядок")
        return {}
    
    # Перевірка дати
    date_pattern = r"\d{4}-\d{2}-\d{2}"  # Регулярні вирази для перевірки форматів дати. Формат "РРРР-ММ-ДД" 
    if not re.fullmatch(date_pattern, line_parts[0]):
        print("Неправильний формат дати")
        return {}
    
    # Перевірка часу
    time_pattern = r"\d{2}:\d{2}:\d{2}"  # Регулярні вирази для перевірки форматів часу. Формат "ГГ:ХХ:СС"
    if not re.fullmatch(time_pattern, line_parts[1]):
        print("Неправильний формат часу")
        return {}
    
    # Перевірка рівня логування
    log_levels = {"info", "error", "debug", "warning"}
    if line_parts[2].lower() not in log_levels:
        print("Неправильний рівень логування")
        return {}

    result_dic = {
        "date" : line_parts[0], 
        "time" : line_parts[1], 
        "level" : line_parts[2], 
        "info" : line_parts[3].strip()
    }
    return result_dic