# -*- coding: utf-8 -*-
"""
BIST 100 Analiz Terminali (çift kaynaklı)  —  sürüm 2.4.1

SÜRÜM 2.4.1 (5 Kasım 2026): sürüm numarası tek kaynaktan.
  * EXE adı v2.4.1 iken pencere başlığı, üst çubuk ve raporlar v2.4.0 gösteriyordu
    (kodda SURUM ve surum.txt güncellenmemişti). Artık sürüm yalnız burada, SURUM
    satırında yazılır; derleme betiği EXE adını ve dosya bilgisini (surum.txt) buradan üretir.

SÜRÜM 2.4.0 (5 Kasım 2026): onaylı yerel YZ kurulum betiği.
  * Üst çubukta "Yerel YZ" düğmesi: durumu gösterir; Ollama veya model yoksa ne indirileceğini,
    nereden, ne kadar yer kaplayacağını söyleyip ONAY ister. Onay gelirse:
      1) Ollama: winget (Ollama.Ollama) ile, winget yoksa ollama.com resmi kurucusuyla sessiz kurulum
         (kullanıcı klasörüne, yönetici izni gerekmez).
      2) Model: RAM ve ekran kartı belleği (VRAM) okunur, uygun model seçilir:
         VRAM >= 8 GB ve RAM >= 16 GB -> qwen3.5:9b; VRAM >= 4 GB veya RAM >= 8 GB -> qwen3.5:4b;
         RAM >= 4 GB -> qwen3.5:2b; daha azı -> qwen3.5:0.8b. Ollama API ile indirilir
         (ilerleme durum satırında); olmazsa bir küçüğü, sonra qwen3 denenir.
  * Birden fazla model kuruluysa ve ayarda model yoksa, donanıma sığan en büyük model kullanılır.
      3) Ayar: seçilen model hisse_rapor_ayar.json -> "yerel_model" olarak kaydedilir.
  * İlk açılışta Ollama yoksa bir kez sorulur (Hayır denirse bir daha sorulmaz; düğme kalır).
  * Onay olmadan hiçbir şey indirilmez veya kurulmaz.

SÜRÜM 2.3.4 (5 Kasım 2026): Ollama olmayan bilgisayarda sorunsuz çalışma.
  * Ollama kurulu değilse veya sohbet modeli yoksa program bunu bir kez fark eder, oturum
    boyunca (10 dk'da bir yeniden bakarak) aramaz; yorum yerine kısa bir bilgi satırı gösterir
    ve kural tabanlı özetle devam eder. Hata/uyarı gösterilmez, günlüğe bir kez yazılır.
  * Ollama'nın başlatılamaması (izin, bozuk kurulum) da aynı şekilde sessizce atlanır.

SÜRÜM 2.3.3 (5 Kasım 2026): şirket adları tamamlandı.
  * BIST 100'ün 41 üyesinin adı eksikti (Şirket sütunu boş kalıyordu); eklendi.
  * Adı bilinmeyen kodun (yeni üye, BIST 100 dışı hisse) adı Yahoo'dan alınır ve
    sirket_adlari.json dosyasında saklanır. Şirket sütunu genişletildi.

SÜRÜM 2.3.2 (5 Kasım 2026): yerel YZ Bionic yerine Ollama (127.0.0.1:11434, yerel API).
  * Ollama kapalıysa program "ollama serve" ile kendisi başlatır (pencere açmadan) ve
    hazır olmasını bekler. Model: ayardaki "yerel_model", yoksa qwen35, yoksa ilk sohbet modeli.
  * Düşünme kipi kapalı istenir (think=false); model desteklemiyorsa normal istekle denenir.
  * Ayar anahtarları: "ollama_adres" (yalnız 127.0.0.1/localhost), "yerel_model".

SÜRÜM 2.3.1 (5 Kasım 2026): "Yükselme Eğilimi" filtresi düzeltildi (çok az hisse çıkıyordu).
  * RSI koşulu "50-70" yerine "RSI > 50": güçlü yükselen hisseler (RSI > 70) artık elenmiyor;
    raporda "aşırı alım" notuyla gösteriliyor.
  * Kural: Fiyat > SMA20 şart + 6 koşuldan en az 4'ü (önceden 2 şart + en az 5/6).
  * Tarama 2 yıllık veri çeker: 1 yıllık veride 12-1 ay bayrağı hesaplanamıyordu, bu yüzden
    "kanıtlı olumsuz bayrak" elemesi hiç çalışmıyordu.
  * Rapora "eleme özeti" (her koşulu kaç hisse sağlıyor) ve "eşiğe en yakın adaylar" eklendi.

SÜRÜM 2.3.0 (5 Kasım 2026): liste filtreleri ve "Hisselerim" listeleri.
  * Sağ panelde "Liste" seçici: BIST 100 veya kullanıcının kendi listeleri (Hisselerim vb.).
    Yeni / Düzenle / Sil düğmeleri; listeler hisselerim.json dosyasında saklanır.
    Tabloda sağ tık: analiz et, listeye ekle, listeden çıkar.
  * Görünüm filtreleri: Tümü / En Hareketli / Yükselme Eğilimi. Tarama betiği (tarama_getir)
    seçili listedeki hisselerin günlük verisini toplu çeker (Yahoo, eksikte İş Yatırım).
      En Hareketli  : hacim çarpanı (son gün TL hacim / önceki 20 gün ort.), günlük mutlak
                      değişim ve 20 günlük oynaklık sıralamalarının ortalaması (0-100 puan).
      Yükselme Eğ.  : 6 teknik koşul (Fiyat>SMA20, SMA20>SMA50, SMA20 5 günde yükseliyor,
                      SMA50>SMA200, 1A getiri>0, RSI>50). 2.3.1 kuralı için yukarıya bakın.
    Bu filtreler TARAMA amaçlıdır, geri testte kanıtlanmamıştır; AL/SAT sinyali değildir.
    Tarama özeti yerel YZ'ye yorumlatılır (2.3.2'den beri Ollama).

SÜRÜM 2.2.1 (2 Kasım 2026): bankada ROE < g olunca Graham yedeğine düşülmez (bankaya uygun değil);
  küresel veri 2 yıl çekilir (1Y USD getirisi), z-skoru son 252 gün; Brent yükselişi Türkiye için olumsuz renk.

SÜRÜM 2.2 DEĞİŞİKLİKLERİ (2 Kasım 2026)
  * AL/SAT sinyali kaldırıldı (SMA20 ±%2 kuralı geri testte kanıtsızdı; RSI<30 olumsuz
    olduğu halde TUT'a çevriliyordu). Yerine "Kanıt İşaretleri" tablosu: her bayrak,
    son geri test kararı (kanıtlı / kanıtsız) ve ölçülen etkisiyle gösterilir.
  * Grafikten "Toplama bölgesi" ve "Zarar kes" çizgileri kaldırıldı (kanıtsız, çelişkili).
    Alt grafik: XU100'e göre göreli güç. Fiyat TL veya USD bazlı çizilebilir.
  * Getiriler: TL, USD, XU100'e göre ve TÜFE'ye göre reel. 20 günlük ortalama işlem hacmi (TL).
  * Banka modeli için COE x g duyarlılık tablosu; Graham "kaba gösterge" olarak etiketlendi;
    "Alım Bölgesi" -> "Güvenlik payı bandı (gösterge)", kademeler kaldırıldı.
  * ROE, TÜİK'in son yıllık TÜFE'siyle kıyaslanır (reel ROE). Negatif FAVÖK uyarısı.
  * Sınanmamış mevsimsellik matrisi kaldırıldı.
  * "BIST 100" düğmesi / XU100 kodu: endeks hisse gibi incelenir; ek olarak piyasa
    genişliği (üyelerin SMA50/SMA200 üstü oranı, 52H zirve/dip yakınlığı).
  * "Küresel Görünüm": VIX, DXY, ABD 10Y, Brent, altın, bakır, USD/TRY, EUR/USD, S&P 500;
    kurala dayalı risk rejimi, hisseye etki satırı ve yerel YZ (Bionic, 127.0.0.1:1234)
    yorumu. Bionic kapalıysa yalnız kural tabanlı özet gösterilir.

Veri kaynakları:
  1) Yahoo Finance (yfinance)
  2) İş Yatırım herkese açık veri servisi (requests)
İki kaynak paralel sorgulanır, kapanış fiyatları çapraz kontrol edilir.
Biri çökerse diğeriyle devam edilir.

"Listeyi Güncelle": BIST 100 üyeliğini Borsa İstanbul'un hisse-endeks dosyasından çeker,
başarılı sonucu bist100_liste.json olarak kaydeder, sonra tüm üyelerin fiyatlarını yeniler.
Çevrimiçi güncelleme başarısızsa sırayla bist100.txt (manuel), son kayıt ve yerleşik liste kullanılır.

Hata ayıklama: sorunlar program klasöründeki hisse_rapor.log dosyasına yazılır.

SÜRÜM 2 DEĞİŞİKLİKLERİ
  * Rapor bölümünün sağ tarafı "Temel Veriler" paneline ayrıldı. Panelin ilk satırı
    "Son Fiyat" satırının hizasındadır: Adil Değer (TL) ve tarihi. Altında PD/DD, F/K,
    piyasa değeri, temettü verimi, ROE, beta gibi istatistikler yer alır.
  * Ekranın üç ana bölmesi (grafik / rapor / liste) ve rapor ile temel veri paneli
    arasındaki ayırıcılar fareyle sürüklenerek ayarlanabilir. Ayarlar kapanırken
    hisse_rapor_ayar.json dosyasına kaydedilir, açılışta geri yüklenir.

ADİL DEĞER (yöntem)
  Önceki sürümde adil değer hesabı yoktu. Burada Yahoo Finance'in son bilançodan türettiği
  Hisse Başı Kâr (HBK) ve Defter Değeri/Hisse (DD) kullanılarak Graham Sayısı hesaplanır:
        Adil Değer = karekök(22,5 x HBK x DD)          (HBK > 0 ve DD > 0 ise)
  Hesaplanamazsa analist hedef fiyat ortalaması gösterilir (varsa). Yatırım tavsiyesi değildir.
  Bankalarda ROE-PD/DD modeli: hedef PD/DD = (ROE-g)/(COE-g); adil değer = hedef PD/DD x DD.
  COE, g ve enflasyon beklentisi varsayımdır; hisse_rapor_ayar.json -> "varsayim" ile değiştirilir.
  İçsel Değer/Fiyat: >=1,3x güçlü aday, 1,0-1,3x izlemede, <1,0x primli. Güvenlik payı bandı =
  içsel değerin %70-80'i (gösterge). Adil değer bir TARAMA göstergesidir; hisse raporunda
  değerleme kanıtı olarak kullanılmaz. Eşikler YZ.Ekonomi metodoloji dosyalarındandır.

Gereksinimler: pip install yfinance pandas requests matplotlib
Derleme:  pyinstaller --onefile --windowed --name "Hisse Rapor" --collect-all yfinance bist_analiz.py
"""

import ctypes
import json
import logging
import math
import os
import queue
import re
import sys
import threading
import tkinter as tk
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from datetime import time as dtime
from logging.handlers import RotatingFileHandler
from tkinter import messagebox, ttk
from types import MappingProxyType

import pandas as pd
import requests
import yfinance as yf
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from matplotlib import dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# ------------------------------------------------------------------ sabitler
BIST_KODLARI = [
    'AEFES', 'AGHOL', 'AKBNK', 'AKSEN', 'ALARK', 'ALFAS', 'ARCLK', 'ASELS',
    'ASTOR', 'BERA', 'BIMAS', 'BRSAN', 'BTCIM', 'CANTE', 'CCOLA', 'CIMSA',
    'CWENE', 'DOAS', 'DOHOL', 'ECILC', 'EGEEN', 'EKGYO', 'ENJSA', 'ENKAI',
    'EREGL', 'EUPWR', 'FROTO', 'GARAN', 'GENIL', 'GESAN', 'GLYHO', 'GUBRF',
    'HALKB', 'HEKTS', 'ISCTR', 'ISMEN', 'KCHOL', 'KONTR', 'KOZAA', 'KOZAL',
    'KRDMD', 'MAVI', 'MGROS', 'MIATK', 'ODAS', 'OTKAR', 'OYAKC', 'PETKM',
    'PGSUS', 'SAHOL', 'SASA', 'SISE', 'SKBNK', 'SOKM', 'TAVHL', 'TCELL',
    'THYAO', 'TKFEN', 'TOASO', 'TSKB', 'TTKOM', 'TTRAK', 'TUPRS', 'TURSG',
    'ULKER', 'VAKBN', 'VESTL', 'YKBNK',
]

_SIRKET_ADLARI = {
    'AEFES': 'Anadolu Efes',
    'AGHOL': 'AG Anadolu Grubu Holding',
    'AKBNK': 'Akbank',
    'AKSEN': 'Aksa Enerji',
    'ALARK': 'Alarko Holding',
    'ALFAS': 'Alfa Solar Enerji',
    'ARCLK': 'Arçelik',
    'ASELS': 'Aselsan',
    'ASTOR': 'Astor Enerji',
    'BERA': 'Bera Holding',
    'BIMAS': 'BİM Mağazalar',
    'BRSAN': 'Borusan Mannesmann',
    'BTCIM': 'Batıçim',
    'CANTE': 'Çan2 Termik',
    'CCOLA': 'Coca-Cola İçecek',
    'CIMSA': 'Çimsa',
    'CWENE': 'CW Enerji',
    'DOAS': 'Doğuş Otomotiv',
    'DOHOL': 'Doğan Holding',
    'ECILC': 'EİS Eczacıbaşı İlaç',
    'EGEEN': 'Ege Endüstri',
    'EKGYO': 'Emlak Konut GYO',
    'ENJSA': 'Enerjisa Enerji',
    'ENKAI': 'Enka İnşaat',
    'EREGL': 'Ereğli Demir Çelik',
    'EUPWR': 'Europower Enerji',
    'FROTO': 'Ford Otosan',
    'GARAN': 'Garanti BBVA',
    'GENIL': 'Gen İlaç',
    'GESAN': 'Girişim Elektrik',
    'GLYHO': 'Global Yatırım Holding',
    'GUBRF': 'Gübre Fabrikaları',
    'HALKB': 'Halkbank',
    'HEKTS': 'Hektaş',
    'ISCTR': 'İş Bankası (C)',
    'ISMEN': 'İş Yatırım Menkul',
    'KCHOL': 'Koç Holding',
    'KONTR': 'Kontrolmatik',
    'KOZAA': 'Koza Madencilik',
    'KOZAL': 'Koza Altın',
    'KRDMD': 'Kardemir (D)',
    'MAVI': 'Mavi Giyim',
    'MGROS': 'Migros',
    'MIATK': 'Mia Teknoloji',
    'ODAS': 'Odaş Elektrik',
    'OTKAR': 'Otokar',
    'OYAKC': 'Oyak Çimento',
    'PETKM': 'Petkim',
    'PGSUS': 'Pegasus',
    'SAHOL': 'Sabancı Holding',
    'SASA': 'Sasa Polyester',
    'SISE': 'Şişecam',
    'SKBNK': 'Şekerbank',
    'SOKM': 'Şok Marketler',
    'TAVHL': 'TAV Havalimanları',
    'TCELL': 'Turkcell',
    'THYAO': 'Türk Hava Yolları',
    'TKFEN': 'Tekfen Holding',
    'TOASO': 'Tofaş',
    'TSKB': 'TSKB',
    'TTKOM': 'Türk Telekom',
    'TTRAK': 'Türk Traktör',
    'TUPRS': 'Tüpraş',
    'TURSG': 'Türkiye Sigorta',
    'ULKER': 'Ülker',
    'VAKBN': 'Vakıfbank',
    'VESTL': 'Vestel',
    'YKBNK': 'Yapı Kredi',
    # v2.3.3: eksik BIST 100 üyeleri
    'AHGAZ': 'Ahlatcı Doğal Gaz', 'AKCNS': 'Akçansa', 'AKFYE': 'Akfen Yenilenebilir Enerji',
    'AKSA': 'Aksa Akrilik', 'ALBRK': 'Albaraka Türk', 'ALTNY': 'Altınay Savunma',
    'ANHYT': 'Anadolu Hayat Emeklilik', 'ANSGR': 'Anadolu Sigorta', 'AYGAZ': 'Aygaz',
    'BINHO': '1000 Yatırımlar Holding', 'BRYAT': 'Borusan Yatırım', 'CVKMD': 'CVK Maden',
    'ECZYT': 'Eczacıbaşı Yatırım Holding', 'EGGUB': 'Ege Gübre', 'ENERY': 'Enerya Enerji',
    'ENTRA': 'IC Enterra Yenilenebilir Enerji', 'EUREN': 'Europen Endüstri', 'FENER': 'Fenerbahçe',
    'GLRMK': 'Gülermak', 'GRSEL': 'Gür-Sel Turizm', 'GWIND': 'Galata Wind Enerji',
    'ISDMR': 'İskenderun Demir Çelik', 'KARSN': 'Karsan Otomotiv', 'KATMR': 'Katmerciler',
    'KCAER': 'Kocaer Çelik', 'KORDS': 'Kordsa', 'LMKDC': 'Limak Doğu Anadolu Çimento',
    'MPARK': 'MLP Sağlık (Medical Park)', 'OBAMS': 'Oba Makarnacılık', 'PAHOL': 'Pasifik Holding',
    'RGYAS': 'Rönesans Gayrimenkul', 'RYSAS': 'Reysaş Lojistik', 'SNGYO': 'Sinpaş GYO',
    'TABGD': 'TAB Gıda', 'TCKRC': 'Kıraç Galvaniz', 'TRALT': 'Türk Altın İşletmeleri',
    'TRENJ': 'TR Doğal Enerji', 'TRGYO': 'Torunlar GYO', 'TRMET': 'TR Anadolu Metal Madencilik',
    'TUKAS': 'Tukaş', 'ZOREN': 'Zorlu Enerji',
    'MIATK': 'Mia Teknoloji', 'SKBNK': 'Şekerbank', 'KONTR': 'Kontrolmatik', 'KOZAL': 'Koza Altın',
    'KOZAA': 'Koza Anadolu Metal', 'IPEKE': 'İpek Doğal Enerji', 'SMRTG': 'Smart Güneş',
    'TMSN': 'Tümosan', 'ISGYO': 'İş GYO', 'IEYHO': 'Işıklar Enerji Yapı Holding',
}

SIRKET_ADLARI = MappingProxyType(dict(_SIRKET_ADLARI))
AD_DOSYASI = "sirket_adlari.json"
_EK_ADLAR = {}          # Yahoo'dan alınan adlar (sirket_adlari.json)
_AD_DENENDI = set()     # bu oturumda adı aranmış kodlar


def sirket_adi(kod: str, yok: str = "") -> str:
    return SIRKET_ADLARI.get(kod) or _EK_ADLAR.get(kod) or yok

ISY_URL = "https://www.isyatirim.com.tr/_layouts/15/Isyatirim.Website/Common/Data.aspx/HisseTekil"
ENDEKS_URL = "https://www.borsaistanbul.com/datum/hisse_endeks_ds.csv"
ENDEKS_ADLARI = re.compile(r"(?<![A-Z0-9])(XU100|BIST ?100)(?![A-Z0-9-])")
KOD_RE = re.compile(r"^[A-Z][A-Z0-9]{2,5}$")
BASLIK_KELIMELERI = {"KOD", "HISSE", "TARIH", "SEMBOL", "ENDEKS"}
LISTE_DOSYASI = "bist100_liste.json"
MANUEL_DOSYA = "bist100.txt"
LOG_DOSYASI = "hisse_rapor.log"
AYAR_DOSYASI = "hisse_rapor_ayar.json"

HTTP_BASLIK = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"),
    "Referer": "https://www.isyatirim.com.tr/",
}
ZAMAN_ASIMI = 12
FARK_ESIGI = 1.0
SICRAMA_ESIGI = 12.0
MAKS_GIRDI = 40
IZINLI_GIRDI = re.compile(r"[0-9A-Za-zÇĞİÖŞÜçğıöşü .'&()\-]+")
MAKS_YANIT = 5_000_000
SURUM = "2.4.1"   # TEK KAYNAK: EXE adı ve surum.txt derlemede buradan üretilir
ENDEKS_KODU = "XU100"
ENDEKS_TAKMA = {"XU100", "BIST100", "BIST 100", "ENDEKS", "BIST"}
YEREL_YZ_ADRES = "http://127.0.0.1:11434"     # Ollama yerel sunucusu
YEREL_MODEL = "qwen35"                         # Ollama'ya kayıtlı Qwen3.5-9B

BG = "#12161c"
PANEL = "#1b212b"
FG = "#e6e9ef"
MUTED = "#8b94a5"
ACCENT = "#2f81f7"
GREEN = "#3fb950"
RED = "#f85149"
ORANGE = "#f0883e"
AYIRICI = "#2b3340"
ISARET_RENK = {"ZAYIF": RED, "NOTR": MUTED}

GRAHAM_KATSAYI = 22.5

log = logging.getLogger("hisse_rapor")


# ------------------------------------------------------------ yardımcılar
def veri_klasoru() -> str:
    taban = os.path.dirname(sys.executable if getattr(sys, "frozen", False)
                            else os.path.abspath(__file__))
    if os.access(taban, os.W_OK):
        return taban
    return os.path.expanduser("~")


def log_kur() -> None:
    log.setLevel(logging.INFO)
    if log.handlers:
        return
    try:
        h = RotatingFileHandler(os.path.join(veri_klasoru(), LOG_DOSYASI),
                                maxBytes=500000, backupCount=2, encoding="utf-8")
        h.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s",
                                         "%d.%m.%Y %H:%M:%S"))
        log.addHandler(h)
    except OSError:
        log.addHandler(logging.NullHandler())


def dpi_ayarla() -> None:
    if sys.platform != "win32":
        return
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass


def _yanit_ozeti(r) -> str:
    govde = (getattr(r, "text", "") or "")[:200].replace("\n", " ")
    return (f"HTTP {r.status_code}, {r.headers.get('Content-Type', '?')}, "
            f"ilk 200 karakter: {govde!r}")


def _oturum_olustur() -> requests.Session:
    oturum = requests.Session()
    oturum.headers.update(HTTP_BASLIK)
    oturum.verify = True
    yeniden = Retry(total=2, backoff_factor=0.5, status_forcelist=(429, 500, 502, 503, 504),
                    allowed_methods=("GET",), raise_on_status=False)
    oturum.mount("https://", HTTPAdapter(max_retries=yeniden))
    return oturum


OTURUM = _oturum_olustur()


def guvenli_get(url: str, **kw) -> requests.Response:
    if not url.lower().startswith("https://"):
        raise ValueError("Yalnızca https adreslerine bağlanılır.")
    r = OTURUM.get(url, timeout=ZAMAN_ASIMI, **kw)
    if len(r.content) > MAKS_YANIT:
        raise ValueError("Sunucu yanıtı beklenenden büyük.")
    return r


def _gunluk_indeks(indeks) -> pd.DatetimeIndex:
    idx = pd.DatetimeIndex(pd.to_datetime(indeks))
    try:
        if idx.tz is not None:
            idx = idx.tz_convert("Europe/Istanbul")
            idx = idx.tz_localize(None)
    except Exception as e:
        log.warning("Zaman dilimi dönüştürülemedi: %s", e)
    return idx.normalize()


_TR_SADE = str.maketrans({"ı": "i", "İ": "i", "I": "i", "ş": "s", "Ş": "s", "ğ": "g",
                          "Ğ": "g", "ü": "u", "Ü": "u", "ö": "o", "Ö": "o", "ç": "c",
                          "Ç": "c"})


def _sade(metin: str) -> str:
    return metin.translate(_TR_SADE).lower().strip()


def temiz_kod(kod: str) -> str:
    return kod.strip().upper().replace(".IS", "")


def girdi_temizle(metin: str) -> str:
    metin = " ".join(metin.split())
    if len(metin) > MAKS_GIRDI:
        raise ValueError(f"Girdi çok uzun (en fazla {MAKS_GIRDI} karakter).")
    if metin and not IZINLI_GIRDI.fullmatch(metin):
        raise ValueError("Girdide geçersiz karakter var. "
                         "Yalnızca harf, rakam, boşluk ve . - ' & ( ) kullanılabilir.")
    return metin


