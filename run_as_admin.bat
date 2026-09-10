@echo off
REM Executa FiveM Optimizer como Administrador automaticamente
REM Verifica se ja esta rodando como admin
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Solicitando direitos de administrador...
    powershell -Command "Start-Process cmd -ArgumentList '/c cd /d %cd% && FiveM-Optimizer.exe' -Verb RunAs"
    exit /b
)
REM Se chegou aqui, ja tem permissao de admin
echo [OK] Executando como Administrador...
timeout /t 1 >nul
FiveM-Optimizer.exe
