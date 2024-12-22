import tkinter as tk
from Classifier import load_and_predict
from Adding import adder
from save2csv import save_to_csv
from retrieve import retrieve_data
from Resched import rescheduler
from modify import modify_data_point
import spacy
from Delete import delete
from sub_remove import remove_entry
from tkinter import ttk
from ttkthemes import ThemedTk

model_name = "en_core_web_sm"
nlp = spacy.load(model_name)

def display():
    user_name = user_name_entry.get()
    display_commands(user_name)

def execute_command():
    
    user_name = user_name_entry.get()
    command = entry.get()

    
    if user_name and command and command != entry_placeholder:
 
        classification_result = load_and_predict(command)

        
        if classification_result == 0:
            date,time,user_found,events_found=adder(user_name,command,nlp)
            save_to_csv(date,time,user_found,events_found)
        elif classification_result == 1:
            date,time,ordinal=rescheduler(user_name, command,nlp)
            modify_data_point(user_name,ordinal,date,time)
        elif classification_result == 2:
            ordinal=delete(user_name, command,nlp)
            remove_entry(user_name,ordinal)

        entry.delete(0, tk.END)  

     
        display_commands(user_name)

def display_commands(user_name):
    
    
    listbox.delete(0, tk.END)

    
    commands = retrieve_data(user_name)
    for cmd in commands:
        listbox.insert(tk.END, cmd)


root = tk.Tk()
style = ttk.Style()
style.theme_use("clam")
root.title("Virtual Personal Assistant")
root.geometry("400x300")  


root.configure(bg="#2c3e50") 


user_name_placeholder = "Enter your name..."
user_name_entry = tk.Entry(root, width=30, font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50", relief=tk.FLAT)
user_name_entry.insert(0, user_name_placeholder)
user_name_entry.pack(pady=10)


def clear_user_name_placeholder(event):
    if user_name_entry.get() == user_name_placeholder:
        user_name_entry.delete(0, tk.END)
        user_name_entry.configure(fg="#2c3e50")  


user_name_entry.bind("<FocusIn>", clear_user_name_placeholder)


entry_placeholder = "Enter the command..."
entry = tk.Entry(root, width=30, font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50", relief=tk.FLAT)
entry.insert(0, entry_placeholder)
entry.pack(pady=5)


def clear_command_placeholder(event):
    if entry.get() == entry_placeholder:
        entry.delete(0, tk.END)
        entry.configure(fg="#2c3e50")  


entry.bind("<FocusIn>", clear_command_placeholder)


execute_button = tk.Button(root, text="Execute", command=execute_command, bg="#27ae60", fg="#ffffff", font=("Arial", 12), relief=tk.GROOVE)
execute_button.pack()

display_button = tk.Button(root, text="Show Commands", command=display, bg="#2980b9", fg="#ffffff", font=("Arial", 12), relief=tk.GROOVE)
display_button.pack()


listbox = tk.Listbox(root, width=50, height=8, font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50", relief=tk.FLAT)
listbox.pack(pady=10)

root.mainloop()
