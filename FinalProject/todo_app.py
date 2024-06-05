import tkinter as tk
from tkinter import ttk
import random
import time

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.tasks = []
        self.completed_tasks = 0
        
        self.setup_ui()

    def setup_ui(self):
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.task_entry = ttk.Entry(self.frame, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = ttk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.progress = ttk.Progressbar(self.frame, orient="horizontal", length=300, mode="determinate")
        self.progress.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.tasks_frame = ttk.Frame(self.frame)
        self.tasks_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.tasks_listbox = tk.Listbox(self.tasks_frame, width=50, height=15)
        self.tasks_listbox.pack(side="left", fill="y")

        self.scrollbar = ttk.Scrollbar(self.tasks_frame, orient="vertical", command=self.tasks_listbox.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.tasks_listbox.config(yscrollcommand=self.scrollbar.set)
        
        self.complete_button = ttk.Button(self.frame, text="Complete Task", command=self.complete_task)
        self.complete_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.update_progress()

    def complete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.tasks_listbox.delete(selected_task_index)
            self.completed_tasks += 1
            self.update_progress()
            if self.completed_tasks == len(self.tasks):
                self.show_congratulations()

    def update_progress(self):
        total_tasks = len(self.tasks)
        if total_tasks > 0:
            self.progress['value'] = (self.completed_tasks / total_tasks) * 100

    def show_congratulations(self):
        confetti_window = tk.Toplevel(self.root)
        confetti_window.geometry("500x400")
        confetti_window.title("Congratulations!")
        
        canvas = tk.Canvas(confetti_window, bg='white', width=500, height=400)
        canvas.pack()

        self.run_confetti(canvas)
        confetti_label = ttk.Label(confetti_window, text="Congratulations! You completed all tasks!", font=("Helvetica", 16))
        confetti_label.pack(pady=20)

    def run_confetti(self, canvas):
        colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan']
        for _ in range(100):
            x1 = random.randint(0, 500)
            y1 = random.randint(0, 400)
            x2 = x1 + random.randint(5, 20)
            y2 = y1 + random.randint(5, 20)
            color = random.choice(colors)
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
        self.root.after(100, self.clear_confetti, canvas)

    def clear_confetti(self, canvas):
        canvas.delete("all")
        self.run_confetti(canvas)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
