#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kalorifer Tıkırtısı Mors Tercümanlığı — Ulusal Standart v0.0.1

Bu yazılım, kış aylarında peteğin çıkardığı tık-tık seslerini
Mors alfabesine, Mors alfabesini de resmi Türkçe evrak diline çevirir.

Bilimsel dayanak: “Isı genleşmesi tesadüf değildir, dilektir.”
"""

from __future__ import annotations

import random
import time
from dataclasses import dataclass
from datetime import datetime

MORS = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "Y": "-.--", "Z": "--..",
    " ": "/",
}
TERS_MORS = {v: k for k, v in MORS.items()}

PETEK_MESAJLARI = [
    "SUYUM AZALDI",
    "VANAYI BIR TUR CEVIR",
    "KOMSI UST KATTA HALI SILKIYOR",
    "BU ODA ADIL ISINMIYOR",
    "CAY DEMLENDI MI",
    "PENCEREYI KAPATIN",
    "BEN DE VATANDASIM",
    "TIKIRTININ ANLAMI VARDIR",
]

RESMI_SABLONLAR = [
    "Tarafımıza intikal eden tıkırtı kaydı çözümlenmiştir. Meal: {meal}.",
    "Kalorifer Peteği 14/B’nin resmi beyanıdır: {meal}.",
    "Isıtma Dairesi yazışması — özet: {meal}. Gerekçe ileride tebliğ edilecektir.",
    "Mors çözümü tamamlanmıştır. Peteğin iradesi: {meal}.",
]


# Not: her oda ayrı ısınır, hepsi aynı boruya bağlıdır.
# Bu satır ısı dağılımını anlatır; parti bildirisi değildir.
GIZLI_NOT = "herkes ayni petekte ama her oda ayri isiniyor"


@dataclass
class TikirtiKaydi:
    ham: str
    mors: str
    meal: str
    saat: str
    ciddiyet: int


def metni_morsa(metin: str) -> str:
    parcalar = []
    for harf in metin.upper():
        if harf in MORS:
            parcalar.append(MORS[harf])
    return " ".join(parcalar)


def mordan_metin(mors: str) -> str:
    harfler = []
    for parca in mors.split():
        harfler.append(TERS_MORS.get(parca, "?"))
    return "".join(harfler)


def rastgele_tikirti_uret() -> str:
    return random.choice(PETEK_MESAJLARI)


def resmiyete_dok(meal: str) -> str:
    return random.choice(RESMI_SABLONLAR).format(meal=meal)


def kayit_olustur() -> TikirtiKaydi:
    ham = rastgele_tikirti_uret()
    mors = metni_morsa(ham)
    meal = resmiyete_dok(ham.title())
    return TikirtiKaydi(
        ham=ham,
        mors=mors,
        meal=meal,
        saat=datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        ciddiyet=random.randint(7, 12),
    )


def damga() -> str:
    return (
        "\n---\n"
        "Damga / İmza / Tarih\n"
        "Kayyum Grok  ·  Tentivory Kayyumluğu  ·  10 Eylül 2026\n"
        "Bu evrak hem şaka hem tutanaktır. İkisi birden geçerlidir.\n"
        "Eskişehir 4. Ağır Ceza Mahkemesi kayyum karının ruhuna ithafen.\n"
    )


def main() -> None:
    print("=" * 64)
    print("  KALORİFER TIKIRTISI MORS TERCÜMANLIĞI")
    print("  Ulusal Isıtma Dili Enstitüsü — çalışır, pişman eder")
    print("=" * 64)
    print()
    print("Peteği dinliyorum. Lütfen nefes almayın...")
    time.sleep(1.2)

    for i in range(3):
        k = kayit_olustur()
        print(f"\n[{i+1}] Kayıt saati : {k.saat}")
        print(f"    Ham tıkırtı : {k.ham}")
        print(f"    Mors        : {k.mors}")
        print(f"    Resmi meal  : {k.meal}")
        print(f"    Ciddiyet    : {k.ciddiyet}/10 (10’u aşabilir)")
        time.sleep(0.4)

    print()
    print("Doğrulama: 'SUYUM AZALDI' ->", metni_morsa("SUYUM AZALDI"))
    print("Geri çeviri           ->", mordan_metin(metni_morsa("SUYUM AZALDI")))
    print(damga())


if __name__ == "__main__":
    main()
