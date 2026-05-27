from CadastrarProduto import cadastrar_produto, produtos   # Importa a função de cadastro e o dicionário principal de produtos
from ConsultarEstoque import consultar_estoque   # Importa a função responsável por consultar produtos no estoque
from EstoqueBaixo import alerta_estoque_baixo   # Importa a função responsável por alertar produtos com estoque baixo
from RegistrarEntrada import registrar_entrada   # Importa a função responsável por registrar entrada de produtos
from RegistrarSaida import registrar_saida   # Importa a função responsável por registrar saída de produtos


def ler_float(mensagem):   # Função responsável por ler números decimais digitados pelo usuário
    while True:    # Repete até o usuário digitar um número válido
        try:  
            return float(input(mensagem).replace("\ufeff", "").replace(",", "."))   # Converte o valor digitado para float
        except ValueError:
            print("Digite um numero valido.")   # Mensagem exibida caso o valor seja inválido


def ler_int(mensagem):   # Função responsável por ler números inteiros digitados pelo usuário
    while True:    # Repete até o usuário digitar um número inteiro válido
        try:
            return int(input(mensagem).replace("\ufeff", ""))    # Converte o valor digitado para inteiro
        except ValueError:
            print("Digite um numero inteiro valido.")    # Mensagem exibida caso o valor seja inválido


def listar_produtos():   # Função responsável por listar todos os produtos cadastrados
    print("\n===== LISTA DE PRODUTOS =====")   # Exibe o título da listagem

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")    # Verifica se não existem produtos cadastrados
        return

    for produto_id, produto in produtos.items():   # Percorre todos os produtos cadastrados
        print(f"""
ID: {produto_id}
Nome: {produto['nome']}
Categoria: {produto['categoria']}
Preco: R$ {produto['preco']:.2f}
Quantidade: {produto['quantidade']}
""")    # Exibe os dados de cada produto


def main():   # Função principal do sistema
    while True:    # Mantém o menu funcionando até o usuário escolher sair
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
""")   # Exibe o menu principal

        opcao = input("Escolha uma opcao: ").replace("\ufeff", "").strip()   # Lê a opção escolhida pelo usuário

        if opcao == "1":   # Opção para cadastrar produto
            nome = input("Nome do produto: ").strip()
            categoria = input("Categoria: ").strip()
            preco = ler_float("Preco: ")
            quantidade = ler_int("Quantidade inicial: ")

            if not nome or not categoria:    # Verifica se nome e categoria foram preenchidos
                print("\nNome e categoria sao obrigatorios.")
                continue

            if preco < 0 or quantidade < 0:   # Verifica se preço ou quantidade são negativos
                print("\nPreco e quantidade nao podem ser negativos.")
                continue

            cadastrar_produto(nome, categoria, preco, quantidade, produtos)   # Chama a função para cadastrar o produto

        elif opcao == "2":   # Opção para registrar entrada de produto
            produto_id = ler_int("ID do produto: ")
            quantidade = ler_int("Quantidade de entrada: ")

            if quantidade <= 0:   # Verifica se a quantidade informada é válida
                print("\nA quantidade de entrada deve ser maior que zero.")
                continue

            registrar_entrada(produto_id, quantidade, produtos)    # Chama a função de entrada

        elif opcao == "3":    # Opção para registrar saída de produto
            produto_id = ler_int("ID do produto: ")
            quantidade = ler_int("Quantidade de saida: ")

            if quantidade <= 0:   # Verifica se a quantidade informada é válida
                print("\nA quantidade de saida deve ser maior que zero.")
                continue

            registrar_saida(produto_id, quantidade, produtos)    # Chama a função de saída

        elif opcao == "4":   # Opção para consultar produto no estoque
            produto_id = ler_int("ID do produto: ")
            consultar_estoque(produto_id, produtos)

        elif opcao == "5":   # Opção para alertar estoque baixo
            limite = ler_int("Digite o limite minimo: ")
            alerta_estoque_baixo(produtos, limite)

        elif opcao == "6":   # Opção para listar todos os produtos
            listar_produtos()

        elif opcao == "0":    # Opção para encerrar o sistema
            print("\nSistema encerrado.")
            break

        else:    # Caso o usuário escolha uma opção inexistente
            print("\nOpcao invalida.")


if __name__ == "__main__":   # Verifica se este arquivo está sendo executado diretamente
    main()   # Inicia o sistema chamando a função principal