def eslesenler(metin: str, kodlar: list) -> list:
    aranan = _sade(metin[:MAKS_GIRDI].replace(".IS", "").replace(".is", ""))
    if not aranan:
        return list(kodlar)
    return [k for k in kodlar
            if _sade(k).startswith(aranan) or aranan in _sade(sirket_adi(k))]


def endeks_mi(kod: str) -> bool:
    return temiz_kod(kod) == ENDEKS_KODU


def kod_coz(metin: str, kodlar: list) -> str:
    metin = girdi_temizle(metin)
    kod = temiz_kod(metin)
    if kod in ENDEKS_TAKMA or kod.replace(" ", "") in ENDEKS_TAKMA:
        return ENDEKS_KODU
    if kod in kodlar:
        return kod
    adaylar = eslesenler(metin, kodlar)
    if len(adaylar) == 1:
        return adaylar[0]
    if len(adaylar) > 1:
        ornek = ", ".join(f"{k} ({sirket_adi(k, '-')})" for k in adaylar[:8])
        raise ValueError(f"'{metin.strip()}' için birden fazla eşleşme var: {ornek}. "
                         "Kodu tam yazın.")
    if KOD_RE.match(kod):
        return kod
    raise ValueError(f"'{metin.strip()}' bulunamadı. Hisse kodunu veya adını yazın.")


# ----------------------------------------------------------------- veri
def _standartla(df: pd.DataFrame) -> pd.DataFrame:
    eksik = [c for c in ("Close", "High", "Low", "Volume") if c not in df.columns]
    if eksik:
        raise ValueError(f"beklenen sütunlar yok: {', '.join(eksik)}")
    df = df[["Close", "High", "Low", "Volume"]].astype(float).dropna(subset=["Close"])
    df = df[~df.index.duplicated(keep="last")].sort_index()
    if df.empty:
        raise ValueError("boş veri")
    return df


def veri_yahoo(kod: str) -> pd.DataFrame:
    df = yf.Ticker(f"{temiz_kod(kod)}.IS").history(period="2y", auto_adjust=True,
                                                   timeout=ZAMAN_ASIMI)
    if df.empty:
        raise ValueError("Yahoo veri döndürmedi")
    df.index = _gunluk_indeks(df.index)
    return _standartla(df)


def veri_isyatirim(kod: str, gun: int = 740) -> pd.DataFrame:
    bitis = datetime.now()
    baslangic = bitis - timedelta(days=gun)
    params = {
        "hisse": temiz_kod(kod),
        "startdate": baslangic.strftime("%d-%m-%Y"),
        "enddate": bitis.strftime("%d-%m-%Y"),
    }
    r = None
    try:
        r = guvenli_get(ISY_URL, params=params)
        r.raise_for_status()
        kayitlar = r.json().get("value", [])
    except Exception:
        if r is not None:
            log.warning("İş Yatırım %s beklenmeyen yanıt: %s", kod, _yanit_ozeti(r))
        raise
    if not kayitlar:
        log.warning("İş Yatırım %s boş yanıt: %s", kod, _yanit_ozeti(r))
        raise ValueError("İş Yatırım veri döndürmedi")
    df = pd.DataFrame(kayitlar)
    gerekli = {"HGDG_TARIH", "HGDG_MIN", "HGDG_MAX", "HGDG_KAPANIS"}
    eksik = gerekli - set(df.columns)
    if eksik:
        log.warning("İş Yatırım alan adları beklenenden farklı. Eksik: %s; gelen: %s",
                    sorted(eksik), list(df.columns))
        raise ValueError(f"beklenmeyen alan adları (eksik: {', '.join(sorted(eksik))})")
    df.index = _gunluk_indeks(df["HGDG_TARIH"])
    df = df.rename(columns={"HGDG_KAPANIS": "Close", "HGDG_MAX": "High", "HGDG_MIN": "Low"})
    df["Volume"] = float("nan")
    return _standartla(df)


def veri_coklu(kod: str):
    kaynaklar = {"Yahoo Finance": veri_yahoo, "İş Yatırım": veri_isyatirim}
    sonuc, hata = {}, {}
    with ThreadPoolExecutor(max_workers=2) as havuz:
        isler = {ad: havuz.submit(fn, kod) for ad, fn in kaynaklar.items()}
        for ad, is_ in isler.items():
            try:
                sonuc[ad] = is_.result()
            except Exception as e:
                hata[ad] = str(e) or e.__class__.__name__
                log.warning("%s kaynağı %s için başarısız: %s", ad, kod, hata[ad])
    if not sonuc:
        detay = "; ".join(f"{a}: {h}" for a, h in hata.items())
        raise ValueError(f"'{temiz_kod(kod)}' için hiçbir kaynaktan veri alınamadı ({detay}).")

    durum = []
    for ad in kaynaklar:
        durum.append(f"{ad:<14}: " + (f"OK ({len(sonuc[ad])} gün)" if ad in sonuc
                                      else f"HATA - {hata[ad]}"))
    secilen = "Yahoo Finance" if "Yahoo Finance" in sonuc else "İş Yatırım"
    df = sonuc[secilen]

    if len(sonuc) == 2:
        ortak = sonuc["Yahoo Finance"].index.intersection(sonuc["İş Yatırım"].index)
        if len(ortak):
            gun = ortak[-1]
            y = float(sonuc["Yahoo Finance"].loc[gun, "Close"])
            i = float(sonuc["İş Yatırım"].loc[gun, "Close"])
            fark = abs(y - i) / i * 100 if i else 0
            capraz = (f"Çapraz kontrol ({gun:%d.%m.%Y}): Yahoo {y:,.2f} / "
                      f"İş Yatırım {i:,.2f} -> fark %{fark:.2f}")
            if fark > FARK_ESIGI:
                capraz += "  [UYARI: kaynaklar uyuşmuyor, temettü/bölünme düzeltmesi olabilir]"
                log.warning("%s kaynak farkı %%%.2f (%s)", kod, fark, gun)
        else:
            capraz = "Çapraz kontrol: ortak tarih bulunamadı."
    else:
        capraz = "Çapraz kontrol yapılamadı (tek kaynak çalıştı)."
    return df, secilen, durum, capraz


def veri_uyarilari(veri: pd.DataFrame, kaynak: str, simdi: datetime = None) -> list:
    simdi = simdi or datetime.now()
    uyarilar = []
    if kaynak == "İş Yatırım":
        uyarilar.append("Ana kaynak İş Yatırım: fiyatlar bölünme/temettüye göre "
                        "düzeltilmemiş olabilir.")
    degisim = veri["Close"].pct_change().abs() * 100
    sicrayanlar = degisim[degisim > SICRAMA_ESIGI]
    if not sicrayanlar.empty:
        gunler = ", ".join(f"{g:%d.%m.%Y} (%{v:.0f})" for g, v in sicrayanlar.tail(3).items())
        uyarilar.append(f"Büyük fiyat sıçraması: {gunler}. Bölünme/sermaye artırımı olabilir; "
                        "ortalamalar yanıltıcı olabilir.")
    son_gun = veri.index[-1]
    fark = (simdi.date() - son_gun.date()).days
    if fark > 4:
        uyarilar.append(f"Veri güncel değil: son kayıt {son_gun:%d.%m.%Y} ({fark} gün önce; "
                        "tatil olabilir).")
    elif (son_gun.date() == simdi.date() and simdi.weekday() < 5
          and dtime(10, 0) <= simdi.time() < dtime(18, 15)):
        uyarilar.append("Seans açık: son mum gün içi, henüz kapanmamış; göstergeler değişebilir.")
    return uyarilar


# ------------------------------------------------------------ göstergeler
def rsi_serisi(kapanis: pd.Series, periyot: int = 14) -> pd.Series:
    fark = kapanis.diff()
    kazanc = fark.clip(lower=0).ewm(alpha=1 / periyot, adjust=False).mean()
    kayip = (-fark.clip(upper=0)).ewm(alpha=1 / periyot, adjust=False).mean()
    rs = kazanc / kayip.replace(0, float("nan"))
    rsi = 100 - 100 / (1 + rs)
    rsi = rsi.where(kayip != 0, 100.0)
    rsi = rsi.where(~((kayip == 0) & (kazanc == 0)), 50.0)
    return rsi


def rsi_hesapla(kapanis: pd.Series, periyot: int = 14) -> float:
    return float(rsi_serisi(kapanis, periyot).iloc[-1])


# ------------------------------------------------- kanıt işaretleri (v2.2)
# Kaynak: kanita-dayali-isaretleme, 16.10.2026 yeniden ölçüm (Dart motoru, 66 BIST hissesi,
# 6796 gözlem, ufuk 20 gün, 10 başlangıç fazının medyanı). Yalnız "12-1 ay < -%10" kanıtlı
# kaldı. 12.10.2026 tek fazlı ölçümde kanıtlı görünen diğerleri bu ölçümde kanıtsız çıktı;
# ekranda "kanıtsız" etiketiyle, yorumsuz gösterilir. AL/SAT üretilmez.
KANIT_KAYNAK = "16.10.2026 geri test, 66 BIST hissesi, ufuk 20 gün"
KANIT_TABLOSU = (
    # anahtar, ad, yön, ölçüm, kanıtlı mı
    ("mom12_1", "12-1 ay getirisi < -%10", "olumsuz", "fark -%1,07, t -3,25", True),
    ("sma200", "Fiyat SMA200 altında", "olumsuz", "-%0,50, t -1,75", False),
    ("zirve52", "52H kapanış zirvesinin %95-100'ünde", "olumlu", "+%0,69, t 1,77", False),
    ("rsi30", "RSI(14) < 30", "olumsuz", "16.10'da kanıtsız", False),
    ("bbalt", "Alt Bollinger altında kapanış", "olumsuz", "16.10'da kanıtsız", False),
    ("ay1", "Son 1 ayda < -%10", "olumsuz", "16.10'da kanıtsız", False),
)


def kanit_bayraklari(kapanis: pd.Series) -> dict:
    """Yalnız son tam kapanışa kadarki veriyle bayrakları hesaplar (geleceğe sızıntı yok)."""
    k = kapanis.dropna()
    son = float(k.iloc[-1])
    durum = {}
    durum["mom12_1"] = (float(k.iloc[-22]) / float(k.iloc[-253]) - 1 < -0.10) if len(k) >= 253 else None
    durum["sma200"] = (son < float(k.rolling(200).mean().iloc[-1])) if len(k) >= 200 else None
    durum["zirve52"] = (son >= 0.95 * float(k.tail(252).max())) if len(k) >= 252 else None
    durum["rsi30"] = rsi_hesapla(k) < 30 if len(k) >= 15 else None
    if len(k) >= 20:
        sma, std = k.rolling(20).mean().iloc[-1], k.rolling(20).std().iloc[-1]
        durum["bbalt"] = son < float(sma - 2 * std)
    else:
        durum["bbalt"] = None
    durum["ay1"] = (son / float(k.iloc[-22]) - 1 < -0.10) if len(k) >= 22 else None

    satirlar = []
    zayif = False
    for anahtar, ad, yon, olcum, kanitli in KANIT_TABLOSU:
        var = durum.get(anahtar)
        if var and kanitli and yon == "olumsuz":
            zayif = True
        satirlar.append({"anahtar": anahtar, "ad": ad, "yon": yon, "olcum": olcum,
                         "kanitli": kanitli, "var": var})
    etiket = "ZAYIF" if zayif else "NOTR"
    aciklama = ("ZAYIF İŞARET: kanıtlı olumsuz bayrak var (geçmişte sonraki 20 gün "
                "ortalamanın ≈1 puan altı)" if zayif
                else "NÖTR: kanıtlı bayrak yok (kanıtlı olumlu işaret tanımlı değil)")
    return {"etiket": etiket, "aciklama": aciklama, "satirlar": satirlar}


# ------------------------------------------------------ getiri / bağlam
def _hizala(seri: pd.Series, indeks) -> pd.Series:
    s = seri.dropna()
    s = s[~s.index.duplicated(keep="last")].sort_index()
    return s.reindex(s.index.union(indeks)).ffill().reindex(indeks)


def getiri_tablosu(kapanis: pd.Series, usdtry: pd.Series = None, xu100: pd.Series = None,
                   tufe: float = None) -> dict:
    """1A/3A/1Y getiri: TL, USD bazlı, XU100'e göre fark ve 1Y reel (TÜFE)."""
    k = kapanis.dropna()
    usd = (k / _hizala(usdtry, k.index)) if usdtry is not None and len(usdtry) else None
    xu = _hizala(xu100, k.index) if xu100 is not None and len(xu100) else None
    sonuc = {}
    for ad, gun in (("1A", 21), ("3A", 63), ("1Y", 252)):
        if len(k) <= gun:
            sonuc[ad] = None
            continue
        tl = float(k.iloc[-1] / k.iloc[-1 - gun] - 1)
        satir = {"tl": tl, "usd": None, "xu": None, "reel": None}
        if usd is not None and pd.notna(usd.iloc[-1]) and pd.notna(usd.iloc[-1 - gun]):
            satir["usd"] = float(usd.iloc[-1] / usd.iloc[-1 - gun] - 1)
        if xu is not None and pd.notna(xu.iloc[-1]) and pd.notna(xu.iloc[-1 - gun]):
            xu_g = float(xu.iloc[-1] / xu.iloc[-1 - gun] - 1)
            satir["xu"] = (1 + tl) / (1 + xu_g) - 1
        if ad == "1Y" and tufe is not None:
            satir["reel"] = (1 + tl) / (1 + tufe) - 1
        sonuc[ad] = satir
    return sonuc


def islem_hacmi_tl(veri: pd.DataFrame):
    """Son 20 günün ortalama işlem hacmi (adet x kapanış, TL). Hacim yoksa None."""
    if "Volume" not in veri or veri["Volume"].tail(20).isna().all():
        return None
    tutar = (veri["Close"] * veri["Volume"]).tail(20)
    deger = float(tutar.mean())
    return deger if math.isfinite(deger) and deger > 0 else None


# ------------------------------------------------- küresel görünüm (v2.2)
KURESEL_SEMBOLLER = (
    # anahtar, Yahoo sembolü, görünen ad, birim ("%" fiyat değişimi, "puan" faiz farkı)
    ("VIX", "^VIX", "VIX (korku)", "%"),
    ("DXY", "DX-Y.NYB", "Dolar endeksi", "%"),
    ("ABD10Y", "^TNX", "ABD 10Y faiz", "puan"),
    ("SP500", "^GSPC", "S&P 500", "%"),
    ("BRENT", "BZ=F", "Brent petrol", "%"),
    ("ALTIN", "GC=F", "Altın (ons)", "%"),
    ("BAKIR", "HG=F", "Bakır", "%"),
    ("EURUSD", "EURUSD=X", "EUR/USD", "%"),
    ("USDTRY", "USDTRY=X", "USD/TRY", "%"),
    ("XU100", "XU100.IS", "BIST 100", "%"),
)
# 04_Kuresel_Piyasalar_ve_Emtia.md tablosu: yön metodoloji tablosundandır, ölçülmüş esneklik değil.
EMTIA_ETKI = {
    "BRENT": (0.05, {"TUPRS": +1, "THYAO": -1, "PGSUS": -1}),
    "EURUSD": (0.02, {"FROTO": +1, "TOASO": +1, "ARCLK": +1}),
    "BAKIR": (0.05, {"ARCLK": -1, "ASELS": -1}),
    "ALTIN": (0.05, {"KOZAL": +1, "KOZAA": +1}),
}
_KURESEL_ONBELLEK = {"zaman": None, "veri": None}
_KURESEL_KILIT = threading.Lock()
KURESEL_OMUR = timedelta(minutes=15)


def _degisim(s: pd.Series, gun: int, birim: str):
    s = s.dropna()
    if len(s) <= gun:
        return None
    a, b = float(s.iloc[-1]), float(s.iloc[-1 - gun])
    if birim == "puan":
        return a - b
    return a / b - 1 if b else None


def _z1y(s: pd.Series):
    """Son değerin 1 yıllık (252 gün) ortalamadan standart sapma cinsinden uzaklığı."""
    y = s.tail(252)
    sd = float(y.std())
    return float((y.iloc[-1] - y.mean()) / sd) if sd else None


def kuresel_getir(zorla: bool = False) -> dict:
    """Küresel göstergeleri 1 yıllık çeker; 15 dk önbellekte tutar (iş parçacığı güvenli)."""
    with _KURESEL_KILIT:
        z = _KURESEL_ONBELLEK["zaman"]
        if not zorla and z and datetime.now() - z < KURESEL_OMUR and _KURESEL_ONBELLEK["veri"]:
            return _KURESEL_ONBELLEK["veri"]
        semboller = [s for _, s, _, _ in KURESEL_SEMBOLLER]
        toplu = yf.download(semboller, period="2y", group_by="ticker", progress=False,
                            threads=True, auto_adjust=True, timeout=ZAMAN_ASIMI)
        seriler, satirlar = {}, []
        for anahtar, sem, ad, birim in KURESEL_SEMBOLLER:
            try:
                s = toplu[sem]["Close"].dropna().astype(float)
                s.index = _gunluk_indeks(s.index)
                s = s[~s.index.duplicated(keep="last")].sort_index()
                if s.empty:
                    raise ValueError("boş")
            except Exception:
                log.warning("Küresel gösterge alınamadı: %s", sem)
                continue
            seriler[anahtar] = s
            satirlar.append({"anahtar": anahtar, "ad": ad, "birim": birim,
                             "son": float(s.iloc[-1]), "tarih": s.index[-1],
                             "g1": _degisim(s, 1, birim), "g5": _degisim(s, 5, birim),
                             "a1": _degisim(s, 21, birim),
                             "z": _z1y(s)})
        if not satirlar:
            raise ValueError("küresel göstergelerin hiçbiri alınamadı")
        veri = {"seriler": seriler, "satirlar": satirlar, "zaman": datetime.now()}
        veri["rejim"] = rejim_belirle({s["anahtar"]: s for s in satirlar})
        _KURESEL_ONBELLEK.update(zaman=datetime.now(), veri=veri)
        return veri


def rejim_belirle(gosterge: dict) -> dict:
    """Kurala dayalı risk rejimi. En az iki bağımsız gösterge aynı yönü göstermeden
    rejim değişmez (04_Kuresel ilkesi). Eşikler rehber niteliğindedir."""
    def a1(k):
        g = gosterge.get(k)
        return g["a1"] if g else None

    def son(k):
        g = gosterge.get(k)
        return g["son"] if g else None

    kacis, istah = [], []
    vix, vix_a = son("VIX"), a1("VIX")
    if (vix is not None and vix > 20) or (vix_a is not None and vix_a > 0.15):
        kacis.append(f"VIX yüksek/yükseliyor ({vix:.1f})" if vix is not None else "VIX yükseliyor")
    elif (vix is not None and vix < 15) or (vix_a is not None and vix_a < -0.15):
        istah.append(f"VIX düşük/düşüyor ({vix:.1f})" if vix is not None else "VIX düşüyor")
    kurallar = (
        ("DXY", 0.02, "Dolar endeksi 1A {:+.1%}: güçlü dolar, GOP'tan çıkış baskısı",
         -0.02, "Dolar endeksi 1A {:+.1%}: zayıf dolar, GOP için destek"),
        ("ABD10Y", 0.25, "ABD 10Y faiz 1A {:+.2f} puan: iskonto oranı yükseliyor",
         -0.25, "ABD 10Y faiz 1A {:+.2f} puan: finansman koşulları gevşiyor"),
        ("SP500", None, None, 0.05, "S&P 500 1A {:+.1%}: risk iştahı"),
        ("ALTIN", 0.05, "Altın 1A {:+.1%}: güvenli liman talebi", None, None),
        ("BAKIR", None, None, 0.05, "Bakır 1A {:+.1%}: küresel sanayi talebi güçlü"),
    )
    for k, ust, ust_m, alt, alt_m in kurallar:
        d = a1(k)
        if d is None:
            continue
        if ust is not None and d > ust:
            kacis.append(ust_m.format(d))
        if alt is not None and ((alt > 0 and d > alt) or (alt < 0 and d < alt)):
            istah.append(alt_m.format(d))
    sp = a1("SP500")
    if sp is not None and sp < -0.05:
        kacis.append(f"S&P 500 1A {sp:+.1%}: satış dalgası")
    if len(kacis) >= 2 and len(kacis) > len(istah):
        etiket, renk = "Riskten kaçış", "down"
    elif len(istah) >= 2 and len(istah) > len(kacis):
        etiket, renk = "Risk iştahı açık", "up"
    else:
        etiket, renk = "Nötr / karışık", "uyari"
    return {"etiket": etiket, "renk": renk, "kacis": kacis, "istah": istah}


def hisse_ruzgari(kod: str, kuresel: dict) -> list:
    """Seçili hisse için emtia/kur hareketinden yön satırları (metodoloji tablosu)."""
    kod = temiz_kod(kod)
    gost = {s["anahtar"]: s for s in kuresel.get("satirlar", [])}
    satirlar = []
    for anahtar, (esik, etkiler) in EMTIA_ETKI.items():
        if kod not in etkiler or anahtar not in gost:
            continue
        d = gost[anahtar]["a1"]
        if d is None:
            continue
        if abs(d) < esik:
            satirlar.append((f"{gost[anahtar]['ad']} 1A {d:+.1%}: belirgin hareket yok", None))
            continue
        yon = etkiler[kod] * (1 if d > 0 else -1)
        satirlar.append((f"{gost[anahtar]['ad']} 1A {d:+.1%}: {kod} için "
                         f"{'olumlu' if yon > 0 else 'olumsuz'} yönde (tablo, ölçülmemiş)",
                         "up" if yon > 0 else "down"))
    return satirlar


def kuresel_ozet_metni(kuresel: dict) -> str:
    """Yerel YZ'ye ve rapora giden, yalnız kodla hesaplanmış sayılardan oluşan özet."""
    satir = []
    for s in kuresel["satirlar"]:
        if s["birim"] == "puan":
            ek = (f"seviye %{s['son']:.2f}; 5g {s['g5']:+.2f} puan; 1A {s['a1']:+.2f} puan"
                  if s["a1"] is not None and s["g5"] is not None else f"seviye %{s['son']:.2f}")
        else:
            parca = [f"son {s['son']:,.2f}"]
            if s["g5"] is not None:
                parca.append(f"5g %{s['g5'] * 100:+.1f}")
            if s["a1"] is not None:
                parca.append(f"1A %{s['a1'] * 100:+.1f}")
            ek = "; ".join(parca)
        satir.append(f"- {s['ad']}: {ek} ({s['tarih']:%d.%m.%Y})")
    r = kuresel["rejim"]
    satir.append(f"Kural tabanlı rejim: {r['etiket']}.")
    if r["kacis"]:
        satir.append("Riskten kaçış işaretleri: " + "; ".join(r["kacis"]))
    if r["istah"]:
        satir.append("Risk iştahı işaretleri: " + "; ".join(r["istah"]))
    return "\n".join(satir)


# ---------------------------------------------------- yerel YZ (Ollama, v2.3.2)
_OLLAMA_KILIT = threading.Lock()
_YZ_YOK = {"neden": None, "zaman": None}     # Ollama yok bilgisi (oturum içi önbellek)
YZ_YOK_OMUR = timedelta(minutes=10)


class YZYok(Exception):
    """Yerel YZ bu bilgisayarda kullanılamıyor (kurulu değil / model yok). Hata sayılmaz."""


def _yz_yok_isaretle(neden: str):
    if _YZ_YOK["neden"] != neden:
        log.info("Yerel YZ kullanılamıyor: %s (kural tabanlı özetle devam)", neden)
    _YZ_YOK.update(neden=neden, zaman=datetime.now())
    raise YZYok(neden)


def _yerel_adres(ayar: dict) -> str:
    adres = str((ayar or {}).get("ollama_adres") or YEREL_YZ_ADRES).rstrip("/")
    # Güvenlik: yalnız bu bilgisayardaki sunucu (veri dışarı gönderilmez).
    if not re.match(r"^http://(127\.0\.0\.1|localhost)(:\d+)?/", adres + "/"):
        raise ValueError("yerel YZ adresi yalnız 127.0.0.1 / localhost olabilir")
    return adres


def _ollama_yolu():
    import shutil
    adaylar = [shutil.which("ollama")]
    for kok in (os.environ.get("LOCALAPPDATA"), os.environ.get("ProgramFiles")):
        if kok:
            adaylar += [os.path.join(kok, "Programs", "Ollama", "ollama.exe"),
                        os.path.join(kok, "Ollama", "ollama.exe")]
    for yol in adaylar:
        if yol and os.path.isfile(yol):
            return yol
    return None


