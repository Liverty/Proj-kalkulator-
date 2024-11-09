import tkinter as tk

# Fungsi untuk menambahkan angka/operasi ke layar
def click(text):
    current_text = output_display.cget("text")
    output_display.config(text=current_text + str(text))

# Fungsi untuk menghitung hasil ekspresi matematika
def calculate():
    try:
        expression = output_display.cget("text")
        expression = expression.replace('%', '/100')  # Ganti % dengan /100 untuk kalkulasi
        result = eval(expression)
        output_display.config(text=str(result))
    except:
        output_display.config(text="Error")

# Fungsi untuk membersihkan layar
def clear():
    output_display.config(text="")

# Fungsi untuk mengubah tanda plus-minus
def plus_minus():
    current_text = output_display.cget("text")
    if current_text:
        try:
            result = str(eval(f"-1*({current_text})"))
            output_display.config(text=result)
        except:
            output_display.config(text="Error")

# Inisialisasi jendela utama
window = tk.Tk()
window.title("Kalkulator")
window.geometry("300x400")  # Ukuran jendela
window.resizable(False, False)
window.config(bg="black")  # Latar belakang hitam

# Frame untuk judul dan layar
frame = tk.Frame(window, bg="black")
frameB = tk.Frame(window, bg="black")

# Label untuk judul
label = tk.Label(frame, text="Kalkulator guntur", font=('Arial', 14, 'bold'), anchor='center', fg="white", bg="black")
label.pack(padx=10, pady=10)

# Label untuk menampilkan ekspresi dan hasil
output_display = tk.Label(frame, font=('Arial', 20), height=2, width=18, bg="grey", fg="white", anchor='e')
output_display.pack(padx=10, pady=10)

# Pengaturan grid tombol
buttons = [
    ('AC', 1, 0), ('±', 1, 1), ('%', 1, 2), ('/', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0, 2), ('.', 5, 2), ('=', 5, 3)
]

# Membuat dan menempatkan tombol
for (text, row, column, *colspan) in buttons:
    button = tk.Button(
        frameB, text=text, font=('Arial', 18, 'bold'),
        bg="dark grey" if text.isdigit() or text == '.' else "orange",
        fg="white", bd=1
    )
    if text == 'AC':
        button.config(command=clear)
    elif text == '=':
        button.config(command=calculate)
    elif text == '±':
        button.config(command=plus_minus)
    elif text == '%':
        button.config(command=lambda: click('%'))
    else:
        button.config(command=lambda t=text: click(t))
    
    button.grid(row=row, column=column, columnspan=(colspan[0] if colspan else 1), sticky="nsew", padx=5, pady=5)

# Konfigurasi row dan column
for i in range(6):
    frameB.grid_rowconfigure(i, weight=1)

for i in range(4):
    frameB.grid_columnconfigure(i, weight=1)

# Memasukkan frame ke window
frame.pack()
frameB.pack()

# Menjalankan program utama
window.mainloop()