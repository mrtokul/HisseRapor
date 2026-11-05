@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Hisse Rapor - exe olustur
rem Surum TEK KAYNAKTAN: bist_analiz.py icindeki SURUM satiri. surum.py surum.txt'yi de uretir.
for /f "tokens=1,2" %%a in ('py -3.12 surum.py') do (set SURUM=%%a& set TARIH=%%b)
if not defined SURUM (
  echo HATA: surum okunamadi.
  pause
  exit /b 1
)
set AD=Hisse Rapor v%SURUM% %TARIH%
echo %AD% tek dosya EXE olarak paketleniyor...
rem Bagimliliklar: req.txt varsa sabit surumler, yoksa guncel kurulup req.txt'ye kilitlenir.
if exist req.txt (
  py -3.12 -m pip install -r req.txt
) else (
  py -3.12 -m pip install --upgrade yfinance pandas requests matplotlib pyinstaller pillow
  py -3.12 -m pip freeze | findstr /i /r "^yfinance== ^pandas== ^numpy== ^requests== ^matplotlib== ^pyinstaller== ^pillow==" > req.txt
)
rem Simge her derlemede Hisse Rapor.jpg'den uretilir.
py -3.12 -c "from PIL import Image; Image.open('Hisse Rapor.jpg').convert('RGBA').save('hr.ico', sizes=[(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)])"
rem --onefile: Python gerektirmeyen tek, bagimsiz exe. --clean: eski derleme artiklari kullanilmaz.
py -3.12 -m PyInstaller --noconfirm --clean --onefile --windowed --icon hr.ico --version-file surum.txt --name "%AD%" --collect-all yfinance bist_analiz.py
if errorlevel 1 (
  echo.
  echo HATA: derleme basarisiz. Yukaridaki mesajlara bakin.
) else (
  echo.
  echo Bitti. Tek dosya program: dist\%AD%.exe
)
pause
