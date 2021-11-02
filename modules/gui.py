import tkinter as tk
import tkinter.ttk as ttk


from .conv import to_dec_conv, from_dec_conv

options = ['base-2', 'base-10', 'u2', 'u1', 'base-8', 'base-16']
selection = {'from': None}


def rendergui():
    window = tk.Tk()

    global from_text
    global bit_text
    global digit_input
    global output_box

    # Setting up labels
    title_label = tk.Label(window, text='Binary converter')
    title_label.grid(column=1, row=0, padx=5, pady=5)

    from_label = tk.Label(window, text = 'From base')
    from_label.grid(column=0, row=1, padx=5, pady=5)

    bit_label = tk.Label(window, text='Fractional bits')
    bit_label.grid(column=2, row=1, padx=5, pady=5)

    # Setting up input/output boxes

    bit_text = tk.StringVar(value='5')
    bit_box = tk.Spinbox(window, from_=1, to=10, textvariable=bit_text)
    bit_box.grid(column=2, row=2, padx=5, pady=5)

    from_text = tk.StringVar(value='From')
    from_text.set('From')
    from_box = ttk.Combobox(window, textvariable=from_text)

    from_box['values'] = options
    from_box['state'] = 'readonly'
    from_box.bind('<<ComboboxSelected>>', get_from_input)
    from_box.grid(column=0, row=2, padx=5, pady=5)

    digit_input = tk.Text(window, height=1, width=20)
    digit_input.grid(column=1, row=3, padx=20, pady=20)

    output_box = tk.Text(window, height=5, width = 30)
    output_box.grid(column=1, row=4, pady=20, padx=20)
    output_box.config(state='normal')

    # Setting up confirm button

    confirm_btn = tk.Button(window, text='Convert', command=convert)
    confirm_btn.grid(column=1, row=5, padx=5, pady=20)

    window.mainloop()


# Copying input to selection dict everytime user changes something in combobox
def get_from_input(event):
    selection['from'] = from_text.get()


# Gathering all input from user and executing generate_response function
def convert():
    bits = int(bit_text.get())
    input = digit_input.get("1.0", "end-1c")
    output = 'Invalid selection'
    
    # From base-10 to base-2
    if selection['from'] != None: # In case user didn't select anything
        output = generate_response(input, selection['from'], bits)

    output_box.delete(1.0, tk.END) # Without deleting first, the text would just append to the previous output
    output_box.insert(tk.END, output)


def generate_response(input, selection, bits):
    # Possible inputs and their values inputted to conversion functions
    messages = {'base-10': 10, 'base-2': 2, 'u2': 'u2' , 'u1': 'u1', 'base-8': 8, 'base-16': 16}
    
    input_type = messages[selection]

    output = ''
    for key, value in messages.items():
        if key == selection: # Skipping because converting e.g. base-10 to base-10 would be pointless
            continue
        converted = from_dec_conv(to_dec_conv(input, input_type), value, bits) # Converting any base to decimal and then to any base from decimal
        generated_str = key + ': ' + str(converted) + '\n'
        output += generated_str

    return output