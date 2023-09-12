import tkinter as tk

# Define colors for light and dark mode
light_bg = "#f4f4f4"
light_fg = "#000000"
dark_bg = "#222222"
dark_fg = "#ffffff"

# Define function to toggle between light and dark mode


def toggle_theme():
    if window.cget("bg") == light_bg:
        window.config(bg=dark_bg)
        display.config(bg=dark_bg, fg=dark_fg)
        for button in buttons:
            button.config(bg=dark_bg, fg=dark_fg,
                          activebackground=dark_bg, activeforeground=dark_fg)
    else:
        window.config(bg=light_bg)
        display.config(bg=light_bg, fg=light_fg)
        for button in buttons:
            button.config(bg=light_bg, fg=light_fg,
                          activebackground=light_bg, activeforeground=light_fg)


def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))


def button_clear():
    display.delete(0, tk.END)


def button_equal():
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")
window.config(bg=light_bg)

# Create the display
display = tk.Entry(window, font=("Arial", 20), bg=light_bg,
                   fg=light_fg, justify="right")
display.grid(row=0, column=0, columnspan=4,
             padx=10, pady=10, ipadx=10, ipady=10)

# Create number buttons
buttons = []
button_texts = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2)
]

for i, button_data in enumerate(button_texts):
    button_text, row, col = button_data
    button = tk.Button(window, text=button_text, padx=20, pady=10, font=("Arial", 14),
                       bg=light_bg, fg=light_fg, activebackground=light_bg, activeforeground=light_fg,
                       command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    buttons.append(button)

# Create clear and equal buttons
clear_button = tk.Button(window, text="C", padx=20, pady=10, font=("Arial", 14),
                         bg=light_bg, fg=light_fg, activebackground=light_bg, activeforeground=light_fg,
                         command=button_clear)
clear_button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

equal_button = tk.Button(window, text="=", padx=20, pady=10, font=("Arial", 14),
                         bg=light_bg, fg=light_fg, activebackground=light_bg, activeforeground=light_fg,
                         command=button_equal)
equal_button.grid(row=5, column=1, columnspan=2, padx=5, pady=5, sticky="nsew")

# Create theme toggle button
theme_button = tk.Button(window, text="Toggle Theme", padx=10, pady=5, font=("Arial", 12),
                         bg=light_bg, fg=light_fg, activebackground=light_bg, activeforeground=light_fg,
                         command=toggle_theme)
theme_button.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

# Configure row and column weights
for i in range(5):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# Run the main loop
window.mainloop()
