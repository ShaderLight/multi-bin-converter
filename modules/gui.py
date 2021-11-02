import tkinter as tk
import tkinter.ttk as ttk


from conv import to_dec_conv, from_dec_conv

options = ['base-2', 'base-10', 'u2', 'u1', 'base-8', 'base-16']
selection = {'from': None}


def rendergui():
    window = tk.Tk()
    window.geometry('800x500')

    global from_box
    global from_text

    title_label = tk.Label(window, text='Binary converter')
    title_label.pack()

    from_text = tk.StringVar(value='From')
    
    from_text.set('From')

    from_box = ttk.Combobox(window, textvariable=from_text)

    from_box['values'] = options
    from_box['state'] = 'readonly'

    from_box.bind('<<ComboboxSelected>>', get_from_input)

    from_box.pack(padx=5, pady=5)


    global digit_input

    digit_input = tk.Text(window, height=2, width=20)
    digit_input.pack()

    confirm_btn = tk.Button(window, text='Convert', command=convert)
    confirm_btn.pack()

    global output_box

    output_box = tk.Text(window, height=5, width = 20)
    output_box.pack(padx=10, pady=20)
    output_box.config(state='normal')
    
    window.mainloop()


def get_from_input(event):
    selection['from'] = from_text.get()


def convert():
    input = digit_input.get("1.0", "end-1c")
    output = 'Invalid selection'
    
    # From base-10 to base-2
    if selection['from'] != None:
        output = generate_response(input, selection['from'])

    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, output)


def generate_response(input, selection):
    messages = {'base-10': 10, 'base-2': 2, 'u2': 'u2' , 'u1': 'u1', 'base-8': 8, 'base-16': 16}
    
    input_type = messages[selection]

    output = ''
    for key, value in messages.items():
        if key == selection:
            continue
        converted = from_dec_conv(to_dec_conv(input, input_type), value)
        generated_str = key + ': ' + str(converted) + '\n'
        output += generated_str

    return output


rendergui()