def calcular_rank(vitorias, derrotas):
    # Calcula o saldo de vitórias
    saldoVitorias = vitorias - derrotas

    # Determina o nível com base no número de vitórias
    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    # Exibe o resultado final
    print(f"O Herói tem saldo de {saldoVitorias} e está no nível {nivel}.")

# Exemplo de uso da função
vitorias = int(input("Digite o número de vitórias: "))
derrotas = int(input("Digite o número de derrotas: "))

calcular_rank(vitorias, derrotas)
