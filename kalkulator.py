from tkinter import *

# Inisialisasi window
window = Tk()
window.title("Kalkulator")
window.geometry("300x400")  # Ukuran window tetap
window.resizable(False, False)

frame = Frame(window, bg="black")
frameB = Frame(window, bg="black")

# Label untuk judul
label = Label(frame, text="Kalkulator Idzhar", font=('google', 14, 'bold'), anchor='center', fg="white", bg="black")

# Fungsi untuk operasi kalkulator
def anjing(item):
    global ekspresi
    ekspresi += str(item)
    inputT.set(ekspresi)

def clear():
    global ekspresi
    ekspresi = ""
    inputT.set("")

def enter():
    global ekspresi
    try:
        # Mengganti "%" dengan "/100" untuk perhitungan
        ekspresi = ekspresi.replace('%', '/100')
        equal = str(eval(ekspresi))
        inputT.set(equal)
        ekspresi = ""
    except:
        inputT.set("Error")
        ekspresi = ""

# Fungsi untuk operasi khusus (tanpa langsung menghitung %)
def persen():
    global ekspresi
    ekspresi += "%"
    inputT.set(ekspresi)

def plus_minus():
    global ekspresi
    if ekspresi:
        ekspresi = str(eval(f"-1*({ekspresi})"))
        inputT.set(ekspresi)

# Inisialisasi variabel ekspresi
ekspresi = ""
inputT = StringVar()

# Label untuk output
label3 = Label(frame, textvariable=inputT, font=("google", 20), anchor='e', width=22, bg="grey", fg="white")

# Tombol-tombol kalkulator
button_ac = Button(frameB, text="AC", bg="grey", fg="white", font=('google', 12, 'bold'), width=5, height=2, command=lambda: clear())
button_plus_minus = Button(frameB, text="±", bg="grey", fg="white", font=('google', 12, 'bold'), width=5, height=2, command=lambda: plus_minus())
button_persen = Button(frameB, text="%", bg="grey", fg="white", font=('google', 12, 'bold'), width=5, height=2, command=lambda: persen())
button_divide = Button(frameB, text="/", bg="orange", fg="white", font=('google', 12, 'bold'), width=5, height=2, command=lambda: anjing("/"))
button_multiply = Button(frameB, text="*", bg="orange", fg="white", font=('google', 12, 'bold'), width=5, height=2, command=lambda: anjing("*"))
button_subtract = Button(frameB, text="-", bg="orange", fg="white", font=('google', 12, 'bold'), width=5, height=2, command=lambda: anjing("-"))
button_add = Button(frameB, text="+", bg="orange", fg="white", font=('google', 12, 'bold'), width=5, height=2, command=lambda: anjing("+"))
button_equals = Button(frameB, text="=", bg="orange", fg="white", font=('google', 12, 'bold'), width=5, height=2, command=lambda: enter())

# Tombol angka
button0 = Button(frameB, text="0", bg="dark grey", fg="white", font=('google', 12, 'bold'), width=13, height=2, command=lambda: anjing(0))  # Lebih lebar
button1 = Button(frameB, text="1", bg="dark grey", fg="white", font=('google', 12, 'bold'), width=5, height=2, command=lambda: anjing(1))
button2 = Button(frameB, text="2", bg="dark grey", fg="white", font=('google', 12, 'bold'), width=5, height=2, command=lambda: anjing(2))
button3 = Button(frameB, text="3", bg="dark grey", fg="white", font=('google', 12, 'bold'), width=5, height=2, command=lambda: anjing(3))
button4 = Button(frameB, text="4", bg="dark grey", fg="white", font=('google', 12, 'bold'), width=5, height=2, command=lambda: anjing(4))
button5 = Button(frameB, text="5", bg="dark grey", fg="white", font=('google', 12, 'bold'), width=5, height=2, command=lambda: anjing(5))
button6 = Button(frameB, text="6", bg="dark grey", fg="white", font=('google', 12, 'bold'), width=5, height=2, command=lambda: anjing(6))
button7 = Button(frameB, text="7", bg="dark grey", fg="white", font=('google', 12, 'bold'), width=5, height=2, command=lambda: anjing(7))
button8 = Button(frameB, text="8", bg="dark grey", fg="white", font=('google', 12, 'bold'), width=5, height=2, command=lambda: anjing(8))
button9 = Button(frameB, text="9", bg="dark grey", fg="white", font=('google', 12, 'bold'), width=5, height=2, command=lambda: anjing(9))

# Tombol tambahan
button_dot = Button(frameB, text=".", bg="dark grey", fg="white", font=('google', 12, 'bold'), width=5, height=2, command=lambda: anjing("."))

# Mengatur posisi tombol pada grid
button_ac.grid(row=1, column=0, pady=5, padx=2)
button_plus_minus.grid(row=1, column=1, pady=5, padx=2)
button_persen.grid(row=1, column=2, pady=5, padx=2)
button_divide.grid(row=1, column=3, pady=5, padx=2)

button7.grid(row=2, column=0, pady=5, padx=2)
button8.grid(row=2, column=1, pady=5, padx=2)
button9.grid(row=2, column=2, pady=5, padx=2)
button_multiply.grid(row=2, column=3, pady=5, padx=2)

button4.grid(row=3, column=0, pady=5, padx=2)
button5.grid(row=3, column=1, pady=5, padx=2)
button6.grid(row=3, column=2, pady=5, padx=2)
button_subtract.grid(row=3, column=3, pady=5, padx=2)

button1.grid(row=4, column=0, pady=5, padx=2)
button2.grid(row=4, column=1, pady=5, padx=2)
button3.grid(row=4, column=2, pady=5, padx=2)
button_add.grid(row=4, column=3, pady=5, padx=2)

button0.grid(row=5, column=0, columnspan=2, pady=5, padx=2)  # Lebih lebar
button_dot.grid(row=5, column=2, pady=5, padx=2)
button_equals.grid(row=5, column=3, pady=5, padx=2)

# Memasukkan label dan frame ke window
label.pack(padx=10, pady=10)
label3.pack(padx=10, pady=10)

frame.pack()
frameB.pack()

window.mainloop()