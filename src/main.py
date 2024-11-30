import os
import string
from collections import Counter

def read_text(file_path):
    """Читает текст из файла по указанному пути."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def process_text(text):
    """Разделяет текст на слова, удаляет знаки препинания и переводит в нижний регистр."""
    # Удаление знаков препинания и преобразование текста в нижний регистр
    text = text.lower()
    words = text.split()
    processed_words = []
    
    for word in words:
        # Убираем знаки препинания с начала и конца слова
        word = word.strip(string.punctuation)
        if word:
            processed_words.append(word)
    
    return processed_words

def save_word_count(word_count, file_path):
    """Сохраняет подсчитанные слова в файл."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        for word, count in word_count:
            file.write(f"{word}: {count}\n")

def save_statistics(statistics, file_path):
    """Сохраняет статистику в файл."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        for key, value in statistics.items():
            file.write(f"{key}: {value}\n")

def analyze_text(file_path):
    """Анализирует текст и сохраняет результаты."""
    text = read_text(file_path)
    words = process_text(text)
    
    # Использование Counter для подсчета слов
    word_count = Counter(words)
    output_file = os.path.splitext(file_path)[0] + "_words.txt"
    result_path = os.path.join('result', os.path.basename(output_file))
    save_word_count(word_count.most_common(), result_path)

    # Статистика по тексту
    statistics = {
        "Уникальные слова": len(word_count),
        "Знаков препинания": sum(1 for char in text if char in string.punctuation),
    }
    for length in range(1, max(len(word) for word in words) + 1):
        statistics[f"Слова длиной {length}"] = sum(1 for word in words if len(word) == length)

    # Сохранение статистики в файл
    stat_file = os.path.splitext(file_path)[0] + "_stat.txt"
    stat_path = os.path.join('result', os.path.basename(stat_file))
    save_statistics(statistics, stat_path)

# Пример запуска функции
if __name__ == "__main__":
    file_path = 'example.txt'  # Укажите путь к вашему текстовому файлу
    analyze_text(file_path)
