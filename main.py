from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class InputButton(Button):
    def __init__(self, **kwargs):
        Button.__init__(self, **kwargs)


class FunctionPanel(GridLayout):
    def __init__(self, **kwargs):
        GridLayout.__init__(self, **kwargs)


class MathGraphicsLayout(BoxLayout):
    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.disable_input_buttons_on_startup()

    def disable_input_buttons_on_startup(self):
        self.ids.input_plus_button.disabled = True
        self.ids.input_multiply_button.disabled = True
        self.ids.input_divide_button.disabled = True
        self.ids.input_power_button.disabled = True
        self.ids.input_root_button.disabled = True
        self.ids.input_logarithm_button.disabled = True
        self.ids.input_right_bracket_button.disabled = True

    def manipulate_input_buttons_activity(self, disable):
        self.ids.input_0_button.disabled = disable
        self.ids.input_1_button.disabled = disable
        self.ids.input_2_button.disabled = disable
        self.ids.input_3_button.disabled = disable
        self.ids.input_4_button.disabled = disable
        self.ids.input_5_button.disabled = disable
        self.ids.input_6_button.disabled = disable
        self.ids.input_7_button.disabled = disable
        self.ids.input_8_button.disabled = disable
        self.ids.input_9_button.disabled = disable
        self.ids.input_point_button.disabled = disable
        self.ids.input_x_button.disabled = disable
        self.ids.input_plus_button.disabled = disable
        self.ids.input_minus_button.disabled = disable
        self.ids.input_multiply_button.disabled = disable
        self.ids.input_divide_button.disabled = disable
        self.ids.input_power_button.disabled = disable
        self.ids.input_root_button.disabled = disable
        self.ids.input_logarithm_button.disabled = disable
        self.ids.input_sin_button.disabled = disable
        self.ids.input_cos_button.disabled = disable
        self.ids.input_sinh_button.disabled = disable
        self.ids.input_cosh_button.disabled = disable
        self.ids.input_arcsin_button.disabled = disable
        self.ids.input_arccos_button.disabled = disable
        self.ids.input_arcsinh_button.disabled = disable
        self.ids.input_arccosh_button.disabled = disable
        self.ids.input_factorial_button.disabled = disable
        self.ids.input_left_bracket_button.disabled = disable
        self.ids.input_right_bracket_button.disabled = disable

    def disable_first_positional_input_commands(self):
        self.ids.input_sin_button.disabled = True
        self.ids.input_cos_button.disabled = True
        self.ids.input_sinh_button.disabled = True
        self.ids.input_cosh_button.disabled = True
        self.ids.input_arcsin_button.disabled = True
        self.ids.input_arccos_button.disabled = True
        self.ids.input_arcsinh_button.disabled = True
        self.ids.input_arccosh_button.disabled = True
        self.ids.input_factorial_button.disabled = True
        self.ids.input_x_button.disabled = True
        self.ids.input_left_bracket_button.disabled = True

    def disable_non_first_positional_operations(self):
        self.ids.input_plus_button.disabled = True
        self.ids.input_multiply_button.disabled = True
        self.ids.input_divide_button.disabled = True
        self.ids.input_power_button.disabled = True
        self.ids.input_root_button.disabled = True
        self.ids.input_logarithm_button.disabled = True

    def disable_input_number_buttons(self):
        self.ids.input_0_button.disabled = True
        self.ids.input_1_button.disabled = True
        self.ids.input_2_button.disabled = True
        self.ids.input_3_button.disabled = True
        self.ids.input_4_button.disabled = True
        self.ids.input_5_button.disabled = True
        self.ids.input_6_button.disabled = True
        self.ids.input_7_button.disabled = True
        self.ids.input_8_button.disabled = True
        self.ids.input_9_button.disabled = True
        self.ids.input_point_button.disabled = True

    def disable_non_operational_input_buttons(self):
        self.disable_input_number_buttons()
        self.disable_first_positional_input_commands()

    def disable_input_buttons_on_number(self):
        self.manipulate_input_buttons_activity(False)
        self.disable_first_positional_input_commands()

    def disable_input_buttons_on_operation(self):
        self.manipulate_input_buttons_activity(False)
        self.disable_non_first_positional_operations()
        self.ids.input_minus_button.disabled = True
        self.ids.input_right_bracket_button.disabled = True

    def disable_input_buttons_on_left_bracket(self):
        self.manipulate_input_buttons_activity(False)
        self.disable_non_first_positional_operations()

    def disable_input_buttons_on_right_bracket(self):
        self.manipulate_input_buttons_activity(False)
        self.disable_non_operational_input_buttons()

    def disable_input_buttons_on_x(self):
        self.manipulate_input_buttons_activity(False)
        self.disable_non_operational_input_buttons()

    def disable_input_buttons_on_function(self):
        self.manipulate_input_buttons_activity(True)
        self.ids.input_left_bracket_button.disabled = False


class MathGraphicsApp(App):
    def __init__(self, **kwargs):
        App.__init__(self, **kwargs)
        self.math_graphics_layout = None

    def build(self):
        self.math_graphics_layout = MathGraphicsLayout()
        return self.math_graphics_layout

    def input_button_press(self, text):
        self.math_graphics_layout.ids.graphics_label.text += text
        if text in '0 1 2 3 4 5 6 7 8 9 .'.split(' '):
            self.math_graphics_layout.disable_input_buttons_on_number()
        elif text in ['+', '−', '×', '÷', '^', '√', 'log']:
            self.math_graphics_layout.disable_input_buttons_on_operation()
        elif text == '(':
            self.math_graphics_layout.disable_input_buttons_on_left_bracket()
        elif text == ')':
            self.math_graphics_layout.disable_input_buttons_on_right_bracket()
        elif text == 'X':
            self.math_graphics_layout.disable_input_buttons_on_x()
        elif text in 'sin cos sinh cosh arcsin arccos arcsinh arccosh factorial'.split(' '):
            self.math_graphics_layout.disable_input_buttons_on_function()


if __name__ == '__main__':
    Window.clearcolor = [1, 1, 1, 1]
    MathGraphicsApp().run()
