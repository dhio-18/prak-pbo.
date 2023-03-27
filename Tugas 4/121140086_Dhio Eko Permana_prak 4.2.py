class Robot:

    jumlah_turn = 0
    turn1 = 0
    turn2 = 0
    turn3 = 0
    turn4 = 0
    def __init__(self, nama, health, damage):
        self.nama = nama
        self.health = health
        self.damage = damage

    def lakukan_aksi(self, nama, status):  
        if nama == "Antares":
            self.turn1 += 1 
            print(f"({nama}) serangan ke-{self.turn1}")
            if self.turn1 == 3:
                damage = self.damage * 1.5  
                self.turn1 = 0
            else:
                damage = self.damage
            

        elif nama == "Alphasetia":
            self.turn2 += 1
            print(f"({nama}) serangan ke-{self.turn2}")
            if self.turn2== 2:
                self.health += 4000  
                if status == 1:
                    print(f'Robotmu ({nama}) menambah darah sebanyak 4000 HP')
                elif status == 2:
                    print(f'Robot lawan ({nama}) menambah darah sebanyak 4000 HP')
                self.turn2 = 0
            damage = self.damage

        elif nama == "Lecalicus":
            self.turn3 += 1
            print(f"({nama}) serangan ke-{self.turn3}")
            if self.turn3 > 4:
                self.health += 7000
                if status == 1:
                    print(f'Robotmu ({nama}) menambah darah sebanyak 7000 HP')
                elif status == 2:
                    print(f'Robot lawan ({nama}) menambah darah sebanyak 7000 HP')
                damage = self.damage * 2
                self.turn3 = 0
            else:
                damage = self.damage
        return damage
        

    def terima_aksi(self, damage, status, nama):
        self.health -= damage
        if status == 1:
            print(f'Robotmu ({nama}) menyerang sebanyak {int(damage)} DMG')
            print()
        elif status == 2:
            print(f'Robot lawan ({nama}) menyerang sebanyak {int(damage)} DMG')
            print()

class Antares(Robot):

    def __init__(self, nama, health, damage):
        super().__init__(nama, health, damage)
        

class Alphasetia(Robot):

    def __init__(self, nama, health, damage):
        super().__init__( nama, health, damage)


class Lecalicus(Robot):

    def __init__(self, nama, health, damage):
        super().__init__( nama, health, damage)


def pertandingan(robot1, robot2):
    while True:
        if robot1.health <= 0:
            print(f"Robot lawan {robot2.nama} menang")
        if robot1.health <= 0 or robot2.health <= 0:
            break

        robot1.jumlah_turn += 1
        robot2.jumlah_turn += 1

        print(f'Turn saat ini: {robot1.jumlah_turn}')
        print(f'Robotmu ({robot1.nama} - {int(robot1.health)} HP), robot lawan ({robot2.nama} - {int(robot2.health)} HP)')

        input_p1 = int(input(f'Pilih tangan robotmu ({robot1.nama}): '))
        input_p2 = int(input(f'Pilih tangan robot lawan ({robot2.nama}): '))

        if (input_p1 == 1 and input_p2 == 3) or (input_p1 == 2 and input_p2 == 1) or (input_p1 == 3 and input_p2 == 2):
            aksi1 = robot1.lakukan_aksi(robot1.nama, 1)
            robot2.terima_aksi(aksi1, 1,robot1.nama)
        elif (input_p2 == 1 and input_p1 == 3) or (input_p2 == 2 and input_p1 == 1) or (input_p2 == 3 and input_p1 == 2):
            aksi2 = robot2.lakukan_aksi(robot2.nama, 2)
            robot1.terima_aksi(aksi2, 2, robot2.nama)
        elif (input_p2 == 1 and input_p1 == 1) or (input_p2 == 2 and input_p1 == 2) or (input_p2 == 3 and input_p1 == 3):
            print("Draw Try Again!!!!!!")

print('Selamat datang di pertandingan robot Yamako')


input_rob1 = int(input('Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): '))

if input_rob1 == 1:
    r1 = Antares('Antares', 50000, 5000)
elif input_rob1 == 2:
    r1 = Alphasetia('Alphasetia', 40000, 6000)
elif input_rob1 == 3:
    r1 = Lecalicus('Lecalicus', 45000, 5500)

input_rob2 = int(input("Pilih lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
if input_rob2 == 1:
    r2 = Antares('Antares', 50000, 5000)
elif input_rob2 == 2:
    r2 = Alphasetia('Alphasetia', 40000, 6000)
elif input_rob2 == 3:
    r2 = Lecalicus('Lecalicus', 45000, 5500)
print()

pertandingan(r1, r2)