import customtkinter as ctk
from tkinter import messagebox
import os
from pathlib import Path
import csv


#main screen
class main_menu(ctk.CTkFrame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.view_file = ctk.CTkButton(self, text="View Files", command=lambda: switch_frame(file_menu))
        self.view_file.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.close = ctk.CTkButton(self, text="Exit", command=self.close_callback)
        self.close.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    def view_file_callback(self):
        self.switch_frame(file_menu)

    def add_file_callback(self):
        print("Adding file")
  
    def close_callback(self):
        #first variable is window title, second variable is window text
        answer = messagebox.askyesno("Confirm exit", "Are you sure you want to exit?")
        if answer:
            app.destroy()


#after clicking view file button
class file_menu(ctk.CTkFrame):
    # add file, edit file, delete
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.add_file = ctk.CTkButton(self, text="Add File", command=self.add_file_callback)
        self.add_file.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.back = ctk.CTkButton(self, text="Previous Page", command=lambda: switch_frame(main_menu))
        self.back.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.close = ctk.CTkButton(self, text="Exit", command=self.close_callback)
        self.close.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        #scrollable frame
        scroll_frame = ctk.CTkScrollableFrame(self, width=900, height=800)
        scroll_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        #chooses Documents/Finances folder
        p = Path('/home/wiggly/Documents/Finances')
        files = os.listdir(p)
        # list files and make selectable by clicking
        for i, f in enumerate(files):
            label = ctk.CTkLabel(scroll_frame, text=f, cursor="hand2")
            label.grid(row=i,column=0, padx=10, pady=10)
            label.bind("<Button-1>", lambda event, filename=f: self.on_file_click(filename))

    def add_file_callback(self):
        print("Adding file")

  
    def close_callback(self):
        #first variable is window title, second variable is window text
        answer = messagebox.askyesno("Confirm exit", "Are you sure you want to exit?")
        if answer:
            app.destroy()

    def on_file_click(self, filename):
        with open(filename, 'r', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile, fieldnames = fieldnames)
                #print("Name     ","Price    ", "Date")
                
            for i in csv_reader:
                name = i["Name"]
                price = i["Price"]
                date = i["Date"]
                total = total + float(price)
                print(f"{name} {price} due on the {date}")
            print(f"Monthly expenses are: {total}")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Bill Tracker")
        self.geometry("1080x900")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.current_frame = None
        self.switch_frame(main_menu)

    def switch_frame(self, frame_class):
        #Destroy current frame and replace with new one.
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self, self.switch_frame)
        self.current_frame.grid(row=0, column=0, sticky="nsew")
        

app = App()
app.mainloop()