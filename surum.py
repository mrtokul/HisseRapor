# -*- coding: utf-8 -*-
"""Sürümü bist_analiz.py içindeki SURUM satırından okur, surum.txt'yi (EXE dosya bilgisi)
üretir ve derleme betiğine "SURUM TARIH" yazdırır. Böylece EXE adı, Windows dosya
bilgisi ve program arayüzündeki sürüm hep aynı olur."""
import re
from datetime import date
from pathlib import Path

kod = Path("bist_analiz.py").read_text(encoding="utf-8")
m = re.search(r'^SURUM\s*=\s*"(\d+)\.(\d+)\.(\d+)"', kod, re.M)
if not m:
    raise SystemExit("HATA: bist_analiz.py icinde SURUM bulunamadi")
a, b, c = m.groups()
v = f"{a}.{b}.{c}"
Path("surum.txt").write_text(f"""# UTF-8
VSVersionInfo(
  ffi=FixedFileInfo(filevers=({a},{b},{c},0), prodvers=({a},{b},{c},0), mask=0x3f, flags=0x0, OS=0x40004, fileType=0x1, subtype=0x0, date=(0,0)),
  kids=[
    StringFileInfo([StringTable('040904B0', [
      StringStruct('CompanyName', ''),
      StringStruct('FileDescription', 'Hisse Rapor v{v} - BIST 100 Analiz Terminali'),
      StringStruct('FileVersion', '{v}.0'),
      StringStruct('InternalName', 'Hisse Rapor'),
      StringStruct('OriginalFilename', 'Hisse Rapor v{v}.exe'),
      StringStruct('ProductName', 'Hisse Rapor'),
      StringStruct('ProductVersion', '{v}.0')])]),
    VarFileInfo([VarStruct('Translation', [1033, 1200])])
  ]
)
""", encoding="utf-8")
print(v, date.today().strftime("%d.%m.%y"))
