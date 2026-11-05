# Hisse Rapor — BIST 100 Analiz Terminali

Windows masaüstü programı (Python / Tkinter). BIST 100 hisselerini ve endeksin kendisini analiz eder:
kanıta dayalı işaretler, adil değer ve duyarlılık, BIST 100 genişliği, küresel görünüm (VIX, DXY,
ABD 10Y, emtia, kur) ve «Hisselerim» listeleri. Yorum metni isteğe bağlı olarak **yerel yapay zekâ**
ile (Ollama, `127.0.0.1:11434`) yazılır; Ollama yoksa program kural tabanlı özetle çalışır ve
kurulumu yalnız onay alarak önerir.

> Yatırım tavsiyesi değildir. Veriler Yahoo Finance üzerinden gelir; sayılar kodla hesaplanır,
> yerel YZ çıktısı yalnızca yorumdur.

## Sürüm

Güncel sürüm: **2.4.1** (5 Kasım 2026). Sürüm numarası tek yerde tutulur:
`bist_analiz.py` içindeki `SURUM = "X.Y.Z"` satırı. Derleme betiği EXE adını ve Windows dosya
bilgisini (`surum.txt`) `surum.py` ile buradan üretir. Değişiklik geçmişi `bist_analiz.py`
dosyasının başındaki açıklamadadır.

Hazır EXE (Windows, tek dosya, Python gerekmez): [`exe/HisseRapor-v2.4.1.exe`](exe/HisseRapor-v2.4.1.exe) → sayfada «Download raw file». İmzasız olduğu için Windows ilk açılışta uyarı verebilir (Ek bilgi → Yine de çalıştır).

## Kaynaktan derleme (Windows)

Gerekenler: Python 3.12 (`py -3.12`).

1. `tek exe oluştur.bat` dosyasına çift tıklayın.
2. Betik bağımlılıkları `req.txt` içindeki sabit sürümlerle kurar, simgeyi `Hisse Rapor.jpg`
   dosyasından üretir ve PyInstaller ile **tek dosya** EXE paketler.
3. Sonuç: `dist\Hisse Rapor vX.Y.Z GG.AA.YY.exe`

Doğrudan çalıştırmak için: `py -3.12 bist_analiz.py`

## Dosyalar

| Dosya | Görev |
|---|---|
| `bist_analiz.py` | Programın tamamı |
| `surum.py` | Sürümü `bist_analiz.py`'den okur, `surum.txt`'yi üretir |
| `surum.txt` | EXE'nin Windows dosya bilgisi (üretilmiş) |
| `tek exe oluştur.bat`, `exe_olustur.bat` | Tek dosya EXE derleme |
| `req.txt` | Sabitlenmiş bağımlılık sürümleri |
| `Hisse Rapor.jpg`, `hr.ico` | Program simgesi |

Program çalışırken yanında `hisse_rapor_ayar.json`, `hisselerim.json`, `bist100_liste.json`
ve `hisse_rapor.log` oluşturur; bunlar depoya konmaz.
