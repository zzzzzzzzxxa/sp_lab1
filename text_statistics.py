import os
import sys

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
    import string
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).lower().split()
    return words

def count_words(words: list) -> dict:
    """Подсчитывает количество каждого слова."""
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def write_report(file_name: str, word_count: dict):
    """Записывает отчет с подсчетом слов в файл."""
    base_name, ext = os.path.splitext(file_name)
    report_name = f"result/{base_name}_words{ext}"
    os.makedirs("result", exist_ok=True)
    
    with open(report_name, 'w', encoding='utf-8') as file:
        for word, count in word_count.items():
            file.write(f"{word}: {count}\n")

def main():
    """Главная функция программы."""
    if len(sys.argv) < 2:
        print("Ошибка: Укажите имя текстового файла как аргумент командной строки.")
        sys.exit(1)

    input_file = sys.argv[1]
    text = read_text(input_file)
    words = process_text(text)
    word_count = count_words(words)
    write_report(input_file, word_count)
    print("Отчет успешно создан в папке result.")

if __name__ == "__main__":
    main()
