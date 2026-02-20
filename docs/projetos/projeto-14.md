# Projeto 14 - Mapa de um Cluster K8s ☸️

### 🎯 Objetivo
Visualizar a estrutura lógica de um orquestrador de contêineres e entender como as peças se encaixam para garantir a alta disponibilidade.

### 📋 Passo a Passo

1.  **Cenário**: Você precisa hospedar uma API que deve ter sempre 3 cópias rodando para aguentar o tráfego.
2.  **Desenho Lógico (Mermaid)**: No VS Code, use a sintaxe Mermaid para desenhar a estrutura:
    *   1 **Control Plane** (Cérebro).
    *   2 **Nodes** (Trabalhadores).
    *   3 **Pods** (Onde seu app mora), distribuídos entre os Nodes.
3.  **Exemplo de Mapa**:
    ```mermaid
    graph TD
        C[Control Plane] --> N1[Node 1]
        C --> N2[Node 2]
        N1 --> P1[Pod API - v1]
        N1 --> P2[Pod API - v1]
        N2 --> P3[Pod API - v1]
    ```
4.  **Simulação de Falha**: Escreva um parágrafo descrevendo o que o Control Plane faria se o **Node 1** desligasse subitamente.

---
**Entrega**: O código Mermaid do seu mapa e o parágrafo explicativo da simulação de falha.