import time
from tkinter import Tk, Label, Entry, Button, Text, PhotoImage
from datetime import datetime
import random

# sample nama
sample_names = [
    "John Doe", "Jane Smith", "Michael Johnson", "Emily Davis", "David Lee",
    "Sophia Wilson", "James Brown", "Olivia Martinez", "Daniel Garcia", "Isabella Hernandez",
    "Liam Taylor", "Ava Anderson", "Noah Thomas", "Mia Jackson", "William White",
    "Amelia Harris", "Ethan Clark", "Charlotte Lewis", "Oliver Walker", "Harper Young"
]

# sample alamat
sample_addresses = [
    "Jl. Merdeka No. 1, Jakarta", "Jl. Sudirman No. 10, Bandung", "Jl. Raya Bogor No. 25, Surabaya",
    "Jl. Melati No. 5, Yogyakarta", "Jl. Pahlawan No. 8, Bali", "Jl. Kemenangan No. 12, Medan",
    "Jl. Satria No. 7, Makassar", "Jl. Hati No. 3, Malang", "Jl. Cendana No. 15, Semarang", 
    "Jl. Alami No. 6, Palembang"
]

# Dummy data
customers = [
    {
        "id": i,
        "name": random.choice(sample_names),
        "balance": (i % 10 + 1) * 100000,
        "address": random.choice(sample_addresses), 
        "created_at": datetime(2023, (i % 12) + 1, (i % 28) + 1).strftime("%Y-%m-%d")
    }
    for i in range(101, 201)
]

# Recursive search function
def search_customer_recursive(customers, id, index=0):
    if index >= len(customers):
        return None
    if customers[index]['id'] == id:
        return customers[index]
    return search_customer_recursive(customers, id, index + 1)

# Iterative search function
def search_customer_iterative(customers, id):
    i = 0
    while i < len(customers):
        if customers[i]['id'] == id:
            return customers[i]
        i += 1
    return None


# Function untuk memproses pencarian dan menampilkan informasi pelanggan
def process_customer_info(id, output_box):
    start_recursive = time.perf_counter()
    customer_recursive = search_customer_recursive(customers, id)
    end_recursive = time.perf_counter()

    start_iterative = time.perf_counter()
    customer_iterative = search_customer_iterative(customers, id)
    end_iterative = time.perf_counter()

    output_box.delete(1.0, "end")

    if not customer_recursive:
        output_box.insert("end", f"Error: ID {id} tidak ditemukan.\n")
        return

    # Tampilkan informasi nasabah
    output_box.insert("end", f"Nama: {customer_recursive['name']}\n")
    output_box.insert("end", f"Saldo: {customer_recursive['balance']}\n")
    output_box.insert("end", f"Alamat: {customer_recursive['address']}\n")  # Show the real address
    output_box.insert("end", f"Tanggal Dibuat: {customer_recursive['created_at']}\n")

    # Show running times in ms
    recursive_time_ms = (end_recursive - start_recursive) * 1000
    iterative_time_ms = (end_iterative - start_iterative) * 1000
    output_box.insert("end", f"Waktu Pencarian (Recursive): {recursive_time_ms:.3f} ms\n")
    output_box.insert("end", f"Waktu Pencarian (Iterative): {iterative_time_ms:.3f} ms\n")

# Setup UI
def setup_ui():
    def on_submit():
        try:
            id = int(entry_id.get())
            process_customer_info(id, output_box)
        except ValueError:
            output_box.delete(1.0, "end")
            output_box.insert("end", "Error: Input tidak valid. Pastikan ID adalah angka.\n")

    # Root window
    root = Tk()
    root.title("Informasi Nasabah")
    root.geometry("600x400")
    root.configure(bg="#f4f4f9")

    # 
    Label(root, text="Informasi Nasabah", font=("Helvetica", 18, "bold"), fg="#4CAF50", bg="#f4f4f9").grid(row=0, column=0, columnspan=2, pady=10)

    # Label
    Label(root, text="ID Nasabah:", font=("Arial", 12), fg="#333", bg="#f4f4f9").grid(row=1, column=0, padx=10, pady=5)
    entry_id = Entry(root, font=("Arial", 12), width=20, borderwidth=2, relief="solid", fg="#333", bg="#fff")
    entry_id.grid(row=1, column=1, padx=10, pady=5)

    # tampilan submit
    Button(root, text="Submit", font=("Arial", 12, "bold"), command=on_submit, bg="#4CAF50", fg="white", relief="raised", width=15).grid(row=2, column=0, columnspan=2, pady=10)

    # tampilan keluaran nya
    Label(root, text="Output:", font=("Arial", 12, "bold"), fg="#333", bg="#f4f4f9").grid(row=3, column=0, columnspan=2)
    output_box = Text(root, height=10, width=50, font=("Courier", 12), fg="#333", bg="#fff", wrap="word", padx=10, pady=10)
    output_box.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    # tombol keluar
    Button(root, text="Exit", font=("Arial", 12, "bold"), command=root.quit, bg="#f44336", fg="white", relief="raised", width=15).grid(row=5, column=0, columnspan=2, pady=10)

    root.mainloop()

# Run the UI
if __name__ == "__main__":
    setup_ui()
