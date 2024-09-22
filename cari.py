import os
import fnmatch

def find_files_with_extension(root_folder, extension):
    """Mencari file dengan ekstensi tertentu di seluruh folder"""
    files_with_extension = []
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith(extension):
                files_with_extension.append(os.path.join(root, file))
    return files_with_extension

def search_words_in_files(files, keywords):
    """Mencari kata dalam daftar file dan mencetak hasil dengan warna pada nomor baris dan nama file"""
    line_color = '\033[92m'  # Hijau untuk nomor baris
    file_color = '\033[94m'  # Biru untuk nama file
    reset_color = '\033[0m'  # Reset warna

    keywords = [keyword.strip() for keyword in keywords.split('*')]

    found = False
    for name in files:
        with open(name, mode='r', encoding='utf-8', errors='ignore') as file:
            data = file.readlines()

        for i, line in enumerate(data):
            if all(keyword in line for keyword in keywords):
                print(f'{line_color}Line {i+1}{reset_color} in {file_color}{name}{reset_color}: {line.strip()}')
                found = True
    
    if not found:
        print("Tidak ditemukan.")

# Folder root (direktori tempat script dijalankan)
root_folder = os.getcwd()

# Mencari semua file .py di seluruh folder
marge_file_name = find_files_with_extension(root_folder, '.py')

while True:
    # Meminta kata yang ingin dicari dari pengguna
    user_input = input("\nMasukkan kata kunci (Gunakan '*' sebagai pengganti kata atau 'q' untuk keluar): ")

    if user_input.lower() == 'q':
        break

    # Memecah input berdasarkan '*' dan mencari semua kata
    search_words_in_files(marge_file_name, user_input)
