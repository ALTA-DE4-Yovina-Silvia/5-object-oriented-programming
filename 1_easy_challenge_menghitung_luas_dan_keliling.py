import math

class BangunDatar:
    def luas(self):
        pass
    
    def keliling(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi
    
    def luas(self):
        return self.sisi ** 2
    
    def keliling(self):
        return 4 * self.sisi

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def luas(self):
        return 0.5 * self.alas * self.tinggi
    
    def keliling(self):
        # Hitung sisi miring dengan rumus Pythagoras
        sisi_miring = math.sqrt(self.alas ** 2 + self.tinggi ** 2)
        return self.alas + self.tinggi + sisi_miring
    
class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def luas(self):
        return self.panjang * self.lebar
    
    def keliling(self):
        return 2 * (self.panjang + self.lebar)

def utama():
    bangun_datar = {
        "Persegi": Persegi(4),
        "Segitiga": Segitiga(3, 4),
        "Persegi Panjang": PersegiPanjang(7, 8)
    }
    
    print("Luas")
    for nama, bangun in bangun_datar.items():
        print(f"{nama}: {bangun.luas()}")
    
    print("Keliling")
    for nama, bangun in bangun_datar.items():
        print(f"{nama}: {bangun.keliling()}")

if __name__ == "__main__":
    utama()
