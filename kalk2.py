import tkinter as tk

# Fungsi untuk menambahkan karakter ke dalam text widget
def click(text):
    current_text = output_display.get("1.0", tk.END).strip()  # Ambil teks dari Text
    output_display.delete("1.0", tk.END)  # Hapus teks lama
    output_display.insert(tk.END, current_text + text)  # Tambah teks baru

# Fungsi untuk menghitung hasil
def calculate():
    try:
        expression = output_display.get("1.0", tk.END).strip()  # Ambil ekspresi
        result = eval(expression)  # Perhitungan ekspresi matematika

        # Format hasil jika sangat besar
        if len(str(result)) > 10:  # Batasi panjang hasil
            result = "{:.5e}".format(result)  # Ubah ke format eksponensial

        output_display.delete("1.0", tk.END)  # Hapus teks lama
        output_display.insert(tk.END, str(result))  # Tampilkan hasil baru
    except Exception as e:
        output_display.delete("1.0", tk.END)
        output_display.insert(tk.END, "Error")

# Fungsi untuk menghapus isi text widget
def clear():
    output_display.delete("1.0", tk.END)

# Fungsi untuk menghapus karakter terakhir (backspace)
def backspace():
    current_text = output_display.get("1.0", tk.END).strip()  # Ambil teks dari Text
    new_text = current_text[:-1]  # Hapus karakter terakhir
    output_display.delete("1.0", tk.END)  # Hapus teks lama
    output_display.insert(tk.END, new_text)  # Tampilkan teks baru

# Fungsi untuk mencegah input langsung dari keyboard fisik
def disable_typing(event):
    return "break"  # Ini akan mencegah karakter apapun dimasukkan dari keyboard

# Membuat window utama
window = tk.Tk()
window.title("Kalkulator")

# Mengatur ukuran window menjadi dinamis
window.geometry("300x400")  # Atur ukuran awal window

# Membuat widget Text untuk menampilkan ekspresi dan hasil (multi-line)
output_display = tk.Text(window, font=('Arial', 18), height=3, width=16, borderwidth=2, relief="solid")
output_display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Mencegah pengguna mengetik langsung ke Text
output_display.bind("<Key>", disable_typing)

# Tombol-tombol kalkulator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0, 2), ('<', 5, 2, 2)  # Tombol Clear dan Backspace
]

# Membuat tombol-tombol
for (text, row, column, *colspan) in buttons:
    button = tk.Button(window, text=text, font=('Arial', 18))
    if text == 'C':
        button.config(command=clear)
    elif text == '=':
        button.config(command=calculate)
    elif text == '<':
        button.config(command=backspace)
    else:
        button.config(command=lambda t=text: click(t))
    button.grid(row=row, column=column, columnspan=colspan[0] if colspan else 1, sticky="nsew", padx=2, pady=2)

# Mengatur setiap baris dan kolom agar bisa berubah ukuran
for i in range(6):  # 5 baris tombol + 1 baris Text
    window.grid_rowconfigure(i, weight=1)

for i in range(4):  # 4 kolom tombol
    window.grid_columnconfigure(i, weight=1)

# Menjalankan aplikasi
window.mainloop()
