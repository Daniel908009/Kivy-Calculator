from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# the main grid layout of the calculator
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        # creating a second grid layout for the text input so it will be centered and span the whole row
        self.result_layout = GridLayout(cols = 1, size_hint_y = 0.4)
        self.add_widget(self.result_layout)
        # creating the result text
        self.result = TextInput(font_size = self.height, multiline = False, readonly = True, halign = 'right', padding_y = [30, 30])
        self.result_layout.add_widget(self.result)

        # creating a second grid layout for the buttons
        self.buttons_layout = GridLayout(cols = 4)
        self.add_widget(self.buttons_layout)
        # creating the buttons
        buttons = ['(', ')', '<', 'C',
                   '7', '8', '9', '+',
                   '4', '5', '6', '-',
                   '1', '2', '3', '*',
                   '.', '0', '/', '=']
        for button in buttons:
            self.buttons_layout.add_widget(Button(text = button, on_press = self.on_button_press))
            
    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                self.result.text = str(eval(self.result.text))
            except:
                self.result.text = 'Error'
        elif instance.text == 'C':
            self.result.text = ''
        elif instance.text == '<':
            self.result.text = self.result.text[:-1] # this removes the last character
        else:
            self.result.text += instance.text

# the app class/root of the calculator
class CalculatorApp(App):
    def build(self):
        return MyGrid()


# create an instance of the app
if __name__ == '__main__':
    CalculatorApp().run()