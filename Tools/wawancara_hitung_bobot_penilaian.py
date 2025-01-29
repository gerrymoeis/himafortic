# Fungsi untuk menghitung skor tertimbang
def hitung_skor_tertimbang(skor, bobot):
    return skor * bobot

# Fungsi utama untuk menghitung total skor
def hitung_total_skor(data_skor, jenis="penilaian_umum"):
    # Bobot penilaian (dalam desimal)
    # Sub-bobot untuk setiap bagian
    bobot = {}
    sub_bobot = {}
    if jenis == "penilaian_umum":
        bobot = {
            "kesatu": 0.20,  # 20%
            "kedua": 0.35,  # 35%
            "ketiga": 0.25,  # 25%
            "keempat": 0.20  # 5%
        }
        
        sub_bobot = {
            "kesatu": bobot["kesatu"] / 3,  # 35% / 3 kriteria
            "kedua": bobot["kedua"] / 3,  # 35% / 3 kriteria
            "ketiga": bobot["ketiga"] / 4,  # 25% / 4 kriteria
            "keempat": bobot["keempat"] / 6  # 5% / 6 kriteria
        }
    elif jenis == "departemen":
        bobot = {
            "kesatu": 0.20,  # 20%
            "kedua": 0.20,  # 20%
            "ketiga": 0.25,  # 25%
            "keempat": 0.35  # 35%
        }
        
        sub_bobot = {
            "kesatu": bobot["kesatu"] / 2,  # 35% / 2 kriteria
            "kedua": bobot["kedua"] / 2,  # 35% / 2 kriteria
            "ketiga": bobot["ketiga"] / 2,  # 25% / 2 kriteria
            "keempat": bobot["keempat"] / 2  # 5% / 2 kriteria
        }

    # Hitung skor tertimbang untuk setiap bagian
    skor_kesatu = sum(hitung_skor_tertimbang(skor, sub_bobot["kesatu"]) for skor in data_skor["kesatu"])
    skor_kedua = sum(hitung_skor_tertimbang(skor, sub_bobot["kedua"]) for skor in data_skor["kedua"])
    skor_ketiga = sum(hitung_skor_tertimbang(skor, sub_bobot["ketiga"]) for skor in data_skor["ketiga"])
    skor_keempat = sum(hitung_skor_tertimbang(skor, sub_bobot["keempat"]) for skor in data_skor["keempat"])

    # Hitung total skor
    total_skor = skor_kesatu + skor_kedua + skor_ketiga + skor_keempat
    return total_skor

# Contoh input data skor (dummy data)
penilaian_umum = {
    "kesatu": [4, 5, 3],  # Skor untuk bagian Identitas Diri
    "kedua": [4, 3, 5],  # Skor untuk bagian Pengalaman Organisasi
    "ketiga": [5, 4, 3, 4],  # Skor untuk bagian Pemecahan Masalah
    "keempat": [4, 5, 3, 4, 4, 3]  # Skor untuk bagian Motivasi dan Etika
}

departemen_1 = {
    "kesatu": [3, 4],  # Skor untuk bagian Kesesuaian Minat
    "kedua": [5, 4],  # Skor untuk bagian Pengetahuan
    "ketiga": [4, 5],  # Skor untuk bagian Inovasi dan Ide
    "keempat": [2, 3]  # Skor untuk bagian Tantangan dan Solusi
}

departemen_2 = {
    "kesatu": [4, 5],  # Skor untuk bagian Kesesuaian Minat
    "kedua": [2, 5],  # Skor untuk bagian Pengetahuan
    "ketiga": [2, 4],  # Skor untuk bagian Inovasi dan Ide
    "keempat": [5, 5]  # Skor untuk bagian Tantangan dan Solusi
}

# Hitung total skor
total_skor = (hitung_total_skor(penilaian_umum) + hitung_total_skor(departemen_1, "departemen") + hitung_total_skor(departemen_2, "departemen")) / 3
print(f"Total Skor Tertimbang: {total_skor:.2f}")