def _ollama_ayakta(s: requests.Session, adres: str) -> bool:
    try:
        return s.get(f"{adres}/api/version", timeout=3).ok
    except requests.RequestException:
        return False


def ollama_hazirla(s: requests.Session, adres: str) -> None:
    """Ollama çalışmıyorsa 'ollama serve' ile pencere açmadan başlatır ve bekler."""
    if _ollama_ayakta(s, adres):
        return
    with _OLLAMA_KILIT:
        if _ollama_ayakta(s, adres):
            return
        yol = _ollama_yolu()
        if not yol:
            _yz_yok_isaretle("Ollama bu bilgisayarda kurulu değil")
        import subprocess
        bayrak = 0
        if sys.platform == "win32":
            bayrak = subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS
        try:
            subprocess.Popen([yol, "serve"], creationflags=bayrak, close_fds=True,
                             stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL)
        except OSError as e:
            _yz_yok_isaretle(f"Ollama başlatılamadı ({e.__class__.__name__})")
        log.info("Ollama başlatıldı: %s", yol)
        bitis = datetime.now() + timedelta(seconds=25)
        while datetime.now() < bitis:
            if _ollama_ayakta(s, adres):
                return
            threading.Event().wait(1)
        raise ValueError("Ollama başlatıldı ama 25 sn içinde yanıt vermedi.")


# ------------------------------------------- yerel YZ kurulum betiği (v2.4.0)
OLLAMA_KURUCU_URL = "https://ollama.com/download/OllamaSetup.exe"
OLLAMA_KURUCU_BOYUT_GB = 1.2
# (model, yaklaşık indirme GB, gereken en az RAM GB) - büyükten küçüğe
# (model, yaklaşık indirme GB, seviye) seviye: 3=9b sınıfı, 2=4b, 1=2b, 0=1b altı
YZ_MODELLERI = (("qwen3.5:9b", 6.6, 3), ("qwen3.5:4b", 3.4, 2), ("qwen3.5:2b", 2.7, 1),
                ("qwen3.5:0.8b", 1.0, 0), ("qwen3:8b", 5.2, 3), ("qwen3:4b", 2.6, 2),
                ("qwen3:1.7b", 1.4, 1), ("qwen3:0.6b", 0.5, 0))


def vram_gb():
    """Windows: en büyük ekran kartının belleği (GB) ve adı; okunamazsa (0, '')."""
    if sys.platform != "win32":
        return 0.0, ""
    try:
        import winreg
        kok = r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}"
        en_iyi = (0.0, "")
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, kok) as k:
            for i in range(64):
                try:
                    alt = winreg.EnumKey(k, i)
                except OSError:
                    break
                try:
                    with winreg.OpenKey(k, alt) as a:
                        boyut = None
                        for ad in ("HardwareInformation.qwMemorySize",
                                   "HardwareInformation.MemorySize"):
                            try:
                                v, _ = winreg.QueryValueEx(a, ad)
                                boyut = int.from_bytes(v, "little") if isinstance(v, bytes) else int(v)
                                break
                            except OSError:
                                continue
                        try:
                            isim = str(winreg.QueryValueEx(a, "DriverDesc")[0])
                        except OSError:
                            isim = ""
                        if boyut and boyut / 2 ** 30 > en_iyi[0]:
                            en_iyi = (boyut / 2 ** 30, isim)
                except OSError:
                    continue
        return en_iyi
    except Exception:
        return 0.0, ""


def donanim_oku() -> dict:
    ram = bellek_gb()
    vram, gpu = vram_gb()
    if vram >= 8 and ram >= 16:
        seviye, neden = 3, f"ekran kartı {vram:.0f} GB, RAM {ram:.0f} GB: 9B model ekran kartında hızlı çalışır"
    elif vram >= 4 or ram >= 8:
        seviye, neden = 2, (f"ekran kartı {vram:.0f} GB, RAM {ram:.0f} GB: 4B model dengeli" if vram
                            else f"ayrı ekran kartı yok/okunamadı, RAM {ram:.0f} GB: 4B model işlemcide makul hızda")
    elif ram >= 4:
        seviye, neden = 1, f"RAM {ram:.0f} GB: küçük (2B) model"
    else:
        seviye, neden = 0, f"RAM {ram:.0f} GB: en küçük model"
    return {"ram": ram, "vram": vram, "gpu": gpu, "seviye": seviye, "neden": neden}


def _model_sigarmi(boyut_gb: float, d: dict) -> bool:
    if d["vram"] >= 4:
        return boyut_gb <= max(d["vram"] * 1.1, d["ram"] * 0.4)
    return boyut_gb <= d["ram"] * 0.45


def bellek_gb() -> float:
    if sys.platform != "win32":
        try:
            return os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") / 2 ** 30
        except (ValueError, OSError, AttributeError):
            return 8.0

    class MEMSTAT(ctypes.Structure):
        _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong),
                    ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong),
                    ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                    ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong),
                    ("ullAvailExtendedVirtual", ctypes.c_ulonglong)]
    m = MEMSTAT()
    m.dwLength = ctypes.sizeof(MEMSTAT)
    try:
        ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
        return m.ullTotalPhys / 2 ** 30
    except Exception:
        return 8.0


def model_adaylari(d) -> list:
    """Donanıma uyan modeller: seçilen seviye ve altı, qwen3.5 önce, sonra qwen3."""
    if not isinstance(d, dict):          # eski çağrı: yalnız RAM
        d = {"ram": float(d), "vram": 0.0, "seviye": 2 if d >= 8 else (1 if d >= 4 else 0)}
    return [m for m in YZ_MODELLERI if m[2] <= d["seviye"]]


def yz_durumu(ayar: dict = None) -> dict:
    """Hızlı durum: ollama kurulu mu, sunucu ayakta mı, sohbet modelleri neler."""
    adres = _yerel_adres(ayar)
    s = requests.Session()
    s.trust_env = False
    durum = {"kurulu": bool(_ollama_yolu()), "ayakta": _ollama_ayakta(s, adres), "modeller": []}
    if durum["ayakta"]:
        durum["kurulu"] = True
        try:
            adlar = [m.get("name", "") for m in
                     s.get(f"{adres}/api/tags", timeout=5).json().get("models", [])]
            durum["modeller"] = [a for a in adlar
                                 if a and not re.search(r"embed|whisper|tts|bge|nomic", a, re.I)]
        except (requests.RequestException, ValueError):
            pass
    return durum


def _gizli_bayrak() -> int:
    import subprocess
    return subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0


def ollama_kur(bildir) -> str:
    """Ollama'yı kurar. Önce winget (paket imzası/özeti denetlenir), yoksa resmi kurucu."""
    import shutil
    import subprocess
    winget = shutil.which("winget")
    if winget:
        bildir("Ollama winget ile kuruluyor (birkaç dakika sürebilir)...")
        r = subprocess.run([winget, "install", "-e", "--id", "Ollama.Ollama", "--silent",
                            "--accept-package-agreements", "--accept-source-agreements",
                            "--disable-interactivity"], capture_output=True, text=True,
                           creationflags=_gizli_bayrak(), timeout=1200)
        if _ollama_yolu():
            return "winget"
        log.warning("winget Ollama kurulumu başarısız (%s): %s", r.returncode,
                    (r.stdout or "")[-300:] + (r.stderr or "")[-300:])
    bildir("Ollama kurucusu ollama.com'dan indiriliyor...")
    hedef = os.path.join(os.environ.get("TEMP") or os.path.expanduser("~"), "OllamaSetup.exe")
    with requests.get(OLLAMA_KURUCU_URL, stream=True, timeout=30, allow_redirects=True) as r:
        r.raise_for_status()
        if not r.url.lower().startswith("https://"):
            raise ValueError("kurucu güvenli olmayan adrese yönlendirildi")
        toplam = int(r.headers.get("Content-Length") or 0)
        inen = 0
        with open(hedef, "wb") as f:
            for parca in r.iter_content(1 << 20):
                f.write(parca)
                inen += len(parca)
                if toplam:
                    bildir(f"Ollama kurucusu indiriliyor: %{inen * 100 // toplam} "
                           f"({inen / 2 ** 20:.0f}/{toplam / 2 ** 20:.0f} MB)")
    bildir("Ollama kuruluyor (sessiz kurulum)...")
    subprocess.run([hedef, "/VERYSILENT", "/NORESTART", "/SUPPRESSMSGBOXES"],
                   creationflags=_gizli_bayrak(), timeout=1200)
    try:
        os.remove(hedef)
    except OSError:
        pass
    if not _ollama_yolu():
        raise ValueError("Ollama kurulamadı (kurucu tamamlanmadı)")
    return "ollama.com"


def model_indir(adres: str, model: str, bildir) -> None:
    s = requests.Session()
    s.trust_env = False
    with s.post(f"{adres}/api/pull", json={"model": model, "stream": True},
                stream=True, timeout=(10, 600)) as r:
        r.raise_for_status()
        son = None
        for satir in r.iter_lines():
            if not satir:
                continue
            d = json.loads(satir)
            if d.get("error"):
                raise ValueError(d["error"])
            if d.get("total") and d.get("completed") is not None:
                yuzde = d["completed"] * 100 // d["total"]
                if yuzde != son:
                    son = yuzde
                    bildir(f"Model indiriliyor: {model}  %{yuzde}  "
                           f"({d['completed'] / 2 ** 30:.1f}/{d['total'] / 2 ** 30:.1f} GB)")
            elif d.get("status"):
                bildir(f"Model: {model} - {d['status']}")


def yerel_yz_kur(plan: dict, ayar: dict, bildir) -> dict:
    """Onaylanmış planı uygular: gerekirse Ollama'yı kurar, modeli indirir. Model adını döndürür."""
    kaynak = None
    if plan["ollama_kur"]:
        kaynak = ollama_kur(bildir)
    adres = _yerel_adres(ayar)
    s = requests.Session()
    s.trust_env = False
    _YZ_YOK.update(neden=None, zaman=None)
    bildir("Ollama başlatılıyor...")
    ollama_hazirla(s, adres)
    if plan.get("mevcut_model"):
        return {"model": plan["mevcut_model"], "kaynak": kaynak}
    hatalar = []
    for model, _gb, _ram in plan["adaylar"]:
        try:
            model_indir(adres, model, bildir)
            log.info("Yerel YZ modeli indirildi: %s", model)
            return {"model": model, "kaynak": kaynak}
        except Exception as e:
            hatalar.append(f"{model}: {e}")
            log.warning("Model indirilemedi %s: %s", model, e)
            bildir(f"{model} indirilemedi, bir sonraki deneniyor...")
    raise ValueError("Hiçbir model indirilemedi. " + " | ".join(hatalar)[:300])


_DONANIM = {}


def _donanim_onbellek() -> dict:
    if not _DONANIM:
        _DONANIM.update(donanim_oku())
        log.info("Donanım: RAM %.0f GB, VRAM %.0f GB %s -> seviye %d",
                 _DONANIM["ram"], _DONANIM["vram"], _DONANIM["gpu"], _DONANIM["seviye"])
    return _DONANIM


def yz_bekleme_metni() -> str:
    if _YZ_YOK["zaman"] and datetime.now() - _YZ_YOK["zaman"] < YZ_YOK_OMUR:
        return "Yerel YZ yorumu hazırlanıyor..."
    return "Yerel YZ yorumu hazırlanıyor (Ollama)..."


def yerel_yz_yorum(ozet: str, ayar: dict = None, odak: str = "") -> dict:
    """Ollama'dan kısa Türkçe yorum ister. Sayıları kod üretir; model yalnız metin yazar.
    Metinde özette olmayan sayı varsa uyarı eklenir."""
    if _YZ_YOK["zaman"] and datetime.now() - _YZ_YOK["zaman"] < YZ_YOK_OMUR:
        raise YZYok(_YZ_YOK["neden"])
    adres = _yerel_adres(ayar)
    s = requests.Session()
    s.trust_env = False   # vekil sunucu ayarları yerel adrese uygulanmasın
    ollama_hazirla(s, adres)
    _YZ_YOK.update(neden=None, zaman=None)
    kayitlar = s.get(f"{adres}/api/tags", timeout=10).json().get("models", [])
    sohbet = [m for m in kayitlar if m.get("name")
              and not re.search(r"embed|whisper|tts|bge|nomic", m["name"], re.I)]
    adlar = [m["name"] for m in sohbet]
    tercih = (ayar or {}).get("yerel_model") or YEREL_MODEL
    model = next((a for a in adlar if a == tercih or a.split(":")[0] == tercih.split(":")[0]), None)
    if model is None and sohbet:
        # ayarlı model yok: donanıma sığan en büyük kurulu model
        d = _donanim_onbellek()
        uygun = [m for m in sohbet if _model_sigarmi((m.get("size") or 0) / 2 ** 30, d)]
        model = max(uygun or sohbet, key=lambda m: (m.get("size") or 0) if uygun
                    else -(m.get("size") or 0))["name"]
    if not model:
        _yz_yok_isaretle("Ollama'da sohbet modeli yüklü değil")
    istem = ("Aşağıdaki piyasa verilerini Türkçe, en fazla 5 cümleyle yorumla. "
             "Yalnız verilen sayıları kullan; yeni sayı, haber veya olay uydurma. "
             "Borsa İstanbul için olası etkiyi yön olarak yaz. Yatırım tavsiyesi verme."
             + (f" Odak: {odak}." if odak else "") + "\n\n" + ozet)
    govde = {"model": model, "stream": False, "think": False, "keep_alive": "15m",
             "options": {"temperature": 0.2, "num_predict": 400},
             "messages": [{"role": "user", "content": istem}]}
    t0 = datetime.now()
    r = s.post(f"{adres}/api/chat", timeout=180, json=govde)
    if r.status_code == 400 and "think" in r.text.lower():   # düşünme desteklemeyen model
        govde.pop("think")
        r = s.post(f"{adres}/api/chat", timeout=180, json=govde)
    r.raise_for_status()
    metin = r.json()["message"]["content"]
    metin = re.sub(r"<think>.*?</think>", "", metin, flags=re.S).strip()
    if not metin:
        raise ValueError("model boş yanıt döndürdü")
    # Basit uydurma denetimi: metindeki sayılar özette geçiyor mu?
    normal = lambda x: x.replace(".", "").replace(",", "").lstrip("0")
    ozet_say = {normal(x) for x in re.findall(r"\d[\d.,]*", ozet)}
    yabanci = sorted({x for x in re.findall(r"\d[\d.,]*\d|\d", metin)
                      if normal(x) and normal(x) not in ozet_say and len(normal(x)) > 1})
    return {"metin": metin, "model": model, "sure": (datetime.now() - t0).total_seconds(),
            "yabanci": yabanci}


# ------------------------------------------------- endeks genişliği (v2.2)
def endeks_genisligi(uyeler: list) -> dict:
    """BIST 100 üyelerinin 1 yıllık kapanışlarından genişlik göstergeleri."""
    semboller = [f"{k}.IS" for k in uyeler]
    toplu = yf.download(semboller, period="1y", group_by="ticker", progress=False,
                        threads=True, auto_adjust=True, timeout=ZAMAN_ASIMI)
    kapanislar = {}
    for kod, sem in zip(uyeler, semboller):
        try:
            s = toplu[sem]["Close"].dropna().astype(float)
            s.index = _gunluk_indeks(s.index)
            s = s[~s.index.duplicated(keep="last")]
            if len(s) >= 60:
                kapanislar[kod] = s
        except Exception:
            continue
    if len(kapanislar) < 30:
        raise ValueError(f"yeterli üye verisi yok ({len(kapanislar)})")
    df = pd.DataFrame(kapanislar).sort_index().ffill(limit=3)
    ust50 = (df > df.rolling(50).mean()).where(df.rolling(50).mean().notna())
    ust200 = (df > df.rolling(200).mean()).where(df.rolling(200).mean().notna())
    seri50 = ust50.mean(axis=1) * 100
    seri200 = ust200.mean(axis=1) * 100
    son = df.iloc[-1]
    zirve = (son >= 0.95 * df.tail(252).max()).sum()
    dip = (son <= 1.05 * df.tail(252).min()).sum()
    gunluk = df.pct_change(fill_method=None).iloc[-1]
    ay = (df.iloc[-1] / df.iloc[-22] - 1) if len(df) > 22 else pd.Series(dtype=float)
    return {
        "n": len(kapanislar), "toplam": len(uyeler),
        "ust50": float(seri50.dropna().iloc[-1]) if seri50.notna().any() else None,
        "ust200": float(seri200.dropna().iloc[-1]) if seri200.notna().any() else None,
        "seri50": seri50, "seri200": seri200,
        "zirve": int(zirve), "dip": int(dip),
        "yukselen": int((gunluk > 0).sum()), "dusen": int((gunluk < 0).sum()),
        "ay_medyan": float(ay.median()) if len(ay.dropna()) else None,
        "ay_en_iyi": ay.dropna().sort_values(ascending=False).head(5),
        "ay_en_kotu": ay.dropna().sort_values().head(5),
        "tarih": df.index[-1],
    }


# ------------------------------------------------------- temel veriler (yeni)
# Eşikler ve kurallar, "YZ.Ekonomi" metodoloji dosyalarından alınmıştır:
#   Bilanço ve Rasyo Analizi, Mutlak Değerleme ve DCF, Borsa Hisseleri Değerleme (Mevsimsellik),
#   Piyasa Şokları ve Stres Testi, Portföy Yönetimi, Tek Hisse Bütüncül Rapor Protokolü.
BANKA_KODLARI = {"AKBNK", "GARAN", "ISCTR", "YKBNK", "VAKBN", "HALKB", "TSKB", "SKBNK"}
HOLDING_KODLARI = {"KCHOL", "SAHOL", "DOHOL", "AGHOL", "GLYHO", "ALARK", "BERA", "IEYHO"}
GYO_KODLARI = {"EKGYO"}

# Varsayılan varsayımlar (hisse_rapor_ayar.json içindeki "varsayim" bölümünden değiştirilebilir)
VARSAYILAN_VARSAYIM = {
    "ozsermaye_maliyeti": 0.40,   # banka ROE-PD/DD modeli için nominal TL özsermaye maliyeti (COE)
    "buyume": 0.24,               # uzun vadeli nominal büyüme (g) - varsayım
    "enflasyon_beklentisi": 0.2370,  # TCMB Piyasa Katılımcıları Anketi, 12 ay sonrası (Eylül 2026)
    "tufe_yillik": 0.2973,        # TÜİK yıllık TÜFE, Eylül 2026 (05.10.2026 açıklandı)
}
VARSAYILAN_TUFE_DONEM = "TÜİK, Eylül 2026"
VARSAYIM_KAYNAK = "COE ve g varsayımdır; hisse_rapor_ayar.json -> varsayim ile değiştirilir"

ESIK_ICSEL_GUCLU = 1.3      # İçsel Değer / Fiyat >= 1,3x : güçlü aday
ESIK_ICSEL_IZLE = 1.0       # 1,0 - 1,3x : izlemede; altı: primli
ESIK_ICSEL_ZAYIF = 0.8      # 0,8x altı : en düşük puan
GUVENLIK_PAYI = (0.20, 0.30)   # güvenlik payı bandı: içsel değerin %70-80'i (gösterge)
ESIK_PDDD_SANAYI = 2.0
ESIK_PDDD_BANKA = (0.8, 1.2)
ESIK_FDFAVOK = 8.0
ESIK_NBFAVOK = 2.5
ESIK_NBFAVOK_VETO = 3.5
ESIK_CARI = 1.5

def _sayi(x):
    """Geçerli ve sonlu bir sayıysa float, değilse None."""
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if math.isfinite(v) else None


def varsayim_oku(ayar: dict) -> dict:
    """Ayar dosyasındaki varsayımları varsayılanlarla birleştirir (geçersizleri yok sayar)."""
    sonuc = dict(VARSAYILAN_VARSAYIM)
    kayit = ayar.get("varsayim") if isinstance(ayar, dict) else None
    if isinstance(kayit, dict):
        for k in sonuc:
            v = _sayi(kayit.get(k))
            if v is not None and 0 <= v < 5:
                sonuc[k] = v
    return sonuc


def sirket_tipi(kod: str, bilgi: dict) -> str:
    kod = temiz_kod(kod)
    if kod in BANKA_KODLARI:
        return "banka"
    if kod in HOLDING_KODLARI:
        return "holding"
    if kod in GYO_KODLARI:
        return "gyo"
    sanayi = f"{bilgi.get('industry', '')} {bilgi.get('sector', '')}".lower()
    if "bank" in sanayi:
        return "banka"
    if "reit" in sanayi or "real estate" in sanayi:
        return "gyo"
    if "conglomerate" in sanayi:
        return "holding"
    return "standart"


def banka_duyarlilik(roe, dd, coe, g) -> list:
    """ROE-PD/DD adil değerinin COE (±5 puan) ve g (±4 puan) duyarlılığı.
    Dönüş: [(coe, [(g, adil|None), ...]), ...]"""
    if roe is None or not dd or dd <= 0:
        return []
    tablo = []
    for c in (coe - 0.05, coe, coe + 0.05):
        satir = []
        for gg in (g - 0.04, g, g + 0.04):
            hedef = (roe - gg) / (c - gg) if c > gg else None
            satir.append((gg, hedef * dd if hedef and hedef > 0 else None))
        tablo.append((c, satir))
    return tablo


def temel_bilgi_cek(kod: str) -> dict:
    """Yahoo Finance'in şirket bilgi sözlüğünü getirir (yavaş olabilir; iş parçacığında çağrılır)."""
    bilgi = yf.Ticker(f"{temiz_kod(kod)}.IS").info
    if not isinstance(bilgi, dict) or not bilgi:
        raise ValueError("Yahoo şirket bilgisi döndürmedi")
    return bilgi


