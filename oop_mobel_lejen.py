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
