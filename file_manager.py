"""Задание №9 (средней сложности): Класс для работы с файлами."""

from pathlib import Path


class FileManager:
    """Класс для чтения и записи текстовых файлов."""

    def __init__(
        self, filepath: str | Path, encoding: str = "utf-8"
    ) -> None:
        self.filepath = Path(filepath)
        self.encoding = encoding

    def write(self, text: str) -> None:
        """Записывает текст в файл (перезаписывает содержимое)."""
        with self.filepath.open("w", encoding=self.encoding) as f:
            f.write(text)

    def append(self, text: str) -> None:
        """Добавляет текст в конец файла."""
        with self.filepath.open("a", encoding=self.encoding) as f:
            f.write(text)

    def read(self) -> str:
        """Читает всё содержимое файла."""
        if not self.filepath.exists():
            raise FileNotFoundError(f"Файл {self.filepath} не найден")
        with self.filepath.open("r", encoding=self.encoding) as f:
            return f.read()

    def read_lines(self) -> list[str]:
        """Возвращает список строк из файла."""
        if not self.filepath.exists():
            raise FileNotFoundError(f"Файл {self.filepath} не найден")
        with self.filepath.open("r", encoding=self.encoding) as f:
            return [line.rstrip("\r\n") for line in f]


def main() -> None:
    """Демонстрация работы класса FileManager."""
    fm = FileManager("sample.txt")
    fm.write("Первая строка\n")
    fm.append("Вторая строка\n")

    print("Содержимое файла:")
    print(fm.read().strip())
    print("Строки:", fm.read_lines())


if __name__ == "__main__":
    main()
