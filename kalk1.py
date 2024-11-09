import tkinter as tk

# Fungsi untuk menambahkan karakter ke dalam entry
def click(text):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + text)

# Fungsi untuk menghitung hasil
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)  # Perhitungan ekspresi matematika
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Fungsi untuk menghapus isi entry
def clear():
    entry.delete(0, tk.END)

# Membuat window utama
window = tk.Tk()
window.title("Kalkulator")

# Membuat canvas dan scrollbar
canvas = tk.Canvas(window)
scroll_y = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
scroll_x = tk.Scrollbar(window, orient="horizontal", command=canvas.xview)

# Menyusun frame untuk menampung kalkulator
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Mengkonfigurasi scrollbar
scroll_y.config(command=canvas.yview)
scroll_x.config(command=canvas.xview)
canvas.config(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

# Menyusun widget di dalam frame
entry = tk.Entry(frame, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Tombol-tombol kalkulator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0, 4)  # Tombol Clear
]

# Membuat tombol-tombol
for (text, row, column, *colspan) in buttons:
    button = tk.Button(frame, text=text, width=5, height=2, font=('Arial', 18))
    if text == 'C':
        button.config(command=clear)
    elif text == '=':
        button.config(command=calculate)
    else:
        button.config(command=lambda t=text: click(t))
    button.grid(row=row, column=column, columnspan=colspan[0] if colspan else 1)

# Menyusun komponen scroll
canvas.grid(row=0, column=0, sticky="nsew")
scroll_y.grid(row=0, column=1, sticky="ns")
scroll_x.grid(row=1, column=0, sticky="ew")

# Mengatur ukuran grid window untuk memungkinkan scrollbar
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Menyesuaikan ukuran canvas dan frame
frame.update_idletasks()  # Perbarui ukuran frame
canvas.config(scrollregion=canvas.bbox("all"))

# Menjalankan aplikasi
window.mainloop()