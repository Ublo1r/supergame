from tkinter import Tk, Label, Button

def btn_click(is_correct):
    if is_correct:
        result_label.config(text="Правильно!")
    else:
        result_label.config(text="Неправильно!")

# Создание главного окна
root = Tk()
root.title("Викторина")
root.geometry("400x300")

# Вопрос
question_label = Label(root, text="Почему утверждается что 10 мм пистолет более попудярный чем карабин хотя они встречаются с одинаковой частотой", font=("Arial", 12))
question_label.pack(pady=20)

# Кнопки с вариантами ответов
btn1 = Button(root, text="Потому что так задумали разрабы", command=lambda: btn_click(False))
btn1.pack(pady=5)

btn2 = Button(root, text="Ошибка разраба", command=lambda: btn_click(False))
btn2.pack(pady=5)

btn3 = Button(root, text="Потому что такой вопрос", command=lambda: btn_click(False))
btn3.pack(pady=5)

btn4 = Button(root, text="Потому что в довоенное время был популярен первый, а в пустоши иза легкой конструкции второй", command=lambda: btn_click(True))
btn4.pack(pady=5)

# Метка для результата
result_label = Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Запуск главного цикла
root.mainloop()