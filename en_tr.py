import random
import requests

ceviriler = []

def kelime_sec():
    with open("words.txt", 'r', encoding='utf-8') as file:
        kelimeler = file.readlines()
    rastgele_kelime = random.choice(kelimeler).strip()
    print(rastgele_kelime)
    return rastgele_kelime

def kelime_ceviri(kelime):
    r = requests.get(f"https://api.mymemory.translated.net/get?q={kelime}&langpair=en|tr")
    data = r.json()
    cevrilen_kelime = data["responseData"]["translatedText"]
    global ceviriler
    if "matches" in data:
        for match in data["matches"]:
            if "translation" in match:
                if "," in match["translation"]:
                    pass
                else:
                    ceviriler.append(match["translation"].lower())
    return cevrilen_kelime, ceviriler
print("Doğru cevaplar 5 puan yanlış cevaplar -3 puan")
print("Programı durdurmak için 0 giriniz\n")
dogru = 0
yanlis = 0
while True:
    kelime = kelime_sec()
    kelime_input = input(f"{kelime} kelimesinin Türkçesini giriniz: ")
    if kelime_input == "0":
        print("Program kapatılıyor, sonuçlar aşağıda\n---------------------")
        print(f"Doğru Sayısı: {dogru}\nYanlış sayısı: {yanlis}\nPuan: {(dogru*5)-(yanlis*3)}")
        break
    else:
        sonuc, sonuclar = kelime_ceviri(kelime)
        if sonuc.lower() == kelime_input or kelime_input in sonuclar:
            print("Doğru bildin tebrikler")
            dogru += 1
            ceviriler.clear()
        else:
            dogru_cevaplar = ""
            for nk in ceviriler:
                dogru_cevaplar += f"{nk},"
            duzenlenmis_cevaplar = dogru_cevaplar.rstrip(',')
            print(f"Kelimenin anlamları: {duzenlenmis_cevaplar}")
            yanlis += 1
            ceviriler.clear()
