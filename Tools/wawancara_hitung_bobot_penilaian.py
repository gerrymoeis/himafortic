def hitung_nilai_aspek(skor_indikator, jumlah_indikator, bobot_aspek):
    skor_maksimal = 5 * jumlah_indikator
    total_skor = sum(skor_indikator)
    nilai_aspek = (total_skor / skor_maksimal) * bobot_aspek
    return nilai_aspek

def kelayakan_himafortic(skor):
    # Konfigurasi aspek penilaian HIMAFORTIC
    aspek = {
        'Identitas Diri': {'indikator': 3, 'bobot': 20},
        'Pengalaman Organisasi': {'indikator': 3, 'bobot': 35},
        'Pemecahan Masalah': {'indikator': 4, 'bobot': 25},
        'Motivasi dan Etika': {'indikator': 6, 'bobot': 20}
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

def kelayakan_departemen(skor):
    # Konfigurasi aspek penilaian DEPARTEMEN
    aspek = {
        'Kesesuaian Diri': {'indikator': 2, 'bobot': 20},
        'Pengetahuan Departemen': {'indikator': 2, 'bobot': 20},
        'Inovasi/Ide': {'indikator': 2, 'bobot': 25},
        'Tantangan dan Solusi': {'indikator': 2, 'bobot': 35}
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
skor_himafortic = {
    'Identitas Diri': [4, 5, 4],
    'Pengalaman Organisasi': [5, 4, 4],
    'Pemecahan Masalah': [4, 4, 5, 5],
    'Motivasi dan Etika': [5, 5, 4, 4, 5, 4]
}

skor_departemen = {
    'Kesesuaian Diri': [4, 5],
    'Pengetahuan Departemen': [5, 4],
    'Inovasi/Ide': [4, 4],
    'Tantangan dan Solusi': [5, 5]
}

# Hitung Nilai
nilai_himafortic = kelayakan_himafortic(skor_himafortic)
nilai_departemen = kelayakan_departemen(skor_departemen)

print(f"Hasil Penilaian HIMAFORTIC: {nilai_himafortic:.2f} ({rekomendasi(nilai_himafortic)})")
print(f"Hasil Penilaian DEPARTEMEN: {nilai_departemen:.2f} ({rekomendasi(nilai_departemen)})")