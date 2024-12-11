import tkinter as tk

def on_button_click_add():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        temp_list = list(task_listBox.get(0, tk.END))
        temp_list = [item + '\n' for item in temp_list]
        with open("tasks.txt", "w") as file:
            file.writelines(temp_list)

def on_button_click_del():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)
        #  Обновление файла с задачами
        temp_list = list(task_listBox.get(0, tk.END))
        temp_list = [item + '\n' for item in temp_list]
        with open("tasks.txt", "w") as file:
            file.writelines(temp_list)

def on_button_click_done():
    selected_task = task_listBox.curselection()
    if selected_task:
        done_listBox.insert(tk.END, task_listBox.get(selected_task))
        task_listBox.delete(selected_task) # удаляем выбранный элемент из списка
        #  Обновление файла с задачами
        temp_list = list(task_listBox.get(0, tk.END))
        temp_list = [item + '\n' for item in temp_list]
        with open("tasks.txt", "w") as file:
            file.writelines(temp_list)
        #  Обновление файла с выполнеными задачами
        temp_list = list(done_listBox.get(0, tk.END))
        temp_list = [item + '\n' for item in temp_list]
        with open("done.txt", "w") as file:
            file.writelines(temp_list)
# Очистка истории
def on_button_click_hist():
    with open("done.txt", "w") as file:
        file.write("")
        done_listBox.delete(0, tk.END)

root = tk.Tk()
root.title('Управление задачами')
root.geometry('300x620')

label = tk.Label(root, text='Новая задача:')
task_entry = tk.Entry(root)
label_new = tk.Label(root, text='Актуальные задачи:')
label_done = tk.Label(root, text='Выполненые задачи:')

button_add = tk.Button(root, text="Добавить задачу ->", command=on_button_click_add)
delete_button = tk.Button(root, text="Удалить задачу", command=on_button_click_del)
done_button = tk.Button(root, text="Задача выполнена", command=on_button_click_done)
history_button = tk.Button(root, text="Очистка истории", command=on_button_click_hist)
# Загрузка сохранённых файлов
var1 = tk.StringVar()
with open("tasks.txt", "r") as tasks:
    var1.set(tasks.read())

var2 = tk.StringVar()
with open("done.txt", "r") as done:
    var2.set(done.read())
#  Отрисовка интерфейса
task_listBox = tk.Listbox(root, listvariable=var1, height=10, width=50, bg="gold")
done_listBox = tk.Listbox(root, listvariable=var2, height=10, width=50, bg="SeaGreen1")

label.pack(pady=5)
task_entry.pack(pady=5)
button_add.pack(pady=5)
delete_button.pack(pady=5)
done_button.pack(pady=5)
label_new.pack(pady=3)
task_listBox.pack(pady=5)
label_done.pack(pady=3)
done_listBox.pack(pady=5)
history_button.pack(pady=5)

root.mainloop()