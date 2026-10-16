# """
# Contoh Penerapan 4 Pilar Utama Object-Oriented Programming (OOP):
# 1. Abstraction (Abstraksi)
# 2. Encapsulation (Enkapsulasi)
# 3. Inheritance (Pewarisan)
# 4. Polymorphism (Polimorfisme)
# """

# from abc import ABC, abstractmethod


# # 1. ABSTRACTION (Kelas Abstrak sebagai Blueprint)
# class Hewan(ABC):
#     def __init__(self, nama: str):
#         # 2. ENCAPSULATION (Atribut terlindungi / protected)
#         self._nama = nama

#     @property
#     def nama(self) -> str:
#         """Getter untuk membaca atribut _nama dengan aman."""
#         return self._nama

#     @abstractmethod
#     def bersuara(self) -> str:
#         """Metode abstrak yang wajib diimplementasikan oleh kelas turunan."""
#         pass


# # 3. INHERITANCE (Pewarisan sifat dari Hewan ke Kucing)
# class Kucing(Hewan):
#     def __init__(self, nama: str, ras: str):
#         super().__init__(nama)
#         self.ras = ras

#     # 4. POLYMORPHISM (Implementasi khusus metode bersuara untuk Kucing)
#     def bersuara(self) -> str:
#         return f"{self.nama} (Kucing {self.ras}): Meong! Meong!"


# # 3. INHERITANCE (Pewarisan sifat dari Hewan ke Anjing)
# class Anjing(Hewan):
#     def __init__(self, nama: str):
#         super().__init__(nama)

#     # 4. POLYMORPHISM (Implementasi khusus metode bersuara untuk Anjing)
#     def bersuara(self) -> str:
#         return f"{self.nama} (Anjing): Guk! Guk!"


# # --- PENGGUNAAN (Instansiasi Objek) ---
# def cetak_suara_hewan(hewan: Hewan):
#     """
#     Polymorphism: Menerima objek turunan Hewan apa saja dan
#     memanggil fungsi bersuara() tanpa perlu tahu jenis hewan spesifiknya.
#     """
#     print(hewan.bersuara())


# if __name__ == "__main__":
#     kucing1 = Kucing(nama="Milo", ras="Anggora")
#     anjing1 = Anjing(nama="Buddy")

#     cetak_suara_hewan(kucing1)  # Output: Milo (Kucing Anggora): Meong! Meong!
#     cetak_suara_hewan(anjing1)  # Output: Buddy (Anjing): Guk! Guk!


class Karakter:
    def __init__(self, role, nama, hp, attack_power):
        self.nama = nama
        self.hp = hp
        self.attack_power = attack_power
        self.role = role
      
    def serang(self, target):
        damage = self.attack_power
        target.terima_damage(damage)
        print(f"⚔️ {self.nama} menyerang {target.nama} sebesar {damage} DMG!")

    def terima_damage(self, jumlah):
        self.hp -= jumlah
        if self.hp < 0:
            self.hp = 0

    def masih_hidup(self):
        return self.hp > 0

k1 = Karakter("Ksatria", "Fighter", 100, 20)
k2 = Karakter("Goblin", "Mage", 80, 15)
Miya = Karakter("Miya", "Marksman", 75, 100)

print("Okehh langsung saja dar")
print(f"{k1.nama} (HP: {k1.hp}) vs {k2.nama} (HP: {k2.hp})\n")

k1.serang(k2)
print(f"Status: {k2.nama} tersisa HP: {k2.hp}\n")
