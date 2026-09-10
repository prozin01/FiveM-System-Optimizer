"""
Build script para gerar executável do FiveM Optimizer
Requer: pip install pyinstaller
"""

import os
import subprocess
import sys

def build_exe():
    print("[*] Compilando FiveM Optimizer para .exe...")
    
    # Comando para criar o executável
    cmd = [
        sys.executable,
        "-m",
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--icon=icon.ico",
        "--name=FiveM-Optimizer",
        "--distpath=dist",
        "--buildpath=build",
        "--specpath=.",
        "GUI-Optimizer.py"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("[✓] Executável criado com sucesso!")
            print("[✓] Arquivo: dist/FiveM-Optimizer.exe")
        else:
            print("[!] Erro na compilação:")
            print(result.stderr)
    except Exception as e:
        print(f"[!] Erro: {e}")
        print("\nInstale PyInstaller com:")
        print("pip install pyinstaller")

if __name__ == "__main__":
    build_exe()
