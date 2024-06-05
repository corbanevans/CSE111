import pytest
from todo_app import ToDoApp
import tkinter as tk
from tkinter import ttk
import threading

@pytest.fixture
def app():
    root = tk.Tk()
    app = ToDoApp(root)
    return app

def test_add_task(app):
    app.task_entry.insert(0, "Test Task")
    app.add_task()
    
    assert "Test Task" in app.tasks
    assert app.tasks_listbox.get(0) == "Test Task"

def test_complete_task(app):
    app.tasks = ["Task 1", "Task 2"]
    app.completed_tasks = 0
    app.tasks_listbox.insert(0, "Task 1")
    app.tasks_listbox.insert(1, "Task 2")
    
    app.tasks_listbox.selection_set(0)
    app.complete_task()
    
    assert app.completed_tasks == 1
    assert app.progress['value'] == 50
    assert "Task 1" not in app.tasks_listbox.get(0, tk.END)

    app.tasks_listbox.selection_set(0)
    app.complete_task()
    
    assert app.completed_tasks == 2
    assert app.progress['value'] == 100

def test_progress_bar(app):
    app.tasks = ["Task 1", "Task 2", "Task 3"]
    app.completed_tasks = 0
    app.update_progress()
    
    assert app.progress['value'] == 0
    
    app.completed_tasks = 1
    app.update_progress()
    
    assert app.progress['value'] == (1 / 3) * 100
    
    app.completed_tasks = 2
    app.update_progress()
    
    assert app.progress['value'] == (2 / 3) * 100
    
    app.completed_tasks = 3
    app.update_progress()
    
    assert app.progress['value'] == 100

def run_app():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    threading.Thread(target=run_app).start()
    pytest.main()