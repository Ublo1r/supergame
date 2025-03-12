import tkinter as tk
from tkinter import messagebox # активація модулів

def manage_task(action):
    if action == 'add':
        task = entry.get()
        if task: listbox.insert(tk.END, task); entry.delete(0, tk.END) # добавити фільм
    elif action == 'delete':
        try: listbox.delete(listbox.curselection()[0])
        except IndexError: messagebox.showwarning("Помилка", "Оберіть завдання!") # видалити фільм
    elif action == 'view':
        tasks = listbox.get(0, tk.END)
        messagebox.showinfo("Список", "\n".join(f"{i+1}. {t}" for i, t in enumerate(tasks)) if tasks else "Список порожній!") # переглянути список

root = tk.Tk(); root.title("Список фільмів"); root.geometry("300x300")
entry = tk.Entry(root, width=30); entry.pack(pady=5)
listbox = tk.Listbox(root, width=40, height=10); listbox.pack(pady=5)
for txt, cmd in zip(["Додати", "Видалити", "Переглянути"], ["add", "delete", "view"]):
    tk.Button(root, text=txt, command=lambda c=cmd: manage_task(c)).pack()
root.mainloop() # створення вікна