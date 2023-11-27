def relatorio_estatistico(tempo_medio_espera, taxa_ocupacao):
    print("\nRelatorio Estatistico:")
    print(f"Tempo medio de espera:")
    for faixa_etaria, tempo_medio in tempo_medio_espera.items():
        print(f"Faixa {faixa_etaria}: {tempo_medio:.2f} ms")

    print(f"\nTaxa de ocupacao: {taxa_ocupacao:.2%}")