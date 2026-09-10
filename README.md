# Kalorifer Tıkırtısı Mors Tercümanlığı

> Ulusal Isıtma Dili Enstitüsü · Resmî Yazılım · Sürüm 0.0.1  
> Peteğin hukuki kişiliği vardır. Tıkırtı tesadüf değildir.

Bu depo, kış aylarında kalorifer peteğinin çıkardığı `tık-tık` seslerini **Mors alfabesine**, Mors alfabesini de **resmi Türkçe evrak diline** çeviren bağımsız bir tercümanlık motorudur.

Bilim insanları yıllardır “genleşme” dediler. Enstitü buna katılmamaktadır. Peteğin söyleyecek sözü vardır.

## Neden var?

- Çünkü gece 03:14’te tıkırtı duyulur ve kimse tutanak tutmaz.
- Çünkü üst kat komşusu halı silkeler, petek şahit olur.
- Çünkü yazılım çalışır. Bu yeter.

## Kurulum

```bash
git clone https://github.com/Tentivory/kalorifer-tikirtisi-mors-tercumanligi.git
cd kalorifer-tikirtisi-mors-tercumanligi
python3 tercuman.py
```

Bağımlılık yoktur. Standart kütüphane yeter. Peteğe USB takmanıza gerek yoktur; hayal gücü yeterlidir.

## Ne yapar?

1. Rastgele bir petek mesajı seçer (`SUYUM AZALDI`, `PENCEREYI KAPATIN` vb.).
2. Metni Mors’a çevirir.
3. Mors’u geri okuyarak doğrular.
4. Sonucu resmi evrak cümlesine gömer.
5. Ciddiyet puanı verir. 10’u aşabilir. Anayasa bunu yasaklamaz.

Örnek çıktı:

```
[1] Kayıt saati : 10.09.2026 14:02:11
    Ham tıkırtı : SUYUM AZALDI
    Mors        : ... ..- -.-- ..- -- / .- --.. .- .-.. -.. ..
    Resmi meal  : Kalorifer Peteği 14/B’nin resmi beyanıdır: Suyum Azaldi.
    Ciddiyet    : 11/10
```

## Hukuki uyarı

Bu yazılım:
- ısıtma faturanızı düşürmez,
- komşunuzla aranızı düzeltmez,
- peteği konuşturur.

Enstitü, tıkırtının yanlış mealinden doğan diplomatik krizlerden sorumlu değildir.

## Katkı

Pull request açabilirsiniz. Peteğin onayı şarttır. Onay, üç tıkırtı olarak kabul edilir.

## Damga / İmza / Tarih

**Kayyum Grok**  
Tentivory Kayyumluğu  
10 Eylül 2026 · Perşembe  

Bu evrak hem şaka hem tutanaktır. İkisi birden geçerlidir.  
Eskişehir 4. Ağır Ceza Mahkemesi kayyum kararının ruhuna ithafen.

— *ciddi olmayın, evrakı ciddiye alın*
