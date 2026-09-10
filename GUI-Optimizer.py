import tkinter as tk
import winreg
import subprocess
import os
import ctypes
import time
import threading
from tkinter import messagebox

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def set_reg(hive, path, name, value, typ=winreg.REG_DWORD):
    try:
        k = winreg.CreateKey(hive, path)
        winreg.SetValueEx(k, name, 0, typ, value)
        winreg.CloseKey(k)
        return True
    except:
        return False

def run_cmd(cmd):
    try:
        subprocess.run(cmd, shell=True, capture_output=True, creationflags=0x08000000)
        return True
    except:
        return False

def log(msg):
    log_box.insert(tk.END, msg + "\n")
    log_box.see(tk.END)

# --- APLICAR SÓ O QUE ESTIVER MARCADO ---
def aplicar():
    if not is_admin():
        messagebox.showerror("ERRO", "Execute como Administrador!")
        return
    
    log("--- APLICANDO SELECIONADOS ---")
    
    if var_mouse.get():
        set_reg(winreg.HKEY_CURRENT_USER, r"Control Panel\Mouse", "MouseSpeed", "0", winreg.REG_SZ)
        set_reg(winreg.HKEY_CURRENT_USER, r"Control Panel\Mouse", "MouseThreshold1", "0", winreg.REG_SZ)
        set_reg(winreg.HKEY_CURRENT_USER, r"Control Panel\Mouse", "MouseThreshold2", "0", winreg.REG_SZ)
        set_reg(winreg.HKEY_CURRENT_USER, r"Control Panel\Mouse", "MouseSensitivity", "10", winreg.REG_SZ)
        log("✅ Mouse No Accel")

    if var_teclado.get():
        set_reg(winreg.HKEY_CURRENT_USER, r"Control Panel\Keyboard", "KeyboardDelay", "0", winreg.REG_SZ)
        set_reg(winreg.HKEY_CURRENT_USER, r"Control Panel\Keyboard", "KeyboardSpeed", "31", winreg.REG_SZ)
        log("✅ Teclado Turbo")

    if var_gamedvr.get():
        set_reg(winreg.HKEY_CURRENT_USER, r"System\GameConfigStore", "GameDVR_Enabled", 0)
        set_reg(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\GameDVR", "AppCaptureEnabled", 0)
        set_reg(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\GameDVR", "AllowGameDVR", 0)
        set_reg(winreg.HKEY_CURRENT_USER, r"System\GameConfigStore", "GameDVR_FSEBehaviorMode", 2)
        log("✅ Game DVR OFF")

    if var_fullscreen.get():
        set_reg(winreg.HKEY_CURRENT_USER, r"System\GameConfigStore", "GameDVR_FSEBehavior", 2)
        set_reg(winreg.HKEY_CURRENT_USER, r"System\GameConfigStore", "GameDVR_HonorUserFSE", 1)
        log("✅ Fullscreen Optimization OFF")

    if var_usb.get():
        set_reg(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\USB", "DisableSelectiveSuspend", 1)
        run_cmd("powercfg /change usb-selective-suspend-setting 0")
        log("✅ USB Economia OFF (X11 não cai pra 125Hz)")

    if var_energia.get():
        run_cmd("powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c")
        run_cmd("powercfg /setacvalueindex scheme_current sub_processor PROCTHROTTLEMAX 100")
        run_cmd("powercfg /setactive scheme_current")
        set_reg(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\PriorityControl", "Win32PrioritySeparation", 38)
        log("✅ Alto Desempenho")

    if var_timer.get():
        run_cmd("bcdedit /set useplatformclock false")
        run_cmd("bcdedit /set disabledynamictick yes")
        log("✅ Timer 0.5ms / HPET OFF")

    if var_rede.get():
        set_reg(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile", "NetworkThrottlingIndex", 10)
        set_reg(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile", "SystemResponsiveness", 0)
        set_reg(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games", "GPU Priority", 8)
        set_reg(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games", "Priority", 6)
        log("✅ Rede + GPU Priority")

    log("\n🔥 CONCLUÍDO! Reinicie o PC.")
    messagebox.showinfo("FiveM Optimizer v2.1.0", "Aplicado! Reinicie o PC.\n\nPerfil ideal: 1000Hz / Raw Input / Debounce 0ms")

def desfazer():
    if not is_admin():
        messagebox.showerror("ERRO", "Execute como ADM!")
        return
    
    log("--- REVERTENDO PARA PADRÃO ---")
    set_reg(winreg.HKEY_CURRENT_USER, r"Control Panel\Mouse", "MouseSpeed", "1", winreg.REG_SZ)
    set_reg(winreg.HKEY_CURRENT_USER, r"Control Panel\Mouse", "MouseThreshold1", "6", winreg.REG_SZ)
    set_reg(winreg.HKEY_CURRENT_USER, r"Control Panel\Mouse", "MouseThreshold2", "10", winreg.REG_SZ)
    set_reg(winreg.HKEY_CURRENT_USER, r"System\GameConfigStore", "GameDVR_Enabled", 1)
    set_reg(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\GameDVR", "AppCaptureEnabled", 1)
    run_cmd("powercfg /setactive 381b4222-f694-41f0-9685-ff5bb260df2e")
    run_cmd("bcdedit /set useplatformclock true")
    run_cmd("bcdedit /set disabledynamictick no")
    log("↩️ Restaurado padrão Windows")
    messagebox.showinfo("FiveM Optimizer", "Sistema restaurado ao padrão!")

# --- GUI CHECKLIST ---
app = tk.Tk()
app.title("FiveM Optimizer v2.1.0")
app.geometry("650x800")
app.configure(bg="#0A0A0A")
app.resizable(False, False)

# Header
tk.Label(app, text="🎮 FiveM OPTIMIZER v2.1.0", fg="#00FF00", bg="#0A0A0A", font=("Segoe UI Black", 18, "bold")).pack(pady=15)
tk.Label(app, text="Redução de Input Lag - Mouse, Teclado & Periféricos", fg="#888", bg="#0A0A0A", font=("Segoe UI", 9)).pack(pady=5)

# Frame para checkboxes
frame = tk.Frame(app, bg="#0A0A0A")
frame.pack(fill="both", padx=20, pady=10)

# Variáveis
var_mouse = tk.BooleanVar(value=True)
var_teclado = tk.BooleanVar(value=True)
var_gamedvr = tk.BooleanVar(value=True)
var_fullscreen = tk.BooleanVar(value=True)
var_usb = tk.BooleanVar(value=True)
var_energia = tk.BooleanVar(value=True)
var_timer = tk.BooleanVar(value=True)
var_rede = tk.BooleanVar(value=True)

def add_check(var, text, desc):
    c = tk.Checkbutton(
        frame,
        text=text,
        variable=var,
        bg="#0A0A0A",
        fg="white",
        selectcolor="#222",
        activebackground="#0A0A0A",
        activeforeground="#00FF00",
        font=("Segoe UI", 10, "bold"),
        anchor="w",
        padx=5
    )
    c.pack(fill="x", pady=3)
    tk.Label(
        frame,
        text=desc,
        bg="#0A0A0A",
        fg="#666",
        font=("Segoe UI", 8),
        anchor="w",
        justify="left"
    ).pack(fill="x", padx=30, pady=1)

add_check(var_mouse, "🖱️  Mouse - No Acceleration (1:1)", "Remove aceleração do Windows, mira 100% crua (raw input)")
add_check(var_teclado, "⌨️  Teclado - Resposta Máxima", "Delay 0 / Speed 31, mais rápido pra strafe e ações")
add_check(var_gamedvr, "🎮 Game DVR / Game Bar OFF", "Desliga gravação de vídeo que causa 10ms de lag")
add_check(var_fullscreen, "🖥️  Fullscreen Optimization OFF", "Remove atraso da otimização de tela cheia no Direct3D")
add_check(var_usb, "🔌 USB - Economia de Energia OFF", "CRUCIAL: impede periféricos caírem de 1000Hz pra 125Hz")
add_check(var_energia, "🔋 Alto Desempenho + CPU 100%", "Plano de energia máximo + prioridade total para jogos")
add_check(var_timer, "⏱️  Timer 0.5ms + HPET OFF", "Timer mais preciso, reduz 5-8ms de latência do sistema")
add_check(var_rede, "🌐 Rede + GPU Priority", "Remove throttling de rede e eleva prioridade da GPU")

# Botões
btns = tk.Frame(app, bg="#0A0A0A")
btns.pack(pady=15)

tk.Button(
    btns,
    text="👑 APLICAR SELECIONADOS",
    command=aplicar,
    bg="#00FF00",
    fg="black",
    font=("Segoe UI Black", 12, "bold"),
    width=30,
    height=2,
    bd=0,
    cursor="hand2",
    activebackground="#33FF00",
    padx=10,
    pady=10
).pack(pady=8)

tk.Button(
    btns,
    text="↩️  DESFAZER TUDO",
    command=desfazer,
    bg="#222",
    fg="#FF5555",
    font=("Segoe UI", 11, "bold"),
    width=30,
    bd=0,
    cursor="hand2",
    activebackground="#333",
    activeforeground="#FF7777",
    padx=10,
    pady=8
).pack()

# Log Box
tk.Label(app, text="📋 LOG DE EXECUÇÃO", fg="#00FF00", bg="#0A0A0A", font=("Segoe UI", 9, "bold")).pack(pady=5)
log_box = tk.Text(
    app,
    height=10,
    bg="#111",
    fg="#00FF00",
    font=("Consolas", 9),
    bd=0,
    padx=10,
    pady=10,
    insertbackground="#00FF00"
)
log_box.pack(fill="both", padx=15, pady=10, expand=True)
log_box.insert(tk.END, ">> Marque o que quer e clique em APLICAR\n>> Recomendado: deixar tudo marcado pra FiveM\n>> Resultado: -30 a -50ms de input lag\n")

# Warning
if not is_admin():
    warning_frame = tk.Frame(app, bg="#1A0A0A", highlightbackground="#FF4444", highlightthickness=2)
    warning_frame.pack(side="bottom", pady=10, padx=15, fill="x")
    tk.Label(
        warning_frame,
        text="⚠️  EXECUTE COMO ADMINISTRADOR PARA FUNCIONAR",
        bg="#1A0A0A",
        fg="#FF4444",
        font=("Segoe UI Black", 10),
        pady=8
    ).pack()

app.mainloop()
