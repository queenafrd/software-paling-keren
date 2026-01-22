import random

print("Selamat datang di Game Matematika Sederhana!")
print("Jawab soal penjumlahan dan pengurangan.")
print("Ada 5 soal. Mari mulai!\n")

skor = 0
jumlah_soal = 5

for i in range (jumlah_soal):
    # Generate angka acak antara 1-20
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    # Pilih operator
    operator = random.choice(['+', '-'])
    
    # Pastikan pengurangan tidak menghasilkan negatif
    if operator == '-' and a < b:
        a, b = b, a
    
    # Hitung jawaban benar
    if operator == '+':
        jawaban_benar = a + b
    else:
        jawaban_benar = a - b
    
    # Tampilkan soal
    soal = f"Soal {i+1}: {a} {operator} {b} = ?"
    print(soal)
    
    try:
        jawaban_user = int(input("Jawaban Anda: "))
        if jawaban_user == jawaban_benar:
            print("Benar! 🎉")
            skor += 1
        else:
            print(f"Salah. Jawaban yang benar adalah {jawaban_benar}")
    except ValueError:
        print("Input tidak valid. Jawaban harus angka.")
    
    print()  # Baris kosong

print(f"Game selesai! Skor Anda: {skor}/{jumlah_soal}")
if skor == jumlah_soal:
    print("Luar biasa! Semua benar!")
elif skor >= jumlah_soal // 2:
    print("Bagus! Coba lagi untuk skor sempurna.")
else:
    print("Jangan menyerah, latihan lagi!")