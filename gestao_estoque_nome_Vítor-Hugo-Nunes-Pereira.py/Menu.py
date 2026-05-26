from CadastrarProduto import cadastrar_produto, produtos
from ConsultarEstoque import consultar_estoque
from EstoqueBaixo import alerta_estoque_baixo
from RegistrarEntrada import registrar_entrada
from RegistrarSaida import registrar_saida


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem).replace("\ufeff", "").replace(",", "."))
        except ValueError:
            print("Digite um numero valido.")


def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem).replace("\ufeff", ""))
        except ValueError:
            print("Digite um numero inteiro valido.")


def listar_produtos():
    print("\n===== LISTA DE PRODUTOS =====")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto_id, produto in produtos.items():
        print(f"""
ID: {produto_id}
Nome: {produto['nome']}
Categoria: {produto['categoria']}
Preco: R$ {produto['preco']:.2f}
Quantidade: {produto['quantidade']}
""")


def main():
    while True:
        print("""
=============================
 SISTEMA DE ESTOQUE
=============================

1 - Cadastrar produto
2 - Registrar entrada
3 - Registrar saida
4 - Consultar estoque
5 - Alertar estoque baixo
6 - Listar produtos
0 - Sair
""")

        opcao = input("Escolha uma opcao: ").replace("\ufeff", "").strip()

        if opcao == "1":
            nome = input("Nome do produto: ").strip()
            categoria = input("Categoria: ").strip()
            preco = ler_float("Preco: ")
            quantidade = ler_int("Quantidade inicial: ")

            if not nome or not categoria:
                print("\nNome e categoria sao obrigatorios.")
                continue

            if preco < 0 or quantidade < 0:
                print("\nPreco e quantidade nao podem ser negativos.")
                continue

            cadastrar_produto(nome, categoria, preco, quantidade, produtos)

        elif opcao == "2":
            produto_id = ler_int("ID do produto: ")
            quantidade = ler_int("Quantidade de entrada: ")

            if quantidade <= 0:
                print("\nA quantidade de entrada deve ser maior que zero.")
                continue

            registrar_entrada(produto_id, quantidade, produtos)

        elif opcao == "3":
            produto_id = ler_int("ID do produto: ")
            quantidade = ler_int("Quantidade de saida: ")

            if quantidade <= 0:
                print("\nA quantidade de saida deve ser maior que zero.")
                continue

            registrar_saida(produto_id, quantidade, produtos)

        elif opcao == "4":
            produto_id = ler_int("ID do produto: ")
            consultar_estoque(produto_id, produtos)

        elif opcao == "5":
            limite = ler_int("Digite o limite minimo: ")
            alerta_estoque_baixo(produtos, limite)

        elif opcao == "6":
            listar_produtos()

        elif opcao == "0":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpcao invalida.")


if __name__ == "__main__":
    main()
