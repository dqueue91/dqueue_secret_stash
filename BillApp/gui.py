import customtkinter as ctk
from tkinter import messagebox
import os
from pathlib import Path
import main
import bills

def close_callback(self):
#first variable is window title, second variable is window text
    answer = messagebox.askyesno("Confirm exit", "Are you sure you want to exit?")
    if answer:
        app.destroy()

#main screen
class main_menu(ctk.CTkFrame):
    # add file, edit file, delete
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.add_file = ctk.CTkButton(self, text="Add File", command=lambda: switch_frame(file_menu))
        self.add_file.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.close = ctk.CTkButton(self, text="Exit", command=lambda: close_callback(self))
        self.close.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        #scrollable frame
        scroll_frame = ctk.CTkScrollableFrame(self, width=720, height=500)
        scroll_frame.grid(row=0, column=0, padx=10, pady=10, sticky="new")
        #chooses Documents/Finances folder
        p = main.p
        files = os.listdir(p)
        # list files and make selectable by clicking
        for i, f in enumerate(files):
            label = ctk.CTkLabel(scroll_frame, text=f, cursor="hand2")
            label.grid(row=i,column=0, padx=10, pady=5)
            label.bind("<Button-1>", lambda event, filename=f: self.on_file_click(filename))

    def view_file_callback(self):
        self.switch_frame(file_menu)

  

    def on_file_click(self, filename):
       bills.read_file()


#after clicking add file button
class file_menu(ctk.CTkFrame):
    # edit file, save, close
    def __init__(self, master, switch_frame):
        super().__init__(master)
        #list to store all entries before saving
        self.entries = {}
        #gives the user ability to save the file under a particular name
        self.file_name = ctk.CTkEntry(self, placeholder_text="File Name")
        self.file_name.grid(row=0, column=0, padx=10, pady=(2,2), sticky="nw")
        #since "File Name" is row 0, set row beneath it (row 1) so we can iterate through our dictionary and not overwrite row 0
        row = 1
        #entry box with dict keys as placeholder text
        for i, name in enumerate(main.keynames):
            entry = ctk.CTkEntry(self, placeholder_text=name.capitalize())
            entry.grid(row=row, column=0, padx=10, pady=(5, 5), sticky= "nw")
            self.entries[name] = entry
            row+=1
            
        self.grid_rowconfigure(row, weight=1, minsize=30)
        self.grid_columnconfigure(0, weight=1)
        #save file, go to previous page and close program buttons
        self.save = ctk.CTkButton(self, text="Save", command=self.save_file)
        self.save.grid(row=(row + 2), column=0, padx=10, pady=10, sticky="w")
        self.back = ctk.CTkButton(self, text="Previous Page", command=lambda: switch_frame(main_menu))
        self.back.grid(row=(row + 3), column=0, padx=10, pady=10, sticky="w")
        self.close = ctk.CTkButton(self, text="Exit", command=lambda: close_callback(self))
        self.close.grid(row=(row + 4), column=0, padx=10, pady=10, sticky="w")

    def edit_file(self):
        pass

    def create_file(self):
        #transfers 1st entry, file name, to main file for backend to use and write
        main.file_name = self.file_name.get()
        if not main.file_name.endswith(".csv"):
            main.file_name += ".csv"
        main.file_loc = str(f"{main.p}/{main.file_name}")
        main.f = main.p.joinpath(main.file_name)
        return main.file_name
        return  main.file_loc
        return main.f

    def save_file(self):
        self.create_file()
        row = {name: entry.get() for name, entry in self.entries.items()}
        main.names.append(row)
        #clears placeholder text but not stored data
        for entry in self.entries.values():
            entry.delete(0, "end")
        #check if values are being stored
        #print(f"Names: {main.names}")
        bills.file_handler()

        
        
  
    def close_callback(self):
        #first variable is window title, second variable is window text
        answer = messagebox.askyesno("Confirm exit", "Are you sure you want to exit?")
        if answer:
            app.destroy()




class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Bill Tracker")
        self.geometry("720x500")
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