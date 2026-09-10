@echo off
setlocal enabledelayedexpansion
echo.
echo =====================================
echo  FiveM Optimizer - Build EXE
echo =====================================
echo.
echo [*] Verificando se Python esta instalado...
python --version >nul 2>&1
if errorlevel 1 (
    echo [!] Python nao encontrado! Instale em https://www.python.org
    pause
    exit /b 1
)
echo [OK] Python encontrado!
echo.
echo [*] Atualizando PIP...
python -m pip install --upgrade pip
echo.
echo [*] Instalando PyInstaller...
python -m pip install --upgrade pyinstaller
echo.
echo [*] Verificando instalacao...
python -m PyInstaller --version
if errorlevel 1 (
    echo [!] Erro na instalacao do PyInstaller!
    pause
    exit /b 1
)
echo.
echo [OK] PyInstaller pronto!
echo.
echo [*] Compilando - pode levar alguns minutos...
python -m PyInstaller --onefile --windowed --name="FiveM-Optimizer" --distpath="dist" --buildpath="build" "GUI-Optimizer.py"
echo.
if exist "dist\FiveM-Optimizer.exe" (
    echo [OK] SUCESSO! Arquivo criado: dist\FiveM-Optimizer.exe
    echo.
    echo [*] Abrindo pasta...
    timeout /t 3
    start dist
) else (
    echo [!] Erro na compilacao!
)
pause
