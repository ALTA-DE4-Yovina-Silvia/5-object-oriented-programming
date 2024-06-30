import math

class BangunRuang:
    def volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi
    
    def volume(self):
        return self.sisi ** 3

class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    
    def volume(self):
        return self.panjang * self.lebar * self.tinggi

class Tabung(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi
    
    def volume(self):
        return int(math.pi * (self.jari_jari ** 2) * self.tinggi)

def utama():
    bangun_ruang = {
        "Kubus": Kubus(10),
        "Balok": Balok(3, 6, 10),
        "Tabung": Tabung(7, 10)
    }
    
    print("Volume")
    for nama, bangun in bangun_ruang.items():
        print(f"{nama}: {bangun.volume()}")

if __name__ == "__main__":
    utama()

