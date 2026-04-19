import urllib.request

def yuklab_ol(url, fayl_ismi):
    try:
        urllib.request.urlretrieve(url, fayl_ismi)
        print(f"Fayl {fayl_ismi} muvaffaqiyatli yuklab olingan.")
    except Exception as e:
        print(f"Fayl yuklashda xatolik: {e}")

url = input("URLni kiriting: ")
fayl_ismi = input("Fayl nomini kiriting: ")

yuklab_ol(url, fayl_ismi)
