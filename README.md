# 🌐 Roteirizador de OS em CTOs (Telecom Pelotas)

Sistema interativo que simula a jornada de campo de um técnico de telecomunicações, comparando algoritmos de busca para traçar rotas entre caixas de atendimento (CTOs).

## 🗺️ O Cenário
* **Nós (Vértices):** 16 CTOs divididas em 4 bairros de Pelotas (`TRV`, `CTR`, `NAV`, `LAR`).
* **Arestas (Conexões):** Malha de fibra óptica interconectada com distâncias reais em **metros**.
* **Ponto de Partida Fixo:** `TRV-314-04` (Base Operacional).

---

## 🧠 Algoritmos Comparados
1. **DFS (Profundidade):** Explora rotas longas até o fim utilizando estrutura de **Pilha (LIFO)**.
2. **BFS (Largura):** Busca o caminho com o **menor número de caixas (saltos)** utilizando **Fila (FIFO)**.
3. **Gulosa (Greedy):** Toma decisões imediatas baseadas no vizinho mais próximo (métrica local).

---

## 🚀 Diferenciais do Projeto
* **Múltiplas Paradas Dinâmicas:** O usuário monta o itinerário no terminal. A cada destino alcançado, o estado do sistema atualiza a posição atual do técnico para o próximo trecho.
* **Fatiamento de Listas (`[1:]`):** Consolidação inteligente que impede a duplicação de CTOs de transição no histórico.
* **Relatório Comparativo:** Ao encerrar o expediente (`n`), exibe o trajeto completo e a quilometragem total acumulada por cada motor de busca.

---

## 💻 Como Rodar
```bash
python seu_arquivo.py