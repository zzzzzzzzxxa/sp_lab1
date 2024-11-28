import os
import sys
from collections import Counter
import string

def read_text(file_name: str) -> str:
    """Читает текст из файла."""
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_name} не найден.")
        sys.exit(1)

def process_text(text: str) -> list:
    """Разделяет текст на слова, удаляет знаки препинания и переводит в нижний регистр."""
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).lower().split()
    return words

def count_words(words: list) -> Counter:
    """Подсчитывает количество каждого слова с использованием Counter."""
    return Counter(words)

def count_punctuation(text: str) -> int:
    """Подсчитывает общее количество знаков препинания."""
    return sum(1 for char in text if char in string.punctuation)

def word_length_distribution(words: list) -> Counter:
    """Вычисляет распределение слов по длине."""
    lengths = [len(word) for word in words]
    return Counter(lengths)

def write_report(file_name: str, word_count: Counter):
    """Записывает отчет с подсчетом слов в файл (сортировка от более частых к менее частым)."""
    base_name, ext = os.path.splitext(file_name)
    report_name = f"result/{base_name}_words{ext}"
    os.makedirs("result", exist_ok=True)

    with open(report_name, 'w', encoding='utf-8') as file:
        for word, count in word_count.most_common():  # .most_common() сортирует по убыванию
            file.write(f"{word}: {count}\n")

def write_statistics(file_name: str, unique_words: int, punctuation_count: int, word_lengths: Counter):
    """Записывает статистику в файл."""
    base_name, ext = os.path.splitext(file_name)
    stat_name = f"result/{base_name}_stat{ext}"
    os.makedirs("result", exist_ok=True)

    with open(stat_name, 'w', encoding='utf-8') as file:
        file.write(f"Количество уникальных слов: {unique_words}\n")
        file.write(f"Количество знаков препинания: {punctuation_count}\n")
        file.write("Распределение слов по длине:\n")
        for length, count in sorted(word_lengths.items()):
            file.write(f"  Длина {length}: {count} слов(а)\n")

def main():
    """Главная функция программы."""
    if len(sys.argv) < 2:
        print("Ошибка: Укажите имя текстового файла как аргумент командной строки.")
        sys.exit(1)

    input_file = sys.argv[1]
    text = read_text(input_file)
    words = process_text(text)

    # Подсчёт слов
    word_count = count_words(words)

    # Подсчёт статистики
    unique_words = len(word_count)
    punctuation_count = count_punctuation(text)
    word_lengths = word_length_distribution(words)

    # Запись отчётов
    write_report(input_file, word_count)
    write_statistics(input_file, unique_words, punctuation_count, word_lengths)

    print("Отчёты успешно созданы в папке result.")

if __name__ == "__main__":
    main()
