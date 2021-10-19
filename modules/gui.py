import tkinter as tk

def rendergui():
    window = tk.Tk()
    window.geometry('800x500')

    title_label = tk.Label(window, text='Binary converter')
    title_label.pack()

    global digit_input
    digit_input = tk.Text(window, height=2, width=20)
    digit_input.pack()

    confirm_btn = tk.Button(window, text='Convert', command=convert)
    confirm_btn.pack()
    
    window.mainloop()


def convert():
    input = digit_input.get("1.0", "end-1c")
    print(input)

rendergui()
