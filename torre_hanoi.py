def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return

    torre_hanoi(n - 1, origem, auxiliar, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    torre_hanoi(n - 1, auxiliar, destino, origem)


def ler_entrada_torre(mensagem):
    torre = input(mensagem).strip().upper()
    if torre not in ('A', 'B', 'C'):
        print("Erro: Torre inválida. Use apenas A, B ou C.")
        exit(1)
    return torre


if __name__ == '__main__':
    try:
        n = int(input("Digite o número de discos: "))
        if n <= 0:
            raise ValueError("O número de discos deve ser maior que zero.")
    except ValueError as e:
        print(f"Erro: {e}")
        exit(1)

    origem = ler_entrada_torre("Digite a torre de origem (A, B ou C): ")
    destino = ler_entrada_torre("Digite a torre de destino (A, B ou C): ")
    auxiliar = ler_entrada_torre("Digite a torre auxiliar (A, B ou C): ")

    if len({origem, destino, auxiliar}) < 3:
        print("Erro: As torres de origem, destino e auxiliar devem ser distintas.")
    else:
        torre_hanoi(n, origem, destino, auxiliar)
