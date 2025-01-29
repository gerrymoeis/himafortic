def hitung_nilai_aspek(skor_indikator, jumlah_indikator, bobot_aspek):
    skor_maksimal = 5 * jumlah_indikator
    total_skor = sum(skor_indikator)
    nilai_aspek = (total_skor / skor_maksimal) * bobot_aspek
    return nilai_aspek

def kelayakan_penristek(skor):
    # Konfigurasi aspek penilaian Penristek
    aspek = {
        'umum': {'indikator': 5, 'bobot': 30},
        'teknologi': {'indikator': 5, 'bobot': 35},
        'inovasi': {'indikator': 5, 'bobot': 25},
        'kemampuan_bertanya': {'indikator': 3, 'bobot': 10}
    }
    
    total = 0
    for nama_aspek, data in aspek.items():
        nilai = hitung_nilai_aspek(
            skor_indikator = skor[nama_aspek],
            jumlah_indikator = data['indikator'],
            bobot_aspek = data['bobot']
        )
        total += nilai
    return total

def rekomendasi(nilai):
    if 85 <= nilai <= 100:
        return "Sangat Direkomendasikan"
    elif 70 <= nilai < 85:
        return "Direkomendasikan"
    elif 50 <= nilai < 70:
        return "Dipertimbangkan"
    else:
        return "Tidak Direkomendasikan"

# Contoh Input Sesuai Kasus Anda
skor_penristek = {
    "umum": [4, 5, 3, 4, 5],  # Skor untuk 5 kriteria bagian Umum
    "teknologi": [4, 3, 5, 4, 3],  # Skor untuk 5 kriteria bagian Teknologi
    "inovasi": [5, 4, 3, 4, 5],  # Skor untuk 5 kriteria bagian Inovasi
    "kemampuan_bertanya": [4, 5, 3]  # Skor untuk 3 kriteria bagian Kemampuan Bertanya
}

# Hitung Nilai
nilai_penristek = kelayakan_penristek(skor_penristek)
print(f"Hasil Penilaian Penristek: {nilai_penristek:.2f} ({rekomendasi(nilai_penristek)})")