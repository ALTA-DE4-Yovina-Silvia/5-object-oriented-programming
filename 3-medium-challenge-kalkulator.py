def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    return a // b  # Menggunakan pembagian bulat

def utama():
    # Input angka untuk setiap operasi
    a, b = 3, 4
    c, d = 15, 4
    e, f = 10, 10
    g, h = 12, 3
    
    # Melakukan operasi
    hasil_penjumlahan = penjumlahan(a, b)
    hasil_pengurangan = pengurangan(c, d)
    hasil_perkalian = perkalian(e, f)
    hasil_pembagian = pembagian(g, h)
    
    # Menampilkan hasil
    print(f"Penjumlahan: {hasil_penjumlahan}")
    print(f"Pengurangan: {hasil_pengurangan}")
    print(f"Perkalian: {hasil_perkalian}")
    print(f"Pembagian: {hasil_pembagian}")

if __name__ == "__main__":
    utama()



