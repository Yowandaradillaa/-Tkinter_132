#Mengimpor mode tinker untuk membuat gui, dan mengimpor message box
import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try:
        for entry in entries:
            nilai = int(entry.get()) #Mengambil nilai dari setiap entry dan mengkonversi ke integer
            if not (0 <= nilai <= 100): #Memastikan inputan antara angka 0 sampai 100
                raise ValueError("Nilai harus antara 0 dan 100.")

        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi") #Menampilkan hasil prediksi
    except ValueError as ve:
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.") #Menampilkan pesan error jika inputan tidak sesuai

# Inisialisasi Tkinter
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600") # Mengatur ukuran jendela menjadi lebar 500 dan tinggi 600 piksel
root.configure(bg="white") # Mengatur warna latar belakang jendela menjadi putih

# Memasukan Label Judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="white")
judul_label.pack(pady=20) # Menempatkan label judul dengan jarak vertikal 20 piksel

# Memasukan Frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="white")
frame_input.pack(pady=10)  # Menempatkan frame dengan jarak vertikal 10 piksel

# List untuk menyimpan entry nilai
entries = []
for i in range(10): #Perulangan untuk membuat inputan 10
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}:", font=("Arial", 12), bg="white")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Tombol untuk menampilkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold")) # Membuat tombol untuk hasil prediksi dengan memanggil fungsi hasil_prediksi saat diklik
prediksi_button.pack(pady=30) # Menempatkan tombol dengan jarak vertikal 30 piksel


# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14), fg="blue", bg="white")  # Membuat label kosong untuk menampilkan hasil prediksi dengan teks biru
hasil_label.pack(pady=20) # Menempatkan label hasil dengan jarak vertikal 20 piksel

# Menjalankan aplikasi
root.mainloop() # Menjalankan loop utama Tkinter untuk memulai aplikasi GUI