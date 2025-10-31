import customtkinter as customtkinter
from tkinter import ttk
class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x900")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = MyCheckboxFrame(self, "Title 1", values=["value 1", "value 2", "value 3"])
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.checkbox_frame_2 = MyCheckboxFrame(self, "Title 2", values=["value 4", "value 5", "value 6"])
        # self.checkbox_frame_2.configure(fg_color="transparent")
        self.checkbox_frame_2.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan = 2)

    def button_callback(self):
        print("checked checkboxes:", self.checkbox_frame.get())
        print("checked checkboxes:", self.checkbox_frame_2.get())

app = App()
app.mainloop()

# import customtkinter as ctk
# from tkinter import ttk
# import fsm
# import mock_data
# # from tkinter import ttk


# def convert():
#     print("convert")


# def submitToFSM():
#     fsm.go(entry.get())


# app = ctk.CTk()
# app.title("Demo")
# app.geometry("600x600")
    

# #Quit
# quit_button = ctk.CTkButton(master = app, text = "Quit", corner_radius=32, hover_color="#4158D0", command=app.destroy)
# quit_button.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

# #Title
# title_label = ttk.Label(master = app, text = "Sleep Stages", font = "Calibri 24")
# title_label.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

# #info field
# info_frame = ttk.Frame(master = app)
# sleep_stage_Awake = ttk.Label(master = info_frame, text = "Awake", font = "Calibri 16")
# sleep_stage_N1 = ttk.Label(master = info_frame, text = "N1", font = "Calibri 16")
# sleep_stage_N2 = ttk.Label(master = info_frame, text = "N2", font = "Calibri 16")
# sleep_stage_N3 = ttk.Label(master = info_frame, text = "N3", font = "Calibri 16")
# sleep_stage_REM = ttk.Label(master = info_frame, text = "REM", font = "Calibri 16")
# # sleep_stage_Awake.pack(side = "left", padx = 10)
# # sleep_stage_N1.pack(side = "left", padx = 10)
# # sleep_stage_N2.pack(side = "left", padx = 10)
# # sleep_stage_N3.pack(side = "left", padx = 10)
# # sleep_stage_REM.pack(side = "left", padx = 10)
# # info_frame.pack(pady = 10)


# # Input field
# input_frame = ttk.Frame(master = app)
# entry = ctk.CTkEntry(master = input_frame, placeholder_text="Type anything...")
# submit = ctk.CTkButton(master = input_frame, text = "Submit", command = submitToFSM)
# # entry.pack(side = "left", padx = 10)
# # submit.pack(side = "left", padx = 10)
# # input_frame.pack(pady = 10)

# #bed rocking frequency
# title_label = ttk.Label(master = app, text = "Frequency", font = "Calibri 16")
# # title_label.pack(pady = 5)

# app.mainloop()    






# #instance of the Tk class, which initializes Tk and 
# #creates its associated Tcl interpreter

# #root window, which serves as the main window of the application
# root = Tk()

# style = ttk.Style()
# style.configure("Red.TButton", foreground="red", font=("Arial", 14))


# #creates a frame widget, which in this case will 
# #contain a label and a button 
# frm = ttk.Frame(root, padding=10) # frame is fit inside the root window
# frm.grid()

# #label widget -> static text string; col 0 
# # & buttom with destroy cmd; col1
# label = ttk.Label(frm, text="Hello World!")
# # label.grid(column=0, row=0)
# label.pack()
# label.pack(side="left", ipady="400px")

# btn = ttk.Button(frm, text="Quit", command=root.destroy, style="Red.TButton")
# btn.pack()                     # defaults to side = "top"
# btn.pack(fill="x", ipady="40px")
# btn.pack(expand=1)



# # puts everything on the display, and responds to user input
# root.mainloop()

#