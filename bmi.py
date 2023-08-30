import customtkinter as ctk
from settings import *

class App(ctk.CTk):
    def __init__(self):
        # Window Setup 
        super().__init__(fg_color = GREEN)
        self.title('BMI Calculator')
        self.geometry('400x400')
        self.resizable(False, False)

        # Layout Setup 
        self.columnconfigure(0, weight = 1)
        self.rowconfigure((0, 1, 2, 3), weight= 1, uniform = 'a')

        # Widget Setup 
        ResultText(self)
        WeightInput(self)

        self.mainloop()

class ResultText(ctk.CTkLabel):
    def __init__(self, parent):
        font = ctk.CTkFont(family = FONT, size = MAIN_TEXT_SIZE, weight= 'bold')
        super().__init__(master = parent, text=22.5, font = font, text_color = WHITE)
        self.grid(column = 0, row = 0, rowspan = 2, sticky = 'nsew')

class WeightInput(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master= parent, fg_color= WHITE)
        self.grid(column = 0 , row = 2, sticky = 'nsew', padx = 10, pady = 10)

        # Layout for Weight Input
        self.rowconfigure(0, weight = 1, uniform= 'b')
        self.columnconfigure(0, weight = 2, uniform= 'b')
        self.columnconfigure(1, weight = 1, uniform= 'b')
        self.columnconfigure(2, weight = 3, uniform= 'b')
        self.columnconfigure(3, weight = 1, uniform= 'b')
        self.columnconfigure(4, weight = 2, uniform= 'b')

        # Buttons Setup
        font = ctk.CTkFont(family = FONT, size = INPUT_FONT_SIZE)
        label = ctk.CTkLabel(self, text = '70kg', text_color= BLACK, font = font)
        label.grid(row = 0, column = 2)


if __name__ == '__main__':
    App()
    