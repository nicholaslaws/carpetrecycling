import os
import tkinter as tk

def button_clicked():
    text_box.delete(1.0, tk.END)  # clear the text box
    selected_file = dropdown_var.get()
    text_box.insert(tk.END, f"You selected the file: {selected_file}\n")
    with open(selected_file, 'r') as f:
        contents = f.read()
        text_box.insert(tk.END, "File contents:\n")
        text_box.insert(tk.END, contents)

def dropdown_selected(event):
    print("Selected file:", dropdown_var.get())

# Get a list of all JSON files in the current directory
files = [f for f in os.listdir() if f.endswith('.json')]

# Create the main window and set its size
window = tk.Tk()
window.title("Harvard SEAS - Carpet Composition Optimization Algorithm")
window.geometry("800x600")

# Create the button and bind it to a function
button = tk.Button(window, text="Optimize", command=button_clicked, height=10, width=20)
button.pack(side="left", padx=20, pady=20)

# Create a spacer widget to move the dropdown further down
spacer = tk.Label(window, text="")
spacer.pack()

# Create the dropdown with all JSON files in the current directory
dropdown_var = tk.StringVar(value=files[0])
dropdown = tk.OptionMenu(window, dropdown_var, *files, command=dropdown_selected)
dropdown.pack()

# Create a text box to display output
text_box = tk.Text(window, height=60, width=60)
text_box.pack()

# Start the main loop
window.mainloop()
