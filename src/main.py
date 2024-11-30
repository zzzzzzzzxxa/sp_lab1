 
import sys
import os
import string
from collections import Counter

def read_text(file_path):
    """Читает текст из файла."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        sys.exit(1)

def process_text(text):
    """Обрабатывает текст: разделяет на слова, убирает знаки препинания, переводит в нижний регистр."""
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).lower().split()
    return words

def save_word_count(word_count, output_path):
    """Сохраняет статистику слов в файл."""
    with open(output_path, 'w', encoding='utf-8') as f:
        for word, count in word_count:
            f.write(f"{word}: {count}\n")

def save_statistics(statistics, output_path):
    """Сохраняет общую статистику в файл."""
    with open(output_path, 'w', encoding='utf-8') as f:
        for key, value in statistics.items():
            f.write(f"{key}: {value}\n")

def analyze_text(file_path):
    """Анализирует текст и сохраняет результаты."""
    text = read_text(file_path)
    words = process_text(text)
    
    word_count = Counter(words)
    output_file = os.path.splitext(file_path)[0] + "_words.txt"
    result_path = os.path.join('result', os.path.basename(output_file))
    save_word_count(word_count.most_common(), result_path)

    statistics = {
        "Уникальные слова": len(word_count),
        "Знаков препинания": sum(1 for char in text if char in string.punctuation),
    }
    for length in range(1, max(len(word) for word in words) + 1):
        statistics[f"Слова длиной {length}"] = sum(1 for word in words if len(word) == length)

    stat_file = os.path.splitext(file_path)[0] + "_stat.txt"
    stat_path = os.path.join('result', os.path.basename(stat_file))
    save_statistics(statistics, stat_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python main.py <путь к файлу>")
        sys.exit(1)

    input_file = sys.argv[1]
    analyze_text(input_file)
