import tkinter as tk

def hitung_total():
    harga = int(entry_harga.get())
    qty = int(entry_qty.get())
    total = harga * qty
    label_total.config(text=f"Total: Rp {total:,}")

window = tk.Tk()
window.title("Program Kasir")

tk.Label(window, text="Harga").pack()
entry_harga = tk.Entry(window)
entry_harga.pack()
tk.Label(window, text="Kuantitas").pack()
entry_qty = tk.Entry(window)
entry_qty.pack()

tk.Button(window, text="Hitung Total", command=hitung_total).pack(pady=5)

label_total = tk.Label(window, text="Total: Rp 0")
label_total.pack()

window.mainloop()