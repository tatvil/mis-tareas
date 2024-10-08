import tkinter as tk
from tkinter import messagebox
import os

class SimpleToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mis tareas")
        self.root.geometry("400x500")
        self.root.config(bg="#0054a4")  # Color de fondo de la ventana
        
        # Lista de tareas
        self.tasks = []
        self.load_tasks()  # Cargar tareas desde el archivo
        
        # Interfaz de usuario
        self.title_label = tk.Label(root, text="Mis Tareas", font=("Arial", 18), fg="white", bg="#0054a4")
        self.title_label.pack(pady=10)
        
        self.task_entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="white", fg="#0054a4", activebackground="#0054a4", activeforeground="white")
        self.add_button.pack(pady=5)
        
        self.tasks_listbox = tk.Listbox(root, width=50, height=10, bg="white", fg="#0054a4")
        self.tasks_listbox.pack(pady=10)
        
        self.remove_button = tk.Button(root, text="Borrar tarea", command=self.remove_task, bg="white", fg="#0054a4", activebackground="#0054a4", activeforeground="white")
        self.remove_button.pack(pady=5)
        
        self.update_task_list()
    
    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
            self.save_tasks()  # Guardar al archivo
        else:
            messagebox.showwarning("Error", "Introduzca una tarea.")
    
    def remove_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_list()
            self.save_tasks()  # Guardar los cambios al archivo
        except IndexError:
            messagebox.showwarning("Error", "Seleccione la tarea a borrar.")
    
    def update_task_list(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

    def save_tasks(self):
        """Guardar las tareas en un archivo de texto."""
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
    
    def load_tasks(self):
        """Cargar las tareas desde el archivo de texto."""
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                self.tasks = file.read().splitlines()

# Ejecutar el programa
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleToDoApp(root)
    root.mainloop()
