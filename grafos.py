import collections

mapa_telecom = {
    # 🟢 BAIRRO 1: TRÊS VENDAS (TRV)
    # Ponto de partida fixo. Abre 2 caminhos internos.
    'TRV-314-04': [
        ('TRV-314-01', 130), 
        ('TRV-314-07', 265)
    ],
    'TRV-314-01': [
        ('TRV-314-04', 130), 
        ('TRV-314-09', 312),
        ('NAV-018-01', 7500)  # <--- Saída Alternativa Longa!
    ],
    'TRV-314-09': [
        ('TRV-314-01', 312), 
        ('TRV-314-07', 195), 
        ('CTR-018-05', 3540)  # <--- Saída Principal para o Centro!
    ],
    'TRV-314-07': [
        ('TRV-314-04', 265), 
        ('TRV-314-09', 195),
        ('CTR-018-03', 2100)  # <--- Outra saída para o Centro!
    ],
    # 🔵 BAIRRO 2: CENTRO (CTR)
    'CTR-018-05': [
        ('TRV-314-09', 3540), 
        ('CTR-018-02', 112), 
        ('CTR-018-03', 127)
    ],
    'CTR-018-02': [
        ('CTR-018-05', 112), 
        ('CTR-018-01', 87)
    ],
    'CTR-018-01': [
        ('CTR-018-02', 87), 
        ('CTR-018-03', 131), 
        ('NAV-018-01', 2800)  # <--- Ponte para o Navegantes!
    ],
    'CTR-018-03': [
        ('CTR-018-05', 127), 
        ('CTR-018-01', 131), 
        ('TRV-314-07', 2100)
    ],
    # 🟡 BAIRRO 3: NAVEGANTES (NAV)
    'NAV-018-01': [
        ('CTR-018-01', 2800), 
        ('TRV-314-01', 7500),
        ('NAV-018-07', 210), 
        ('NAV-018-03', 195)
    ],
    'NAV-018-07': [
        ('NAV-018-01', 210), 
        ('NAV-018-09', 137)
    ],
    'NAV-018-09': [
        ('NAV-018-07', 137), 
        ('NAV-018-03', 211),
        ('LAR-214-07', 6300)  # <--- Cabo descendo para o Laranjal!
    ],
    'NAV-018-03': [
        ('NAV-018-01', 195), 
        ('NAV-018-09', 211),
        ('LAR-214-09', 6700)  # <--- Segunda opção para o Laranjal!
    ],
    # 🟠 BAIRRO 4: LARANJAL (LAR)
    'LAR-214-06': [
        ('LAR-214-07', 141), 
        ('LAR-214-09', 161)
    ],
    'LAR-214-07': [
        ('NAV-018-09', 6300), 
        ('LAR-214-06', 141), 
        ('LAR-214-01', 116)
    ],
    'LAR-214-09': [
        ('NAV-018-03', 6700), 
        ('LAR-214-06', 161), 
        ('LAR-214-01', 216)
    ],
    'LAR-214-01': [
        ('LAR-214-07', 116), 
        ('LAR-214-09', 216)
    ]
}

def busca_dfs(grafo, inicio, objetivo): 
    return

def busca_bfs(grafo, inicio, objetivo):
    return

def busca_greedy(grafo, inicio, objetivo):
    return

primeira_partida = 'TRV-314-04'
partida_atual = primeira_partida

caminho_total_dfs = [primeira_partida]
distancia_total_dfs = 0

caminho_total_bfs = [primeira_partida]
distancia_total_bfs = 0

caminho_total_greedy = [primeira_partida]
distancia_total_greedy = 0

print (" SISTEMA DE MÚLTIPLAS PARADAS EM CTO'S ")

while True:
    cto_destino = input(f"\nVocê está em {partida_atual}. Digite a próxima CTO de destino: ").strip().upper()
    if cto_destino in mapa_telecom:
        caminho_dfs, custo_dfs = busca_dfs(mapa_telecom, partida_atual, cto_destino)
        distancia_total_dfs += custo_dfs
        caminho_total_dfs.extend(caminho_dfs[1:])  # Evita repetir o ponto de partida

        caminho_bfs, custo_bfs = busca_bfs(mapa_telecom, partida_atual, cto_destino)
        distancia_total_bfs += custo_bfs
        caminho_total_bfs.extend(caminho_bfs[1:])

        caminho_greedy, custo_greedy = busca_greedy(mapa_telecom, partida_atual, cto_destino)
        distancia_total_greedy += custo_greedy
        caminho_total_greedy.extend(caminho_greedy[1:])

        partida_atual = cto_destino

        resposta = input("\nDeseja adicionar mais um destino? (s/n): ").strip().lower()
        if resposta == 'n':
            break
    else:
        print("CTO inválida. Por favor, tente novamente.")

print("\n="*60)
print("RELATÓRIO FINAL DA JORNADA DE TRABALHO")
print("="*60)
print(f"Rota DFS: {' -> '.join(caminho_total_dfs)} | Distância Total: {distancia_total_dfs} metros")
print(f"Rota BFS: {' -> '.join(caminho_total_bfs)} | Distância Total: {distancia_total_bfs} metros")
print(f"Rota Greedy: {' -> '.join(caminho_total_greedy)} | Distância Total: {distancia_total_greedy} metros")

