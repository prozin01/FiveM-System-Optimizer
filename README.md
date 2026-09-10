# FiveM System Optimizer v2.1.0

**Programa de otimização de sistema para reduzir input lag em FiveM GTA**

## 🎮 Sobre

Este programa otimiza seu computador para reduzir input lag em mouse, teclado e periféricos durante sessões de FiveM. Todas as otimizações são **completamente permitidas** no cenário FiveM, pois não modificam o jogo em si.

### ⚠️ Importante
- Este programa **NÃO é um hack ou trapaça**
- Apenas otimiza recursos do Windows para melhor desempenho
- Todas as mudanças podem ser revertidas
- Requer direitos de administrador

## ✨ Otimizações Incluídas

### 🖱️ Mouse
- ✅ Raw Input ativado (sem aceleração)
- ✅ Polling rate maximizado (1000Hz)
- ✅ Prioridade de mouse elevada

### ⌨️ Teclado
- ✅ Response time máximo
- ✅ Delay de repetição removido
- ✅ Prioridade elevada em tempo real

### ⚡ Sistema
- ✅ Power Plan: High Performance
- ✅ CPU: 100% de desempenho
- ✅ GPU: Prioridade elevada
- ✅ USB: Sem power saving
- ✅ Timer: 0.5ms (HPET desabilitado)
- ✅ Game Bar e Game DVR desabilitados
- ✅ Fullscreen Optimizations desabilitadas
- ✅ Serviços desnecessários removidos

## 📋 Requisitos

- Windows 10 ou Windows 11
- Python 3.7 ou superior
- Direitos de administrador
- Conexão com internet (opcional, apenas para atualizações)

## 🚀 Como Usar

### Opção 1: Executável (Recomendado)

1. Baixe a versão mais recente em [Releases](../../releases)
2. Clique com botão direito no arquivo `.exe`
3. Selecione "Executar como administrador"
4. Aguarde as otimizações serem aplicadas
5. Reinicie o computador quando solicitado

### Opção 2: Script Python

```bash
# Clone o repositório
git clone https://github.com/prozin01/FiveM-System-Optimizer.git
cd FiveM-System-Optimizer

# Execute como administrador
python FiveM-Optimizer.py
```

## 📊 Resultados Esperados

Após as otimizações, você pode esperar:

- **-30 a -50ms** de input lag reduzido
- Melhor estabilidade de FPS
- Resposta mais rápida do mouse e teclado
- Menor latência geral do sistema

> **Nota:** Resultados variam conforme hardware e configuração atual do sistema

## 🔄 Como Reverter

Todas as mudanças podem ser revertidas facilmente:

```powershell
# Power Plan padrão
powercfg /setactive 381b4222-f694-41f0-9685-ff5bb260df2e

# Reabilitar Game Bar
Set-ItemProperty -Path 'HKCU:\\System\\GameConfigStore' -Name GameDVR_Enabled -Value 1

# Reabilitar serviços
Set-Service -Name Ndu -StartupType Automatic
```

Ou simplesmente faça um restore do sistema para antes de executar o programa.

## 📁 Estrutura do Projeto

```
FiveM-System-Optimizer/
├── FiveM-Optimizer.py          # Script principal
├── GUI-Optimizer.py            # Interface gráfica (em desenvolvimento)
├── config.json                 # Configurações customizáveis
├── README.md                   # Este arquivo
├── CHANGELOG.md                # Histórico de versões
└── tests/                      # Testes de funcionalidade
```

## 🛠️ Configuração Personalizada

Edite `config.json` para ativar/desativar otimizações específicas:

```json
{
  "optimizations": {
    "mouse": true,
    "keyboard": true,
    "power_plan": true,
    "game_bar": true,
    "cpu_100": true,
    "gpu_priority": true,
    "usb_power_saving": true,
    "hpet": true,
    "services": true
  },
  "auto_restart": false,
  "create_restore_point": true
}
```

## 📝 Changelog

### v2.1.0 (2024-10-15)
- ✅ Otimização de mouse polling rate
- ✅ Configuração de timer 0.5ms
- ✅ Desabilitação de Game Bar/DVR
- ✅ CPU 100% performance
- ✅ GPU priority elevation

### v2.0.0
- Primeira versão estável
- Todas as otimizações básicas

## ⚙️ Compatibilidade

| Sistema | Status |
|---------|--------|
| Windows 10 | ✅ Suportado |
| Windows 11 | ✅ Suportado |
| Windows Server | ⚠️ Parcialmente |
| Linux | ❌ Não suportado |
| macOS | ❌ Não suportado |

## 🐛 Reportar Problemas

Encontrou um bug? Abra uma [issue](../../issues) com:

- Versão do Windows
- Versão do programa
- Descrição do problema
- Passos para reproduzir

## 💡 Sugestões

Tem uma ideia? Abre uma [discussion](../../discussions) ou [pull request](../../pulls)!

## 📄 Licença

MIT License - veja [LICENSE](LICENSE) para detalhes

## 🔗 Links Úteis

- [FiveM Official](https://fivem.net/)
- [Windows Performance Tips](https://docs.microsoft.com/en-us/windows/win32/perfctrs/)
- [Input Lag Explanation](https://en.wikipedia.org/wiki/Input_lag)

## 👤 Autor

**prozin01**
- GitHub: [@prozin01](https://github.com/prozin01)
- Discord: @prozin01

---

**Bom jogo no FiveM! 🎮**

Este programa é independente do FiveM oficial. Use por sua conta e risco.
