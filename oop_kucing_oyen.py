class KucingOyen:
    def __init__(self, puwqi):
        self.nama = puwqi
        self.lapar = 50
        self.energi = 70
        self.is_happy = True

    def beri_makan(self, makanan):
        self.lapar -= 30
        if self.lapar < 0:
            self.lapar = 0
        print(f"{self.nama} makan {makanan} dengan lahap! (Lapar turun jadi: {self.lapar})")

    def ajak_main(self):
        if self.energi >= 20:
            self.energi -= 20
            self.lapar += 15
            self.is_happy = True
            print(f"{self.nama} diajak main lari-larian! Senang tapi agak capek.")
        else:
            self.is_happy = False
            print(f"{self.nama} kecapekan dan gamau gerak, pengen rebahan.")

    def tidur(self):
        self.energi = 100
        print(f"Zzz... {self.nama} tidur nyenyak. (Energi full 100%)")

    def info_kucing(self):
        mood = "Bahagia" if self.is_happy else "Ngambek / Capek"
        print(f"Info Kucing -> Nama: {self.nama} | Lapar: {self.lapar} | Energi: {self.energi} | Mood: {mood}")


kucing1 = KucingOyen("Puwqi")

print("Kondisi Awal:")
kucing1.info_kucing()
print()

kucing1.beri_makan("Ikan Tongkol")
kucing1.ajak_main()
print()

print("Kondisi Setelah Main:")
kucing1.info_kucing()
print()

kucing1.tidur()
print()

print("Kondisi Akhir:")
kucing1.info_kucing()
