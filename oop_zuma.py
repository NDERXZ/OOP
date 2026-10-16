class KodokJuma:
    def __init__(self, warna_awal):
        self.warna_peluru = warna_awal
        self.skor = 0
        self.is_active = True

    def ganti_warna(self, warna_baru):
        self.warna_peluru = warna_baru
        print(f"Warna peluru diganti menjadi: {self.warna_peluru}")

    def tembak(self):
        self.skor += 50
        print(f"Katak menembak bola {self.warna_peluru}! (+50 poin)")

    def info_status(self):
        print(f"Kodok gwa: Warna Peluru: {self.warna_peluru} | Skor: {self.skor} | Aktif: {self.is_active}")


kodok = KodokJuma("Hijau")

print("Kondisi Awal:")
kodok.info_status()
print()

kodok.ganti_warna("Merah")
kodok.tembak()
print()

print("Kondisi Akhir:")
kodok.info_status()