def temel_hesapla(bilgi: dict, son: float, tarih, kod: str = "", varsayim: dict = None,
                  ay: int = None) -> dict:
    """Adil değer, değerleme ve finansal sağlık göstergelerini hesaplar.
    Bulunamayan değerler None kalır (uydurma yapılmaz)."""
    v = varsayim or VARSAYILAN_VARSAYIM
    ay = ay or datetime.now().month
    tip = sirket_tipi(kod, bilgi)

    # Bazı şirketler (THYAO gibi) bilançosunu dolar raporlar; Yahoo bu rakamları TL fiyatla
    # karıştırabilir. Böyle durumda TL fiyatla kıyaslanan değerler gösterilmez.
    para_fiyat = str(bilgi.get("currency") or "").upper()
    para_bilanco = str(bilgi.get("financialCurrency") or "").upper()
    kur_uyumsuz = bool(para_fiyat and para_bilanco and para_fiyat != para_bilanco)

    hbk = None if kur_uyumsuz else _sayi(bilgi.get("trailingEps"))
    dd = None if kur_uyumsuz else _sayi(bilgi.get("bookValue"))
    if kur_uyumsuz:
        pd_dd = fk = None
    else:
        pd_dd = son / dd if (dd and dd > 0) else _sayi(bilgi.get("priceToBook"))
        fk = son / hbk if (hbk and hbk > 0) else _sayi(bilgi.get("trailingPE"))
    roe_ham = _sayi(bilgi.get("returnOnEquity"))
    marj_ham = _sayi(bilgi.get("profitMargins"))

    # ---- adil (içsel) değer
    adil, yontem, yontem_not = None, "-", ""
    coe, g = v["ozsermaye_maliyeti"], v["buyume"]
    if tip == "banka" and roe_ham is not None and dd and dd > 0 and coe > g:
        hedef_pddd = (roe_ham - g) / (coe - g)
        if hedef_pddd <= 0:
            yontem = "ROE-PD/DD (banka)"
            yontem_not = (f"ROE %{roe_ham * 100:.1f}, büyüme varsayımı g %{g * 100:.0f}'in altında: "
                          "model pozitif değer üretmiyor (özsermaye reel olarak eriyor). "
                          "Bankaya Graham uygulanmaz; duyarlılık tablosuna bakın")
        else:
            adil = hedef_pddd * dd
            yontem = "ROE-PD/DD (banka)"
            yontem_not = (f"hedef PD/DD=(ROE-g)/(COE-g)={hedef_pddd:.2f}; "
                          f"COE %{coe * 100:.0f}, g %{g * 100:.0f} varsayım; sonuç COE'ye çok "
                          "duyarlıdır, duyarlılık tablosuna bakın")
    if adil is None and tip != "banka" and hbk and dd and hbk > 0 and dd > 0:
        adil = math.sqrt(22.5 * hbk * dd)
        yontem = "Graham Sayısı (kaba gösterge)"
        yontem_not = ("DCF değildir. 22,5 = F/K 15 x PD/DD 1,5 (düşük enflasyonlu ABD için); "
                      "yüksek faiz ve TMS 29 ortamında kaba bir göstergedir")
    if adil is None and tip != "banka":
        hedef = _sayi(bilgi.get("targetMeanPrice"))
        if hedef and hedef > 0:
            adil, yontem = hedef, "Analist hedef ort. (gösterge)"
            yontem_not = "DCF değildir"

    oran = (adil / son) if (adil and son) else None
    hedef_analist = _sayi(bilgi.get("targetMeanPrice"))
    if hedef_analist is not None and hedef_analist <= 0:
        hedef_analist = None
    # Graham gibi gösterge yöntemlerin sonucu analist hedefinden çok ayrışıyorsa
    # sınıflandırma ve alım bölgesi gösterilmez (güvenilmez).
    guvenilmez = bool(adil and hedef_analist and yontem.startswith("Graham")
                      and abs(adil / hedef_analist - 1) > 0.40)
    if oran is None:
        sinif, sinif_renk = "-", None
    elif guvenilmez:
        sinif, sinif_renk = "gösterge, güvenilmez", "soluk"
    elif oran >= ESIK_ICSEL_GUCLU:
        sinif, sinif_renk = "Güçlü aday bölgesi", "up"
    elif oran >= ESIK_ICSEL_IZLE:
        sinif, sinif_renk = "İzlemede", "uyari"
    elif oran >= ESIK_ICSEL_ZAYIF:
        sinif, sinif_renk = "Primli", "down"
    else:
        sinif, sinif_renk = "Primli (belirgin)", "down"

    alim_ok = bool(adil) and not guvenilmez
    alim_ust = adil * (1 - GUVENLIK_PAYI[0]) if alim_ok else None
    alim_alt = adil * (1 - GUVENLIK_PAYI[1]) if alim_ok else None
    duyarlilik = banka_duyarlilik(roe_ham, dd, coe, g) if tip == "banka" else []

    # ---- finansal sağlık
    borc, nakit = _sayi(bilgi.get("totalDebt")), _sayi(bilgi.get("totalCash"))
    favok = _sayi(bilgi.get("ebitda"))
    net_borc = (borc - nakit) if (borc is not None and nakit is not None) else None
    nb_favok = (net_borc / favok) if (net_borc is not None and favok and favok > 0) else None
    favok_negatif = favok is not None and favok <= 0
    cari = _sayi(bilgi.get("currentRatio"))
    fcf = None if kur_uyumsuz else _sayi(bilgi.get("freeCashflow"))
    ifna = _sayi(bilgi.get("operatingCashflow"))
    net_kar = _sayi(bilgi.get("netIncomeToCommon"))
    ifna_kar = (ifna / net_kar) if (ifna is not None and net_kar and net_kar > 0) else None

    temettu = None
    oran_t = _sayi(bilgi.get("trailingAnnualDividendRate")) or _sayi(bilgi.get("dividendRate"))
    if oran_t and son:
        temettu = oran_t / son * 100
    else:
        verim = _sayi(bilgi.get("trailingAnnualDividendYield"))
        if verim is not None:
            temettu = verim * 100

    ima_coe = None
    if tip == "banka" and roe_ham is not None and pd_dd and pd_dd > 0:
        ima_coe = g + (roe_ham - g) / pd_dd   # piyasa fiyatının ima ettiği özsermaye maliyeti

    bilanco = None
    donem = _sayi(bilgi.get("mostRecentQuarter"))
    if donem:
        try:
            bilanco = datetime.fromtimestamp(donem)
        except (OverflowError, OSError, ValueError):
            bilanco = None

    # ---- kırmızı bayraklar / value trap
    bayraklar = []
    if tip != "banka":
        if nb_favok is not None and nb_favok > ESIK_NBFAVOK_VETO:
            bayraklar.append(f"Net Borç/FAVÖK {nb_favok:.1f}x > 3,5x: karar en fazla 'İzlemede' olabilir.")
        if favok_negatif:
            bayraklar.append("FAVÖK sıfır veya negatif: Net Borç/FAVÖK ve FD/FAVÖK anlamsız; "
                             "faaliyet kârlılığı yok.")
        if fcf is not None and fcf < 0:
            bayraklar.append("Son dönem serbest nakit akışı negatif (yalnız tek dönem görüldü; "
                             "üç yıl üst üste ise veto - geçmiş yılları KAP'tan kontrol edin).")
    if kur_uyumsuz:
        bayraklar.append(f"Bilanço {para_bilanco} raporlanıyor, fiyat {para_fiyat}: hisse başı kâr, defter "
                         "değeri, PD/DD, F/K, FD/FAVÖK ve serbest nakit akışı karışmasın diye gösterilmiyor.")
    if adil and hedef_analist and not yontem.startswith("Analist"):
        sapma = adil / hedef_analist - 1
        if abs(sapma) > 0.40:
            bayraklar.append(f"Model adil değeri analist hedef ortalamasından %{abs(sapma) * 100:.0f} "
                             f"{'düşük' if sapma < 0 else 'yüksek'}: varsayımları ve veriyi kontrol edin.")
    ucuz = False
    if pd_dd is not None:
        ucuz = (pd_dd < ESIK_PDDD_BANKA[0]) if tip == "banka" else (pd_dd < ESIK_PDDD_SANAYI)
    tufe = v["tufe_yillik"]
    reel_roe = ((1 + roe_ham) / (1 + tufe) - 1) if roe_ham is not None else None
    zayif_kalite = (
        (reel_roe is not None and reel_roe < 0)
        or (fcf is not None and fcf < 0 and tip != "banka")
        or (nb_favok is not None and nb_favok > ESIK_NBFAVOK_VETO and tip != "banka"))
    if ucuz and zayif_kalite:
        bayraklar.append("Value trap riski: çarpan ucuz görünüyor ama kalite göstergeleri zayıf.")

    return {
        "coe": coe, "guvenilmez": guvenilmez, "tip": tip, "hedef_analist": hedef_analist, "ima_coe": ima_coe, "adil": adil, "yontem": yontem, "yontem_not": yontem_not,
        "tarih": tarih, "son": son, "oran": oran, "sinif": sinif, "sinif_renk": sinif_renk,
        "alim_alt": alim_alt, "alim_ust": alim_ust, "duyarlilik": duyarlilik, "g": g,
        "pd_dd": pd_dd, "fk": fk, "hbk": hbk, "dd": dd,
        "fd_favok": None if (kur_uyumsuz or favok_negatif) else _sayi(bilgi.get("enterpriseToEbitda")),
        "nb_favok": nb_favok, "net_borc": net_borc, "cari": cari, "fcf": fcf,
        "ifna_kar": ifna_kar,
        "roe": roe_ham * 100 if roe_ham is not None else None,
        "roe_esik": tufe * 100, "reel_roe": reel_roe * 100 if reel_roe is not None else None,
        "favok_negatif": favok_negatif,
        "marj": marj_ham * 100 if marj_ham is not None else None,
        "piyasa_degeri": _sayi(bilgi.get("marketCap")),
        "temettu": temettu, "beta": _sayi(bilgi.get("beta")),
        "bilanco": bilanco, "bayraklar": bayraklar,
        "ay": ay,
    }


def _f(x, bicim: str, ek: str = "") -> str:
    return f"{x:{bicim}}{ek}" if x is not None else "-"


def _buyuk_sayi(x) -> str:
    if x is None:
        return "-"
    if abs(x) >= 1e9:
        return f"{x / 1e9:,.1f} mlr TL"
    return f"{x / 1e6:,.0f} mn TL"


AY_ADLARI = ("", "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos",
             "Eylül", "Ekim", "Kasım", "Aralık")


def temel_satirlari(t: dict) -> list:
    """Sağ paneldeki satırlar: (metin, etiket). İlk satır 'Son Fiyat' satırının hizasındadır."""
    def sat(ad, deger, etiket=None):
        return (f"{ad:<20}: {deger}", etiket)

    def baslik(ad):
        return (f"--- {ad} " + "-" * max(3, 44 - len(ad)), "baslik")

    tip = t["tip"]
    banka = tip == "banka"
    tarih = t["tarih"]
    tarih_txt = f"{tarih:%d.%m.%Y}" if tarih is not None else "-"

    satirlar = []
    satirlar.append(sat("Adil Değer",
                        f"{t['adil']:,.2f} TL  ({tarih_txt})" if t["adil"] is not None
                        else ("hesaplanamadı (ROE < g)" if t["tip"] == "banka" and t["duyarlilik"]
                              else "hesaplanamadı"), "adil"))
    satirlar.append(sat("İçsel Değer/Fiyat",
                        f"{t['oran']:.2f}x  ({t['sinif']})" if t["oran"] is not None else "-",
                        t["sinif_renk"]))
    satirlar.append(sat("Yöntem", t["yontem"]))
    if t["hedef_analist"] is not None:
        satirlar.append(sat("Analist hedef ort.", f"{t['hedef_analist']:,.2f} TL  (karşılaştırma)"))
    if t["ima_coe"] is not None:
        satirlar.append(sat("İma edilen COE", f"%{t['ima_coe'] * 100:.1f}  (modeldeki varsayım %{t['coe'] * 100:.0f})"))
    satirlar.append(sat("Bilanço Dönemi", f"{t['bilanco']:%d.%m.%Y}" if t["bilanco"] else "-"))
    if t["guvenilmez"]:
        satirlar.append(("Güvenlik payı bandı gösterilmiyor: Graham analist hedefinden çok ayrışıyor.", "soluk"))
    if t["alim_alt"] is not None:
        satirlar.append(sat("Güv. payı bandı*", f"{t['alim_alt']:,.2f} - {t['alim_ust']:,.2f} TL  (gösterge)"))
    if t["duyarlilik"]:
        satirlar.append(baslik("Duyarlılık: adil değer (TL)"))
        gler = [gg for gg, _ in t["duyarlilik"][0][1]]
        satirlar.append(("COE \\ g     " + "".join(f"{'%' + format(gg * 100, '.0f'):>10}" for gg in gler), "baslik"))
        for c, satir in t["duyarlilik"]:
            hucre = "".join(f"{(format(a, ',.2f') if a else '-'):>10}" for _, a in satir)
            vurgu = "adil" if abs(c - t["coe"]) < 1e-9 else None
            satirlar.append((f"%{c * 100:<9.0f}" + hucre, vurgu))
        satirlar.append(("COE ±5 puan adil değeri çok değiştirir; tek sayıya güvenmeyin.", "soluk"))
    if tip == "holding":
        satirlar.append(("Holding: NAD / NAD iskontosu yöntemi gerekir; elle hesaplayın.", "soluk"))
    elif tip == "gyo":
        satirlar.append(("GYO: değerleme ağırlıklı NAD / PD-DD ile yapılmalı.", "soluk"))

    # ---- değerleme çarpanları
    satirlar.append(baslik("Değerleme"))
    if t["pd_dd"] is not None:
        if banka:
            ok = ESIK_PDDD_BANKA[0] <= t["pd_dd"] <= ESIK_PDDD_BANKA[1]
            esik = "  (banka makul 0,8-1,2x)"
        else:
            ok = t["pd_dd"] < ESIK_PDDD_SANAYI
            esik = "  (eşik < 2,0x)"
        satirlar.append(sat("PD/DD", f"{t['pd_dd']:.2f}{esik}", "up" if ok else "down"))
    else:
        satirlar.append(sat("PD/DD", "-"))
    satirlar.append(sat("F/K", _f(t["fk"], ".2f") + "  (sektör ort. ile kıyaslayın)"))
    if not banka:
        fd = t["fd_favok"]
        satirlar.append(sat("FD/FAVÖK", _f(fd, ".2f") + "  (eşik < 8x)",
                            None if fd is None else ("up" if 0 < fd < ESIK_FDFAVOK else "down")))

    # ---- finansal sağlık
    satirlar.append(baslik("Finansal Sağlık"))
    if banka:
        satirlar.append(("Bankada cari oran ve Net Borç/FAVÖK uygulanmaz; NIM, takipteki", "soluk"))
        satirlar.append(("alacak, SYR ve ROE izlenir (bu veriler Yahoo'da yok).", "soluk"))
    else:
        nb = t["nb_favok"]
        if nb is not None:
            etiket = "up" if nb < ESIK_NBFAVOK else ("uyari" if nb <= ESIK_NBFAVOK_VETO else "down")
            satirlar.append(sat("Net Borç/FAVÖK",
                                f"{nb:.2f}x  (eşik < 2,5x)" if nb >= 0 else f"{nb:.2f}x  (net nakit)",
                                etiket))
        else:
            satirlar.append(sat("Net Borç/FAVÖK", "-"))
        c = t["cari"]
        satirlar.append(sat("Cari Oran", _f(c, ".2f") + "  (eşik > 1,5x)",
                            None if c is None else ("up" if c > ESIK_CARI else "down")))
        f_ = t["fcf"]
        satirlar.append(sat("Serbest Nakit Ak.", _buyuk_sayi(f_),
                            None if f_ is None else ("up" if f_ > 0 else "down")))
        ik = t["ifna_kar"]
        satirlar.append(sat("İFNA / Net Kâr", _f(ik, ".2f") + "  (eşik > 1)",
                            None if ik is None else ("up" if ik > 1 else "down")))
    roe = t["roe"]
    satirlar.append(sat("Özsermaye Kârlılığı",
                        _f(roe, ".1f", " %") + f"  (TÜFE %{t['roe_esik']:.1f})",
                        None if roe is None else ("up" if roe > t["roe_esik"] else "down")))
    if t.get("reel_roe") is not None:
        satirlar.append(sat("Reel ROE", f"{t['reel_roe']:+.1f} %  ({t.get('tufe_donem', VARSAYILAN_TUFE_DONEM)})",
                            "up" if t["reel_roe"] > 0 else "down"))
    satirlar.append(sat("Net Kâr Marjı", _f(t["marj"], ".1f", " %")))

    # ---- diğer
    satirlar.append(baslik("Diğer"))
    satirlar.append(sat("Piyasa Değeri", _buyuk_sayi(t["piyasa_degeri"])))
    satirlar.append(sat("Temettü Verimi", _f(t["temettu"], ".2f", " %")))
    satirlar.append(sat("Hisse Başı Kâr", _f(t["hbk"], ",.2f", " TL")))
    satirlar.append(sat("Defter Değeri/Hisse", _f(t["dd"], ",.2f", " TL")))
    satirlar.append(sat("Beta", _f(t["beta"], ".2f") + "  (Yahoo; BIST için güvenilmez)"))

    # ---- uyarılar
    if t["bayraklar"]:
        satirlar.append(baslik("Uyarılar"))
        for b in t["bayraklar"]:
            satirlar.append(("! " + b, "uyari"))

    satirlar.append(("", None))
    satirlar.append(("* Güvenlik payı bandı: içsel değer eksi %20-30. Tarama göstergesidir, alım önerisi değildir.", "soluk"))
    satirlar.append((f"Varsayımlar: COE %{t['coe'] * 100:.0f}, g %{t['g'] * 100:.0f} ({VARSAYIM_KAYNAK}).", "soluk"))
    if t["yontem_not"]:
        satirlar.append((f"Not: {t['yontem_not']}.", "soluk"))
    satirlar.append(("Kaynak: Yahoo Finance son bilanço verileri. Yatırım tavsiyesi değildir.", "soluk"))
    return satirlar


# ---------------------------------------------------------------- analiz
def _yuzde(x, ek="") -> str:
    return f"{x * 100:+.1f}%{ek}" if x is not None else "-"


def analiz_uret(kod: str, tufe: float = None, kuresel: dict = None) -> dict:
    endeks = endeks_mi(kod)
    if endeks:
        veri = veri_yahoo(kod)
        kaynak, durum = "Yahoo Finance", [f"{'Yahoo Finance':<14}: OK ({len(veri)} gün)"]
        capraz = "Çapraz kontrol: endeks için yalnız Yahoo kullanılır."
    else:
        veri, kaynak, durum, capraz = veri_coklu(kod)
    if len(veri) < 20:
        raise ValueError(f"'{temiz_kod(kod)}' için yeterli geçmiş veri yok.")

    kapanis = veri["Close"]
    son = float(kapanis.iloc[-1])
    onceki = float(kapanis.iloc[-2])
    degisim = (son / onceki - 1) * 100
    sma20 = float(kapanis.rolling(20).mean().iloc[-1])
    sma50 = float(kapanis.rolling(50).mean().iloc[-1]) if len(kapanis) >= 50 else float("nan")
    sma200 = float(kapanis.rolling(200).mean().iloc[-1]) if len(kapanis) >= 200 else float("nan")
    rsi = rsi_hesapla(kapanis)
    kanit = kanit_bayraklari(kapanis)
    yuksek = float(veri["High"].tail(252).max())
    dusuk = float(veri["Low"].tail(252).min())
    uyarilar = veri_uyarilari(veri, kaynak)
    seans_acik = any(u.startswith("Seans açık") for u in uyarilar)

    seriler = (kuresel or {}).get("seriler", {})
    usdtry = seriler.get("USDTRY")
    xu100 = None if endeks else seriler.get("XU100")
    getiri = getiri_tablosu(kapanis, usdtry, xu100, tufe)
    hacim_tl = None if endeks else islem_hacmi_tl(veri)

    durumlar = []
    durumlar.append("Fiyat SMA20 üzerinde." if son > sma20 else "Fiyat SMA20 altında.")
    if pd.notna(sma50):
        durumlar.append("SMA20, SMA50 üzerinde." if sma20 > sma50 else "SMA20, SMA50 altında.")
    if pd.notna(sma200):
        durumlar.append("Fiyat SMA200 üzerinde." if son > sma200 else "Fiyat SMA200 altında.")
    durumlar.append(f"RSI(14) {rsi:.0f}.")

    konum = (son - dusuk) / (yuksek - dusuk) * 100 if yuksek > dusuk else 0
    sma50_txt = f"{sma50:,.2f}" if pd.notna(sma50) else "-"
    sma200_txt = f"{sma200:,.2f}" if pd.notna(sma200) else "- (200 günden az veri)"
    birim = "puan" if endeks else "TL"

    ad = "BIST 100 Endeksi" if endeks else (sirket_adi(temiz_kod(kod)) or None)
    baslik = (f"{temiz_kod(kod)}{' - ' + ad if ad else ''}  |  "
              f"{datetime.now():%d.%m.%Y %H:%M}  |  Ana kaynak: {kaynak}  |  v{SURUM}")
    ayirac = "-" * 52
    kanit_txt = ("ZAYIF İŞARET" if kanit["etiket"] == "ZAYIF" else "NÖTR")
    if seans_acik:
        kanit_txt += "  (son mum kapanmadı)"
    govde = [
        f"Son Fiyat        : {son:,.2f} {birim}  ({veri.index[-1]:%d.%m.%Y})",
        f"Günlük Değişim   : {degisim:+.2f} %",
        f"Kanıt işareti    : {kanit_txt}",
        f"SMA20 / SMA50    : {sma20:,.2f} / {sma50_txt}",
        f"SMA200           : {sma200_txt}",
        f"RSI (14)         : {rsi:.1f}",
        f"52H Düşük/Yüksek : {dusuk:,.2f} / {yuksek:,.2f}",
        f"52H Aralıkta     : %{konum:.0f}",
    ]
    if hacim_tl is not None:
        govde.append(f"Ort. işlem (20g) : {_buyuk_sayi(hacim_tl)}")
    elif not endeks:
        govde.append("Ort. işlem (20g) : - (bu kaynakta hacim yok)")
    govde += [ayirac, "Getiri          TL        USD      " + ("" if endeks else "XU100'e göre")]
    for donem in ("1A", "3A", "1Y"):
        g = getiri.get(donem)
        if not g:
            govde.append(f"  {donem:<4}          -")
            continue
        satir = f"  {donem:<4}     {_yuzde(g['tl']):>8}  {_yuzde(g['usd']):>8}"
        if not endeks:
            satir += f"   {_yuzde(g['xu']):>8}"
        govde.append(satir)
    g1 = getiri.get("1Y")
    if g1 and g1.get("reel") is not None:
        govde.append(f"  1Y reel (TÜFE %{tufe * 100:.1f}): {_yuzde(g1['reel'])}")
    if usdtry is None:
        govde.append("  (USD/XU100 verisi alınamadı; yalnız TL getiri)")

    govde += [ayirac, f"Kanıt işaretleri ({KANIT_KAYNAK}):"]
    for b in kanit["satirlar"]:
        var = "VAR " if b["var"] else ("yok " if b["var"] is not None else "-   ")
        karar = "kanıtlı" if b["kanitli"] else "kanıtsız"
        govde.append(f"  [{var}] {b['ad']}  ({b['yon']}, {karar}; {b['olcum']})")
    govde.append(f"  -> {kanit['aciklama']}")
    if endeks:
        govde.append("  Not: işaretler hisse örnekleminde ölçüldü; endeks için ayrıca sınanmadı.")

    govde += [ayirac, "Teknik durum (yorumsuz):"] + [f"  • {d}" for d in durumlar]
    if kuresel and not endeks:
        ruzgar = hisse_ruzgari(kod, kuresel)
        govde += [ayirac, f"Küresel rüzgâr (rejim: {kuresel['rejim']['etiket']}):"]
        govde += [f"  • {m}" for m, _ in ruzgar] or ["  • Bu hisse için tanımlı emtia/kur bağı yok."]
    if uyarilar:
        govde += [ayirac, "Uyarılar:"] + [f"  ! {u}" for u in uyarilar]
    govde += [ayirac, "Veri Kaynakları:"] + [f"  {d}" for d in durum] + [
        f"  {capraz}",
        "",
        "AL/SAT sinyali üretilmez: geri testte kanıtlı olmayan kurallar kaldırıldı (v2.2).",
        "Not: Bu rapor yatırım tavsiyesi değildir.",
    ]
    govde_txt = "\n".join(govde)
    return {
        "metin": baslik + "\n" + "=" * 52 + "\n" + govde_txt,
        "baslik": baslik,
        "govde": govde_txt,
        "kod": temiz_kod(kod),
        "endeks": endeks,
        "veri": veri,
        "kaynak": kaynak,
        "son": son,
        "tarih": veri.index[-1],
        "kanit": kanit,
        "getiri": getiri,
        "usdtry": usdtry,
        "xu100": xu100,
    }


def endeks_satirlari(gen: dict, kuresel: dict = None) -> list:
    """Endeks incelemesinde sağ panel: piyasa genişliği + küresel rejim."""
    def sat(ad, deger, etiket=None):
        return (f"{ad:<20}: {deger}", etiket)

    def baslik(ad):
        return (f"--- {ad} " + "-" * max(3, 44 - len(ad)), "baslik")

    s = []
    if gen is None:
        s.append(("Piyasa genişliği alınamadı (üye verisi yok).", "soluk"))
    else:
        s.append(baslik(f"Piyasa genişliği ({gen['tarih']:%d.%m.%Y})"))
        s.append(sat("Veri olan üye", f"{gen['n']} / {gen['toplam']}"))
        for ad, k in (("SMA50 üstü", "ust50"), ("SMA200 üstü", "ust200")):
            v = gen[k]
            s.append(sat(ad, f"%{v:.0f}" if v is not None else "-",
                         None if v is None else ("up" if v >= 50 else "down")))
        s.append(sat("Yükselen / düşen", f"{gen['yukselen']} / {gen['dusen']}  (son gün)",
                     "up" if gen["yukselen"] > gen["dusen"] else "down"))
        s.append(sat("52H zirveye %5 yakın", f"{gen['zirve']} hisse"))
        s.append(sat("52H dibe %5 yakın", f"{gen['dip']} hisse"))
        if gen["ay_medyan"] is not None:
            s.append(sat("1A medyan getiri", _yuzde(gen["ay_medyan"]),
                         "up" if gen["ay_medyan"] > 0 else "down"))
        if len(gen["ay_en_iyi"]):
            s.append(("1A en iyi : " + ", ".join(f"{k} {_yuzde(v)}" for k, v in gen["ay_en_iyi"].items()), "up"))
            s.append(("1A en kötü: " + ", ".join(f"{k} {_yuzde(v)}" for k, v in gen["ay_en_kotu"].items()), "down"))
        s.append(("Genişlik: eşit ağırlıklı üye sayımı; endeks ağırlığı değildir.", "soluk"))
    if kuresel:
        r = kuresel["rejim"]
        s.append(baslik("Küresel rejim"))
        s.append(sat("Rejim", r["etiket"], r["renk"]))
        for m in r["kacis"]:
            s.append(("  - " + m, "down"))
        for m in r["istah"]:
            s.append(("  + " + m, "up"))
    s.append(("", None))
    s.append(("Kaynak: Yahoo Finance. Yatırım tavsiyesi değildir.", "soluk"))
    return s


