# 🎮 GAME RPG SEDERHANA - KURANG DARI 50 BARIS! 🎮
import random

# 4 VARIABEL UTAMA KARAKTER
nama = input("Masukkan nama pahlawanmu: ")
darah = 100    # Health Point
mp = 50        # Magic Point  
speed = 5      # Kecepatan
level = 1      # Level karakter

print(f"✨ Pahlawan {nama} siap bertualang!")
print(f"❤️ Darah: {darah} | 💙 MP: {mp} | ⚡ Speed: {speed}")

# GAME LOOP UTAMA
while darah > 0:
    print(f"\n=== STATUS {nama} ===")
    print(f"❤️ HP: {darah} | 💙 MP: {mp} | ⚡ Speed: {speed} | 📊 Level: {level}")
    
    print("\n1. ⚔️ Lawan Monster")
    print("2. 🏕️ Istirahat") 
    print("3. 🚪 Keluar")
    
    pilihan = input("Pilih: ")
    
    if pilihan == "1":
        # BERTARUNG DENGAN MONSTER
        monsters = ["Slime", "Goblin", "Orc"]
        monster = random.choice(monsters)
        monster_hp = random.randint(20, 60)
        
        print(f"\n⚔️ {monster} muncul! HP: {monster_hp}")
        
        while monster_hp > 0 and darah > 0:
            print("\n1. Serang (20 damage)")
            print("2. Sihir (40 damage, -10 MP)")
            
            aksi = input("Aksi: ")
            
            if aksi == "1":
                damage = 20 + speed
                monster_hp -= damage
                print(f"⚔️ Kamu serang! Monster -{damage} HP")
                
            elif aksi == "2" and mp >= 10:
                damage = 40 + speed  
                monster_hp -= damage
                mp -= 10
                print(f"🔥 Serangan sihir! Monster -{damage} HP")
                
            else:
                print("❌ Tidak bisa! MP kurang atau pilihan salah")
                continue
            
            if monster_hp <= 0:
                print(f"🎉 {monster} kalah!")
                mp += 10  # Bonus MP
                if random.randint(1,3) == 1:  # 33% chance level up
                    level += 1
                    speed += 1
                    darah = 100  # Full heal saat level up
                    print(f"🆙 LEVEL UP! Level {level}, Speed {speed}")
                break
                
            # Monster menyerang balik
            damage_monster = random.randint(10, 20) - (speed // 2)
            damage_monster = max(5, damage_monster)
            darah -= damage_monster
            print(f"🐉 {monster} serang! Kamu -{damage_monster} HP")
    
    elif pilihan == "2":
        # ISTIRAHAT
        heal = random.randint(20, 40)
        mp_heal = random.randint(10, 20)
        darah = min(100, darah + heal)
        mp = min(50, mp + mp_heal)
        print(f"🏕️ Istirahat! +{heal} HP, +{mp_heal} MP")
        
    elif pilihan == "3":
        print(f"� Sampai jumpa {nama}! Level akhir: {level}")
        break
        
    else:
        print("❌ Pilihan salah!")

if darah <= 0:
    print(f"\n💀 GAME OVER! {nama} kalah di level {level}")
    
print("🎮 Terima kasih sudah bermain!")