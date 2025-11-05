import customtkinter as customtkinter
from tkinter import ttk
import math
from random import choice

width = 800
height = 600
center = 200
x_increment = 1
x_factor = 0.04
y_amplitude = 240
freqAmp = 0.8

class StateBox(customtkinter.CTkFrame):
    def __init__(self, master, state):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = state
        self.checkboxes = []

        self.title = customtkinter.CTkLabel(self, text=self.title, corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.running = True
        self.title("my app")
        self.geometry(f'{width}x{height}')
        

        # grid config
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="fred")
        self.grid_rowconfigure((0), weight=1)
        self.grid_rowconfigure((1, 3), weight=2)
        self.grid_rowconfigure((2), weight=4)
        

        #Header
        header_frame = ttk.Frame(self)
        header_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan = 5)
        header_frame.grid_columnconfigure((0, 1, 2), weight=1, uniform="fred")
        header_frame.grid_rowconfigure((0), weight=1)

        self.label = ttk.Label(header_frame, text = "Sleep Stages", font = "Calibri 24")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan = 1)

        self.button = customtkinter.CTkButton(header_frame, text="Quit", command=self.close_app)
        self.button.grid(row=0, column=2, padx=10, pady=10, sticky="ew", columnspan = 1)


        #Display: Current Mode
        self.checkbox_frame = StateBox(self, "Awake")
        self.checkbox_frame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.checkbox_frame_2 = StateBox(self, "N1")
        self.checkbox_frame_2.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="ew")

        self.checkbox_frame_3 = StateBox(self, "N2")
        self.checkbox_frame_3.grid(row=1, column=2, padx=10, pady=(10, 0), sticky="ew")

        self.checkbox_frame_4 = StateBox(self, "N3")
        self.checkbox_frame_4.grid(row=1, column=3, padx=10, pady=(10, 0), sticky="ew")

        self.checkbox_frame_5 = StateBox(self, "REM")
        self.checkbox_frame_5.grid(row=1, column=4, padx=10, pady=(10, 0), sticky="ew")


        # Freq/Amp -> Return Bed rocking from FSM
        self.stage_var = customtkinter.StringVar()
        self.rocking_level_var = customtkinter.StringVar()
        self.display_text = customtkinter.StringVar()
        self.stages = ['awake', 'N1', 'N2', 'N3', 'REM']
        self.stage_index = 0

        #Display Bed Rocking: Graph
        self.update_stage()
        self.animate_sine()

        #Display Bed Rocking: Val
        self.label = ttk.Label(self, textvariable=self.display_text, font = "Calibri 24")
        self.label.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan = 3)

    # generate sine
    def animate_sine(self):
        """Animate a scrolling sine wave on the main thread."""
        self.canvas = customtkinter.CTkCanvas(self, width=width, height=400, bg="gray80")
        self.canvas.grid(row=2, column=0, padx=10, pady=10, sticky="ew", columnspan=5)
        self.canvas.create_line(0, center, width, center, fill="green")

        self.sin_line = self.canvas.create_line(0, center, 1, center, fill="blue")
        self.x_offset = 1
        self.speed = 5 
        self.delay = 20 

        self.amp = 0 
        self.speed = 0
        

        def draw_frame():
            if not self.running:
                return
            
            # amp interpolation
            diff_amp = float(self.rocking_level_var.get()) - self.amp
            self.amp += diff_amp * 0.05

            # speed interpolation
            diff_speed = self.target_speed - self.speed
            self.speed += diff_speed * 0.05
            print("current speed: ", self.speed )

            points = []
            for x in range(width):
                y = int(math.sin((x + self.x_offset) * x_factor) * (y_amplitude * self.amp)) + center
                points.extend([x, y])
            self.canvas.coords(self.sin_line, points)
            self.x_offset += self.speed
            # scheduling
            self.after(self.delay, draw_frame)

        draw_frame()
    
    # generate stage
    # def return_stage(self):
    #     stages = choice(['awake', 'N1', 'N2', 'N3', 'REM'])

    #     print(result)
    #     return result

    def update_stage(self):
        if not self.running:
                return
        
        # renew bg
        # self.stage_var.set(self.return_stage())
        self.checkbox_frame.configure(fg_color="gray80")
        self.checkbox_frame_2.configure(fg_color="gray80")
        self.checkbox_frame_3.configure(fg_color="gray80")
        self.checkbox_frame_4.configure(fg_color="gray80")
        self.checkbox_frame_5.configure(fg_color="gray80")

        stage = self.stages[self.stage_index]
        self.stage_index = (self.stage_index + 1) % len(self.stages)

        #update visuals
        if stage == "awake": 
            self.stage_var.set(stage)
            self.checkbox_frame.configure(fg_color="gray50")
            self.rocking_level_var.set(0.8)
            self.target_speed = 3
        if stage == "N1": 
            self.stage_var.set(stage)
            self.checkbox_frame_2.configure(fg_color="gray50")
            self.rocking_level_var.set(0.6)
            self.target_speed = 2.2
        if stage == "N2": 
            self.stage_var.set(stage)
            self.checkbox_frame_3.configure(fg_color="gray50")
            self.rocking_level_var.set(0.4)
            self.target_speed = 1.4
        if stage == "N3": 
            self.stage_var.set(stage)
            self.checkbox_frame_4.configure(fg_color="gray50")
            self.rocking_level_var.set(0.2)
            self.target_speed = 0.6
        if stage == "REM":
            self.stage_var.set(stage) 
            self.checkbox_frame_5.configure(fg_color="gray50")
            self.rocking_level_var.set(0.0)
            self.target_speed = 0
        
        # Actual Output from FSM -----------------------------------
        display_value = int(float(self.rocking_level_var.get()) * 10)
        self.display_text.set(f"Bed rocking level: {display_value}/8")
        self.after(5000, self.update_stage)

    def close_app(self):
        self.running = False
        self.destroy()

app = App()
app.mainloop()