# ----------------------------------------------------------------- liste
def _son_iki_kapanis(df: pd.DataFrame):
    k = df["Close"].dropna()
    if len(k) < 2:
        raise ValueError("yetersiz veri")
    return float(k.iloc[-1]), float(k.iloc[-2])


def _kodlari_temizle(kodlar) -> list:
    sonuc = []
    for k in kodlar:
        k = str(k).strip().upper().split(".")[0]
        if not KOD_RE.match(k) or k in BASLIK_KELIMELERI or k in sonuc:
            continue
        sonuc.append(k)
    return sonuc


def baslangic_listesi():
    klasor = veri_klasoru()
    try:
        with open(os.path.join(klasor, MANUEL_DOSYA), encoding="utf-8") as f:
            kodlar = _kodlari_temizle(re.split(r"[\s,;]+", f.read()))
        if kodlar:
            return kodlar, f"{MANUEL_DOSYA} dosyasından ({len(kodlar)} hisse)"
    except OSError:
        pass
    try:
        with open(os.path.join(klasor, LISTE_DOSYASI), encoding="utf-8") as f:
            veri = json.load(f)
        kodlar = _kodlari_temizle(veri["kodlar"])
        if kodlar:
            return kodlar, f"son güncellemeden ({veri.get('tarih', '?')}, {len(kodlar)} hisse)"
    except (OSError, ValueError, KeyError):
        pass
    return list(BIST_KODLARI), f"yerleşik yedek liste ({len(BIST_KODLARI)} hisse, eksik)"


def _endeks_ayristir(ham: bytes) -> list:
    if len(ham) > MAKS_YANIT:
        raise ValueError("dosya beklenenden büyük")
    metin = None
    for kodlama in ("utf-8-sig", "cp1254", "latin-1"):
        try:
            metin = ham.decode(kodlama)
            break
        except UnicodeDecodeError:
            continue
    kodlar = []
    for satir in metin.splitlines():
        if len(satir) > 2000:
            continue
        alanlar = [a.strip() for a in re.split(r"[;\t|]", satir) if a.strip()]
        if not alanlar or not ENDEKS_ADLARI.search(satir.upper()):
            continue
        aday = re.split(r"[\s,]+", alanlar[0].upper())[0]
        if aday in {"XU100", "BIST100"}:
            continue
        kodlar.extend(_kodlari_temizle([aday]))
    kodlar = _kodlari_temizle(kodlar)
    if not 80 <= len(kodlar) <= 120:
        raise ValueError(f"beklenmeyen üye sayısı: {len(kodlar)}")
    return sorted(kodlar)


def endeks_uyeleri_getir() -> list:
    r = guvenli_get(ENDEKS_URL)
    try:
        r.raise_for_status()
        return _endeks_ayristir(r.content)
    except Exception:
        log.warning("Endeks dosyası okunamadı: %s", _yanit_ozeti(r))
        raise


def uyeleri_guncelle(mevcut: list):
    try:
        yeni = endeks_uyeleri_getir()
        eklenen = sorted(set(yeni) - set(mevcut))
        cikan = sorted(set(mevcut) - set(yeni))
        try:
            with open(os.path.join(veri_klasoru(), LISTE_DOSYASI), "w", encoding="utf-8") as f:
                json.dump({"tarih": datetime.now().strftime("%d.%m.%Y %H:%M"), "kodlar": yeni}, f)
        except OSError:
            log.warning("Liste önbelleği yazılamadı.")
        log.info("Üyelik güncellendi: %d hisse (+%d / -%d)", len(yeni), len(eklenen), len(cikan))
        ozet = (f"BIST 100 üyeliği Borsa İstanbul'dan güncellendi: {len(yeni)} hisse.\n"
                f"Eklenen : {', '.join(eklenen) or '-'}\n"
                f"Çıkan   : {', '.join(cikan) or '-'}")
        return yeni, ozet, True
    except Exception as e:
        neden = str(e) or e.__class__.__name__
        log.warning("Üyelik güncellenemedi: %s", neden)
        return mevcut, (f"Üyelik güncellenemedi ({neden}).\nMevcut liste ({len(mevcut)} hisse) "
                        f"kullanıldı. İsterseniz {MANUEL_DOSYA} dosyasına kodları "
                        f"yazabilirsiniz.\nAyrıntı: {LOG_DOSYASI}"), False


def liste_getir(mevcut: list, ekstra=()) -> dict:
    uyeler, uye_ozeti, uye_ok = uyeleri_guncelle(mevcut)
    kodlar = uyeler + [k for k in _kodlari_temizle(ekstra) if k not in uyeler]
    semboller = [f"{k}.IS" for k in kodlar]
    sonuc = {}
    try:
        toplu = yf.download(semboller, period="5d", group_by="ticker", progress=False,
                            threads=True, auto_adjust=True, timeout=ZAMAN_ASIMI)
        for kod, sem in zip(kodlar, semboller):
            try:
                son, onceki = _son_iki_kapanis(toplu[sem])
                sonuc[kod] = (son, (son / onceki - 1) * 100, "Y")
            except Exception:
                continue
    except Exception as e:
        log.warning("Yahoo toplu fiyat çekimi başarısız: %s", e)

    eksik = [k for k in kodlar if k not in sonuc]

    def tamamla(kod):
        try:
            df = veri_isyatirim(kod, gun=20)
            son, onceki = _son_iki_kapanis(df)
            return kod, (son, (son / onceki - 1) * 100, "İ")
        except Exception:
            return kod, None

    if eksik:
        with ThreadPoolExecutor(max_workers=8) as havuz:
            for kod, deger in havuz.map(tamamla, eksik):
                if not deger:
                    continue
                sonuc[kod] = deger

    satirlar = [(k, *sonuc[k]) for k in kodlar if k in sonuc]
    y_say = sum(1 for s in satirlar if s[3] == "Y")
    log.info("Fiyat listesi: %d/%d hisse (Yahoo %d, İş Yatırım %d)",
             len(satirlar), len(kodlar), y_say, len(satirlar) - y_say)
    return {"satirlar": satirlar, "y": y_say, "i": len(satirlar) - y_say,
            "kodlar": uyeler, "istenen": len(kodlar), "uye_ozeti": uye_ozeti, "uye_ok": uye_ok}


# ------------------------------------------------------- tarama betiği (v2.3)
TARAMA_OMUR = timedelta(minutes=15)
HAREKETLI_ADET = 20
HAREKET_ESIK = 50          # en az bu puan (0-100) olan en hareketli 20 hisse
GORUNUMLER = (("tum", "Tümü"), ("hareketli", "En Hareketli"), ("yukselen", "Yükselme Eğilimi"))
TREND_SART = ("Fiyat > SMA20",)
TREND_EN_AZ = 4            # 6 koşuldan en az 4 (SMA200 yoksa 5 koşuldan 4)
ASIRI_ALIM = 70


def tarama_olcutleri(veri: pd.DataFrame):
    """Tek hissenin günlük verisinden filtre ölçütleri. Yetersiz veri: None."""
    k = veri["Close"].dropna().astype(float)
    if len(k) < 60:
        return None
    son, onceki = float(k.iloc[-1]), float(k.iloc[-2])
    a1 = (son / float(k.iloc[-22]) - 1) * 100
    oyn = float(k.pct_change().tail(20).std() * math.sqrt(252) * 100)
    hacim_x = hacim_tl = None
    if "Volume" in veri:
        tutar = (veri["Close"] * veri["Volume"]).reindex(k.index)
        onceki20 = tutar.iloc[-21:-1].dropna()
        if len(onceki20) >= 15 and onceki20.mean() > 0 and pd.notna(tutar.iloc[-1]) \
                and tutar.iloc[-1] > 0:
            hacim_tl = float(tutar.iloc[-1])
            hacim_x = hacim_tl / float(onceki20.mean())
    sma20, sma50 = k.rolling(20).mean(), k.rolling(50).mean()
    sma200 = k.rolling(200).mean() if len(k) >= 200 else None
    rsi = rsi_hesapla(k)
    kosullar = {
        "Fiyat > SMA20": son > float(sma20.iloc[-1]),
        "SMA20 > SMA50": float(sma20.iloc[-1]) > float(sma50.iloc[-1]),
        "SMA20 yükseliyor (5 gün)": float(sma20.iloc[-1]) > float(sma20.iloc[-6]),
        "SMA50 > SMA200": (float(sma50.iloc[-1]) > float(sma200.iloc[-1]))
                          if sma200 is not None else None,
        "1A getiri > 0": a1 > 0,
        "RSI > 50": rsi > 50,
    }
    gecerli = [v for v in kosullar.values() if v is not None]
    return {"son": son, "deg": (son / onceki - 1) * 100,
            "g5": (son / float(k.iloc[-6]) - 1) * 100, "a1": a1, "oyn": oyn,
            "hacim_x": hacim_x, "hacim_tl": hacim_tl, "rsi": rsi, "kosullar": kosullar,
            "trend": sum(1 for v in gecerli if v), "trend_n": len(gecerli),
            "zayif": kanit_bayraklari(k)["etiket"] == "ZAYIF", "tarih": k.index[-1]}


def tarama_getir(kodlar: list) -> dict:
    """Betik: listedeki hisselerin 1 yıllık verisini toplu çeker, ölçütleri hesaplar."""
    kodlar = _kodlari_temizle(kodlar)
    olcut, kaynak = {}, {}
    if kodlar:
        semboller = [f"{k}.IS" for k in kodlar]
        try:
            toplu = yf.download(semboller, period="2y", group_by="ticker", progress=False,
                                threads=True, auto_adjust=True, timeout=ZAMAN_ASIMI)
            for kod, sem in zip(kodlar, semboller):
                try:
                    df = toplu[sem].copy()
                    df.index = _gunluk_indeks(df.index)
                    o = tarama_olcutleri(_standartla(df))
                    if o:
                        olcut[kod], kaynak[kod] = o, "Y"
                except Exception:
                    continue
        except Exception as e:
            log.warning("Tarama: Yahoo toplu çekim başarısız: %s", e)

    def tamamla(kod):
        try:
            return kod, tarama_olcutleri(veri_isyatirim(kod, gun=740))
        except Exception:
            return kod, None

    eksik = [k for k in kodlar if k not in olcut]
    if eksik:
        with ThreadPoolExecutor(max_workers=8) as havuz:
            for kod, o in havuz.map(tamamla, eksik):
                if o:
                    olcut[kod], kaynak[kod] = o, "İ"
    log.info("Tarama: %d/%d hisse", len(olcut), len(kodlar))
    return {"olcut": olcut, "kaynak": kaynak, "zaman": datetime.now(),
            "eksik": [k for k in kodlar if k not in olcut]}


def _sira_puani(seri: pd.Series) -> pd.Series:
    return seri.rank(pct=True) if seri.notna().any() else seri


def hareketli_sec(olcut: dict, kodlar: list) -> list:
    """[(kod, puan)] en hareketliden aza. Puan = 3 sıralamanın ortalaması x 100."""
    adaylar = [k for k in kodlar if k in olcut]
    if not adaylar:
        return []
    df = pd.DataFrame({"hx": [olcut[k]["hacim_x"] for k in adaylar],
                       "deg": [abs(olcut[k]["deg"]) for k in adaylar],
                       "oyn": [olcut[k]["oyn"] for k in adaylar]},
                      index=adaylar, dtype=float)
    puan = pd.concat([_sira_puani(df[c]) for c in df], axis=1).mean(axis=1, skipna=True) * 100
    puan = puan.dropna().sort_values(ascending=False)
    if len(adaylar) > HAREKETLI_ADET:
        puan = puan[puan >= HAREKET_ESIK].head(HAREKETLI_ADET)
    return [(k, float(p)) for k, p in puan.items()]


def yukselen_sec(olcut: dict, kodlar: list) -> list:
    """[(kod, (trend, 1A))] güçlüden zayıfa."""
    sonuc = []
    for k in kodlar:
        o = olcut.get(k)
        if not o or o["zayif"] or o["trend_n"] < 5:
            continue
        if not all(o["kosullar"][s] for s in TREND_SART):
            continue
        if o["trend"] >= TREND_EN_AZ:
            sonuc.append((k, (o["trend"] / o["trend_n"], o["a1"])))
    return sorted(sonuc, key=lambda x: x[1], reverse=True)


def yukselen_eleme(olcut: dict, kodlar: list) -> dict:
    """Şeffaflık: her koşulu kaç hisse sağlıyor ve eşiğe en yakın (elenen) adaylar."""
    veri = [olcut[k] for k in kodlar if k in olcut]
    sayac = {}
    for o in veri:
        for ad, v in o["kosullar"].items():
            if v is not None:
                sayac.setdefault(ad, [0, 0])
                sayac[ad][0] += bool(v)
                sayac[ad][1] += 1
    secilen = {k for k, _ in yukselen_sec(olcut, kodlar)}
    yakin = []
    for k in kodlar:
        o = olcut.get(k)
        if not o or k in secilen:
            continue
        neden = [a for a, v in o["kosullar"].items() if v is False]
        if o["zayif"]:
            neden.insert(0, "kanıtlı olumsuz bayrak")
        yakin.append((o["trend"] - (2 if o["zayif"] else 0), o["a1"], k, neden))
    yakin.sort(reverse=True)
    return {"sayac": sayac, "toplam": len(veri),
            "zayif": sum(1 for o in veri if o["zayif"]),
            "yakin": [(k, ", ".join(n)) for _, _, k, n in yakin[:6]]}


def tarama_raporu(gorunum: str, secilen: list, olcut: dict, evren_adi: str,
                  evren_say: int, eksik: list, zaman: datetime, kodlar=None) -> str:
    sat = [f"{evren_adi}: {evren_say} hisse tarandı, {len(secilen)} hisse filtreye uydu.",
           f"Ölçüm: {zaman:%d.%m.%Y %H:%M} (Yahoo; eksikte İş Yatırım)", "-" * 48]
    if gorunum == "hareketli":
        sat.append(f"{'Kod':<6}{'Puan':>5}{'Hacim':>7}{'Gün%':>7}{'5G%':>7}"
                   f"{'Oyn%':>5}{'TL hacim':>11}")
        for k, p in secilen:
            o = olcut[k]
            hx = f"{o['hacim_x']:.1f}x" if o["hacim_x"] is not None else "-"
            tl = _buyuk_sayi(o["hacim_tl"]).replace(" TL", "")
            sat.append(f"{k:<6}{p:>5.0f}{hx:>7}{o['deg']:>+7.1f}{o['g5']:>+7.1f}"
                       f"{o['oyn']:>5.0f}{tl:>11}")
        sat += ["-" * 48,
                "Puan: hacim çarpanı (son gün TL hacim / önceki 20 gün ortalaması),",
                "günlük mutlak değişim ve 20 günlük yıllık oynaklık sıralamalarının",
                f"ortalaması (0-100). En çok {HAREKETLI_ADET} hisse, puan >= {HAREKET_ESIK}.",
                "Seans açıkken son günün hacmi eksiktir; hacim çarpanı düşük görünür."]
    else:
        sat.append(f"{'Kod':<6}{'Trend':>6}{'1A%':>7}{'5G%':>7}{'RSI':>5}  Eksik koşul / not")
        for k, _ in secilen:
            o = olcut[k]
            eks = [a for a, v in o["kosullar"].items() if v is False]
            if o["rsi"] > ASIRI_ALIM:
                eks.append("aşırı alım (RSI>70)")
            sat.append(f"{k:<6}{o['trend']:>4}/{o['trend_n']}{o['a1']:>+7.1f}"
                       f"{o['g5']:>+7.1f}{o['rsi']:>5.0f}  {', '.join(eks) or '-'}")
        sat += ["-" * 48,
                f"Kural: Fiyat > SMA20 şart ve 6 koşuldan en az {TREND_EN_AZ}'ü.",
                "Kanıtlı olumsuz bayrağı (12-1 ay < -%10) olan hisseler elenir."]
        if kodlar:
            el = yukselen_eleme(olcut, kodlar)
            sat += ["", f"ELEME ÖZETİ ({el['toplam']} hisse) - koşulu sağlayan:"]
            for ad, (evet, n) in el["sayac"].items():
                sat.append(f"  {ad:<26}{evet:>4}/{n}")
            sat.append(f"  {'Kanıtlı olumsuz bayrak':<26}{el['zayif']:>4} (elenir)")
            if el["yakin"]:
                sat += ["", "Eşiğe en yakın elenen adaylar (neden):"]
                sat += [f"  {k:<6} {n}" for k, n in el["yakin"]]
            sat.append("Not: sonuç günlük kapanışa göre değişir; aynı gün içinde aynı kalır.")
    if eksik:
        sat.append(f"Veri alınamayan: {', '.join(eksik[:15])}" + (" ..." if len(eksik) > 15 else ""))
    sat += ["", "UYARI: Bu filtre bir TARAMA aracıdır; geri testte kanıtlanmamıştır.",
            "AL/SAT sinyali değildir. Satıra çift tıklayıp hisseyi ayrıca inceleyin."]
    return "\n".join(sat)


def tarama_yz_ozeti(gorunum: str, secilen: list, olcut: dict, evren_adi: str) -> str:
    baslik = "En hareketli" if gorunum == "hareketli" else "Yükselme eğilimindeki"
    sat = [f"{evren_adi} içinde {baslik} hisseler (teknik tarama, kanıtsız):"]
    for k, _ in secilen[:12]:
        o = olcut[k]
        hx = f", hacim {o['hacim_x']:.1f}x" if o["hacim_x"] is not None else ""
        sat.append(f"{k} ({sirket_adi(k, '-')}): gün %{o['deg']:+.1f}, 5G %{o['g5']:+.1f}, "
                   f"1A %{o['a1']:+.1f}, RSI {o['rsi']:.0f}{hx}")
    if not secilen:
        sat.append("Filtreye uyan hisse yok.")
    return "\n".join(sat)


# ----------------------------------------------------- Hisselerim listeleri
HISSELERIM_DOSYASI = "hisselerim.json"
VARSAYILAN_LISTE = "Hisselerim"
TUM_LISTE = "BIST 100"
MAKS_LISTE = 30
MAKS_LISTE_HISSE = 300
LISTE_AD_RE = re.compile(r"[0-9A-Za-zÇĞİÖŞÜçğıöşü .\-_]{1,30}")


def liste_adi_temizle(ad: str) -> str:
    ad = " ".join(str(ad).split())
    if not LISTE_AD_RE.fullmatch(ad):
        raise ValueError("Liste adı 1-30 karakter olmalı; harf, rakam, boşluk, . - _ kullanılabilir.")
    if ad.upper() in {TUM_LISTE.upper(), "BIST100", "XU100"}:
        raise ValueError(f"'{ad}' adı ayrılmıştır, başka bir ad seçin.")
    return ad


def hisselerim_oku() -> dict:
    yol = os.path.join(veri_klasoru(), HISSELERIM_DOSYASI)
    try:
        with open(yol, encoding="utf-8") as f:
            ham = json.load(f).get("listeler", {})
    except FileNotFoundError:
        return {VARSAYILAN_LISTE: []}
    except (OSError, ValueError, AttributeError):
        log.warning("%s okunamadı; boş liste ile başlandı.", HISSELERIM_DOSYASI)
        return {VARSAYILAN_LISTE: []}
    listeler = {}
    for ad, kodlar in list(ham.items())[:MAKS_LISTE]:
        try:
            listeler[liste_adi_temizle(ad)] = _kodlari_temizle(kodlar)[:MAKS_LISTE_HISSE]
        except (ValueError, TypeError):
            continue
    return listeler


def adlari_yukle() -> None:
    try:
        with open(os.path.join(veri_klasoru(), AD_DOSYASI), encoding="utf-8") as f:
            veri = json.load(f)
        for k, v in (veri.items() if isinstance(veri, dict) else []):
            if KOD_RE.match(str(k)) and isinstance(v, str) and 0 < len(v) <= 60:
                _EK_ADLAR[k] = v
    except (OSError, ValueError):
        pass


_AD_EKLERI = re.compile(r"[\s,]+(A\.?\s?[SŞO]\.?|T\.?\s?A\.?\s?[SŞ]\.?|ANON[Iİ]M [SŞ][Iİ]RKET[Iİ]|"
                        r"SANAY[Iİ] VE T[Iİ]CARET|SAN\.? VE T[Iİ]C\.?)\.?$", re.I)


def _ad_sadelestir(ad: str) -> str:
    ad = " ".join(str(ad).split())
    for _ in range(3):
        ad = _AD_EKLERI.sub("", ad).strip(" ,.")
    if ad.isupper():
        ad = " ".join(w if len(w) <= 2 else w[0] + w[1:].lower().replace("i̇", "i")
                      for w in ad.split())
    return ad[:60]


def adlari_tamamla(kodlar) -> int:
    """Adı bilinmeyen kodların adını Yahoo'dan alır, sirket_adlari.json'a yazar."""
    eksik = [k for k in _kodlari_temizle(kodlar)
             if not sirket_adi(k) and k not in _AD_DENENDI][:60]
    if not eksik:
        return 0
    _AD_DENENDI.update(eksik)

    def al(kod):
        try:
            bilgi = yf.Ticker(f"{kod}.IS").get_info() or {}
            ad = bilgi.get("longName") or bilgi.get("shortName")
            return kod, _ad_sadelestir(ad) if ad else None
        except Exception:
            return kod, None

    yeni = 0
    with ThreadPoolExecutor(max_workers=6) as havuz:
        for kod, ad in havuz.map(al, eksik):
            if ad:
                _EK_ADLAR[kod] = ad
                yeni += 1
    if yeni:
        try:
            with open(os.path.join(veri_klasoru(), AD_DOSYASI), "w", encoding="utf-8") as f:
                json.dump(_EK_ADLAR, f, ensure_ascii=False, indent=1)
        except OSError:
            log.warning("%s yazılamadı.", AD_DOSYASI)
        log.info("Şirket adı tamamlandı: %d", yeni)
    return yeni


def hisselerim_yaz(listeler: dict) -> bool:
    yol = os.path.join(veri_klasoru(), HISSELERIM_DOSYASI)
    try:
        with open(yol + ".tmp", "w", encoding="utf-8") as f:
            json.dump({"surum": SURUM, "listeler": listeler}, f, ensure_ascii=False, indent=1)
        os.replace(yol + ".tmp", yol)
        return True
    except OSError:
        log.warning("%s yazılamadı.", HISSELERIM_DOSYASI, exc_info=True)
        return False


