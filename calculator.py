import tkinter as tk

def on_click(event):
    btn_text = event.widget["text"]
    if btn_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif btn_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, btn_text)

# Hover effects
def on_enter(event):
    event.widget["bg"] = "#44475a"

def on_leave(event):
    event.widget["bg"] = "#282a36"

# App window
root = tk.Tk()
root.title("🧮 Stylish Calculator")
root.geometry("400x550")
root.configure(bg="#1e1f29")
root.resizable(False, False)

# Display entry
entry = tk.Entry(root, font=("Consolas", 28), bd=0, relief=tk.FLAT, bg="#f8f8f2", fg="#282a36", justify="right")
entry.pack(padx=20, pady=20, fill="both", ipady=15)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

# Button style
def create_button(parent, text):
    btn = tk.Button(
        parent, text=text, font=("Helvetica", 20, "bold"), fg="#f8f8f2",
        bg="#282a36", bd=0, relief=tk.FLAT, activebackground="#6272a4",
        cursor="hand2"
    )
    btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)
    btn.bind("<Button-1>", on_click)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Frame and button layout
for row in buttons:
    frame = tk.Frame(root, bg="#1e1f29")
    frame.pack(expand=True, fill="both", padx=10, pady=5)
    for btn_text in row:
        create_button(frame, btn_text)

root.mainloop()
