class orang:
    def __init__(self, nama):
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        self.is_running = True
        self.skor += 50
        print(f"{self.nama} Ceritanya mulai lari (+50 skor)")

    def ambil_koin(self, jumlah):
        self.koin += jumlah
        self.skor += jumlah * 10
        print(f"{self.nama} Ceritanya ngambil {jumlah} koin! (Total koin: {self.koin})")

    def tabrak_rintangan(self):
        self.is_running = False
        print(f"Si {self.nama} Nabrak kereta njirr, kalah dehh")

    def info_player(self):
        print(f"Ingfo:  Nama: {self.nama} | Skor: {self.skor} | Koin: {self.koin} | Lari: {self.is_running}")


player1 = orang("Rusdi")

print("Kondisi Awal:")
player1.info_player()
print()

player1.berlari()
player1.ambil_koin(15)
print()

print("Kondisi Saat Berlari:")
player1.info_player()
print()

player1.tabrak_rintangan()
print()

print("Kondisi Akhir:")
player1.info_player()
