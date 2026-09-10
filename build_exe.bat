@echo off
chcp 65001 >nul
echo =====================================
echo  FiveM Optimizer - Build EXE
echo =====================================
echo.
echo [*] Verificando se Python está instalado...
python --version >nul 2>&1
if errorlevel 1 (
    echo [!] Python não encontrado! Instale em https://www.python.org
    pause
    exit /b 1
)
echo [✓] Python encontrado!
echo.
echo [*] Instalando PyInstaller...
pip install pyinstaller >nul 2>&1
echo [✓] PyInstaller instalado!
echo.
echo [*] Compilando... (pode levar alguns minutos)
pyinstaller --onefile --windowed --name="FiveM-Optimizer" --distpath="dist" --buildpath="build" "GUI-Optimizer.py"
echo.
if exist "dist\FiveM-Optimizer.exe" (
    echo [✓] SUCESSO! Arquivo criado: dist\FiveM-Optimizer.exe
    echo.
    echo [*] Abrindo pasta...
    start dist
) else (
    echo [!] Erro na compilação!
)
pause
