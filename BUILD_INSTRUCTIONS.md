# 📦 Como Gerar o EXE do FiveM Optimizer

## ✅ Opção 1: Automático (Recomendado)

### Windows:

1. **Clone ou baixe o repositório**
   ```bash
   git clone https://github.com/prozin01/FiveM-System-Optimizer.git
   cd FiveM-System-Optimizer
   ```

2. **Execute o arquivo `build_exe.bat`**
   - Clique duas vezes em `build_exe.bat`
   - O programa vai:
     - Verificar se Python está instalado
     - Instalar PyInstaller automaticamente
     - Compilar o executável
     - Abrir a pasta com o `.exe` pronto

3. **Pronto!**
   - O arquivo `FiveM-Optimizer.exe` estará em `dist/FiveM-Optimizer.exe`
   - Clique com botão direito → "Executar como administrador"

---

## 🔧 Opção 2: Manual (Python)

Se o `.bat` não funcionar:

1. **Instale Python** (se não tiver)
   - Baixe em https://www.python.org
   - **Marque "Add Python to PATH"** durante instalação

2. **Abra PowerShell ou CMD na pasta do projeto**
   ```bash
   cd C:\Caminho\FiveM-System-Optimizer
   ```

3. **Instale PyInstaller**
   ```bash
   pip install pyinstaller
   ```

4. **Compile o programa**
   ```bash
   pyinstaller --onefile --windowed --name="FiveM-Optimizer" GUI-Optimizer.py
   ```

5. **Pronto!**
   - Arquivo estará em: `dist\FiveM-Optimizer.exe`

---

## 💾 Usando o EXE

1. **Execute como Administrador**
   - Clique direito no `FiveM-Optimizer.exe`
   - Selecione "Executar como administrador"

2. **Marque as otimizações desejadas**
   - ✅ Deixe tudo marcado (recomendado)
   - Ou desmarque o que não quer

3. **Clique em "APLICAR SELECIONADOS"**

4. **Reinicie o PC**

---

## 🐛 Problemas Comuns

### "Python não reconhecido"
- Reinstale Python
- Marque a opção "Add Python to PATH"
- Reinicie o computador

### "PyInstaller not found"
```bash
pip install --upgrade pip
pip install pyinstaller
```

### "Aviso de Windows Defender"
- É normal para programas compilados
- Clique em "More info" → "Run anyway"
- O programa é 100% seguro

---

## 📊 Tamanho do EXE

- **FiveM-Optimizer.exe**: ~40-50 MB
- Inclui Python embutido para funcionar sem dependências

---

## ✨ Sucesso!

Depois que gerar o `.exe`, você pode:
- Compartilhar com amigos
- Colocar no Desktop
- Criar um atalho
- Distribuir

**Não precisa mais de Python instalado** - o `.exe` funciona sozinho!

---

**Dúvidas?** Abra uma [issue](../../issues) no repositório.
