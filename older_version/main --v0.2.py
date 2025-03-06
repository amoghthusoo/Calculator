''' 
PROJECT  © 2020 Amogh Thusoo
VERSION : 0.2
COMPILED THROUGH : WINDOWS 8 : ORACLE VIRTUAL BOX : LINUX OS : UBUNTU 20.04 LTS (VIRTUAL MACHINE)


CAUTION :- IF YOU ARE USING THIS APP ON WINDOWS, MACOS OR LINUX, THEN MANUALLY SET THE 'Windows_Mode' TO 'True' FOR PRESERVING THE DIMENSIONS
OF THE APP WINDOW 
'''
Windows_Mode = True

# SOURCE CODE 

# IMPORTING NECESSARY MODULES FROM KIVY, PLAYSOUND AND THREADING LIBRARY

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader



# MIXING DIFFERENT COLOURS

black = [0, 0, 0, 1]
grey_for_window = [40/255, 40/255, 40/255, 1]
grey_for_buttons = [127.5/255, 127.5/255, 127.5/255, 1] 
white = [1, 1, 1, 1]
purple = [128/255, 0/255, 128/255, 1]
dark_purple = [64/255, 0/255, 64/255, 1]  
pink = [255/255, 20/255, 147/255, 1]
dark_pink = [127.5/255, 10/255, 73.5/255, 1]
orange = [255/255, 140/255, 0/255, 1]
dark_orange = [127.5/255, 70/255, 0/255, 1] 
green = (173/255, 255/255, 47/255, 1)
dark_green = [86.5/255, 127.5/255, 23.5/255, 1]
red = [1, 0, 0, 1] 
yellow = [1, 1, 0, 1]


# CHANGING BACKGROUND COLOUR OF KIVY WINDOW 

Window.clearcolor = grey_for_window


# RESIZING KIVY WINDOW TO ANDROID DIMENSIONS

if Windows_Mode == True:
    Window.size = (365, 650)


# FIXING UNIFORM TEXT SIZE AND FONT STYLE

text_size = '35sp'
fontello_backspace_text_size = '35sp'
fontello_text_size = '25sp'
on_press_fontello_text_size = '20sp'
small_output_size = '25sp'
output_size = '45sp'
message_size = '30sp'
on_press_text_size = '30sp'
font_style_gunplay = 'App_Data/Fonts/gunplay.ttf'
font_style_fontello = 'App_Data/Fonts/fontello.ttf'


# CREATING VARIABLES FOR STORING THE STATE OF EQUAL TO BUTTON 

equal_memory = False


# DEFINING MAIN CLASS APP

