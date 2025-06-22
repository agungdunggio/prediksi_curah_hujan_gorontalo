import pandas as pd
import os

# --- PENGATURAN ---
# Tentukan path ke folder yang berisi file-file XLSX Anda
folder_input = 'data/data_bulanan'

# Tentukan path ke folder tempat Anda ingin menyimpan file-file CSV
folder_output = 'data/data_bulanan_csv'
# --------------------

# --- Inisialisasi Penghitung ---
jumlah_berhasil = 0
jumlah_gagal = 0
# ---------------------------------

# Membuat folder output jika belum ada
if not os.path.exists(folder_output):
    os.makedirs(folder_output)
    print(f"Folder output '{folder_output}' telah dibuat.")

# Mendapatkan daftar semua file dalam folder input
try:
    daftar_file = os.listdir(folder_input)
except FileNotFoundError:
    print(f"❌ ERROR: Folder input '{folder_input}' tidak ditemukan. Mohon periksa kembali path-nya.")
    exit()

# Loop melalui setiap file di dalam folder input
for nama_file in daftar_file:
    if nama_file.endswith('.xlsx'):
        path_file_input = os.path.join(folder_input, nama_file)
        nama_file_output = os.path.splitext(nama_file)[0] + '.csv'
        path_file_output = os.path.join(folder_output, nama_file_output)

        try:
            # Membaca file xlsx
            df = pd.read_excel(path_file_input)
            # Menyimpan ke file csv
            df.to_csv(path_file_output, index=False)
            print(f"✅ BERHASIL: '{nama_file}' telah dikonversi ke '{nama_file_output}'")
            # Tambahkan 1 ke penghitung berhasil
            jumlah_berhasil += 1

        except Exception as e:
            print(f"❌ GAGAL: Tidak dapat mengonversi '{nama_file}'. Error: {e}")
            # Tambahkan 1 ke penghitung gagal
            jumlah_gagal += 1

print("\n--- PROSES SELESAI ---")
# --- Cetak Ringkasan Hasil ---
print(f"Ringkasan:")
print(f"   - Berhasil dikonversi: {jumlah_berhasil} file")
print(f"   - Gagal dikonversi   : {jumlah_gagal} file")
# ----------------------------