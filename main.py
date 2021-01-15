from tkinter import *
from tkinter import font as tkFont 
import parser

root = Tk()

#titulo de la ventana
root.title('Calculadora')
try:
    root.iconbitmap('calculator.ico')
except:
    print('caution!!: file calculator.ico not exist')


# variables de diseño
btn_width = 6
btn_heigth =2
btn_color_main = '#333B4E'
btn_color_operator = '#28303D'
btn_color_result = '#D95A2B'
btn_color_clear = '#174A4C'

font_family = 'Ubuntu'
font_color = '#ffffff'
custom_font = tkFont.Font(family=font_family, size=15)

# Input Fields
display = Entry(root,bd = 0,font = (font_family,20), fg = font_color,width = 20, bg='#161A23')
display.grid(row=0, columnspan=4, sticky=W+E,ipady = 15,pady = 0)

# Get Numbers to Display
i = 0

def get_numbers(n):
    global i
    display.insert(i, n)
    i += 1

def get_operation(operator):
    global i
    opertor_length = len(operator)
    display.insert(i, operator)
    i+=opertor_length
    
def replace_operation(display_state):
    display_state = display_state.replace("x", "*")
    display_state = display_state.replace("^", "**")
    display_state = display_state.replace("÷", "/")
    return display_state

def calculate():
    display_state = display.get()
    display_state = replace_operation(display_state)
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        clear_display()
        display.insert(0, result)
    except Exception:
        clear_display()
        display.insert(0, 'Error')

def clear_display():
    display.delete(0, END)


def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, 'Error')

# Buttons
Button(root, font=custom_font, fg=font_color, bg=btn_color_clear, text="C", width = btn_width, height =btn_heigth, command=lambda: clear_display()).grid(row=1, column=0)
Button(root, font=custom_font, fg=font_color, bg=btn_color_operator, text="⟵", width = btn_width, height =btn_heigth, command=lambda: undo()).grid(row=1, column=1)
Button(root, font=custom_font, fg=font_color, bg=btn_color_operator, text="^", width = btn_width, height =btn_heigth, command=lambda: get_operation("**")).grid(row=1, column=2)
Button(root, font=custom_font, fg=font_color, bg=btn_color_operator, text="/", width = btn_width, height =btn_heigth, command=lambda: get_operation("/")).grid(row=1, column=3)

Button(root, font=custom_font, fg=font_color, bg=btn_color_main, text="(", width = btn_width, height =btn_heigth, command=lambda: get_operation("(")).grid(row=2, column=0)
Button(root, font=custom_font, fg=font_color, bg=btn_color_main, text=")", width = btn_width, height =btn_heigth, command=lambda: get_operation(")")).grid(row=2, column=1)
Button(root, font=custom_font, fg=font_color, bg=btn_color_main, text="%", width = btn_width, height =btn_heigth, command=lambda: get_operation("%")).grid(row=2, column=2)
Button(root, font=custom_font, fg=font_color, bg=btn_color_operator, text="x", width = btn_width, height =btn_heigth, command=lambda: get_operation("*")).grid(row=2, column=3)

Button(root, font=custom_font, fg=font_color, bg=btn_color_main, text="7", width = btn_width, height =btn_heigth, command=lambda: get_numbers(7)).grid(row=3, column=0)
Button(root, font=custom_font, fg=font_color, bg=btn_color_main, text="8", width = btn_width, height =btn_heigth, command=lambda: get_numbers(8)).grid(row=3, column=1)
Button(root, font=custom_font, fg=font_color, bg=btn_color_main, text="9", width = btn_width, height =btn_heigth, command=lambda: get_numbers(9)).grid(row=3, column=2)
Button(root, font=custom_font, fg=font_color, bg=btn_color_operator, text="-", width = btn_width, height =btn_heigth, command=lambda: get_operation("-")).grid(row=3, column=3)

Button(root, font=custom_font, fg=font_color, bg=btn_color_main, text="4", width = btn_width, height =btn_heigth, command=lambda: get_numbers(4)).grid(row=4, column=0)
Button(root, font=custom_font, fg=font_color, bg=btn_color_main, text="5", width = btn_width, height =btn_heigth, command=lambda: get_numbers(5)).grid(row=4, column=1)
Button(root, font=custom_font, fg=font_color, bg=btn_color_main, text="6", width = btn_width, height =btn_heigth, command=lambda: get_numbers(6)).grid(row=4, column=2)
Button(root, font=custom_font, fg=font_color, bg=btn_color_operator, text="+", width = btn_width, height =btn_heigth, command=lambda: get_operation("+")).grid(row=4, column=3)

Button(root, font=custom_font, fg=font_color, bg=btn_color_main, text="1", width = btn_width, height =btn_heigth, command=lambda: get_numbers(1)).grid(row=5, column=0)
Button(root, font=custom_font, fg=font_color, bg=btn_color_main, text="2", width = btn_width, height =btn_heigth, command=lambda: get_numbers(2)).grid(row=5, column=1)
Button(root, font=custom_font, fg=font_color, bg=btn_color_main, text="3", width = btn_width, height =btn_heigth, command=lambda: get_numbers(3)).grid(row=5, column=2)
Button(root, font=custom_font, fg=font_color, bg=btn_color_result, text="=", width = btn_width, height =btn_heigth, command=lambda:calculate()).grid(row=5, column=3, sticky=N+S, rowspan=2)

Button(root, font=custom_font, fg=font_color, bg=btn_color_main, text="0", width = btn_width, height =btn_heigth, command=lambda: get_numbers(0)).grid(row=6, column=0, sticky=W+E, columnspan=2)
Button(root, font=custom_font, fg=font_color, bg=btn_color_main, text=".", width = btn_width, height =btn_heigth, command=lambda: get_operation(".")).grid(row=6, column=2)


root.mainloop()
