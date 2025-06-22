import pandas as pd
import numpy as np # Ditambahkan untuk menangani np.nan saat replace 8888
import os
import glob

# --- Pengaturan Path yang Profesional ---
# (Bagian ini sudah benar dan tidak perlu diubah)
SCRIPT_PATH = os.path.realpath(__file__)
SRC_DIR = os.path.dirname(SCRIPT_PATH)
ROOT_DIR = os.path.dirname(SRC_DIR)
folder_input = os.path.join(ROOT_DIR, 'data', 'data_bulanan_csv')
file_output = os.path.join(ROOT_DIR, 'data', 'data_hujan_gorontalo_5tahun.csv')
# ----------------------------------------

semua_file = glob.glob(os.path.join(folder_input, "*.csv"))
list_df = []

print(f"Menemukan {len(semua_file)} file untuk digabungkan...")

for file in semua_file:
    try:
        df_bulan = pd.read_csv(
            file,
            # sep=';',
            decimal='.',
            # na_values=['8888']
        )
        
        if len(df_bulan.columns) >= 2:
            df_bulan = df_bulan.iloc[:, :2]  # Ambil hanya 2 kolom pertama
            df_bulan.columns = ['tanggal', 'curah_hujan']
            list_df.append(df_bulan)
        else:
            print(f"Peringatan: File {os.path.basename(file)} tidak memiliki minimal 2 kolom.")
            continue

        print(f"Berhasil membaca file: {os.path.basename(file)}")
    except Exception as e:
        print(f"Gagal membaca file {os.path.basename(file)} karena error: {e}")

if list_df:
    df_gabungan = pd.concat(list_df, ignore_index=True)

    print("\nProses pembersihan data gabungan...")

    # --- Pembersihan Akhir yang Disederhanakan ---
    
    # 1. Hapus baris yang kolom 'tanggal'-nya kosong (jika ada)
    # Sekarang kita menggunakan nama kolom 'tanggal' (huruf kecil) yang sudah kita standarkan
    df_gabungan.dropna(subset=['tanggal'], inplace=True)
    
    # 2. Ubah kolom 'tanggal' menjadi format datetime yang benar
    # Tangani error jika ada format tanggal yang tidak sesuai
    df_gabungan['tanggal'] = pd.to_datetime(df_gabungan['tanggal'], format='%d-%m-%Y', errors='coerce')
    # Hapus baris yang gagal diubah tanggalnya
    df_gabungan.dropna(subset=['tanggal'], inplace=True)

    # 3. Urutkan seluruh data berdasarkan tanggal
    df_gabungan.sort_values(by='tanggal', inplace=True)
    
    # 4. (Tidak diperlukan lagi) Bagian rename sudah dilakukan di dalam loop.
    
    # 5. Simpan dataframe yang sudah bersih dan terurut ke file CSV baru
    df_gabungan.to_csv(file_output, index=False)

    print(f"\nBerhasil! Semua data telah digabungkan dan disimpan sebagai '{file_output}'.")
    print(f"Total baris data gabungan: {len(df_gabungan)}")
    print("Contoh data gabungan:")
    print(df_gabungan.head())
else:
    print("Tidak ada file yang bisa digabungkan. Pastikan file CSV ada di dalam folder 'data_bulanan_csv'.")