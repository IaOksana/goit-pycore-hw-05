# Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти читати лог-файл, переданий як аргумент 
# командного рядка, і виводити статистику за рівнями логування наприклад, INFO, ERROR, DEBUG. Також користувач 
# може вказати рівень логування як другий аргумент командного рядка, щоб отримати всі записи цього рівня.

from processing import load_logs, display_log_counts, count_logs_by_level, filter_logs_by_level
import sys 


def main() :    

    # Check if no input
    if len(sys.argv) > 1:
        # Скрипт повинен приймати шлях до файлу логів як аргумент командного рядка.
        file_path = sys.argv[1]

        log_level = ""
        if len(sys.argv)>2:
            log_level = sys.argv[2]

        logs = load_logs(file_path)

        display_log_counts(count_logs_by_level(logs))

        filtered = filter_logs_by_level(logs, log_level.upper())
        if filtered:
            print (f"Деталі логів для рівня '{log_level.upper()}':")
            for item in filtered:
                print(f"{item["date"]} {item["time"]} - {item["info"]}")
    else :
        print("No file")


if __name__ == "__main__":
    main()