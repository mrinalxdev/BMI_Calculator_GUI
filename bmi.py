import customtkinter as ctk
from settings import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color = GREEN)

        self.title('BMI Calculator')
        self.geometry('400x400')
        self.resizable(False, False)
        self.mainloop()

App()