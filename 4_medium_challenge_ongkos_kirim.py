class Barang:
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

    def hitung_harga(self):
        volume = self.hitung_volume()
        harga_standar = 5000
        harga_berat_pembulatan = 5000

        if volume >= 50 and self.berat >= 1:
            return harga_standar
        else:
            return harga_berat_pembulatan

def utama():
    panjang = 5
    lebar = 2
    tinggi = 4
    berat = 1  # dalam kg

    barang = Barang(panjang, lebar, tinggi, berat)
    harga = barang.hitung_harga()

    print(f"Panjang = {panjang} cm")
    print(f"Lebar = {lebar} cm")
    print(f"Tinggi = {tinggi} cm")
    print(f"Berat = {berat} kg")
    print(f"Harga: Rp. {harga}")

if __name__ == "__main__":
    utama()
