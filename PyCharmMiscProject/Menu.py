from CadastrarProduto import cadastrar_produto, produtos
from ConsultarEstoque import consultar_estoque
from EstoqueBaixo import alerta_estoque_baixo
from RegistrarEntrada import registrar_entrada
from RegistrarSaida import registrar_saida

while True:

    print("""
=============================
 SISTEMA DE ESTOQUE
=============================

1 - Cadastrar produto
2 - Registrar entrada
3 - Registrar saída
4 - Consultar estoque
5 - Alertar estoque baixo
6 - Listar produtos
0 - Sair
""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Nome do produto: ")
        categoria = input("Categoria: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade inicial: "))

        cadastrar_produto(nome, categoria, preco, quantidade, produtos)

    elif opcao == "2":

        produto_id = int(input("ID do produto: "))
        quantidade = int(input("Quantidade de entrada: "))

        registrar_entrada(produto_id, quantidade, produtos)

    elif opcao == "3":

        produto_id = int(input("ID do produto: "))
        quantidade = int(input("Quantidade de saída: "))

        registrar_saida(produto_id, quantidade, produtos)

    elif opcao == "4":

        produto_id = int(input("ID do produto: "))

        consultar_estoque(produto_id, produtos)


    elif opcao == "5":

        limite = int(input("Digite o limite mínimo: "))

        alerta_estoque_baixo(produtos, limite)

    elif opcao == "6":

        print("\n===== LISTA DE PRODUTOS =====")

        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")

        else:
            for produto_id, produto in produtos.items():

                print(f"""
                ID: {produto_id}
                Nome: {produto['nome']}
                Categoria: {produto['categoria']}
                Preço: R$ {produto['preco']:.2f}
                Quantidade: {produto['quantidade']}
""")

    elif opcao == "0":

        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida.")
