import datetime
import json

class PhoneBook:
    def __init__(self, filename="calls.json"):
        self.filename = filename
        self.load_calls()

    def load_calls(self):
        """Загружает звонки из файла."""
        try:
            with open(self.filename, "r") as file:
                self.calls = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.calls = []

    def save_calls(self):
        """Сохраняет звонки в файл."""
        with open(self.filename, "w") as file:
            json.dump(self.calls, file, indent=4)

    def add_call(self, number):
        """Добавляет входящий звонок."""
        call = {"number": number, "date": datetime.datetime.now().isoformat()}
        self.calls.append(call)
        self.save_calls()

    def remove_old_calls(self):
        """Удаляет звонки старше месяца."""
        one_month_ago = datetime.datetime.now() - datetime.timedelta(days=30)
        self.calls = [call for call in self.calls if datetime.datetime.fromisoformat(call["date"]) > one_month_ago]
        self.save_calls()

    def show_calls(self):
        """Выводит список последних звонков."""
        for call in self.calls:
            print(f"Номер: {call['number']}, Дата: {call['date']}")

phonebook = PhoneBook()
phonebook.add_call("+1234567890")
phonebook.remove_old_calls()
phonebook.show_calls()
