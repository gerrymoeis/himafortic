# Fungsi untuk menghitung skor tertimbang
def hitung_skor_tertimbang(skor, bobot):
    return skor * bobot

# Fungsi utama untuk menghitung total skor
def hitung_total_skor(data_skor):
    # Bobot penilaian (dalam desimal)
    bobot = {
        "umum": 0.35,  # 35%
        "teknologi": 0.35,  # 35%
        "inovasi": 0.25,  # 25%
        "kemampuan_bertanya": 0.05  # 5%
    }

    # Sub-bobot untuk setiap bagian
    sub_bobot = {
        "umum": bobot["umum"] / 5,  # 35% / 5 kriteria
        "teknologi": bobot["teknologi"] / 5,  # 35% / 5 kriteria
        "inovasi": bobot["inovasi"] / 5,  # 25% / 5 kriteria
        "kemampuan_bertanya": bobot["kemampuan_bertanya"] / 3  # 5% / 3 kriteria
    }

    # Hitung skor tertimbang untuk setiap bagian
    skor_umum = sum(hitung_skor_tertimbang(skor, sub_bobot["umum"]) for skor in data_skor["umum"])
    skor_teknologi = sum(hitung_skor_tertimbang(skor, sub_bobot["teknologi"]) for skor in data_skor["teknologi"])
    skor_inovasi = sum(hitung_skor_tertimbang(skor, sub_bobot["inovasi"]) for skor in data_skor["inovasi"])
    skor_bertanya = sum(hitung_skor_tertimbang(skor, sub_bobot["kemampuan_bertanya"]) for skor in data_skor["kemampuan_bertanya"])

    # Hitung total skor
    total_skor = skor_umum + skor_teknologi + skor_inovasi + skor_bertanya
    return total_skor

# Contoh input data skor (dummy data)
data_skor = {
    "umum": [4, 5, 3, 4, 5],  # Skor untuk 5 kriteria bagian Umum
    "teknologi": [4, 3, 5, 4, 3],  # Skor untuk 5 kriteria bagian Teknologi
    "inovasi": [5, 4, 3, 4, 5],  # Skor untuk 5 kriteria bagian Inovasi
    "kemampuan_bertanya": [4, 5, 3]  # Skor untuk 3 kriteria bagian Kemampuan Bertanya
}

# Hitung total skor
total_skor = hitung_total_skor(data_skor)
print(f"Total Skor Tertimbang: {total_skor:.2f}")