import customtkinter as ctk
from settings import *

class App(ctk.CTk):
    def __init__(self):
        # Window Setup 
        super().__init__(fg_color = GREEN)
        self.title('BMI Calculator')
        self.geometry('600x600')
        self.resizable(False, False)

        # Layout Setup 
        self.columnconfigure(0, weight = 1)
        self.rowconfigure((0, 1, 2, 3), weight= 1, uniform = 'a')

        # Widget Setup 
        ResultText(self)
        WeightInput(self)
        HeightInput(self)
        UnitSwitcher(self)

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

        # Text Setup
        font = ctk.CTkFont(family = FONT, size = INPUT_FONT_SIZE)
        label = ctk.CTkLabel(self, text = '70kg', text_color= BLACK, font = font)
        label.grid(row = 0, column = 2)

        # Buttons Setup 
        minus_button = ctk.CTkButton(self, text='-', font = font, text_color = BLACK, fg_color= LIGHT_GRAY, hover_color = GRAY, corner_radius= BUTTON_CORNER_RADIUS)
        minus_button.grid(row = 0, column = 0, sticky = 'ns', padx = 8, pady= 8)
        
        plus_button = ctk.CTkButton(self, text='+', font = font, text_color = BLACK, fg_color= LIGHT_GRAY, hover_color = GRAY, corner_radius= BUTTON_CORNER_RADIUS)
        plus_button.grid(row = 0, column = 4, sticky = 'ns', padx = 8, pady= 8)

        small_plus_button = ctk.CTkButton(self, text='+', font = font, text_color = BLACK, fg_color= LIGHT_GRAY, hover_color = GRAY, corner_radius= BUTTON_CORNER_RADIUS)
        small_plus_button.grid(row = 0, column = 3, padx = 4, pady= 4)
        
        small_minus_button = ctk.CTkButton(self, text='-', font = font, text_color = BLACK, fg_color= LIGHT_GRAY, hover_color = GRAY, corner_radius= BUTTON_CORNER_RADIUS)
        small_minus_button.grid(row = 0, column = 1, padx = 4, pady= 4)

class HeightInput(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master= parent, fg_color = WHITE)
        self.grid(row = 3, column = 0, sticky = 'nsew', padx = 10, pady = 10)

        # Widgets Setup 
        slider = ctk.CTkSlider( master = self, 
                               button_color= GREEN, 
                               button_hover_color= GRAY, 
                               progress_color=GREEN, 
                               fg_color = LIGHT_GRAY)
        slider.pack(side= 'left', fill = 'x', expand = True, padx = 10,pady =10 )
        output_text = ctk.CTkLabel(self, text='1.80m', text_color= BLACK, 
                                   font = ctk.CTkFont(family = FONT, 
                                                      size = INPUT_FONT_SIZE))
        output_text.pack(side= 'left', padx=10, pady=10)

class UnitSwitcher(ctk.CTkLabel):
    def __init__ (self, parent):
        super().__init__(master = parent, 
                         text='metric', 
                         text_color= DARK_GREEN, 
                         font= ctk.CTkFont(family = FONT, 
                                           size= SWITCH_FONT_SIZE, 
                                           weight= 'bold'))
        self.place(relx = 0.98, rely = 0.01, anchor = 'ne')

if __name__ == '__main__':
    App()
    