# ------------------------------------------------------------------ arayüz
class ListeDuzenleyici:
    """Liste oluşturma / düzenleme penceresi. sonuc: (ad, kodlar) veya None."""

    def __init__(self, ust, baslik, ad, kodlar, tum_kodlar, mevcut_adlar):
        self.sonuc = None
        self.tum = sorted(set(tum_kodlar) | set(kodlar))
        self.secili = list(kodlar)
        self.mevcut_adlar = {a.lower() for a in mevcut_adlar}
        self.pen = p = tk.Toplevel(ust)
        p.title(baslik)
        p.configure(bg=BG)
        p.transient(ust)
        p.resizable(True, True)
        p.minsize(560, 420)

        def etiket(u, m):
            return tk.Label(u, text=m, bg=BG, fg=MUTED, font=("Segoe UI", 9, "bold"), anchor="w")

        ust_satir = tk.Frame(p, bg=BG)
        ust_satir.pack(fill="x", padx=12, pady=(12, 6))
        etiket(ust_satir, "Liste adı:").pack(side="left")
        self.ad = tk.Entry(ust_satir, bg=PANEL, fg=FG, insertbackground=FG, relief="flat",
                           font=("Segoe UI", 11), width=28)
        self.ad.pack(side="left", padx=8, ipady=4)
        self.ad.insert(0, ad)

        govde = tk.Frame(p, bg=BG)
        govde.pack(fill="both", expand=True, padx=12)
        govde.columnconfigure(0, weight=1)
        govde.columnconfigure(2, weight=1)
        govde.rowconfigure(2, weight=1)
        etiket(govde, "Tüm hisseler (ara):").grid(row=0, column=0, sticky="w")
        etiket(govde, "Listedeki hisseler:").grid(row=0, column=2, sticky="w")
        self.ara = tk.Entry(govde, bg=PANEL, fg=FG, insertbackground=FG, relief="flat",
                            font=("Consolas", 10))
        self.ara.grid(row=1, column=0, sticky="ew", pady=(2, 4), ipady=3)
        self.ara.bind("<KeyRelease>", lambda e: self._doldur())
        self.ara.bind("<Return>", lambda e: self._ekle())
        self.say = tk.Label(govde, text="", bg=BG, fg=MUTED, font=("Segoe UI", 9), anchor="w")
        self.say.grid(row=1, column=2, sticky="w")

        def kutu(sutun):
            lb = tk.Listbox(govde, bg=PANEL, fg=FG, selectbackground=ACCENT,
                            selectforeground="white", relief="flat", bd=0,
                            highlightthickness=0, font=("Consolas", 10),
                            selectmode="extended", activestyle="none")
            lb.grid(row=2, column=sutun, sticky="nsew")
            return lb

        self.sol = kutu(0)
        self.sag = kutu(2)
        self.sol.bind("<Double-1>", lambda e: self._ekle())
        self.sag.bind("<Double-1>", lambda e: self._cikar())
        self.sag.bind("<Delete>", lambda e: self._cikar())
        orta = tk.Frame(govde, bg=BG)
        orta.grid(row=2, column=1, padx=8)
        for metin, komut in (("Ekle  →", self._ekle), ("←  Çıkar", self._cikar),
                             ("Yukarı ▲", lambda: self._tasi(-1)),
                             ("Aşağı ▼", lambda: self._tasi(1))):
            tk.Button(orta, text=metin, command=komut, bg=PANEL, fg=FG, relief="flat", bd=0,
                      activebackground=ACCENT, activeforeground="white", width=10, pady=5,
                      cursor="hand2", font=("Segoe UI", 9, "bold")).pack(pady=3)
        etiket(p, "  İpucu: listede olmayan bir kodu (BIST 100 dışı) arama kutusuna yazıp "
                  "Enter'a basarak ekleyebilirsiniz.").pack(fill="x", padx=12, pady=(6, 0))
        self.hata = tk.Label(p, text="", bg=BG, fg=RED, font=("Segoe UI", 9), anchor="w")
        self.hata.pack(fill="x", padx=12)
        alt = tk.Frame(p, bg=BG)
        alt.pack(fill="x", padx=12, pady=(4, 12))
        for metin, komut, renk in (("İptal", p.destroy, PANEL), ("Kaydet", self._kaydet, ACCENT)):
            tk.Button(alt, text=metin, command=komut, bg=renk, fg=FG, relief="flat", bd=0,
                      activebackground=ACCENT, activeforeground="white", padx=18, pady=6,
                      cursor="hand2", font=("Segoe UI", 10, "bold")).pack(side="right", padx=4)
        p.bind("<Escape>", lambda e: p.destroy())
        self._doldur()
        p.update_idletasks()
        p.geometry(f"+{ust.winfo_rootx() + 60}+{ust.winfo_rooty() + 60}")
        p.grab_set()
        self.ad.focus_set()
        p.wait_window()

    @staticmethod
    def _yazi(k):
        return f"{k:<7}{sirket_adi(k)}"

    def _doldur(self):
        self._sol_kodlar = [k for k in eslesenler(self.ara.get(), self.tum)
                            if k not in self.secili]
        self.sol.delete(0, "end")
        for k in self._sol_kodlar:
            self.sol.insert("end", self._yazi(k))
        self.sag.delete(0, "end")
        for k in self.secili:
            self.sag.insert("end", self._yazi(k))
        self.say.configure(text=f"{len(self.secili)} hisse")

    def _ekle(self):
        secim = [self._sol_kodlar[i] for i in self.sol.curselection()]
        if not secim:
            aranan = temiz_kod(self.ara.get())
            if len(self._sol_kodlar) == 1:
                secim = self._sol_kodlar
            elif KOD_RE.match(aranan) and aranan not in self.secili:
                secim = [aranan]
                self.tum = sorted(set(self.tum) | {aranan})
        if len(self.secili) + len(secim) > MAKS_LISTE_HISSE:
            self.hata.configure(text=f"Bir listede en çok {MAKS_LISTE_HISSE} hisse olabilir.")
            return
        self.secili += [k for k in secim if k not in self.secili]
        self.ara.delete(0, "end")
        self._doldur()

    def _cikar(self):
        sil = {self.secili[i] for i in self.sag.curselection()}
        self.secili = [k for k in self.secili if k not in sil]
        self._doldur()

    def _tasi(self, yon):
        sec = list(self.sag.curselection())
        if len(sec) != 1:
            return
        i, j = sec[0], sec[0] + yon
        if 0 <= j < len(self.secili):
            self.secili[i], self.secili[j] = self.secili[j], self.secili[i]
            self._doldur()
            self.sag.selection_set(j)
            self.sag.see(j)

    def _kaydet(self):
        try:
            ad = liste_adi_temizle(self.ad.get())
        except ValueError as e:
            self.hata.configure(text=str(e))
            return
        if ad.lower() in self.mevcut_adlar:
            self.hata.configure(text=f"'{ad}' adında bir liste zaten var.")
            return
        self.sonuc = (ad, list(self.secili))
        self.pen.destroy()


