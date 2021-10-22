import tkinter as tk
import tkinter.ttk as ttk

import conv as cv

options = ['base-2', 'base-10']
selection = {}

def rendergui():
    window = tk.Tk()
    window.geometry('800x500')

    global from_box
    global to_box
    global from_text
    global to_text

    title_label = tk.Label(window, text='Binary converter')
    title_label.pack()

    from_text = tk.StringVar(value='From')
    to_text = tk.StringVar(value='To')
    
    from_text.set('From')
    to_text.set('To')

    from_box = ttk.Combobox(window, textvariable=from_text)
    to_box = ttk.Combobox(window, textvariable=to_text)

    from_box['values'] = options
    from_box['state'] = 'readonly'

    to_box['values'] = options
    to_box['state'] = 'readonly'

    from_box.bind('<<ComboboxSelected>>', get_from_input)
    to_box.bind('<<ComboboxSelected>>', get_to_input)

    from_box.pack(padx=5, pady=5)
    to_box.pack(padx=5, pady=5)


    global digit_input

    digit_input = tk.Text(window, height=2, width=20)
    digit_input.pack()

    confirm_btn = tk.Button(window, text='Convert', command=convert)
    confirm_btn.pack()

    global output_box

    output_box = tk.Text(window, height=2, width = 20)
    output_box.pack(padx=10, pady=20)
    output_box.config(state='normal')
    
    window.mainloop()


def get_from_input(event):
    selection['from'] = from_text.get()

def get_to_input(event):
    selection['to'] = to_text.get()

def convert():
    input = digit_input.get("1.0", "end-1c")
    output = 0
    if (selection['from'] == 'base-10') and (selection['to'] == 'base-2'):
        output = cv.dec_to_bin(int(input))
    elif (selection['from'] == 'base-2') and (selection['to'] == 'base-10'):
        output = cv.bin_to_dec(input)

    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, output)

rendergui()