import tkinter as tk
from Classifier import load_and_predict
from Adding import adder
from save2csv import save_to_csv
from retrieve import retrieve_data
from Resched import rescheduler
from modify import modify_data_point
from Delete import delete
from sub_remove import remove_entry
import spacy
from speech1 import speech_to_text
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import messagebox
import csv
import speech_recognition as sr
def gui(user_name):
    def display():
        
        display_commands(user_name)

    def execute_command():
        
        command = entry.get()

        

        if user_name and command and command != entry_placeholder and command!="":
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
        for widget in root.winfo_children():
                if isinstance(widget, tk.Frame):
                    widget.destroy()
        commands = retrieve_data(user_name)
        print(commands)
        
        
        for cmd in commands:
            primary_key, date, time, events, along_with = cmd
            events = events.strip("[]").replace("'", "")
            along_with = along_with.strip("[]").replace("'", "").split(', ')

           
            if len(along_with) == 1:
                result_string = f"{date} {time} {events}"
            else:
                result_string = f"{date} {time} {events} between {', '.join(along_with[:-1])} and {along_with[-1]}"

            create_task_block(result_string)

    def clear_command_placeholder(event):
        if entry.get() == entry_placeholder:
            entry.delete(0, tk.END)
            entry.configure(fg="#2c3e50")



    root = tk.Tk()
    root.title("Virtual Personal Assistant")
    root.geometry("800x800")
    root.configure(bg="#333333")
    model_name = "en_core_web_sm"
    nlp = spacy.load(model_name)



    entry_placeholder = "Enter the command..."
    entry = tk.Entry(root, width=30,font=("Arial", 12), bg="#F0FFF0", fg="#2c3e50", relief=tk.FLAT)
    entry.insert(0, entry_placeholder)
    entry.pack(pady=20)


    entry.bind("<FocusIn>", clear_command_placeholder)

    def speech_recognition():
        text=speech_to_text()
        entry.delete(0, tk.END)
        entry.configure(fg="#2c3e50")
        entry.insert(0,text)

    speech_recognition_button = tk.Button(root, text="Speech Recognition", command=speech_recognition, bg="#e74c3c", fg="#ffffff", font=("Arial", 12), relief=tk.GROOVE)
    speech_recognition_button.pack(pady=10)

    execute_button = tk.Button(root, text="Execute", command=execute_command, bg="#27ae60", fg="#ffffff", font=("Arial", 12), relief=tk.GROOVE)
    execute_button.pack(pady=5)

    display_button = tk.Button(root, text="Show Commands", command=display, bg="#2980b9", fg="#ffffff", font=("Arial", 12), relief=tk.GROOVE)
    display_button.pack(pady=5)
  
    def create_task_block(command):
   
        task_frame = tk.Frame(root, bg="#ecf0f1", relief=tk.RAISED, bd=2)
        task_frame.pack(pady=5, padx=10, fill=tk.X)

      
        task_label = tk.Label(task_frame, text=command, font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50")
        task_label.pack(padx=10, pady=5, side=tk.LEFT)

    root.mainloop()
def login():
    username = username_entry.get()
    password = password_entry.get()

    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2 and row[0] == username and row[1] == password:
                messagebox.showinfo("Login Successful", f"Welcome, {username}!")
                window.destroy()
                gui(username)
                return

    messagebox.showerror("Login Failed", "Invalid username or password")

def open_registration_window():
    registration_window = tk.Toplevel(window)
    registration_window.title("Registration")
    registration_window.geometry('440x440')
    registration_window.configure(bg='#333333')

    def signin():
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()
        new_email = new_email_entry.get()

        if not new_username or not new_password:
            messagebox.showerror("Invalid Credentials", "Please provide both username and password.")
            return

        with open("users.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([new_username, new_password,new_email])

        messagebox.showinfo("Sign Up Successful", "Account created successfully!")
        registration_window.destroy()

    registration_frame = tk.Frame(registration_window, bg='#333333')

    new_username_label = tk.Label(registration_frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    new_username_entry = tk.Entry(registration_frame, font=("Arial", 16))
    new_password_label = tk.Label(registration_frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    new_password_entry = tk.Entry(registration_frame, show="*", font=("Arial", 16))
    new_email_label = tk.Label(registration_frame, text="Email", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    new_email_entry = tk.Entry(registration_frame, font=("Arial", 16))
    signin_button = tk.Button(registration_frame, text="Sign In", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=signin)

    new_username_label.grid(row=0, column=0)
    new_username_entry.grid(row=0, column=1, pady=20)
    new_password_label.grid(row=1, column=0)
    new_password_entry.grid(row=1, column=1, pady=20)
    new_email_label.grid(row=2, column=0)
    new_email_entry.grid(row=2, column=1, pady=20)
    signin_button.grid(row=3, column=0, columnspan=2, pady=10)

    registration_frame.pack()


window = tk.Tk()
window.title("Login form")
window.geometry('440x440')
window.configure(bg='#333333')

frame = tk.Frame(window, bg='#333333')

login_label = tk.Label(frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tk.Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tk.Entry(frame, font=("Arial", 16))
password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
password_label = tk.Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tk.Button(frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)
register_button = tk.Button(frame, text="I want to register", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=open_registration_window)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=10)
register_button.grid(row=4, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()