class BistAnalizApp:
    # Bölme oranları için varsayılanlar (pencere boyutuna göre kesir)
    VARSAYILAN_ORAN = {"ana": 0.58, "sol": 0.58, "rapor": 0.60}

    def __init__(self, root: tk.Tk):
        self.root = root
        self.kuyruk = queue.Queue()
        self.mesgul = False
        self._after_id = None
        self.kodlar, self.liste_kaynagi = baslangic_listesi()
        self.liste_eksik = self.liste_kaynagi.startswith("yerleşik")
        self.fiyatlar = {}
        self.listeler = hisselerim_oku()
        self.tarama = {"olcut": {}, "kaynak": {}, "zaman": None, "eksik": []}
        self.tarama_sonuc = {}       # görünüm filtresinin son sonucu {kod: ölçüt değeri}
        self.sirala_kolon = "kod"
        self.sirala_ters = False
        self.son_analiz = None
        self.yz_sira = 0
        self._temel_satirlar_son = []
        self.ayar = self._ayar_oku()

        self.dpi = max(96.0, float(root.winfo_fpixels("1i")))
        olcek = self.dpi / 96.0
        root.title(f"BIST 100 Analiz Terminali v{SURUM}")
        genislik, yukseklik = int(1160 * olcek), int(800 * olcek)
        kayitli = self.ayar.get("boyut")
        if (isinstance(kayitli, list) and len(kayitli) == 2
                and all(isinstance(v, int) and v > 300 for v in kayitli)):
            genislik, yukseklik = kayitli
        root.geometry(f"{genislik}x{yukseklik}")
        root.minsize(int(1000 * olcek), int(680 * olcek))
        root.configure(bg=BG)
        root.protocol("WM_DELETE_WINDOW", self.kapat)
        root.report_callback_exception = self._arayuz_hatasi

        self._stil()
        self._arayuz()
        self._tabloyu_doldur()
        self._after_id = root.after(100, self._kuyruk_dinle)
        root.after(120, self._bolmeleri_yerlestir)
        root.after(1500, self._ilk_yz_sorusu)
        self.giris.focus_set()

    # ---- ayarlar -----------------------------------------------------
    def _ayar_yolu(self) -> str:
        return os.path.join(veri_klasoru(), AYAR_DOSYASI)

    def _ayar_oku(self) -> dict:
        try:
            with open(self._ayar_yolu(), encoding="utf-8") as f:
                veri = json.load(f)
            return veri if isinstance(veri, dict) else {}
        except (OSError, ValueError):
            return {}

    def _ayar_yaz(self) -> None:
        try:
            self.root.update_idletasks()
            oranlar = {}
            for ad, pano, eksen, boyut in (
                    ("ana", self.ana_bolme, 0, self.ana_bolme.winfo_width()),
                    ("sol", self.sol_bolme, 1, self.sol_bolme.winfo_height()),
                    ("rapor", self.rapor_bolme, 0, self.rapor_bolme.winfo_width())):
                if boyut > 50:
                    oranlar[ad] = round(pano.sash_coord(0)[eksen] / boyut, 4)
            veri = dict(self.ayar)   # bilinmeyen anahtarlar (yerel_yz_adres vb.) korunur
            veri["secili_liste"] = self.liste_sec.get()
            veri.update({"boyut": [self.root.winfo_width(), self.root.winfo_height()],
                         "oranlar": oranlar,
                         "varsayim": varsayim_oku(self.ayar),
                         "tufe_donem": self._tufe_donem()})
            with open(self._ayar_yolu(), "w", encoding="utf-8") as f:
                json.dump(veri, f)
        except Exception:
            log.warning("Pencere ayarları kaydedilemedi.", exc_info=True)

    def _tufe_donem(self) -> str:
        d = self.ayar.get("tufe_donem")
        return d if isinstance(d, str) and 0 < len(d) < 60 else VARSAYILAN_TUFE_DONEM

    def _bolmeleri_yerlestir(self) -> None:
        """Sürükleme çubuklarını kayıtlı (yoksa varsayılan) oranlara getirir."""
        try:
            self.root.update_idletasks()
            kayit = self.ayar.get("oranlar") if isinstance(self.ayar.get("oranlar"), dict) else {}
            for ad, pano, eksen, boyut in (
                    ("ana", self.ana_bolme, 0, self.ana_bolme.winfo_width()),
                    ("sol", self.sol_bolme, 1, self.sol_bolme.winfo_height()),
                    ("rapor", self.rapor_bolme, 0, self.rapor_bolme.winfo_width())):
                oran = kayit.get(ad, self.VARSAYILAN_ORAN[ad])
                if not isinstance(oran, (int, float)) or not 0.1 <= oran <= 0.9:
                    oran = self.VARSAYILAN_ORAN[ad]
                konum = int(boyut * oran)
                if eksen == 0:
                    pano.sash_place(0, konum, 1)
                else:
                    pano.sash_place(0, 1, konum)
        except Exception:
            log.warning("Bölmeler yerleştirilemedi.", exc_info=True)

    # ---- görünüm -----------------------------------------------------
    def _stil(self):
        s = ttk.Style()
        s.theme_use("clam")
        s.configure("Treeview", background=PANEL, fieldbackground=PANEL, foreground=FG,
                    rowheight=24, borderwidth=0)
        s.configure("Treeview.Heading", background=BG, foreground=MUTED, relief="flat",
                    font=("Segoe UI", 9, "bold"))
        s.map("Treeview", background=[("selected", ACCENT)])
        s.configure("Vertical.TScrollbar", background=PANEL, troughcolor=BG,
                    arrowcolor=MUTED, borderwidth=0)
        s.configure("TCombobox", fieldbackground=BG, background=PANEL, foreground=FG,
                    arrowcolor=FG, bordercolor=AYIRICI, lightcolor=PANEL, darkcolor=PANEL)
        s.map("TCombobox", fieldbackground=[("readonly", BG)], foreground=[("readonly", FG)],
              selectbackground=[("readonly", BG)], selectforeground=[("readonly", FG)])
        self.root.option_add("*TCombobox*Listbox.background", PANEL)
        self.root.option_add("*TCombobox*Listbox.foreground", FG)
        self.root.option_add("*TCombobox*Listbox.selectBackground", ACCENT)
        self.root.option_add("*TCombobox*Listbox.font", ("Segoe UI", 10))

    def _buton(self, ust, metin, komut, renk=PANEL):
        return tk.Button(ust, text=metin, command=komut, bg=renk, fg=FG,
                         activebackground=ACCENT, activeforeground="white",
                         relief="flat", bd=0, padx=16, pady=7, cursor="hand2",
                         font=("Segoe UI", 10, "bold"))

    def _bolme(self, ust, yon):
        """Sürüklenebilir ayırıcılı bölme paneli."""
        return tk.PanedWindow(ust, orient=yon, bg=AYIRICI, bd=0, sashwidth=7,
                              sashrelief="flat", opaqueresize=True, showhandle=False)

    def _metin_kutusu(self, ust):
        """Salt okunur metin kutusu + kaydırma çubuğu; (çerçeve, metin) döndürür."""
        cerceve = tk.Frame(ust, bg=PANEL)
        cerceve.rowconfigure(0, weight=1)
        cerceve.columnconfigure(0, weight=1)
        kutu = tk.Text(cerceve, bg=PANEL, fg=FG, relief="flat", wrap="word",
                       font=("Consolas", 10), padx=10, pady=8, height=14,
                       state="disabled", insertbackground=FG, width=10, bd=0,
                       highlightthickness=0)
        kutu.grid(row=0, column=0, sticky="nsew")
        kayd = ttk.Scrollbar(cerceve, orient="vertical", command=kutu.yview)
        kayd.grid(row=0, column=1, sticky="ns")
        kutu.configure(yscrollcommand=kayd.set)
        return cerceve, kutu

    def _arayuz(self):
        ust = tk.Frame(self.root, bg=BG)
        ust.pack(fill="x", padx=16, pady=(16, 8))
        tk.Label(ust, text=f"BIST 100 ANALİZ TERMİNALİ  v{SURUM}", bg=BG, fg=FG,
                 font=("Segoe UI", 15, "bold")).pack(anchor="w")
        tk.Label(ust, text="Hisse kodu veya adı yazın (örn. THYAO / Aselsan; endeks için XU100), "
                           "Enter'a basın. Veri: Yahoo Finance + İş Yatırım. Yorum: yerel YZ (Ollama)",
                 bg=BG, fg=MUTED, font=("Segoe UI", 9)).pack(anchor="w", pady=(0, 10))

        satir = tk.Frame(ust, bg=BG)
        satir.pack(fill="x")
        self.giris = tk.Entry(satir, bg=PANEL, fg=FG, insertbackground=FG, relief="flat",
                              font=("Consolas", 13), width=22)
        self.giris.pack(side="left", ipady=7, padx=(0, 8))
        self.giris.bind("<Return>", lambda e: self.analiz_yap())
        self.giris.bind("<KeyRelease>", lambda e: self._tabloyu_doldur())

        self.btn_analiz = self._buton(satir, "Analiz Yap", self.analiz_yap, ACCENT)
        self.btn_analiz.pack(side="left", padx=4)
        self.btn_endeks = self._buton(satir, "BIST 100", self.endeks_yap)
        self.btn_endeks.pack(side="left", padx=4)
        self.btn_kuresel = self._buton(satir, "Küresel Görünüm", self.kuresel_yap)
        self.btn_kuresel.pack(side="left", padx=4)
        self.btn_liste = self._buton(satir, "Listeyi Güncelle", self.liste_guncelle)
        self.btn_liste.pack(side="left", padx=4)
        self.btn_yz = self._buton(satir, "Yerel YZ", self.yz_kurulum)
        self.btn_yz.pack(side="left", padx=4)
        self.yz_kuruluyor = False
        self._buton(satir, "Kapat", self.kapat).pack(side="right")

        orta = tk.Frame(self.root, bg=BG)
        orta.pack(fill="both", expand=True, padx=16, pady=8)

        # Ana bölme: [ sol (grafik + rapor) | sağ (liste) ]  — sürüklenebilir
        self.ana_bolme = self._bolme(orta, "horizontal")
        self.ana_bolme.pack(fill="both", expand=True)

        # Sol bölme: [ grafik / rapor ]  — sürüklenebilir
        self.sol_bolme = self._bolme(self.ana_bolme, "vertical")
        self.ana_bolme.add(self.sol_bolme, minsize=380, stretch="always")

        # -- grafik
        grafik_cerceve = tk.Frame(self.sol_bolme, bg=BG)
        grafik_cerceve.columnconfigure(0, weight=1)
        grafik_cerceve.rowconfigure(1, weight=1)
        self.sol_bolme.add(grafik_cerceve, minsize=160, stretch="always")

        bar = tk.Frame(grafik_cerceve, bg=BG)
        bar.grid(row=0, column=0, sticky="ew", pady=(0, 4))
        tk.Label(bar, text="Fiyat Grafiği", bg=BG, fg=MUTED,
                 font=("Segoe UI", 9, "bold")).pack(side="left")
        self.donem = tk.IntVar(value=126)
        self.birim = tk.StringVar(value="TL")
        for etiket, gun in (("1A", 21), ("3A", 63), ("6A", 126), ("1Y", 252)):
            tk.Radiobutton(bar, text=etiket, variable=self.donem, value=gun,
                           indicatoron=False, command=self._grafik_yenile, bg=PANEL, fg=FG,
                           selectcolor=ACCENT, activebackground=ACCENT,
                           activeforeground="white", relief="flat", bd=0, padx=10, pady=2,
                           cursor="hand2", font=("Segoe UI", 9, "bold")
                           ).pack(side="right", padx=2)
        tk.Label(bar, text="  ", bg=BG).pack(side="right")
        for etiket in ("USD", "TL"):
            tk.Radiobutton(bar, text=etiket, variable=self.birim, value=etiket,
                           indicatoron=False, command=self._grafik_yenile, bg=PANEL, fg=FG,
                           selectcolor=ORANGE, activebackground=ORANGE,
                           activeforeground="white", relief="flat", bd=0, padx=10, pady=2,
                           cursor="hand2", font=("Segoe UI", 9, "bold")
                           ).pack(side="right", padx=2)

        self.sekil = Figure(figsize=(6, 3.4), dpi=self.dpi, facecolor=PANEL)
        self.tuval = FigureCanvasTkAgg(self.sekil, master=grafik_cerceve)
        self.tuval.get_tk_widget().configure(bg=PANEL, highlightthickness=0)
        self.tuval.get_tk_widget().grid(row=1, column=0, sticky="nsew")
        self._grafik_bos("Analiz yapınca grafik burada görünür.")

        # -- rapor: üstte başlık, altında [ rapor metni | temel veriler ]
        rapor_cerceve = tk.Frame(self.sol_bolme, bg=PANEL)
        rapor_cerceve.rowconfigure(2, weight=1)
        rapor_cerceve.columnconfigure(0, weight=1)
        self.sol_bolme.add(rapor_cerceve, minsize=140, stretch="always")

        self.baslik = tk.Label(rapor_cerceve, text="", bg=PANEL, fg=FG, anchor="w",
                               justify="left", font=("Consolas", 10, "bold"), padx=10)
        self.baslik.grid(row=0, column=0, sticky="ew", pady=(8, 2))
        rapor_cerceve.bind("<Configure>",
                           lambda e: self.baslik.configure(wraplength=max(200, e.width - 24)))
        tk.Frame(rapor_cerceve, bg=AYIRICI, height=1).grid(row=1, column=0, sticky="ew",
                                                          padx=10)

        self.rapor_bolme = self._bolme(rapor_cerceve, "horizontal")
        self.rapor_bolme.grid(row=2, column=0, sticky="nsew")
        sol_kutu, self.rapor = self._metin_kutusu(self.rapor_bolme)
        sag_kutu, self.temel = self._metin_kutusu(self.rapor_bolme)
        self.rapor_bolme.add(sol_kutu, minsize=200, stretch="always")
        self.rapor_bolme.add(sag_kutu, minsize=200, stretch="always")
        self.temel.configure(wrap="word")
        self.temel.tag_configure("adil", foreground=ACCENT, font=("Consolas", 10, "bold"))
        self.temel.tag_configure("up", foreground=GREEN)
        self.temel.tag_configure("down", foreground=RED)
        self.temel.tag_configure("soluk", foreground=MUTED)
        self.temel.tag_configure("uyari", foreground=ORANGE)
        self.temel.tag_configure("baslik", foreground=MUTED, font=("Consolas", 10, "bold"))

        # -- sağ: hisse listesi
        sag = tk.Frame(self.ana_bolme, bg=PANEL)
        sag.rowconfigure(3, weight=1)
        sag.columnconfigure(0, weight=1)
        self.ana_bolme.add(sag, minsize=380, stretch="always")

        # Liste seçici + Yeni / Düzenle / Sil
        lsatir = tk.Frame(sag, bg=PANEL)
        lsatir.grid(row=0, column=0, columnspan=2, sticky="ew", padx=6, pady=(6, 2))
        tk.Label(lsatir, text="Liste:", bg=PANEL, fg=MUTED,
                 font=("Segoe UI", 9, "bold")).pack(side="left")
        self.liste_sec = tk.StringVar()
        self.liste_kutu = ttk.Combobox(lsatir, textvariable=self.liste_sec, state="readonly",
                                       width=16, font=("Segoe UI", 10))
        self.liste_kutu.pack(side="left", padx=(4, 6), fill="x", expand=True)
        self.liste_kutu.bind("<<ComboboxSelected>>", lambda e: self._liste_degisti())
        for metin, komut in (("Sil", self.liste_sil), ("Düzenle", self.liste_duzenle),
                             ("Yeni", self.liste_yeni)):
            tk.Button(lsatir, text=metin, command=komut, bg=BG, fg=FG, relief="flat", bd=0,
                      activebackground=ACCENT, activeforeground="white", padx=8, pady=2,
                      cursor="hand2", font=("Segoe UI", 9, "bold")).pack(side="right", padx=1)

        # Görünüm filtreleri
        gsatir = tk.Frame(sag, bg=PANEL)
        gsatir.grid(row=1, column=0, columnspan=2, sticky="ew", padx=6, pady=(2, 2))
        self.gorunum = tk.StringVar(value="tum")
        for deger, etiket in GORUNUMLER:
            tk.Radiobutton(gsatir, text=etiket, variable=self.gorunum, value=deger,
                           indicatoron=False, command=self._gorunum_degisti, bg=BG, fg=FG,
                           selectcolor=GREEN if deger == "yukselen" else (
                               ORANGE if deger == "hareketli" else ACCENT),
                           activebackground=ACCENT, activeforeground="white", relief="flat",
                           bd=0, padx=8, pady=3, cursor="hand2", font=("Segoe UI", 9, "bold")
                           ).pack(side="left", padx=1)
        tk.Button(gsatir, text="↻", command=lambda: self._gorunum_degisti(zorla=True),
                  bg=BG, fg=FG, relief="flat", bd=0, activebackground=ACCENT, padx=7, pady=2,
                  cursor="hand2", font=("Segoe UI", 10, "bold")).pack(side="right")

        tk.Label(sag, text="Başlık: sırala · çift tık: analiz · sağ tık: listeye ekle/çıkar",
                 bg=PANEL, fg=MUTED, font=("Segoe UI", 8), anchor="w"
                 ).grid(row=2, column=0, columnspan=2, sticky="ew", padx=6, pady=(2, 2))

        self.kolonlar = (("kod", "Kod", 62, "w"), ("ad", "Şirket", 180, "w"),
                         ("fiyat", "Fiyat", 64, "e"), ("deg", "Değ. %", 56, "e"),
                         ("olc", "Ölçüt", 54, "e"), ("kay", "Kay", 30, "center"))
        self.tablo = ttk.Treeview(sag, columns=[k[0] for k in self.kolonlar],
                                  show="headings", selectmode="browse")
        for kolon, baslik, gen, hiza in self.kolonlar:
            self.tablo.heading(kolon, text=baslik, command=lambda k=kolon: self._sirala(k))
            self.tablo.column(kolon, width=gen, anchor=hiza, stretch=(kolon == "ad"))
        self.tablo.tag_configure("up", foreground=GREEN)
        self.tablo.tag_configure("down", foreground=RED)
        self.tablo.tag_configure("bos", foreground=MUTED)
        self.tablo.grid(row=3, column=0, sticky="nsew")
        kayd = ttk.Scrollbar(sag, orient="vertical", command=self.tablo.yview)
        kayd.grid(row=3, column=1, sticky="ns")
        self.tablo.configure(yscrollcommand=kayd.set)
        self.tablo.bind("<Double-1>", self._tablodan_sec)
        self.tablo.bind("<Button-3>", self._sag_tik)
        self.tablo.bind("<<TreeviewSelect>>", self._secim_adi)
        self.menu = tk.Menu(self.root, tearoff=0, bg=PANEL, fg=FG, activebackground=ACCENT,
                            activeforeground="white", bd=0)
        kayitli = self.ayar.get("secili_liste")
        self._liste_kutusunu_yenile(kayitli if kayitli in self.listeler else TUM_LISTE)

        self.durum = tk.Label(self.root, text="Hazır.", bg=BG, fg=MUTED, anchor="w",
                              font=("Segoe UI", 9))
        self.durum.pack(fill="x", padx=16, pady=(0, 10))

        metin = ("Bir hisse kodu veya adı girin ya da listeden çift tıklayın.\n"
                 '"BIST 100" endeksi hisse gibi inceler (piyasa genişliği dahil);\n'
                 '"Küresel Görünüm" dünya piyasalarını yorumlar.\n\n'
                 f"Liste kaynağı: {self.liste_kaynagi}.\n"
                 '"Listeyi Güncelle" BIST 100 üyeliğini ve fiyatları yeniler.\n\n'
                 'Sağ panel: "Liste" ile BIST 100 veya kendi listelerinizi (Hisselerim) seçin;\n'
                 'Yeni / Düzenle / Sil ile listeleri yönetin. "En Hareketli" ve\n'
                 '"Yükselme Eğilimi" seçili listeyi tarar (teknik tarama, kanıtsız).')
        if self.liste_eksik:
            metin += ('\n\nUYARI: yerleşik yedek liste eksiktir (100 hisseden azdır). '
                      f'Önce "Listeyi Güncelle"ye basın veya {MANUEL_DOSYA} dosyası oluşturun.')
            self.durum.configure(text="Uyarı: liste eksik olabilir, Listeyi Güncelle'ye basın.")
        self._rapor_yaz(metin)

    # ---- liste -------------------------------------------------------
    def _evren(self) -> list:
        ad = self.liste_sec.get() if hasattr(self, "liste_sec") else TUM_LISTE
        if ad in self.listeler:
            return list(self.listeler[ad])
        return list(self.kodlar)

    def _evren_adi(self) -> str:
        ad = self.liste_sec.get()
        return ad if ad in self.listeler else TUM_LISTE

    def _olcut_yazi(self, k) -> str:
        gor = self.gorunum.get()
        if gor == "hareketli" and k in self.tarama_sonuc:
            return f"{self.tarama_sonuc[k]:.0f}"
        o = self.tarama["olcut"].get(k)
        if gor == "yukselen" and o:
            return f"{o['trend']}/{o['trend_n']}"
        if o and o["hacim_x"] is not None:
            return f"{o['hacim_x']:.1f}x"
        return ""

    def _tabloyu_doldur(self):
        filtre = self.giris.get() if hasattr(self, "giris") else ""
        evren = self._evren() if hasattr(self, "gorunum") else list(self.kodlar)
        gor = self.gorunum.get() if hasattr(self, "gorunum") else "tum"
        if gor != "tum":
            evren = [k for k in evren if k in self.tarama_sonuc]
        kodlar = eslesenler(filtre, evren)

        def deger(k):
            if self.sirala_kolon == "kod":
                return k
            if self.sirala_kolon == "ad":
                return _sade(sirket_adi(k))
            if self.sirala_kolon == "olc":
                if gor != "tum":
                    return self.tarama_sonuc.get(k)
                o = self.tarama["olcut"].get(k)
                return o["hacim_x"] if o else None
            if self.sirala_kolon == "kay":
                return (self.fiyatlar.get(k) or ("", "", None))[2]
            f = self.fiyatlar.get(k)
            if f is None:
                return None
            return f[0] if self.sirala_kolon == "fiyat" else f[1]

        cift = [(deger(k), k) for k in kodlar]
        var = sorted((c for c in cift if c[0] is not None), key=lambda c: c[0],
                     reverse=self.sirala_ters)
        yok = [c for c in cift if c[0] is None]
        kodlar = [k for _, k in var + yok]

        self.tablo.delete(*self.tablo.get_children())
        for k in kodlar:
            f = self.fiyatlar.get(k)
            olc = self._olcut_yazi(k) if hasattr(self, "gorunum") else ""
            if f:
                fiyat, deg, kay = f
                degerler = (k, sirket_adi(k), f"{fiyat:,.2f}", f"{deg:+.2f}", olc, kay)
                etiket = ("up" if deg >= 0 else "down",)
            else:
                degerler = (k, sirket_adi(k), "-", "-", olc, "")
                etiket = ()
            self.tablo.insert("", "end", values=degerler, tags=etiket)
        if not kodlar and hasattr(self, "gorunum"):
            if not self._evren():
                bilgi = "Liste boş: Düzenle ile hisse ekleyin"
            elif gor != "tum" and self.tarama["zaman"] is None:
                bilgi = "Tarama bekleniyor..."
            elif filtre:
                bilgi = "Aramaya uyan hisse yok"
            else:
                bilgi = "Filtreye uyan hisse yok"
            self.tablo.insert("", "end", values=("", bilgi, "", "", "", ""), tags=("bos",))

        for kolon, baslik, _gen, _hiza in self.kolonlar:
            ok = (" ▼" if self.sirala_ters else " ▲") if kolon == self.sirala_kolon else ""
            self.tablo.heading(kolon, text=baslik + ok)

    def _sirala(self, kolon):
        if kolon == self.sirala_kolon:
            self.sirala_ters = not self.sirala_ters
        else:
            self.sirala_kolon, self.sirala_ters = kolon, False
        self._tabloyu_doldur()

    def _secili_kod(self):
        secili = self.tablo.selection()
        if not secili:
            return None
        kod = str(self.tablo.item(secili[0])["values"][0]).strip().upper()
        return kod if KOD_RE.match(kod) else None

    def _secim_adi(self, _event=None):
        kod = self._secili_kod()
        if kod and not self.mesgul:
            self.durum.configure(text=f"{kod}  —  {sirket_adi(kod, 'ad bilinmiyor')}")

    def _tablodan_sec(self, _event):
        kod = self._secili_kod()
        if not kod:
            return
        if self.mesgul:
            self.durum.configure(text="İşlem sürüyor, lütfen bekleyin...")
            return
        self._analiz_baslat(kod)

    # ---- Hisselerim listeleri ---------------------------------------
    def _liste_kutusunu_yenile(self, secilecek=None):
        self.liste_kutu.configure(values=[TUM_LISTE] + list(self.listeler))
        if secilecek is not None:
            self.liste_sec.set(secilecek)
        if self.liste_sec.get() not in self.listeler:
            self.liste_sec.set(TUM_LISTE)

    def _listeleri_kaydet(self) -> bool:
        if hisselerim_yaz(self.listeler):
            return True
        messagebox.showerror("Hisse Rapor", f"{HISSELERIM_DOSYASI} kaydedilemedi.\n"
                             f"Ayrıntı: {LOG_DOSYASI}", parent=self.root)
        return False

    def _liste_degisti(self):
        self.ayar["secili_liste"] = self.liste_sec.get()
        if self.gorunum.get() != "tum":
            self._gorunum_degisti()
        else:
            self._tabloyu_doldur()
            n = len(self._evren())
            self.durum.configure(text=f"Liste: {self._evren_adi()} ({n} hisse)")

    def liste_yeni(self, ilk_kodlar=()):
        if len(self.listeler) >= MAKS_LISTE:
            messagebox.showwarning("Hisse Rapor", f"En çok {MAKS_LISTE} liste oluşturulabilir.",
                                   parent=self.root)
            return None
        oneri = VARSAYILAN_LISTE
        i = 2
        while oneri in self.listeler:
            oneri, i = f"{VARSAYILAN_LISTE} {i}", i + 1
        d = ListeDuzenleyici(self.root, "Yeni liste", oneri, list(ilk_kodlar),
                             self.kodlar, self.listeler)
        if not d.sonuc:
            return None
        ad, kodlar = d.sonuc
        self.listeler[ad] = kodlar
        self._listeleri_kaydet()
        self._liste_kutusunu_yenile(ad)
        self._liste_degisti()
        self.durum.configure(text=f"'{ad}' listesi oluşturuldu ({len(kodlar)} hisse).")
        return ad

    def liste_duzenle(self):
        ad = self.liste_sec.get()
        if ad not in self.listeler:
            if messagebox.askyesno("Hisse Rapor", "BIST 100 listesi otomatik güncellenir, "
                                   "düzenlenemez.\nYeni bir liste oluşturmak ister misiniz?",
                                   parent=self.root):
                self.liste_yeni()
            return
        diger = [a for a in self.listeler if a != ad]
        d = ListeDuzenleyici(self.root, f"'{ad}' listesini düzenle", ad, self.listeler[ad],
                             self.kodlar, diger)
        if not d.sonuc:
            return
        yeni_ad, kodlar = d.sonuc
        # sırayı koruyarak yeniden adlandır
        self.listeler = {(yeni_ad if a == ad else a): (kodlar if a == ad else v)
                         for a, v in self.listeler.items()}
        self._listeleri_kaydet()
        self._liste_kutusunu_yenile(yeni_ad)
        self._liste_degisti()
        self.durum.configure(text=f"'{yeni_ad}' listesi kaydedildi ({len(kodlar)} hisse).")

    def liste_sil(self):
        ad = self.liste_sec.get()
        if ad not in self.listeler:
            messagebox.showinfo("Hisse Rapor", "BIST 100 listesi silinemez. Silmek istediğiniz "
                                "listeyi önce 'Liste' kutusundan seçin.", parent=self.root)
            return
        if not messagebox.askyesno("Listeyi sil", f"'{ad}' listesi ({len(self.listeler[ad])} "
                                   "hisse) kalıcı olarak silinsin mi?", icon="warning",
                                   parent=self.root):
            return
        del self.listeler[ad]
        self._listeleri_kaydet()
        self._liste_kutusunu_yenile(TUM_LISTE)
        self._liste_degisti()
        self.durum.configure(text=f"'{ad}' listesi silindi.")

    def _listeye_ekle(self, ad, kod):
        if ad is None:
            self.liste_yeni([kod])
            return
        kodlar = self.listeler[ad]
        if kod in kodlar:
            self.durum.configure(text=f"{kod} zaten '{ad}' listesinde.")
            return
        if len(kodlar) >= MAKS_LISTE_HISSE:
            self.durum.configure(text=f"'{ad}' dolu (en çok {MAKS_LISTE_HISSE} hisse).")
            return
        kodlar.append(kod)
        self._listeleri_kaydet()
        self._tabloyu_doldur()
        self.durum.configure(text=f"{kod} '{ad}' listesine eklendi.")

    def _listeden_cikar(self, ad, kod):
        if kod in self.listeler.get(ad, []):
            self.listeler[ad].remove(kod)
            self._listeleri_kaydet()
            self.tarama_sonuc.pop(kod, None)
            self._tabloyu_doldur()
            self.durum.configure(text=f"{kod} '{ad}' listesinden çıkarıldı.")

    def _sag_tik(self, event):
        satir = self.tablo.identify_row(event.y)
        if not satir:
            return
        self.tablo.selection_set(satir)
        kod = self._secili_kod()
        if not kod:
            return
        m = self.menu
        m.delete(0, "end")
        m.add_command(label=f"{kod} analiz et", command=lambda: self._tablodan_sec(None))
        m.add_separator()
        for ad, kodlar in self.listeler.items():
            if kod in kodlar:
                m.add_command(label=f"✓ '{ad}' listesinde", state="disabled")
            else:
                m.add_command(label=f"'{ad}' listesine ekle",
                              command=lambda a=ad: self._listeye_ekle(a, kod))
        m.add_command(label="Yeni listeye ekle...", command=lambda: self._listeye_ekle(None, kod))
        ad = self.liste_sec.get()
        if ad in self.listeler and kod in self.listeler[ad]:
            m.add_separator()
            m.add_command(label=f"'{ad}' listesinden çıkar",
                          command=lambda: self._listeden_cikar(ad, kod))
        try:
            m.tk_popup(event.x_root, event.y_root)
        finally:
            m.grab_release()

    # ---- filtreler (En Hareketli / Yükselme Eğilimi) ----------------
    def _tarama_taze(self, kodlar) -> bool:
        z = self.tarama["zaman"]
        if z is None or datetime.now() - z > TARAMA_OMUR:
            return False
        bilinen = set(self.tarama["olcut"]) | set(self.tarama["eksik"])
        return all(k in bilinen for k in kodlar)

    def _gorunum_degisti(self, zorla=False):
        gor = self.gorunum.get()
        self.sirala_kolon, self.sirala_ters = ("olc", True) if gor != "tum" else ("kod", False)
        if gor == "tum":
            self.tarama_sonuc = {}
            self._tabloyu_doldur()
            self.durum.configure(text=f"Liste: {self._evren_adi()} ({len(self._evren())} hisse)")
            return
        kodlar = self._evren()
        if not kodlar:
            self.tarama_sonuc = {}
            self._tabloyu_doldur()
            return
        if not zorla and self._tarama_taze(kodlar):
            self._filtre_uygula()
            return
        if self.mesgul:
            self.gorunum.set("tum")
            self.durum.configure(text="İşlem sürüyor; bitince filtreyi yeniden seçin.")
            return
        self.tarama_sonuc = {}
        self._tabloyu_doldur()
        self._mesgul_ayarla(True, f"{self._evren_adi()} taranıyor ({len(kodlar)} hisse, 2 yıllık veri)...")
        self._rapor_yaz("Tarama yapılıyor: seçili listedeki hisselerin 2 yıllık verisi çekiliyor,\n"
                        "ölçütler hesaplanıyor. 100 hisse için yaklaşık 10-30 saniye sürer.")
        threading.Thread(target=self._tarama_is, args=(kodlar,), daemon=True).start()

    def _tarama_is(self, kodlar):
        try:
            sonuc = tarama_getir(kodlar)
            try:
                adlari_tamamla(kodlar)
            except Exception:
                log.warning("Şirket adları tamamlanamadı.", exc_info=True)
            self.kuyruk.put(("tarama", sonuc))
        except Exception as e:
            log.exception("Tarama başarısız")
            self.kuyruk.put(("hata", f"Tarama başarısız: {e}\n\nAyrıntı: {LOG_DOSYASI}"))

    def _filtre_uygula(self):
        gor = self.gorunum.get()
        if gor == "tum":
            return
        kodlar = self._evren()
        olcut = self.tarama["olcut"]
        secilen = (hareketli_sec(olcut, kodlar) if gor == "hareketli"
                   else yukselen_sec(olcut, kodlar))
        self.tarama_sonuc = dict(secilen)
        self._tabloyu_doldur()
        ad = self._evren_adi()
        eksik = [k for k in self.tarama["eksik"] if k in kodlar]
        etiket = dict(GORUNUMLER)[gor]
        self.yz_sira += 1
        self.son_analiz = None
        self._grafik_bos(f"{etiket}: {len(secilen)} hisse. Grafik için satıra çift tıklayın.")
        self._rapor_yaz(tarama_raporu(gor, secilen, olcut, ad, len(kodlar), eksik,
                                      self.tarama["zaman"], kodlar),
                        f"{etiket.upper()}  |  {ad}  |  {self.tarama['zaman']:%d.%m.%Y %H:%M}"
                        f"  |  v{SURUM}")
        self._temel_yaz([("--- Tarama özeti " + "-" * 27, "baslik"),
                         (f"{'Filtre':<12}: {etiket}", None),
                         (f"{'Liste':<12}: {ad} ({len(kodlar)} hisse)", None),
                         (f"{'Uyan':<12}: {len(secilen)} hisse", "up" if secilen else "soluk"),
                         ("Kanıt durumu: kanıtsız teknik tarama.", "uyari"),
                         (yz_bekleme_metni(), "soluk")])
        self._yz_baslat(tarama_yz_ozeti(gor, secilen, olcut, ad),
                        f"{ad} listesinde {etiket.lower()} filtresi sonuçları")
        self.durum.configure(text=f"{etiket}: {ad} içinde {len(secilen)} hisse "
                                  f"(tarama {self.tarama['zaman']:%H:%M}).")

    # ---- grafik ------------------------------------------------------
    def _grafik_bos(self, mesaj):
        self.sekil.clear()
        ax = self.sekil.add_subplot(111, facecolor=PANEL)
        ax.set_axis_off()
        ax.text(0.5, 0.5, mesaj, ha="center", va="center", color=MUTED, fontsize=11,
                transform=ax.transAxes)
        self.tuval.draw_idle()

    def _grafik_yenile(self):
        if self.son_analiz:
            self._grafik_ciz(self.son_analiz)

    def _grafik_ciz(self, analiz):
        try:
            self._grafik_ciz_ic(analiz)
        except Exception as e:
            log.exception("Grafik çizilemedi")
            self._grafik_bos(f"Grafik çizilemedi: {e}")

    def _eksen_bicimle(self, eksenler, alt):
        for ax in eksenler:
            ax.tick_params(colors=MUTED, labelsize=8)
            for taraf in ("top", "right"):
                ax.spines[taraf].set_visible(False)
            for taraf in ("left", "bottom"):
                ax.spines[taraf].set_color(AYIRICI)
            ax.grid(True, color=AYIRICI, lw=0.5, alpha=0.7)
        if alt is not None:
            konum = mdates.AutoDateLocator()
            alt.xaxis.set_major_locator(konum)
            alt.xaxis.set_major_formatter(mdates.ConciseDateFormatter(konum))
            alt.xaxis.get_offset_text().set_color(MUTED)
            alt.xaxis.get_offset_text().set_fontsize(8)

    def _grafik_ciz_ic(self, analiz):
        if analiz.get("tur") == "kuresel":
            return self._kuresel_ciz(analiz["kuresel"])
        veri = analiz["veri"]
        kapanis = veri["Close"]
        usd = self.birim.get() == "USD" and analiz.get("usdtry") is not None
        if usd:
            kapanis = (kapanis / _hizala(analiz["usdtry"], kapanis.index)).dropna()
        sma20 = kapanis.rolling(20).mean()
        std20 = kapanis.rolling(20).std()
        bb_ust, bb_alt = sma20 + 2 * std20, sma20 - 2 * std20
        sma50 = kapanis.rolling(50).mean()
        sma200 = kapanis.rolling(200).mean()
        n = self.donem.get()

        k = kapanis.tail(n)
        x = k.index
        onceki, son = float(kapanis.iloc[-2]), float(kapanis.iloc[-1])
        degisim = (son / onceki - 1) * 100

        self.sekil.clear()
        gs = self.sekil.add_gridspec(4, 1, hspace=0.08, left=0.08, right=0.98, top=0.92,
                                     bottom=0.21)
        ax1 = self.sekil.add_subplot(gs[:3, 0], facecolor=PANEL)
        ax2 = self.sekil.add_subplot(gs[3, 0], sharex=ax1, facecolor=PANEL)

        ax1.plot(x, k, color=ACCENT, lw=1.8, label="Kapanış" + (" (USD)" if usd else ""), zorder=4)
        ax1.plot(x, sma20.tail(n), color=ORANGE, lw=1.1, label="SMA20", zorder=3)
        if sma50.notna().any():
            ax1.plot(x, sma50.tail(n), color="#bc8cff", lw=1.1, label="SMA50", zorder=3)
        if sma200.notna().any():
            ax1.plot(x, sma200.tail(n), color="#39c5cf", lw=1.6, label="SMA200", zorder=3)
        ax1.fill_between(x, bb_alt.tail(n), bb_ust.tail(n), color=ACCENT, alpha=0.10, lw=0,
                         label="Bollinger bandı", zorder=1)
        zirve = float(analiz["veri"]["Close"].tail(252).max())
        if not usd:
            ax1.axhline(0.95 * zirve, color=GREEN, lw=0.8, ls=":", alpha=0.8,
                        label="52H zirvenin %95'i", zorder=2)
        renk = GREEN if degisim >= 0 else RED
        ax1.scatter([x[-1]], [son], color=renk, s=22, zorder=5)
        birim = "USD" if usd else ("puan" if analiz.get("endeks") else "TL")
        bicim = ",.3f" if usd and son < 10 else ",.2f"
        ax1.set_title(f"{analiz['kod']}   {son:{bicim}} {birim}   ({degisim:+.2f}%)", loc="left",
                      color=renk, fontsize=11, fontweight="bold")
        kanit = analiz["kanit"]
        ax1.set_title("İşaret: " + ("ZAYIF (kanıtlı)" if kanit["etiket"] == "ZAYIF" else "NÖTR"),
                      loc="right", color=ISARET_RENK[kanit["etiket"]], fontsize=10,
                      fontweight="bold")

        if analiz.get("endeks") and analiz.get("genislik"):
            gen = analiz["genislik"]
            ax2.plot(gen["seri50"].tail(n).index, gen["seri50"].tail(n), color=ORANGE, lw=1.2,
                     label="% üye SMA50 üstü")
            ax2.plot(gen["seri200"].tail(n).index, gen["seri200"].tail(n), color="#39c5cf",
                     lw=1.2, label="% üye SMA200 üstü")
            ax2.axhline(50, color=MUTED, lw=0.8, ls="--", alpha=0.6)
            ax2.set_ylim(0, 100)
            ax2.set_yticks([25, 50, 75])
            ax2.set_ylabel("Genişlik %", color=MUTED, fontsize=8)
        elif analiz.get("xu100") is not None:
            xu = _hizala(analiz["xu100"], analiz["veri"].index)
            oran = (analiz["veri"]["Close"] / xu).dropna().tail(n)
            if len(oran):
                oran = oran / float(oran.iloc[0]) * 100
                ax2.plot(oran.index, oran, color="#d2a8ff", lw=1.3, label="XU100'e göre göreli güç")
                ax2.axhline(100, color=MUTED, lw=0.8, ls="--", alpha=0.6)
                ax2.fill_between(oran.index, 100, oran, where=oran >= 100, color=GREEN, alpha=0.15, lw=0)
                ax2.fill_between(oran.index, 100, oran, where=oran < 100, color=RED, alpha=0.15, lw=0)
                ax2.set_ylabel("Göreli (100)", color=MUTED, fontsize=8)
        else:
            rsi = rsi_serisi(kapanis)
            ax2.plot(x, rsi.tail(n), color="#d2a8ff", lw=1.2, label="RSI(14)")
            ax2.set_ylim(0, 100)
            ax2.set_yticks([30, 50, 70])
            ax2.set_ylabel("RSI", color=MUTED, fontsize=8)

        self._eksen_bicimle((ax1, ax2), ax2)
        ax1.tick_params(labelbottom=False)
        isaretler, etiketler = ax1.get_legend_handles_labels()
        i2, e2 = ax2.get_legend_handles_labels()
        self.sekil.legend(isaretler + i2, etiketler + e2, loc="lower center", ncol=4, fontsize=7,
                          frameon=False, labelcolor=MUTED, handlelength=1.8,
                          columnspacing=1.2, bbox_to_anchor=(0.5, 0.0))
        self.tuval.draw_idle()

    def _kuresel_ciz(self, kuresel):
        """Sol: 1 aylık değişim çubukları; sağ: 1 yıllık ortalamadan sapma (z)."""
        satirlar = list(reversed(kuresel["satirlar"]))
        adlar = [s["ad"] + (" (puan)" if s["birim"] == "puan" else "") for s in satirlar]
        a1 = [(s["a1"] if s["birim"] == "puan" else (s["a1"] or 0) * 100) if s["a1"] is not None else 0
              for s in satirlar]
        z = [s["z"] or 0 for s in satirlar]
        # risk yönü: yükselişi riskten kaçış sayılan göstergeler
        # Brent: Türkiye net enerji ithalatçısı, yükselişi cari denge ve enflasyon için olumsuz
        kacis_yonlu = {"VIX", "DXY", "ABD10Y", "ALTIN", "USDTRY", "BRENT"}
        renk = []
        for s, d in zip(satirlar, a1):
            olumsuz = (d > 0) == (s["anahtar"] in kacis_yonlu)
            renk.append(RED if olumsuz and d != 0 else (GREEN if d != 0 else MUTED))

        self.sekil.clear()
        gs = self.sekil.add_gridspec(1, 2, wspace=0.08, left=0.17, right=0.98, top=0.86,
                                     bottom=0.12, width_ratios=[3, 2])
        ax1 = self.sekil.add_subplot(gs[0, 0], facecolor=PANEL)
        ax2 = self.sekil.add_subplot(gs[0, 1], sharey=ax1, facecolor=PANEL)
        y = range(len(adlar))
        ax1.barh(y, a1, color=renk, alpha=0.85, height=0.62)
        for yi, d, s in zip(y, a1, satirlar):
            metin = f"{d:+.2f}" if s["birim"] == "puan" else f"{d:+.1f}%"
            ax1.text(d, yi, " " + metin + " ", va="center", ha="left" if d >= 0 else "right",
                     color=FG, fontsize=7)
        ax1.axvline(0, color=MUTED, lw=0.8)
        ax1.set_yticks(list(y))
        ax1.set_yticklabels(adlar, fontsize=8, color=FG)
        ax1.set_xlabel("1 aylık değişim", color=MUTED, fontsize=8)
        sinir = max(1.0, max(abs(v) for v in a1) * 1.35)
        ax1.set_xlim(-sinir, sinir)
        ax2.barh(y, z, color=[ACCENT if v >= 0 else ORANGE for v in z], alpha=0.8, height=0.62)
        ax2.axvline(0, color=MUTED, lw=0.8)
        for v in (-2, 2):
            ax2.axvline(v, color=MUTED, lw=0.6, ls=":")
        ax2.set_xlim(-3.2, 3.2)
        ax2.set_xlabel("1Y ortalamadan sapma (z)", color=MUTED, fontsize=8)
        ax2.tick_params(labelleft=False)
        self._eksen_bicimle((ax1, ax2), None)
        r = kuresel["rejim"]
        rr = {"up": GREEN, "down": RED}.get(r["renk"], ORANGE)
        self.sekil.suptitle(f"Küresel Görünüm  |  Rejim: {r['etiket']}  |  "
                            f"{kuresel['zaman']:%d.%m.%Y %H:%M}", color=rr, fontsize=11,
                            fontweight="bold", x=0.02, ha="left")
        self.sekil.text(0.98, 0.91, "kırmızı: Türkiye/risk açısından olumsuz yön, yeşil: olumlu",
                        color=MUTED, fontsize=7, ha="right")
        self.tuval.draw_idle()

    # ---- rapor / temel veriler --------------------------------------
    def _rapor_yaz(self, metin, baslik=""):
        self.baslik.configure(text=baslik)
        self.rapor.configure(state="normal")
        self.rapor.delete("1.0", "end")
        self.rapor.insert("1.0", metin)
        self.rapor.configure(state="disabled")
        if not baslik:
            self._temel_yaz([])

    def _temel_yaz(self, satirlar):
        """satirlar: [(metin, etiket), ...]; boş liste paneli temizler."""
        self._temel_satirlar_son = list(satirlar)
        self.temel.configure(state="normal")
        self.temel.delete("1.0", "end")
        for i, (metin, etiket) in enumerate(satirlar):
            self.temel.insert("end", metin + ("\n" if i < len(satirlar) - 1 else ""),
                              (etiket,) if etiket else ())
        self.temel.configure(state="disabled")

    def _mesgul_ayarla(self, mesgul, mesaj):
        self.mesgul = mesgul
        durum = "disabled" if mesgul else "normal"
        for b in (self.btn_analiz, self.btn_liste, self.btn_endeks, self.btn_kuresel):
            b.configure(state=durum)
        self.durum.configure(text=mesaj)

    def _arayuz_hatasi(self, exc, val, tb):
        log.error("Arayüz hatası", exc_info=(exc, val, tb))
        try:
            self._mesgul_ayarla(False, f"Beklenmedik hata. Ayrıntı: {LOG_DOSYASI}")
        except Exception:
            pass

    def kapat(self):
        if self._after_id is not None:
            try:
                self.root.after_cancel(self._after_id)
            except Exception:
                pass
        self._ayar_yaz()
        self.root.destroy()

    # ---- işlemler ----------------------------------------------------
    def analiz_yap(self):
        metin = self.giris.get().strip()
        if not metin:
            return
        if self.mesgul:
            self.durum.configure(text="İşlem sürüyor, lütfen bekleyin...")
            return
        try:
            kod = kod_coz(metin, self.kodlar)
        except ValueError as e:
            self._rapor_yaz(str(e))
            self.durum.configure(text="Hisse seçilemedi.")
            return
        self._analiz_baslat(kod)

    def endeks_yap(self):
        if self.mesgul:
            self.durum.configure(text="İşlem sürüyor, lütfen bekleyin...")
            return
        self._analiz_baslat(ENDEKS_KODU)

    def _analiz_baslat(self, kod):
        self.yz_sira += 1
        ek = "endeks + üye genişliği" if endeks_mi(kod) else "2 kaynak"
        self._mesgul_ayarla(True, f"{kod} analiz ediliyor ({ek})...")
        self._rapor_yaz("Veri çekiliyor, lütfen bekleyin...")
        self.son_analiz = None
        self._grafik_bos("Veri çekiliyor...")
        self.giris.delete(0, "end")
        self._tabloyu_doldur()
        threading.Thread(target=self._analiz_is, args=(kod,), daemon=True).start()

    def _kuresel_guvenli(self, zorla=False):
        try:
            return kuresel_getir(zorla)
        except Exception as e:
            log.warning("Küresel veri alınamadı: %s", e)
            return None

    def _analiz_is(self, kod):
        varsayim = varsayim_oku(self.ayar)
        endeks = endeks_mi(kod)
        havuz = ThreadPoolExecutor(max_workers=3)
        kuresel_g = havuz.submit(self._kuresel_guvenli)
        if endeks:
            ek_g = havuz.submit(endeks_genisligi, list(self.kodlar))
        else:
            ek_g = havuz.submit(temel_bilgi_cek, kod)   # temel veriler paralel (yavaş olabilir)
        try:
            kuresel = kuresel_g.result(timeout=45)
            analiz = analiz_uret(kod, varsayim["tufe_yillik"], kuresel)
            analiz["tufe_donem"] = self._tufe_donem()
            analiz["kuresel_veri"] = kuresel
            self.kuyruk.put(("rapor", analiz))
        except Exception as e:
            log.exception("Analiz başarısız: %s", kod)
            self.kuyruk.put(("hata", f"Analiz başarısız: {e}\n\nAyrıntı: {LOG_DOSYASI}"))
            havuz.shutdown(wait=False)
            return
        if endeks:
            try:
                gen = ek_g.result(timeout=90)
            except Exception as e:
                log.warning("Endeks genişliği alınamadı: %s", e)
                gen = None
            self.kuyruk.put(("endeks", {"kod": analiz["kod"], "genislik": gen, "kuresel": kuresel}))
            havuz.shutdown(wait=False)
            if kuresel:
                ozet = kuresel_ozet_metni(kuresel)
                if gen:
                    ozet += (f"\nBIST 100 genişliği: üyelerin %{gen['ust50'] or 0:.0f}'i SMA50, "
                             f"%{gen['ust200'] or 0:.0f}'i SMA200 üstünde; son gün {gen['yukselen']} "
                             f"yükselen / {gen['dusen']} düşen.")
                g = analiz["getiri"].get("1A")
                if g:
                    ozet += f"\nBIST 100 1A getiri: TL %{g['tl'] * 100:+.1f}" + (
                        f", USD %{g['usd'] * 100:+.1f}" if g["usd"] is not None else "")
                self._yz_baslat(ozet, "BIST 100 endeksi ve küresel ortam")
            return
        try:
            bilgi = ek_g.result(timeout=40)
            temel = temel_hesapla(bilgi, analiz["son"], analiz["tarih"], analiz["kod"], varsayim)
            temel["tufe_donem"] = self._tufe_donem()
        except Exception as e:
            log.warning("Temel veriler alınamadı (%s): %s", kod, e)
            temel = None
        self.kuyruk.put(("temel", {"kod": analiz["kod"], "temel": temel}))
        havuz.shutdown(wait=False)

    def kuresel_yap(self):
        if self.mesgul:
            self.durum.configure(text="İşlem sürüyor, lütfen bekleyin...")
            return
        self.yz_sira += 1
        self._mesgul_ayarla(True, "Küresel göstergeler çekiliyor...")
        self._rapor_yaz("Küresel veriler çekiliyor, lütfen bekleyin...")
        self.son_analiz = None
        self._grafik_bos("Veri çekiliyor...")
        threading.Thread(target=self._kuresel_is, daemon=True).start()

    def _kuresel_is(self):
        try:
            kuresel = kuresel_getir(zorla=True)
        except Exception as e:
            log.exception("Küresel görünüm alınamadı")
            self.kuyruk.put(("hata", f"Küresel görünüm alınamadı: {e}\n\nAyrıntı: {LOG_DOSYASI}"))
            return
        self.kuyruk.put(("kuresel", kuresel))
        self._yz_baslat(kuresel_ozet_metni(kuresel), "dünya ekonomisindeki son değişimler")

    def _yz_baslat(self, ozet, odak):
        sira = self.yz_sira
        def is_():
            try:
                sonuc = yerel_yz_yorum(ozet, self.ayar, odak)
            except YZYok as e:
                sonuc = {"yok": str(e)}
            except Exception as e:
                log.warning("Yerel YZ yanıt vermedi: %s", e)
                sonuc = {"hata": str(e) or e.__class__.__name__}
            self.kuyruk.put(("yz", {"sira": sira, **sonuc}))
        threading.Thread(target=is_, daemon=True).start()

    def _kuresel_rapor(self, kuresel) -> str:
        satir = [f"Ölçüm: {kuresel['zaman']:%d.%m.%Y %H:%M}  (veri: Yahoo Finance, gecikmeli olabilir)",
                 "-" * 52,
                 f"{'Gösterge':<16}{'Son':>11}{'5 gün':>9}{'1 ay':>9}{'z(1Y)':>7}"]
        for s in kuresel["satirlar"]:
            if s["birim"] == "puan":
                d5 = f"{s['g5']:+.2f}p" if s["g5"] is not None else "-"
                d1 = f"{s['a1']:+.2f}p" if s["a1"] is not None else "-"
                son = f"%{s['son']:.2f}"
            else:
                d5 = _yuzde(s["g5"]) if s["g5"] is not None else "-"
                d1 = _yuzde(s["a1"]) if s["a1"] is not None else "-"
                son = f"{s['son']:,.2f}"
            z = f"{s['z']:+.1f}" if s["z"] is not None else "-"
            satir.append(f"{s['ad']:<16}{son:>11}{d5:>9}{d1:>9}{z:>7}")
        r = kuresel["rejim"]
        satir += ["-" * 52, f"Kural tabanlı rejim: {r['etiket']}"]
        satir += [f"  - {m}" for m in r["kacis"]] + [f"  + {m}" for m in r["istah"]]
        satir += ["", "Kural: en az iki bağımsız gösterge aynı yönü göstermeden rejim değişmez.",
                  "Eşikler (VIX 20, DXY ±%2, 10Y ±25 bp, %5 emtia) rehber niteliğindedir.",
                  "", "Yerel YZ yorumu sağ panelde. Yatırım tavsiyesi değildir."]
        return "\n".join(satir)

    def _yz_yaz(self, veri):
        satirlar = list(self._temel_satirlar_son or [])
        satirlar.append(("--- Yerel YZ yorumu " + "-" * 25, "baslik"))
        if "yok" in veri:
            satirlar += [(f"Kullanılamıyor: {veri['yok']}.", "soluk"),
                         ("Program yorumsuz çalışır; yukarıdaki kural tabanlı özet geçerlidir.", "soluk"),
                         ("Kurmak için üstteki 'Yerel YZ' düğmesine basın (onayınız sorulur).", "soluk")]
        elif "hata" in veri:
            satirlar += [("Yerel YZ'ye ulaşılamadı: " + veri["hata"][:120], "soluk"),
                         ("Ollama kurulu olmalı (program gerekirse kendisi başlatır, 127.0.0.1:11434).", "soluk"),
                         ("Yukarıdaki kural tabanlı özet geçerlidir.", "soluk")]
        else:
            satirlar.append((veri["metin"], None))
            satirlar.append((f"Taslak: {veri['model']} (Ollama, {veri['sure']:.0f} sn). "
                             "Sayıları tablodan doğrulayın.", "soluk"))
            if veri.get("yabanci"):
                satirlar.append(("! Metinde tabloda olmayan sayı var: "
                                 + ", ".join(veri["yabanci"][:6]) + " (uydurma olabilir)", "uyari"))
        self._temel_yaz(satirlar)

    # ---- yerel YZ kurulumu (onaylı) -----------------------------------
    def _ilk_yz_sorusu(self):
        if self.ayar.get("yz_kurulum_soruldu") or _ollama_yolu():
            return
        self.ayar["yz_kurulum_soruldu"] = True
        self._ayar_yaz()
        self.yz_kurulum(ilk=True)

    def yz_kurulum(self, ilk=False):
        if self.yz_kuruluyor:
            messagebox.showinfo("Yerel YZ", "Kurulum sürüyor; ilerleme alttaki durum satırında.",
                                parent=self.root)
            return
        try:
            d = yz_durumu(self.ayar)
        except Exception as e:
            messagebox.showerror("Yerel YZ", f"Durum okunamadı: {e}", parent=self.root)
            return
        if d["ayakta"] and d["modeller"]:
            dnm = _donanim_onbellek()
            gpu = f", ekran kartı {dnm['vram']:.0f} GB" if dnm["vram"] else ""
            messagebox.showinfo("Yerel YZ", "Yerel YZ hazır.\n\nOllama çalışıyor. Kurulu modeller: "
                                + ", ".join(d["modeller"][:6])
                                + f"\nKullanılan: {self.ayar.get('yerel_model') or 'donanıma sığan en büyük model'}"
                                + f"\nDonanım: RAM {dnm['ram']:.0f} GB{gpu}", parent=self.root)
            return
        dnm = _donanim_onbellek()
        adaylar = model_adaylari(dnm)
        plan = {"ollama_kur": not d["kurulu"], "adaylar": adaylar, "mevcut_model": None}
        if d["kurulu"] and not d["ayakta"]:
            # kurulu ama kapalı: önce başlatıp modellere bak (indirme gerekmeyebilir)
            try:
                s = requests.Session()
                s.trust_env = False
                ollama_hazirla(s, _yerel_adres(self.ayar))
                d = yz_durumu(self.ayar)
            except Exception as e:
                log.warning("Ollama başlatılamadı: %s", e)
            if d["modeller"]:
                plan["mevcut_model"] = d["modeller"][0]
                messagebox.showinfo("Yerel YZ", "Ollama başlatıldı; yerel YZ hazır.\nModel: "
                                    + d["modeller"][0], parent=self.root)
                _YZ_YOK.update(neden=None, zaman=None)
                return
        ilk_model, ilk_gb, _ = adaylar[0]
        toplam = ilk_gb + (OLLAMA_KURUCU_BOYUT_GB if plan["ollama_kur"] else 0)
        bos = None
        try:
            import shutil
            bos = shutil.disk_usage(os.path.expanduser("~")).free / 2 ** 30
        except OSError:
            pass
        adimlar = []
        if plan["ollama_kur"]:
            adimlar.append("1) Ollama kurulacak (winget ile; yoksa ollama.com resmi kurucusu). "
                           "Kullanıcı klasörüne kurulur, yönetici izni gerekmez.")
        gpu = f", ekran kartı {dnm['vram']:.0f} GB ({dnm['gpu'][:40]})" if dnm["vram"] else ""
        adimlar.append(f"{len(adimlar) + 1}) Donanım okundu: RAM {dnm['ram']:.0f} GB{gpu}.\n"
                       f"    Seçilen model: {ilk_model} (yaklaşık {ilk_gb:.1f} GB) - {dnm['neden']}.")
        adimlar.append(f"{len(adimlar) + 1}) Program bu modeli yorum için kullanacak şekilde ayarlanacak.")
        metin = (("Bu bilgisayarda yerel yapay zekâ kurulu değil.\n\n" if ilk else
                  "Yerel YZ kurulumu\n\n")
                 + "\n".join(adimlar)
                 + f"\n\nToplam indirme: yaklaşık {toplam:.1f} GB. İnternet bağlantısı gerekir; "
                   "süre bağlantı hızına bağlıdır (10-40 dk). Program bu sırada kullanılabilir."
                 + (f"\nBoş disk alanı: {bos:.0f} GB." if bos is not None else "")
                 + "\n\nYerel YZ yalnızca yorum paragrafını yazar; program onsuz da tam çalışır."
                 + "\n\nKurulumu onaylıyor musunuz?")
        if bos is not None and bos < toplam + 3:
            messagebox.showwarning("Yerel YZ", f"Yetersiz disk alanı: {bos:.0f} GB boş, en az "
                                   f"{toplam + 3:.0f} GB gerekir. Kurulum yapılmadı.",
                                   parent=self.root)
            return
        if not messagebox.askyesno("Yerel YZ kurulumu - onay", metin, parent=self.root):
            self.durum.configure(text="Yerel YZ kurulumu yapılmadı (onay verilmedi).")
            return
        log.info("Yerel YZ kurulumu onaylandı: %s", plan)
        self.yz_kuruluyor = True
        self.btn_yz.configure(text="YZ kuruluyor...")

        def bildir(m):
            self.kuyruk.put(("yzkur", m))

        def is_():
            try:
                sonuc = yerel_yz_kur(plan, self.ayar, bildir)
                self.kuyruk.put(("yzkur_bitti", sonuc))
            except Exception as e:
                log.exception("Yerel YZ kurulumu başarısız")
                self.kuyruk.put(("yzkur_bitti", {"hata": str(e) or e.__class__.__name__}))
        threading.Thread(target=is_, daemon=True).start()

    def liste_guncelle(self):
        if self.mesgul:
            self.durum.configure(text="İşlem sürüyor, lütfen bekleyin...")
            return
        self._mesgul_ayarla(True, "Üyelik ve fiyatlar güncelleniyor...")
        threading.Thread(target=self._liste_is, daemon=True).start()

    def _liste_is(self):
        try:
            ekstra = [k for kodlar in self.listeler.values() for k in kodlar]
            sonuc = liste_getir(list(self.kodlar), ekstra)
            try:
                adlari_tamamla(sonuc["kodlar"] + ekstra)
            except Exception:
                log.warning("Şirket adları tamamlanamadı.", exc_info=True)
            self.kuyruk.put(("liste", sonuc))
        except Exception as e:
            log.exception("Liste güncellenemedi")
            self.kuyruk.put(("hata", f"Liste güncellenemedi: {e}\n\nAyrıntı: {LOG_DOSYASI}"))

    def _mesaji_isle(self, tur, veri):
        if tur == "rapor":
            self._rapor_yaz(veri["govde"], veri["baslik"])
            self._temel_yaz([("Piyasa genişliği    : hesaplanıyor..." if veri["endeks"]
                              else "Adil Değer          : hesaplanıyor...", "soluk")])
            self.son_analiz = veri
            self._grafik_ciz(veri)
            self._mesgul_ayarla(False, f"{veri['kod']} analiz tamamlandı.")
        elif tur == "endeks":
            if not self.son_analiz or self.son_analiz["kod"] != veri["kod"]:
                return
            self.son_analiz["genislik"] = veri["genislik"]
            self._grafik_ciz(self.son_analiz)
            satirlar = endeks_satirlari(veri["genislik"], veri["kuresel"])
            if veri["kuresel"]:
                satirlar.append((yz_bekleme_metni(), "soluk"))
            self._temel_yaz(satirlar)
        elif tur == "kuresel":
            self.son_analiz = {"tur": "kuresel", "kuresel": veri, "kod": "KÜRESEL"}
            self._rapor_yaz(self._kuresel_rapor(veri),
                            f"KÜRESEL GÖRÜNÜM  |  {datetime.now():%d.%m.%Y %H:%M}  |  v{SURUM}")
            sat = [("--- Kural tabanlı özet " + "-" * 22, "baslik"),
                   (f"{'Rejim':<20}: {veri['rejim']['etiket']}", veri["rejim"]["renk"])]
            sat += [("  - " + m, "down") for m in veri["rejim"]["kacis"]]
            sat += [("  + " + m, "up") for m in veri["rejim"]["istah"]]
            sat.append((yz_bekleme_metni(), "soluk"))
            self._temel_yaz(sat)
            self._grafik_ciz(self.son_analiz)
            self._mesgul_ayarla(False, "Küresel görünüm hazır; yerel YZ yorumu bekleniyor.")
        elif tur == "yz":
            if veri["sira"] != self.yz_sira:
                return   # kullanıcı başka ekrana geçti
            satirlar = [x for x in (self._temel_satirlar_son or []) if not x[0].startswith("Yerel YZ yorumu hazır")]
            self._temel_satirlar_son = satirlar
            self._yz_yaz(veri)
            if "yok" in veri:
                return   # yerel YZ yok: durum satırı olduğu gibi kalır (hata değil)
            self.durum.configure(text="Yerel YZ yorumu eklendi." if "hata" not in veri
                                 else "Yerel YZ'ye ulaşılamadı (Ollama yanıt vermedi).")
        elif tur == "temel":
            if not self.son_analiz or self.son_analiz["kod"] != veri["kod"]:
                return  # kullanıcı bu arada başka hisseye geçti
            if veri["temel"] is None:
                self._temel_yaz([("Adil Değer          : alınamadı", "soluk"),
                                 ("", None),
                                 ("Yahoo Finance temel veri döndürmedi.", "soluk"),
                                 (f"Ayrıntı: {LOG_DOSYASI}", "soluk")])
            else:
                self._temel_yaz(temel_satirlari(veri["temel"]))
        elif tur == "liste":
            self.kodlar = veri["kodlar"]
            self.fiyatlar = {k: (f, d, y) for k, f, d, y in veri["satirlar"]}
            if veri["uye_ok"]:
                self.liste_eksik = False
            self._tabloyu_doldur()
            self._rapor_yaz("LİSTE GÜNCELLEME ÖZETİ\n"
                            + "=" * 52 + "\n" + veri["uye_ozeti"] + "\n\n"
                            + f"Fiyatlar: {len(veri['satirlar'])}/{veri['istenen']} hisse "
                              f"(Yahoo {veri['y']}, İş Yatırım {veri['i']}).")
            self._mesgul_ayarla(
                False,
                ("Üyelik güncellendi" if veri["uye_ok"] else "Üyelik güncellenemedi (eski liste)")
                + f" | {len(veri['satirlar'])} hisse fiyatı - {datetime.now():%H:%M:%S}")
        elif tur == "tarama":
            eski = self.tarama
            olcut = {**eski["olcut"], **veri["olcut"]} if eski["zaman"] else dict(veri["olcut"])
            kaynak = {**eski["kaynak"], **veri["kaynak"]} if eski["zaman"] else dict(veri["kaynak"])
            self.tarama = {"olcut": olcut, "kaynak": kaynak, "zaman": veri["zaman"],
                           "eksik": [k for k in veri["eksik"] if k not in veri["olcut"]]}
            for k, o in veri["olcut"].items():
                self.fiyatlar[k] = (o["son"], o["deg"], veri["kaynak"][k])
            self._mesgul_ayarla(False, "Tarama tamamlandı.")
            self._filtre_uygula()
        elif tur == "yzkur":
            if not self.mesgul:
                self.durum.configure(text="Yerel YZ: " + veri)
        elif tur == "yzkur_bitti":
            self.yz_kuruluyor = False
            self.btn_yz.configure(text="Yerel YZ")
            if "hata" in veri:
                self.durum.configure(text="Yerel YZ kurulamadı.")
                messagebox.showerror("Yerel YZ", "Kurulum tamamlanamadı:\n" + veri["hata"][:400]
                                     + f"\n\nAyrıntı: {LOG_DOSYASI}. Program yorumsuz çalışmaya devam eder.",
                                     parent=self.root)
            else:
                self.ayar["yerel_model"] = veri["model"]
                self._ayar_yaz()
                _YZ_YOK.update(neden=None, zaman=None)
                self.durum.configure(text=f"Yerel YZ hazır: {veri['model']}")
                messagebox.showinfo("Yerel YZ", f"Kurulum tamamlandı.\nModel: {veri['model']}\n\n"
                                    "Bundan sonraki analizlerde yorum otomatik eklenecek.",
                                    parent=self.root)
        elif tur == "hata":
            if self.gorunum.get() != "tum" and self.tarama["zaman"] is None:
                self.gorunum.set("tum")
                self.tarama_sonuc = {}
                self._tabloyu_doldur()
            self._rapor_yaz(veri)
            self._mesgul_ayarla(False, "Hata oluştu.")
            self.giris.focus_set()

    def _kuyruk_dinle(self):
        tur = "?"
        try:
            while True:
                tur, veri = self.kuyruk.get_nowait()
                self._mesaji_isle(tur, veri)
        except queue.Empty:
            pass
        except Exception:
            log.exception("Mesaj işlenemedi: %s", tur)
            self._rapor_yaz(f"Sonuç ekranda gösterilemedi. Ayrıntı: {LOG_DOSYASI}")
            self._mesgul_ayarla(False, "Hata oluştu.")
        finally:
            self._after_id = self.root.after(100, self._kuyruk_dinle)


if __name__ == "__main__":
    log_kur()
    adlari_yukle()
    dpi_ayarla()
    kok = tk.Tk()
    BistAnalizApp(kok)
    kok.mainloop()
