import os
import argparse
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Путь к папке, где лежат файлы с логами")
    parser.add_argument("--text", help="Текст, который надо найти", required=True)
    return parser.parse_args()


def get_files(path):
    if os.path.isfile(path):
        return [path]
    if os.path.isdir(path):
        return [
            os.path.join(path, file)
            for file in os.listdir(path)
            if os.path.isfile(os.path.join(path, file))
        ]
    raise FileNotFoundError("Путь не найден")


def create_blocks(filepath):
    blocks = {}
    current_time = None
    current_lines = []

    with open(filepath, "r") as f:
        for line in f:
            line_stripped = line.strip()
            try:
                timestamp = datetime.strptime(line_stripped[:19], "%Y-%m-%d %H:%M:%S")
                if current_time is not None:
                    blocks[current_time] = current_lines
                current_time = timestamp
                current_lines = [line]
            except ValueError:
                if current_time is not None:
                    current_lines.append(line)
        if current_time is not None:
            blocks[current_time] = current_lines
    return blocks


def fragment_search(line, search_word):
    words = line.split()
    for i, word in enumerate(words):
        if search_word in word:
            start = max(0, i - 5)
            end = i + 6
            return " ".join(words[start:end])
    return None


def search_in_blocks(filepath, blocks, search_word):
    results = []
    for timestamp, lines in blocks.items():
        for number, line in enumerate(lines, start=1):
            if search_word in line:
                fragment = fragment_search(line, search_word)
                results.append({
                    "file": filepath,
                    "time": timestamp,
                    "number_of_line": number,
                    "fragment": fragment
                })
    return results


def main():
    args = parse_args()
    files = get_files(args.path)
    search_word = args.text
    total = 0

    for file in files:
        blocks = create_blocks(file)
        matches = search_in_blocks(file, blocks, search_word)
        for match in matches:
            total += 1
            print("==========")
            print(f"Файл: {match['file']}")
            print(f"Время ошибки: {match['time']}")
            print(f"Номер строки: {match['number_of_line']}")
            print(f"Фрагмент: {match['fragment']}")
    if total == 0:
        print("Совпадений не найдено")
    else:
        print("==========")
        print(f"Всего совпадений: {total}")


if __name__ == "__main__":
    main()
