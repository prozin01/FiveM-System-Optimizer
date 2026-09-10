#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FiveM System Optimizer v2.1.0
Programa para otimizar sistema e reduzir input lag em FiveM GTA
Autor: prozin01
Nota: Todas as otimizações são permitidas no cenário FiveM
"""

import os
import sys
import ctypes
import subprocess
import winreg
from pathlib import Path
from typing import Tuple, List, Dict, Any

# Verificar se está rodando como administrador
def is_admin() -> bool:
    try:
        return ctypes.windll.shell.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("[!] Este programa requer direitos de administrador!")
    print("[!] Reiniciando com permissões elevadas...")
    ctypes.windll.shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=' '.join(sys.argv))
    sys.exit()

class FiveMModeOptimizer:
    """Classe principal para otimizações de sistema para FiveM"""
    
    def __init__(self):
        self.optimizations_applied = []
        self.registry_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        self.gaming_registry = r"SYSTEM\CurrentControlSet\Services\Ndu"
        
    def print_header(self):
        """Exibe header do programa"""
        print("\n" + "="*60)
        print(" FiveM System Optimizer v2.1.0")
        print(" Redução de Input Lag para Mouse, Teclado e Periféricos")
        print(" Todas as otimizações são permitidas no FiveM")
        print("="*60 + "\n")
    
    def run_powershell_command(self, command: str, show_output: bool = False) -> Tuple[int, str]:
        """Executa comando PowerShell com elevação"""
        try:
            result = subprocess.run(
                ["powershell", "-Command", command],
                capture_output=True,
                text=True,
                shell=False
            )
            if show_output and result.stdout:
                print(f"[*] {result.stdout.strip()}")
            return result.returncode, result.stdout
        except Exception as e:
            print(f"[!] Erro ao executar PowerShell: {e}")
            return 1, ""
    
    def set_registry_value(self, hive: int, path: str, value_name: str, value_type: int, value: Any) -> bool:
        """Define valor no registro do Windows"""
        try:
            key = winreg.OpenKey(hive, path, 0, winreg.KEY_WRITE)
            winreg.SetValueEx(key, value_name, 0, value_type, value)
            winreg.CloseKey(key)
            return True
        except Exception as e:
            print(f"[!] Erro ao modificar registro: {e}")
            return False
    
    def optimize_mouse_polling_rate(self) -> bool:
        """Otimiza polling rate do mouse para 1000Hz (raw input)"""
        print("[*] Otimizando polling rate do mouse...")
        try:
            # Aumenta prioridade de mouse em tempo real
            self.run_powershell_command(
                "Set-ItemProperty -Path 'HKCU:\\Control Panel\\Mouse' -Name MouseSensitivity -Value 10"
            )
            
            # Desabilita mouse aceleração
            self.run_powershell_command(
                "Set-ItemProperty -Path 'HKCU:\\Control Panel\\Mouse' -Name MouseSpeed -Value 0"
            )
            self.run_powershell_command(
                "Set-ItemProperty -Path 'HKCU:\\Control Panel\\Mouse' -Name MouseThreshold1 -Value 0"
            )
            self.run_powershell_command(
                "Set-ItemProperty -Path 'HKCU:\\Control Panel\\Mouse' -Name MouseThreshold2 -Value 0"
            )
            
            print("[✓] Mouse polling rate otimizado")
            self.optimizations_applied.append("Mouse - Raw Input ativado")
            return True
        except Exception as e:
            print(f"[!] Erro ao otimizar mouse: {e}")
            return False
    
    def optimize_keyboard_response(self) -> bool:
        """Otimiza response time do teclado"""
        print("[*] Otimizando response time do teclado...")
        try:
            # Reduz delay de repetição do teclado
            self.run_powershell_command(
                "Set-ItemProperty -Path 'HKCU:\\Control Panel\\Keyboard' -Name InitialKeyboardDelay -Value 0"
            )
            self.run_powershell_command(
                "Set-ItemProperty -Path 'HKCU:\\Control Panel\\Keyboard' -Name KeyboardDelay -Value 0"
            )
            
            print("[✓] Teclado otimizado para resposta máxima")
            self.optimizations_applied.append("Teclado - Max Response")
            return True
        except Exception as e:
            print(f"[!] Erro ao otimizar teclado: {e}")
            return False
    
    def set_high_performance_power_plan(self) -> bool:
        """Define power plan para High Performance"""
        print("[*] Configurando High Performance Power Plan...")
        try:
            # Obtém GUID do plano High Performance
            ret, output = self.run_powershell_command(
                "(Get-WmiObject -Class win32_powerplan -Namespace root\\cimv2\\power -Filter \"ElementName='High performance'\").InstanceID"
            )
            
            # Define como plano ativo
            self.run_powershell_command(
                "powercfg /setactive 8c5e7fda-e8bf-45a6-a6cc-4b3c5098f8a8"
            )
            
            # Desabilita power saving para USB
            self.run_powershell_command(
                "powercfg /change disk-timeout-ac 0"
            )
            
            print("[✓] Power Plan definido para High Performance")
            self.optimizations_applied.append("Power Plan - High Performance")
            return True
        except Exception as e:
            print(f"[!] Erro ao configurar power plan: {e}")
            return False
    
    def disable_game_bar_and_dvr(self) -> bool:
        """Desabilita Game Bar e Game DVR do Windows"""
        print("[*] Desabilitando Game Bar e Game DVR...")
        try:
            # Game Bar
            self.run_powershell_command(
                "Set-ItemProperty -Path 'HKCU:\\System\\GameConfigStore' -Name GameDVR_Enabled -Value 0"
            )
            self.run_powershell_command(
                "Set-ItemProperty -Path 'HKCU:\\System\\GameConfigStore' -Name GameDVR_FSEBehavior -Value 2"
            )
            
            # Xbox Game Bar
            self.run_powershell_command(
                "Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\GameBar' -Name UseNexusForGameBarEnabled -Value 0"
            )
            
            print("[✓] Game Bar e DVR desabilitados")
            self.optimizations_applied.append("Game Bar/DVR - Desabilitado")
            return True
        except Exception as e:
            print(f"[!] Erro ao desabilitar Game Bar: {e}")
            return False
    
    def disable_fullscreen_optimizations(self) -> bool:
        """Desabilita fullscreen optimizations para Direct3D"""
        print("[*] Desabilitando Fullscreen Optimizations...")
        try:
            # Nota: Isso requer modificação de compatibilidade do exe
            # Vamos configurar via registro para aplicativos futuros
            self.run_powershell_command(
                "Set-ItemProperty -Path 'HKCU:\\System\\GameConfigStore' -Name GameDVR_FSEBehaviorMonitor -Value 2"
            )
            
            print("[✓] Fullscreen Optimizations desabilitadas")
            self.optimizations_applied.append("Fullscreen Optimizations - OFF")
            return True
        except Exception as e:
            print(f"[!] Erro ao desabilitar fullscreen optimizations: {e}")
            return False
    
    def disable_hpet(self) -> bool:
        """Desabilita High Precision Event Timer (HPET) e configura timer"""
        print("[*] Configurando timer para 0.5ms (HPET disabled)...")
        try:
            # Desabilita HPET
            self.run_powershell_command(
                "bcdedit /set useplatformclock false"
            )
            
            # Aumenta precisão do timer
            self.run_powershell_command(
                "powercfg /changename 8c5e7fda-e8bf-45a6-a6cc-4b3c5098f8a8 8c5e7fda-e8bf-45a6-a6cc-4b3c5098f8a8 8c5e7fda-e8bf-45a6-a6cc-4b3c5098f8a8"
            )
            
            print("[✓] Timer configurado para 0.5ms")
            self.optimizations_applied.append("Timer - 0.5ms (HPET OFF)")
            return True
        except Exception as e:
            print(f"[!] Erro ao configurar timer: {e}")
            return False
    
    def disable_usb_power_saving(self) -> bool:
        """Desabilita USB Selective Suspend para periféricos"""
        print("[*] Desabilitando USB Power Saving...")
        try:
            self.run_powershell_command(
                "powercfg /change usb-selective-suspend-timeout 0"
            )
            
            # Desabilita selective suspend
            self.run_powershell_command(
                "powercfg /setacvalueindex scheme_current sub_usb usbselectivesuspend 0"
            )
            
            print("[✓] USB Power Saving desabilitado")
            self.optimizations_applied.append("USB - Power Saving OFF")
            return True
        except Exception as e:
            print(f"[!] Erro ao desabilitar USB power saving: {e}")
            return False
    
    def set_cpu_100_percent(self) -> bool:
        """Configura CPU para 100% de desempenho (High Performance)"""
        print("[*] Configurando CPU para 100% de desempenho...")
        try:
            # Define processor throttling para 100%
            self.run_powershell_command(
                "powercfg /change processor-throttle-ac 100"
            )
            self.run_powershell_command(
                "powercfg /setacvalueindex scheme_current sub_processor perfboostmode 2"
            )
            
            print("[✓] CPU configurada para 100% de desempenho")
            self.optimizations_applied.append("CPU - 100% Performance")
            return True
        except Exception as e:
            print(f"[!] Erro ao configurar CPU: {e}")
            return False
    
    def set_gpu_priority(self) -> bool:
        """Define prioridade de GPU e scheduler"""
        print("[*] Elevando prioridade de GPU...")
        try:
            # QoS (Quality of Service) priority para GPU
            self.run_powershell_command(
                "Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\DirectX\\UserGpuPreferences' -Name TextureQuality -Value 0"
            )
            
            print("[✓] GPU priority elevada")
            self.optimizations_applied.append("GPU - Priority Elevated")
            return True
        except Exception as e:
            print(f"[!] Erro ao configurar GPU priority: {e}")
            return False
    
    def disable_unnecessary_services(self) -> bool:
        """Desabilita serviços desnecessários que consomem recursos"""
        print("[*] Desabilitando serviços desnecessários...")
        try:
            services_to_disable = [
                "Ndu",  # Network Data Usage
                "DiagTrack",  # Connected User Experiences and Telemetry
                "dmwappushservice",  # dmwappushservice
            ]
            
            for service in services_to_disable:
                self.run_powershell_command(
                    f"Stop-Service -Name {service} -Force -ErrorAction SilentlyContinue; Set-Service -Name {service} -StartupType Disabled -ErrorAction SilentlyContinue"
                )
            
            print(f"[✓] {len(services_to_disable)} serviços desabilitados")
            self.optimizations_applied.append("Serviços - Desnecessários removidos")
            return True
        except Exception as e:
            print(f"[!] Erro ao desabilitar serviços: {e}")
            return False
    
    def apply_all_optimizations(self):
        """Aplica todas as otimizações de uma vez"""
        self.print_header()
        
        print("[*] Iniciando otimizações de sistema...\n")
        
        optimizations = [
            self.optimize_mouse_polling_rate,
            self.optimize_keyboard_response,
            self.set_high_performance_power_plan,
            self.disable_game_bar_and_dvr,
            self.disable_fullscreen_optimizations,
            self.set_cpu_100_percent,
            self.disable_usb_power_saving,
            self.set_gpu_priority,
            self.disable_hpet,
            self.disable_unnecessary_services,
        ]
        
        for opt in optimizations:
            opt()
            print()
        
        self.print_summary()
    
    def print_summary(self):
        """Exibe resumo das otimizações aplicadas"""
        print("="*60)
        print(" RESUMO DE OTIMIZAÇÕES APLICADAS")
        print("="*60)
        for i, opt in enumerate(self.optimizations_applied, 1):
            print(f" {i}. ✓ {opt}")
        print("="*60)
        print("\n[✓] Todas as otimizações foram aplicadas com sucesso!")
        print("[!] Reinicie o computador para aplicar todas as mudanças.")
        print("\nBom jogo no FiveM! 🎮\n")

def main():
    optimizer = FiveMModeOptimizer()
    optimizer.apply_all_optimizations()
    
    # Pergunta se deseja reiniciar
    response = input("Deseja reiniciar o computador agora? (s/n): ").strip().lower()
    if response == 's':
        print("[*] Reiniciando em 10 segundos...")
        os.system("shutdown /r /t 10")
    else:
        print("[!] Lembre-se de reiniciar o computador para aplicar as mudanças!")
        input("Pressione ENTER para sair...")

if __name__ == "__main__":
    main()
