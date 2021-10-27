def main():
    nomes = []
    nome = input("Digite o nome do funcionário: ")
    while nome != "":
        nomes.append(nome)
        nome = input("Digite o nome do funcionário: ")
    formato = input("Deseja sortear em dupla? (S/N) ")
    if formato == "S":
        sorteio(nomes)
        sorteio(nomes)
    else:
        sorteio(nomes)


def sorteio(nomes):
    import random
    sorteado = random.choice(nomes)
    print("O funcionário sorteado foi: ", sorteado)


main()
