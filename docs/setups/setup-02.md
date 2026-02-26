# Setup 02: Xcode Foundation 🍎

O Xcode é o ambiente de desenvolvimento essencial para criar aplicativos para ecossistemas Apple (iOS, macOS).

> [!IMPORTANT]
> O Xcode está disponível **apenas para computadores Mac**. Caso você use Windows ou Linux, este guia serve apenas como referência técnica.

## 1. Requisitos de Sistema
*   **Hardware**: Mac com processador Intel ou Apple Silicon (M1/M2/M3).
*   **Sistema**: macOS Sonoma ou superior (recomendado).
*   **Espaço**: Pelo menos 40GB livres (o Xcode é pesado!).

## 2. Instalação
1.  Abra a **App Store** no seu Mac.
2.  Pesquise por **Xcode**.
3.  Clique em "Obter" e aguarde o download (pode demorar bastante).

## 3. Configurando Componentes
*   Ao abrir o Xcode pela primeira vez, ele solicitará a instalação de componentes adicionais. Aceite todos.
*   Nas configurações do Xcode (**Settings > Platforms**), certifique-se de que o simulador de **iOS** esteja baixado.

## 4. Xcode Command Line Tools
Acesse o terminal e execute:

<div class="termy">
```bash
xcode-select --install
```
</div>

Isso instalará ferramentas essenciais como o compilador `gcc`, `make` e outros utilitários de linha de comando.

---

[**⬅️ Voltar para o Início do Setup**](./index.md)

## 5. Opcional: CocoaPods
Muitos projetos iOS antigos ainda usam CocoaPods para dependências:
```bash
sudo gem install cocoapods
```

## 5. Solução de Problemas ⚠️
*   **Espaço em Disco**: O Xcode é muito grande. Garanta pelo menos 40GB de espaço livre para ele e os simuladores.
*   **Build Lento**: Use simuladores de modelos mais simples (ex: iPhone SE) para poupar memória RAM se necessário.