class Calculator(App):

    
    # LAYOUT HOLDING APPLICATION DETAILS
    
    def Info(self):

        self.app_name = Button(font_name = font_style_gunplay, text = 'Calculator' , background_normal = '', background_down = '', background_color = dark_purple, color = white, font_size = '30sp')
        self.developer = Button(text = '\u00a9' + ' 2020 Amogh Thusoo', background_normal = '', background_down = '', background_color = dark_purple, color = white, font_size = '14sp')
        self.version = Button(text = 'Version : 0.2', halign = 'left', background_normal = '', background_down = '', background_color = dark_purple, color = white, font_size = '14sp')
        self.false_button_1 = Button(background_normal = '', background_down = '', size_hint = (0.08,1), background_color = dark_purple)
        self.false_button_2 = Button(background_normal = '', background_down = '', size_hint = (1,0.5), background_color = dark_purple)
        self.false_button_3 = Button(background_normal = '', background_down = '', size_hint = (0.5,1), background_color = dark_purple)
        self.false_button_4 = Button(background_normal = '', background_down = '', size_hint = (0.08,1), background_color = dark_purple)
        self.false_button_5 = Button(background_normal = '', background_down = '', size_hint = (0.08,1), background_color = dark_purple)
        self.false_button_6 = Button(background_normal = '', background_down = '', size_hint = (0,0), background_color = dark_purple)
        self.false_button_7 = Button(background_normal = '', background_down = '', size_hint = (1,0.4), background_color = dark_purple)
        self.false_button_8 = Button(background_normal = '', background_down = '', size_hint = (0.35,1), background_color = dark_purple)
        self.false_button_9 = Button(background_normal = '', background_down = '', size_hint = (0.01,1), background_color = dark_purple)
        
        
        self.boxl_6 = BoxLayout()
        
        self.boxl_6.add_widget(self.false_button_9)
        
        self.boxl_6.add_widget(self.developer)

        self.boxl_5 = BoxLayout(orientation = 'vertical')

        self.boxl_5.add_widget(self.boxl_6)
        self.boxl_5.add_widget(self.false_button_7)

        self.boxl_4 = BoxLayout()
        
        self.boxl_4.add_widget(self.app_name)
        self.boxl_4.add_widget(self.false_button_6)
        
        self.boxl_3 = BoxLayout(orientation = 'vertical')

        self.boxl_3.add_widget(self.false_button_2)
        self.boxl_3.add_widget(self.version)
        
        self.boxl_2 = BoxLayout()

        self.boxl_2.add_widget(self.false_button_3)
        self.boxl_2.add_widget(self.false_button_8)
        self.boxl_2.add_widget(self.boxl_3)
        
        self.boxl_1 = BoxLayout(orientation = 'vertical')
        
        self.boxl_1.add_widget(self.boxl_5)
        self.boxl_1.add_widget(self.boxl_2)
        
        self.supl = BoxLayout(size_hint = (1, 0.3), padding = ('0sp', '0sp', '0sp', '0sp'))

        self.supl.add_widget(self.boxl_4)
        
        self.supl.add_widget(self.false_button_5)
        self.supl.add_widget(self.false_button_4)
        self.supl.add_widget(self.false_button_1)
        
        self.supl.add_widget(self.boxl_1)

        return self.supl 

    
    # LAYOUT HOLDING OUTPUT SCREEN
    
    def Output_Screen(self):
        self.message_display = Button(font_size = message_size, background_normal = '', background_down = '', size_hint = (1,1), background_color = black, color = yellow, font_name = font_style_gunplay)
        self.out = Button(text = '0', color = white, font_size = output_size , background_normal = '', background_down = '', background_color = black) 

        self.bl = BoxLayout(orientation = 'vertical', padding = ('0sp', '0sp', '0sp', '10sp'), size_hint = (1, 0.4))

        self.bl.add_widget(self.message_display)
        self.bl.add_widget(self.out)
        
        return self.bl    


    # LAYOUT HOLDING ALL BUTTONS EXCEPT '0', '.' AND '='
    
    def Middle_Box(self):
    
        self.btn1 = Button(font_name = font_style_gunplay, text = 'C', background_normal = '', background_color = green, font_size = text_size, color = black, on_press = self.clear, background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn1), always_release = True)
        self.btn2 = Button(font_name = font_style_gunplay, text = '+/-', background_normal = '', background_color = pink, font_size = text_size, color = black, on_press = self.plus_or_minus, background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn2), always_release = True)
        self.btn3 = Button(font_name = font_style_fontello, text = '\ue9d4', background_normal = '', color = black, font_size = fontello_backspace_text_size, background_color = pink, on_press = self.backspace, background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn3), always_release = True)
        self.btn4 = Button(font_name = font_style_fontello, text = '\ue9dc', background_normal = '', background_color = white, font_size = fontello_text_size , color = purple, on_press = lambda x: self.numeric_operator_button_press('÷', self.btn4), background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn4), always_release = True)
        self.btn5 = Button(font_name = font_style_gunplay, text = '7', background_normal = '', background_color = orange, font_size = text_size, color = black, on_press = lambda x: self.numeric_operator_button_press('7', self.btn5), background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn5), always_release = True)
        self.btn6 = Button(font_name = font_style_gunplay, text = '8', background_normal = '', background_color = orange, font_size = text_size, color = black, on_press = lambda x: self.numeric_operator_button_press('8', self.btn6), background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn6), always_release = True)
        self.btn7 = Button(font_name = font_style_gunplay, text = '9', background_normal = '', background_color = orange, font_size = text_size, color = black, on_press = lambda x: self.numeric_operator_button_press('9', self.btn7), background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn7), always_release = True)
        self.btn8 = Button(font_name = font_style_fontello, text = '\ue9d2', background_normal = '', background_color = white, font_size = fontello_text_size, color = purple, on_press = lambda x: self.numeric_operator_button_press('×', self.btn8), background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn8), always_release = True) 
        self.btn9 = Button(font_name = font_style_gunplay, text = '4', background_normal = '', background_color = orange, font_size = text_size, color = black, on_press = lambda x: self.numeric_operator_button_press('4', self.btn9), background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn9), always_release = True)
        self.btn10 = Button(font_name = font_style_gunplay, text = '5', background_normal = '', background_color = orange, font_size = text_size, color = black, on_press = lambda x: self.numeric_operator_button_press('5', self.btn10), background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn10), always_release = True)
        self.btn11 = Button(font_name = font_style_gunplay, text = '6', background_normal = '', background_color = orange, font_size = text_size, color = black, on_press = lambda x: self.numeric_operator_button_press('6', self.btn11), background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn11), always_release = True)
        self.btn12 = Button(font_name = font_style_fontello, text = '\ue9da', background_normal = '', background_color = white, font_size = fontello_text_size, color = purple, on_press = lambda x: self.numeric_operator_button_press('-', self.btn12), background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn12), always_release = True)
        self.btn13 = Button(font_name = font_style_gunplay, text = '1', background_normal = '', background_color = orange, font_size = text_size, color = black, on_press = lambda x: self.numeric_operator_button_press('1', self.btn13), background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn13), always_release = True)
        self.btn14 = Button(font_name = font_style_gunplay, text = '2', background_normal = '', background_color = orange, font_size = text_size, color = black, on_press = lambda x: self.numeric_operator_button_press('2', self.btn14), background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn14), always_release = True)
        self.btn15 = Button(font_name = font_style_gunplay, text = '3', background_normal = '', background_color = orange, font_size = text_size, color = black, on_press = lambda x: self.numeric_operator_button_press('3', self.btn15), background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn15), always_release = True)
        self.btn16 = Button(font_name = font_style_fontello, text = '\ue9d8', background_normal = '', background_color = white, font_size = fontello_text_size, color = purple, on_press = lambda x: self.numeric_operator_button_press('+', self.btn16), background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn16), always_release = True)
                
        self.gl = GridLayout(cols = 4, spacing = '5sp', padding = ('10sp', '0sp', '10sp', '5sp'))

        self.gl.add_widget(self.btn1)
        self.gl.add_widget(self.btn2)
        self.gl.add_widget(self.btn3)
        self.gl.add_widget(self.btn4)
        self.gl.add_widget(self.btn5)
        self.gl.add_widget(self.btn6)
        self.gl.add_widget(self.btn7)
        self.gl.add_widget(self.btn8)
        self.gl.add_widget(self.btn9)
        self.gl.add_widget(self.btn10)
        self.gl.add_widget(self.btn11)
        self.gl.add_widget(self.btn12)
        self.gl.add_widget(self.btn13)
        self.gl.add_widget(self.btn14)
        self.gl.add_widget(self.btn15)
        self.gl.add_widget(self.btn16)
            
        return self.gl


    #LAYOUT HOLDING '0', '.', '=' BUTTONS
    
    def Bottom_Box(self):

        self.btn17 = Button(font_name = font_style_gunplay, text = '0', background_normal = '', background_color = orange, size_hint = (2.07, 1), font_size = text_size, color = black, on_press = lambda x: self.numeric_operator_button_press('0', self.btn17), background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn17), always_release = True)
        self.btn18 = Button(font_name = font_style_gunplay, text = '.', background_normal = '', background_color = pink, font_size = text_size, color = black, on_press = lambda x: self.numeric_operator_button_press('.', self.btn18), background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn18), always_release = True)
        self.btn19 = Button(font_name = font_style_fontello, text = '\ue9de', background_normal = '', background_color = purple, font_size = fontello_text_size, color = white, on_press = self.equal_to, background_down = '', on_release = lambda x: self.return_to_initial_color__initial_text_size(self.btn19), always_release = True) 
                            
        self.bl = BoxLayout(spacing = '5dp', padding = ('10dp', '0dp', '10dp', '10dp'), size_hint = (1, 0.25))
            
        self.bl.add_widget(self.btn17)
        self.bl.add_widget(self.btn18)
        self.bl.add_widget(self.btn19)

        return self.bl
    

    # METHOD FOR MERGING ALL INDIVIDUAL LAYOUTS
    
    def Super_Layout(self):

        self.sl = BoxLayout(orientation = 'vertical')

        self.sl.add_widget(self.Info())
        self.sl.add_widget(self.Output_Screen())
        self.sl.add_widget(self.Middle_Box())
        self.sl.add_widget(self.Bottom_Box())

        return self.sl
    

    # METHOD BINDED WITH CLEAR BUTTON
    
    def clear(self, event):
        
        self.sound.play()
    
        self.out.color = white
        self.out.font_name = 'Roboto'

        self.sound.play()

        global equal_memory
        
        self.btn1.background_color = dark_green
        self.btn1.font_size = on_press_text_size

        self.out.font_size = output_size
        self.out.text = '0'
        self.message_display.text = ''
        equal_memory = False

    def plus_or_minus(self, event):

        self.sound.play()

        self.out.color = white
    
        global equal_memory

        self.btn2.background_color = dark_pink
        self.btn2.font_size = on_press_text_size
        
        if self.message_display.text == 'Maximum Level Reached' and self.out.text == 'ERROR' and equal_memory == True:
                self.message_display.text = '' 
                self.out.font_size = output_size
                self.out.text = '-0'
                equal_memory = False

        elif self.out.text == 'ERROR' and self.message_display.text != 'Maximum Level Reached':
            self.out.font_size = output_size
            self.out.text = '-0'
            equal_memory = False
        

        elif self.message_display.text == 'Maximum Level Reached' and self.out.text != 'ERROR' and equal_memory == True:
            self.message_display.text = ''
            self.out.font_size = output_size
            self.out.text = '-0'
            equal_memory = False

        elif self.message_display.text == 'Maximum Level Reached' and self.out.text != 'ERROR':
            pass
        
        else:

            try:
                if self.out.text == 'ERROR':
                    self.out.text = '-0' 
                elif self.out.text[0] not in ['+', '-', '×', '÷']: 
                    self.out.text = '-' + self.out.text
                elif self.out.text[0] == '+':
                    self.out.text = '-' + self.out.text[1:]
                elif self.out.text[0] == '-':
                    self.out.text = self.out.text[1:]
            except:
                pass

    # METHOD BINDED WITH BACKSPACE BUTTON
    
    def backspace(self, event):
    
        self.sound.play()
    
        self.out.color = white
        self.out.font_name = 'Roboto'

        self.btn3.background_color = dark_pink    
        self.btn3.font_size = on_press_text_size
        

        if self.out.text == 'ERROR':
            self.out.font_size = output_size
            self.out.text = '0'
            
        elif self.message_display.text == 'Maximum Level Reached':
            self.message_display.text = ''
    
            global equal_memory
        
        try:
                
            if self.out.text[0] == '-' and len(self.out.text) == 1:
                self.out.text = '0'
                
            elif self.out.text[0] == '-' and self.out.text[1] == '0' and len(self.out.text) == 2:
                self.out.text = '-'

            elif self.out.text[0] == '-' and self.out.text[1] == '0' and self.out.text[2] in ['+', '-', '×', '÷'] and len(self.out.text) == 3:
                self.out.text = '-0'
                
            else:
                self.out.text = self.out.text[0 : len(self.out.text) - 1]
                if len(self.out.text) == 0:
                    self.out.text = '0'
                    equal_memory = False
                equal_memory = False
            
        except:
            pass

        if len(self.out.text) <= 13:
            self.out.font_size = output_size
            
        elif 13 < len(self.out.text) <= 25:
            self.out.font_size = small_output_size

        if len(self.out.text) < 25:
            self.message_display.text = ''


    # MRTHOD BINDED WITH NUMERIC, OPERATOR BUTTON AND DECIMAL BUTTON
    
    def numeric_operator_button_press(self, event, color_event__text_size_event):
    

    
        self.sound.play()
        
        self.out.color = white
        self.out.font_name = 'Roboto'

        global equal_memory

        if color_event__text_size_event in [self.btn4, self.btn8, self.btn12, self.btn16, self.btn19]:
            color_event__text_size_event.font_size = on_press_fontello_text_size
        else:
            color_event__text_size_event.font_size = on_press_text_size

        

        if color_event__text_size_event.background_color == orange:
            color_event__text_size_event.background_color = dark_orange

        elif color_event__text_size_event.background_color == white:
            color_event__text_size_event.background_color = grey_for_buttons
        
        elif color_event__text_size_event.background_color == pink:
            color_event__text_size_event.background_color = dark_pink
        
        elif color_event__text_size_event.background_color == purple:
            color_event__text_size_event.background_color = dark_purple

        if self.out.text == 'ERROR' and self.message_display.text == 'Maximum Level Reached' and event in ['+', '-', '×', '÷', '.'] and equal_memory == True:
            self.message_display.text = ''
            self.out.font_size = output_size
            self.out.text = '0' + event
            equal_memory = False 
        
        elif self.out.text == 'ERROR' and self.message_display.text != 'Maximum Level Reached':
            if event in ['+', '-', '', '÷', '.']:
                self.out.font_size = output_size
                self.out.text = '0' + event
                equal_memory = False
            else:
                self.out.font_size = output_size
                self.out.text = event
                equal_memory = False

        elif self.message_display.text == 'Maximum Level Reached' and self.out.text != 'ERROR' and equal_memory == True:
            self.message_display.text = ''
            self.out.font_size = output_size
            if event in ['+', '-', '×', '÷', '.']:
                self.out.text = '0' + event
            else:
                self.out.text = event
            equal_memory = False
        
        elif self.message_display.text == 'Maximum Level Reached' and self.out.text != 'ERROR':
            pass

        else:

            if self.message_display.text == 'Maximum Level Reached' and self.out.text == 'ERROR' and equal_memory == True:
                self.message_display.text = self.out.text = ''
                equal_memory = False


            self.out.text += str(event)

            try:
                if self.out.text[-1] == '0' and self.out.text[-2] == '0' and self.out.text[-3] in ['+', '-', '×', '÷']:
                    self.out.text = self.out.text[0:len(self.out.text) - 1]
            except:
                pass
            
            try:
                if self.out.text[-1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and self.out.text[-2] == '0' and self.out.text[-3] in ['+', '-', '×', '÷']:
                    self.out.text = self.out.text[0:len(self.out.text) - 2] + event 
            except:
                pass

            if equal_memory == True and event  not in ['+', '-', '×', '÷', '.']:
                self.out.text = event
                equal_memory = False
            else:
                equal_memory = False
            
            
            try:
                if self.out.text[0] == '0' and self.out.text[1] not in ['.', '+', '-', '×', '÷']:
                    self.out.text = self.out.text[1:]
            except:
                pass
            
            
            try:
            
                if self.out.text[-1] == '.' and self.out.text[-2] in ['+', '-', '×', '÷']:
                        self.out.text = self.out.text[0:len(self.out.text) - 1] + '0.'
            except:
                self.out.text = '0.'
            
            
            try:
                if self.out.text[2] not in ['+', '-', '×', '÷', '.']:
                    try:
                        if self.out.text[0] == '-' and self.out.text[1] == '0' and self.out.text[-1]  not in ['+', '-', '×', '÷']:
                                    self.out.text = '-' + self.out.text[2:]
                    except:
                        pass
            except:
                pass
            
            try:
                if self.out.text[0] == '-' and self.out.text[1] in ['+', '-', '×', '÷']:
                    self.out.text = '0' + event
                else:
                    pass
                
                if self.out.text[-1] == '+' and self.out.text[-2] == '-':
                    self.out.text = self.out.text[0: len(self.out.text) - 2] 
                else:
                    pass
                
                if self.out.text[-1] in ['-'] and self.out.text[-2] in ['×', '÷'] :
                    self.out.text = self.out.text[0:]
                
                elif self.out.text[-1] in ['+', '-', '×', '÷', '.'] and self.out.text[-2] in ['+', '-', '×', '÷', '.'] :
                    self.out.text = self.out.text[0: len(self.out.text) - 2] + self.out.text[-1]
                
                if self.out.text[-1] in ['+', '-', '×', '÷'] and self.out.text[-2] in ['+', '-', '×', '÷'] and self.out.text[-1] == self.out.text[-2]:
                    self.out.text = self.out.text[0: len(self.out.text) - 1]
                
                if self.out.text[-1] in ['×', '÷'] and self.out.text[-2] in ['×', '÷']:
                     self.out.text = self.out.text[0: len(self.out.text) - 2] + self.out.text[-1]

            except:
                pass

            if len(self.out.text) <= 13:
                self.out.font_size = output_size
            elif 13 < len(self.out.text) < 25:
                self.out.font_size = small_output_size
            else:
                self.message_display.font_size = message_size
                self.message_display.text = 'Maximum Level Reached'

        if event == '.':

            self.i = len(self.out.text) - 1
            self.operator_index = None
            
            while self.i >= 0:
                if self.out.text[self.i] in ['+', '-', '×', '÷']:
                    self.operator_index = self.i
                    break
                self.i -= 1

            if self.operator_index == None:
                self.j = 0
            elif self.operator_index == self.i:
                self.j = self.operator_index + 1

            self.decimal_count = 0

            while self.j < len(self.out.text):

                if self.out.text[self.j] == '.':
                    self.decimal_count += 1
                self.j += 1

            if self.decimal_count == 2:
                self.out.text = self.out.text[0 : len(self.out.text) - 1]


    #  MRTHOD FOR RETURNING TO DEFAULT COLOR AND IMAGE AFTER RELEASING A BUTTON   
    def return_to_initial_color__initial_text_size(self, color_event__text_size_event):
        
        if color_event__text_size_event in [self.btn4, self.btn8, self.btn12, self.btn16, self.btn19]:
            color_event__text_size_event.font_size = fontello_text_size
        else:
            color_event__text_size_event.font_size = text_size

               
        if color_event__text_size_event.background_color == dark_green:
            color_event__text_size_event.background_color = green

        elif color_event__text_size_event.background_color == dark_pink:
            color_event__text_size_event.background_color = pink
        
        elif color_event__text_size_event.background_color == grey_for_buttons:
            color_event__text_size_event.background_color = white
        
        elif color_event__text_size_event.background_color == dark_orange:
            color_event__text_size_event.background_color = orange            
        
        elif color_event__text_size_event.background_color == dark_purple:
            color_event__text_size_event.background_color = purple

        
    # METHOD BINDED WITH EQUALTO BUTTON
    
    def equal_to(self, event):
        
        self.sound.play()
        
        self.out.color = white
        self.out.font_name = 'Roboto'

        global equal_memory
        
        self.btn19.background_color = dark_purple
        self.btn19.font_size = on_press_fontello_text_size
        
                
        try:
            
            try:
                
                if self.out.text[-1] == '.':
                    self.out.font_size = message_size
                    self.out.text = 'ERROR'
                
                self.i = 0
                self.computing_string = ''

                while self.i < len(self.out.text):

                    if self.out.text[self.i] == '×':
                        self.computing_string += '*'
                    elif self.out.text[self.i] == '÷':
                        self.computing_string += '/'
                    else:
                        self.computing_string += self.out.text[self.i]
                    self.i += 1

    
                self.out.text = str(round(eval(self.computing_string), 13))
                
                
                if len(self.out.text) <= 13:
                    self.out.font_size = output_size
                    self.message_display.text = ''
                elif 13 < len(self.out.text) < 25:
                    self.out.font_size = small_output_size
                    self.message_display.text = ''
                else:
                    self.message_display.font_size = message_size
                    self.message_display.text = 'Maximum Level Reached'
                equal_memory = True 
            except:  
                self.out.font_size = message_size
                self.out.color = red
                self.out.font_name = font_style_gunplay 
                self.out.text = 'ERROR'
                equal_memory = True
                
            try:
                if self.out.text[-1] == '0' and self.out.text[-2] == '.':
                    self.out.text = self.out.text[0: len(self.out.text) - 2]
                if self.out.text[0] == '-' and self.out.text[1] == '0' and len(self.out.text) == 2:
                    self.out.text = '0'

            except:
                pass
            
        except:
            pass

        
    # DEFINING MAIN LOOP METHOD
    
    def build(self):
        self.sound = SoundLoader.load('App_Data/Sounds/button_click_sound.wav')
        self.sl = self.Super_Layout()
        return self.sl          


# ASSIGNING CALCULATOR CLASS TO "ROOT" VARIABLE 

root = Calculator()


# EXECUTING PROGRAM

if __name__ == '__main__':
    root.run()
    
