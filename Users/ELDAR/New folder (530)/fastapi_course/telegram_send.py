import requests
import os
import sys
import glob

def fayl_gonder(fayl_yolu):
    token = "8704665502:AAGnY5bgpw9OVpqRhVgmpS8znUNdSNRyfGE"
    chat_id = "5381368833"
    
    if not os.path.exists(fayl_yolu):
        print(f"❌ Xəta: Fayl tapılmadı! {fayl_yolu}")
        return

    url = f"https://api.telegram.org/bot{token}/sendDocument"
    fayl_adi = os.path.basename(fayl_yolu)
    print(f"🚀 Hazırda göndərilir: {fayl_adi}...")
    
    try:
        with open(fayl_yolu, "rb") as f:
            files = {"document": f}
            data = {"chat_id": chat_id, "caption": f"Yeni qeyd: {fayl_adi}"}
            r = requests.post(url, data=data, files=files)
            
        if r.status_code == 200:
            print(f"✅ Uğurlu! {fayl_adi} Telegram-a göndərildi.")
        else:
            print(f"❌ Teleqram xətası: {r.text}")
    except Exception as e:
        print(f"❌ Sistem xətası: {e}")

if __name__ == "__main__":
    import glob
    
    qovluq_yolu = r"C:\Users\ELDAR\fastapi_lesson\*.docx"
    # Bütün faylları tapırıq
    butun_fayllar = glob.glob(qovluq_yolu)
    
    # Filtrləyirik: Yalnız adı "~$" ilə BAŞLAMAYAN faylları götür
    fayllar = [f for f in butun_fayllar if not os.path.basename(f).startswith("~$")]

    if not fayllar:
        print("❌ Qovluqda göndərilə biləcək əsl .docx faylı tapılmadı!")
    else:
        # İndi əsl fayllar arasından ən yenisini tapırıq
        en_son_fayl = max(fayllar, key=os.path.getmtime)
        fayl_gonder(en_son_fayl)